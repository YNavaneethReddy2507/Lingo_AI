"""Unit tests for KnowledgeBase."""
import json
import os
import tempfile
import pytest

from src.engine.knowledge_base import KnowledgeBase


def test_knowledge_base_loading():
    kb = KnowledgeBase()
    topics = kb.get_all_topics()
    modules = kb.get_all_modules()

    # Must cover at least 8 modules (now expanded to 10)
    assert len(modules) >= 8
    module_ids = [m.id for m in modules]
    expected_modules = [
        "module_a", "module_b", "module_c", "module_d",
        "module_e", "module_f", "module_g", "module_h",
        "module_i", "module_j"
    ]
    for exp in expected_modules:
        assert exp in module_ids

    # Topics must be substantial (at least 75 topics)
    assert len(topics) >= 75


def test_topic_fields_integrity():
    kb = KnowledgeBase()
    for topic in kb.get_all_topics():
        assert topic.id, "Topic id must not be empty"
        assert topic.name, "Topic name must not be empty"
        assert topic.category, "Topic category must not be empty"
        assert topic.category_id, "Topic category_id must not be empty"
        assert topic.definition, f"Topic {topic.id} missing definition"
        assert topic.explanation, f"Topic {topic.id} missing explanation"
        assert topic.example, f"Topic {topic.id} missing example"
        assert isinstance(topic.aliases, list)
        assert isinstance(topic.keywords, list)
        assert isinstance(topic.related_topics, list)


def test_search_topics():
    kb = KnowledgeBase()
    results = kb.search_topics("YOLO")
    assert len(results) > 0
    assert any("yolo" in t.id.lower() or "yolo" in t.name.lower() for t in results)

    results_svm = kb.search_topics("Support Vector")
    assert len(results_svm) > 0
    assert any(t.id == "ml_svm" for t in results_svm)


def test_malformed_entry_error():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Write invalid JSON missing required field 'definition'
        invalid_json = {
            "module_id": "module_bad",
            "module_name": "Bad Module",
            "topics": [
                {
                    "id": "bad_topic",
                    "name": "Bad Topic",
                    "category": "Bad",
                    "category_id": "module_bad",
                    "aliases": [],
                    "keywords": [],
                    # Missing definition
                    "explanation": "test",
                    "example": "test"
                }
            ]
        }
        with open(os.path.join(tmpdir, "bad.json"), "w", encoding="utf-8") as f:
            json.dump(invalid_json, f)

        with pytest.raises(ValueError, match="missing required non-empty field"):
            KnowledgeBase(kb_dir=tmpdir)


def test_duplicate_id_error():
    with tempfile.TemporaryDirectory() as tmpdir:
        duplicate_json = {
            "module_id": "module_dup",
            "module_name": "Dup Module",
            "topics": [
                {
                    "id": "dup_1",
                    "name": "Topic 1",
                    "category": "Test",
                    "category_id": "module_dup",
                    "aliases": [],
                    "keywords": [],
                    "definition": "def",
                    "explanation": "exp",
                    "example": "ex"
                },
                {
                    "id": "dup_1",  # Duplicate ID
                    "name": "Topic 2",
                    "category": "Test",
                    "category_id": "module_dup",
                    "aliases": [],
                    "keywords": [],
                    "definition": "def",
                    "explanation": "exp",
                    "example": "ex"
                }
            ]
        }
        with open(os.path.join(tmpdir, "dup.json"), "w", encoding="utf-8") as f:
            json.dump(duplicate_json, f)

        with pytest.raises(ValueError, match="Duplicate topic ID"):
            KnowledgeBase(kb_dir=tmpdir)
