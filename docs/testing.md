# Testing Documentation & Verification Guide

## 1. Overview

The AI KnowledgeBot test suite provides automated unit, regression, and end-to-end integration testing for all rule-based components. All tests are offline, deterministic, and execute without external network requests.

---

## 2. Test Suites Summary

| Test File | Target Component | Coverage Focus | Total Tests |
| :--- | :--- | :--- | :--- |
| `tests/test_normalizer.py` | `TextNormalizer` | Contractions, punctuation, Unicode normalization, whitespace, domain preservation (`A*`, hyphens) | 7 |
| `tests/test_tokenizer.py` | `Tokenizer` | Lexical tokenization, compound preservation, selective stopword filtering, n-gram windows | 5 |
| `tests/test_knowledge_base.py` | `KnowledgeBase` | All 8 modules loaded, 80 topics verified, field completeness, search, error handling for malformed/duplicate JSON | 5 |
| `tests/test_intent_classifier.py` | `IntentClassifier` | Deterministic intent classification (greetings, goodbye, help, modules, topics, define, explain, example, compare, formula, algorithm, unknown) | 9 |
| `tests/test_topic_matcher.py` | `TopicMatcher` | Exact alias matching, technical acronym boundaries (CNN, RNN, SVM, YOLO, A*, RAG), comparative pair extraction | 4 |
| `tests/test_chatbot_engine.py` | `AIKnowledgeBot` | End-to-end conversational flows, multi-turn follow-ups, unknown fallback queries, edge cases, repeat clarification | 15 |
| **Total** | **All Modules** | **Comprehensive System Validation** | **45 Tests** |

---

## 3. How to Execute Tests on Windows (PowerShell)

### Run all tests with verbose output:
```powershell
$env:PYTHONIOENCODING="utf-8"
python -m pytest -v
```

### Run specific test files:
```powershell
# Run end-to-end conversational integration tests
python -m pytest -v tests/test_chatbot_engine.py

# Run knowledge base schema validation tests
python -m pytest -v tests/test_knowledge_base.py

# Run NLP normalizer and tokenizer tests
python -m pytest -v tests/test_normalizer.py tests/test_tokenizer.py
```

### Run with short traceback / summary:
```powershell
python -m pytest --tb=short
```

---

## 4. Key Verified Scenarios

1. **"What is AI?"**: Correctly classified as `define_topic`, resolving to `ai_definition` with 1.0 confidence.
2. **"What are its branches?"**: Resolved via contextual pronoun follow-up to `ai_definition`, returning the 7 major branches of AI.
3. **"Explain NLP."**: Matches `nlp_fundamentals` via exact alias match.
4. **"Difference between AI and ML?"**: Correctly split into comparative pair `ai_definition` vs `ml_definition`, outputting a Markdown comparison table.
5. **"Give an example."**: Resolved against active conversational context without requiring repeated topic names.
6. **"Compare CNN and RNN."**: Extracts `dl_cnn` and `dl_rnn` into side-by-side comparison.
7. **"What is named entity recognition?"**: Matches `nlp_ner`.
8. **"Explain A* search."**: Correctly matches `search_astar` preserving the `*` symbol.
9. **"Show me deep learning topics."**: Correctly filters `module_c` topic listing.
10. **"What is the weather today?"**: Returns a transparent, non-hallucinating rule-based fallback response offering AI suggestions.
11. **Punctuation & Empty Queries**: Handled gracefully without runtime crashes.
