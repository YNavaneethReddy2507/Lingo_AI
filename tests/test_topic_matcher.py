"""Unit tests for TopicMatcher."""
import pytest
from src.engine.knowledge_base import KnowledgeBase
from src.engine.topic_matcher import TopicMatcher


@pytest.fixture(scope="module")
def matcher():
    kb = KnowledgeBase()
    return TopicMatcher(kb)


def test_exact_alias_matching(matcher):
    top, conf, _ = matcher.match_topic("nlp")
    assert top is not None
    assert top.id == "nlp_fundamentals"
    assert conf >= 0.90

    top, conf, _ = matcher.match_topic("artificial intelligence")
    assert top is not None
    assert top.id == "ai_definition"


def test_special_acronyms(matcher):
    # CNN
    top, conf, _ = matcher.match_topic("explain cnn")
    assert top is not None
    assert top.id == "dl_cnn"

    # RNN
    top, conf, _ = matcher.match_topic("how do rnns work")
    assert top is not None
    assert top.id == "dl_rnn"

    # SVM
    top, conf, _ = matcher.match_topic("svm classifier")
    assert top is not None
    assert top.id == "ml_svm"

    # YOLO
    top, conf, _ = matcher.match_topic("yolo object detection")
    assert top is not None
    assert top.id == "cv_yolo"

    # A*
    top, conf, _ = matcher.match_topic("a* search algorithm")
    assert top is not None
    assert top.id == "search_astar"

    # RAG
    top, conf, _ = matcher.match_topic("tell me about rag")
    assert top is not None
    assert top.id == "genai_rag"


def test_comparison_extraction(matcher):
    t1, t2, _ = matcher.match_two_topics_for_comparison("difference between AI and ML")
    assert t1 is not None and t2 is not None
    assert {t1.id, t2.id} == {"ai_definition", "ml_definition"}

    t1, t2, _ = matcher.match_two_topics_for_comparison("compare CNN and RNN")
    assert t1 is not None and t2 is not None
    assert {t1.id, t2.id} == {"dl_cnn", "dl_rnn"}

    t1, t2, _ = matcher.match_two_topics_for_comparison("supervised vs unsupervised")
    assert t1 is not None and t2 is not None
    assert {t1.id, t2.id} == {"ml_supervised", "ml_unsupervised"}


def test_unknown_topic(matcher):
    top, conf, _ = matcher.match_topic("weather in paris")
    assert top is None
    assert conf == 0.0
