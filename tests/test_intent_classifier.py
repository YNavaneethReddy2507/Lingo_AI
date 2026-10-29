"""Unit tests for IntentClassifier."""
import pytest
from src.engine.intent_classifier import IntentClassifier
from src.engine.models import Intent


def test_greeting_intent():
    assert IntentClassifier.classify("hello")[0] == Intent.GREETING
    assert IntentClassifier.classify("Hi there")[0] == Intent.GREETING
    assert IntentClassifier.classify("Good morning")[0] == Intent.GREETING


def test_goodbye_intent():
    assert IntentClassifier.classify("bye")[0] == Intent.GOODBYE
    assert IntentClassifier.classify("goodbye see you later")[0] == Intent.GOODBYE
    assert IntentClassifier.classify("exit")[0] == Intent.GOODBYE


def test_help_intent():
    assert IntentClassifier.classify("help")[0] == Intent.HELP
    assert IntentClassifier.classify("what can you do?")[0] == Intent.HELP
    assert IntentClassifier.classify("how to use")[0] == Intent.HELP


def test_list_modules_and_topics():
    assert IntentClassifier.classify("list modules")[0] == Intent.LIST_MODULES
    assert IntentClassifier.classify("show all categories")[0] == Intent.LIST_MODULES
    assert IntentClassifier.classify("list all topics")[0] == Intent.LIST_TOPICS
    assert IntentClassifier.classify("show me deep learning topics")[0] == Intent.LIST_TOPICS


def test_comparison_intent():
    assert IntentClassifier.classify("difference between AI and ML?")[0] == Intent.COMPARE_TOPICS
    assert IntentClassifier.classify("compare CNN and RNN")[0] == Intent.COMPARE_TOPICS
    assert IntentClassifier.classify("supervised vs unsupervised")[0] == Intent.COMPARE_TOPICS


def test_example_intent():
    assert IntentClassifier.classify("give an example")[0] == Intent.GIVE_EXAMPLE
    assert IntentClassifier.classify("show me an example of SVM")[0] == Intent.GIVE_EXAMPLE


def test_formula_and_algorithm():
    assert IntentClassifier.classify("show formula for TF-IDF")[0] == Intent.SHOW_FORMULA
    assert IntentClassifier.classify("what is its formula?")[0] == Intent.SHOW_FORMULA
    assert IntentClassifier.classify("steps of BFS algorithm")[0] == Intent.EXPLAIN_ALGORITHM
    assert IntentClassifier.classify("how does K-Means algorithm work?")[0] == Intent.EXPLAIN_ALGORITHM


def test_define_and_explain():
    assert IntentClassifier.classify("what is Artificial Intelligence?")[0] == Intent.DEFINE_TOPIC
    assert IntentClassifier.classify("define Named Entity Recognition")[0] == Intent.DEFINE_TOPIC
    assert IntentClassifier.classify("explain Deep Learning")[0] == Intent.EXPLAIN_TOPIC
    assert IntentClassifier.classify("tell me about NLP")[0] == Intent.EXPLAIN_TOPIC


def test_empty_and_unknown():
    assert IntentClassifier.classify("")[0] == Intent.UNKNOWN
    # Out of domain query without question framing
    assert IntentClassifier.classify("weather forecast today in new york city")[0] == Intent.UNKNOWN
