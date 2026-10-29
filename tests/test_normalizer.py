"""Unit tests for TextNormalizer."""
import pytest
from src.nlp.normalizer import TextNormalizer


def test_empty_and_whitespace():
    assert TextNormalizer.normalize("") == ""
    assert TextNormalizer.normalize("   ") == ""
    assert TextNormalizer.normalize(None) == ""


def test_lowercasing_and_spacing():
    assert TextNormalizer.normalize("  ARTIFICIAL   INTELLIGENCE  ") == "artificial intelligence"
    assert TextNormalizer.normalize("Deep\t\nLearning") == "deep learning"


def test_contractions_expansion():
    assert TextNormalizer.normalize("What's AI?") == "what is ai"
    assert TextNormalizer.normalize("don't overfit") == "do not overfit"
    assert TextNormalizer.normalize("it's a model") == "it is a model"
    assert TextNormalizer.normalize("can't do it") == "cannot do it"
    assert TextNormalizer.normalize("ai's branches") == "ai branches"


def test_punctuation_handling():
    assert TextNormalizer.normalize("What is Machine Learning?!") == "what is machine learning"
    assert TextNormalizer.normalize("Hello, world; test: (parens) [brackets]") == "hello world test parens brackets"


def test_preserves_special_tokens():
    # Preserves '*' when attached to 'a' for A*
    assert TextNormalizer.normalize("Explain A* search") == "explain a* search"
    # Preserves hyphens in compound words
    assert TextNormalizer.normalize("K-Means and TF-IDF") == "k-means and tf-idf"


def test_unicode_normalization():
    # Smart quotes and typographic dashes
    text = "“What’s AI?” — asked Dr. René"
    normalized = TextNormalizer.normalize(text)
    assert "what is ai" in normalized
    assert "rene" in normalized


def test_clean_query_for_topic_extraction():
    assert TextNormalizer.clean_query_for_topic_extraction("What is Deep Learning?") == "deep learning"
    assert TextNormalizer.clean_query_for_topic_extraction("Can you please explain Named Entity Recognition?") == "named entity recognition"
    assert TextNormalizer.clean_query_for_topic_extraction("Show me the formula for TF-IDF") == "tf-idf"
