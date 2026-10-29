"""End-to-End integration tests for AI KnowledgeBot rule-based chatbot engine."""
import pytest
from src.engine.chatbot import AIKnowledgeBot
from src.engine.models import Intent


@pytest.fixture
def bot():
    return AIKnowledgeBot()


def test_what_is_ai(bot):
    resp = bot.process_message("What is AI?")
    assert resp.intent == Intent.DEFINE_TOPIC
    assert resp.matched_topic is not None
    assert resp.matched_topic.id == "ai_definition"
    assert "Artificial Intelligence" in resp.text
    assert resp.confidence >= 0.95


def test_explain_artificial_intelligence(bot):
    resp = bot.process_message("Explain artificial intelligence.")
    assert resp.matched_topic is not None
    assert resp.matched_topic.id == "ai_definition"
    assert "reasoning" in resp.text.lower()


def test_tell_me_about_nlp(bot):
    resp = bot.process_message("Tell me about NLP.")
    assert resp.matched_topic is not None
    assert resp.matched_topic.id == "nlp_fundamentals"
    assert "Natural Language Processing" in resp.text


def test_difference_between_ai_and_ml(bot):
    resp = bot.process_message("Difference between AI and ML?")
    assert resp.intent == Intent.COMPARE_TOPICS
    assert resp.matched_topic is not None
    assert resp.secondary_topic is not None
    assert {resp.matched_topic.id, resp.secondary_topic.id} == {"ai_definition", "ml_definition"}
    assert "|" in resp.text  # Markdown comparison table


def test_compare_cnn_and_rnn(bot):
    resp = bot.process_message("Compare CNN and RNN.")
    assert resp.intent == Intent.COMPARE_TOPICS
    assert {resp.matched_topic.id, resp.secondary_topic.id} == {"dl_cnn", "dl_rnn"}


def test_what_is_named_entity_recognition(bot):
    resp = bot.process_message("What is named entity recognition?")
    assert resp.matched_topic is not None
    assert resp.matched_topic.id == "nlp_ner"
    assert "Named Entity Recognition" in resp.text


def test_contextual_followup_flow(bot):
    # Step 1: User asks What is AI?
    resp1 = bot.process_message("What is AI?")
    assert resp1.matched_topic.id == "ai_definition"

    # Step 2: User asks What are its branches?
    resp2 = bot.process_message("What are its branches?")
    assert resp2.intent == Intent.RELATIONSHIPS
    assert resp2.context_used is True
    assert "Machine Learning" in resp2.text

    # Step 3: User asks Give an example.
    resp3 = bot.process_message("Give an example.")
    assert resp3.intent == Intent.GIVE_EXAMPLE
    assert resp3.context_used is True
    assert resp3.matched_topic.id == "ai_definition"

    # Step 4: User asks What are its limitations?
    resp4 = bot.process_message("What are its limitations?")
    assert resp4.intent == Intent.ADVANTAGES_LIMITATIONS
    assert resp4.context_used is True


def test_explain_astar_search(bot):
    resp = bot.process_message("Explain A* search.")
    assert resp.matched_topic is not None
    assert resp.matched_topic.id == "search_astar"
    assert "f(n) = g(n) + h(n)" in resp.text or "h(n)" in resp.text


def test_explain_word2vec_and_glove(bot):
    resp = bot.process_message("Explain Word2Vec and GloVe.")
    assert resp.matched_topic is not None
    assert resp.matched_topic.id == "nlp_word2vec_glove"


def test_what_is_an_expert_system(bot):
    resp = bot.process_message("What is an expert system?")
    assert resp.matched_topic is not None
    assert resp.matched_topic.id == "kb_expert_systems"


def test_show_me_deep_learning_topics(bot):
    resp = bot.process_message("Show me deep learning topics.")
    assert resp.intent == Intent.LIST_TOPICS
    assert "Deep Learning" in resp.text


def test_unknown_query_weather(bot):
    # Crucial test: should not fabricate an answer
    resp = bot.process_message("What is the weather today?")
    assert resp.intent == Intent.UNKNOWN
    assert resp.matched_topic is None
    assert "couldn't find an exact rule match" in resp.text.lower()
    assert "zero hallucinations" in resp.text.lower() or "rule-based" in resp.text.lower()


def test_empty_and_punctuation_queries(bot):
    resp_empty = bot.process_message("")
    assert resp_empty.intent == Intent.UNKNOWN
    assert "Please type an AI question" in resp_empty.text

    resp_punct = bot.process_message("??? !!! ...")
    assert resp_punct.intent == Intent.UNKNOWN


def test_unicode_query(bot):
    resp = bot.process_message("“What is AI?”")
    assert resp.matched_topic is not None
    assert resp.matched_topic.id == "ai_definition"


def test_repeat_clarify(bot):
    bot.process_message("Define K-Means.")
    resp_repeat = bot.process_message("Repeat that please.")
    assert resp_repeat.intent == Intent.REPEAT_CLARIFY
    assert "K-Means" in resp_repeat.text
