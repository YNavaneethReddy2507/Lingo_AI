"""Unit tests for Tokenizer."""
import pytest
from src.nlp.tokenizer import Tokenizer


def test_basic_tokenization():
    tokens = Tokenizer.tokenize("artificial intelligence and machine learning")
    assert tokens == ["artificial", "intelligence", "and", "machine", "learning"]


def test_preserves_compounds_and_astar():
    tokens = Tokenizer.tokenize("k-means tf-idf a* q-learning")
    assert "k-means" in tokens
    assert "tf-idf" in tokens
    assert "a*" in tokens
    assert "q-learning" in tokens


def test_stopword_filtering():
    tokens = ["what", "is", "the", "difference", "between", "supervised", "and", "unsupervised"]
    # With intent preservation: words like 'difference', 'between', 'and' are preserved
    filtered_with_intent = Tokenizer.filter_stopwords(tokens, preserve_intent_words=True)
    assert "difference" in filtered_with_intent
    assert "between" in filtered_with_intent
    assert "and" in filtered_with_intent
    assert "supervised" in filtered_with_intent
    assert "the" not in filtered_with_intent
    assert "is" not in filtered_with_intent

    # Standard stopword test on raw words
    raw_tokens = ["the", "quick", "brown", "fox", "is", "over", "a", "lazy", "dog"]
    filtered_raw = Tokenizer.filter_stopwords(raw_tokens, preserve_intent_words=False)
    assert "the" not in filtered_raw
    assert "is" not in filtered_raw
    assert "a" not in filtered_raw
    assert "quick" in filtered_raw
    assert "fox" in filtered_raw


def test_ngrams():
    tokens = ["named", "entity", "recognition"]
    unigrams = Tokenizer.get_ngrams(tokens, 1)
    bigrams = Tokenizer.get_ngrams(tokens, 2)
    trigrams = Tokenizer.get_ngrams(tokens, 3)

    assert unigrams == ["named", "entity", "recognition"]
    assert bigrams == ["named entity", "entity recognition"]
    assert trigrams == ["named entity recognition"]


def test_all_ngrams_order():
    tokens = ["support", "vector", "machines"]
    all_grams = Tokenizer.get_all_ngrams(tokens, max_n=3)
    # Longest n-grams come first
    assert all_grams[0] == "support vector machines"
    assert "support vector" in all_grams
    assert "support" in all_grams
