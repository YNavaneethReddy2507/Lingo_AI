# 🧠 AI KnowledgeBot — Rule-Based Artificial Intelligence Chatbot

> **A complete, deterministic educational AI chatbot and curriculum dashboard built with Python and Streamlit.**
>
> ⚡ **100% Rule-Based AI Engine** — Zero OpenAI / LLM API dependencies, zero cloud subscriptions, zero hallucinations, fully verifiable symbolic execution, and complete local offline support on Windows.

---

## 🌟 Key Features

### 1. Deterministic Rule-Based Response Engine
- **Syntactic & Pattern Matching:** Powered by explicit regular expressions, tokenization, n-gram windows, and multi-tier alias matching.
- **Context-Aware Follow-Up Handling:** Resolves pronoun and contextual queries like *"Give an example"*, *"What are its branches?"*, *"What are its limitations?"*, and *"Explain it"* against the preceding conversation topic.
- **Zero Hallucination Guarantee:** Responses strictly derive from structured, curated knowledge bases. Out-of-scope questions receive graceful educational fallbacks with topic recommendations.
- **Rule Engine Match Inspector:** Every assistant answer displays the active intent, triggered rule pattern, confidence score, and context resolution flag for complete auditability.

### 2. Comprehensive AI Curriculum (8 Modules, 80 Topics)
- **Module A — AI Fundamentals:** History (Turing, Dartmouth), Narrow AI vs AGI vs ASI, PEAS Agent framework, Rational Agents, Ethics.
- **Module B — Machine Learning:** Supervised, Unsupervised, Semi-Supervised, Reinforcement Learning, Decision Trees, Naive Bayes, SVM, K-Means, Train/Val/Test splits, Bias-Variance tradeoff.
- **Module C — Deep Learning:** ANNs, Neurons, Weights & Biases, Activation Functions (ReLU, Sigmoid, Softmax), Forward & Backpropagation, Gradient Descent (SGD, Adam), CNNs, RNNs, LSTMs, Transformers & Self-Attention.
- **Module D — Natural Language Processing:** Normalization, Tokenization (BPE), Regex, POS Tagging, Named Entity Recognition (NER), Rule-Based NER, HMMs & Viterbi, N-grams & Smoothing, Word2Vec & GloVe, TF-IDF, Cosine Similarity, Text Classification, Sentiment Analysis (VADER).
- **Module E — Computer Vision:** Image Classification, Object Detection, Semantic & Instance Segmentation (U-Net), CNN feature extractors, YOLO Real-Time Detection, Image Preprocessing & Augmentation.
- **Module F — Knowledge-Based AI:** Knowledge Representation, Expert Systems (MYCIN), Facts & Rules, Inference Engines, Forward Chaining, Backward Chaining, Propositional & First-Order Logic, Pros & Cons of Symbolic AI.
- **Module G — Search, Planning & Robotics:** State-Space Search, BFS, DFS, Uniform-Cost Search (Dijkstra), Greedy Best-First, A* Search & Heuristics, STRIPS/PDDL Automated Planning, SLAM & Robotics.
- **Module H — Generative AI:** Foundation Models, LLMs (Pre-training, SFT, RLHF), Prompt Engineering (Few-Shot, CoT), Retrieval-Augmented Generation (RAG), Dense Embeddings, Hallucination Mitigation, Responsible AI.

### 3. Modern Interactive UI (Streamlit)
- **💬 AI Knowledge Chat:** Modern dark navy/slate dashboard with quick-start prompt cards, chat bubbles, clickable follow-up chips, and expandable rule match inspector.
- **⚖️ Automated Topic Comparison Tool:** Select any two topics from the 80-topic directory to generate instant side-by-side comparison tables.
- **🧠 Interactive AI Quiz Mode:** 8 curriculum multiple-choice questions with instant scoring, feedback, and pedagogical explanations.
- **📚 Curriculum Explorer:** Full directory browser across all 8 modules and 80 topics.
- **💾 Conversation Export:** Download the conversation history as formatted **JSON** or **Markdown/TXT**.

---

## 🛠️ Tech Stack & Architecture

- **Language:** Python 3.11+ / Python 3.13 (compatible with standard local Python on Windows)
- **Frontend:** Streamlit 1.30+ with custom CSS styling
- **Engine:** Python standard library (`re`, `json`, `dataclasses`, `unicodedata`, `os`, `sys`, `glob`)
- **Testing:** Pytest 7.0+ (45 automated unit & integration tests)
- **Knowledge Base:** 8 modular JSON files in `knowledge_base/`

For detailed technical specifications, see [docs/architecture.md](file:///d:/Lingo_AI/docs/architecture.md).

---

## 🚀 Quick Start on Windows (PowerShell)

### Step 1: Clone or Navigate to the Workspace
```powershell
cd d:\Lingo_AI
```

### Step 2: (Optional) Create & Activate a Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```powershell
python -m pip install -r requirements.txt
```

### Step 4: Run the Application
```powershell
python -m streamlit run app.py
```
The application will launch automatically in your default browser at:
👉 **`http://localhost:8501`**

---

## 🧪 Running Automated Tests

Run the full automated test suite (45 tests) with pytest:

```powershell
$env:PYTHONIOENCODING="utf-8"
python -m pytest -v
```

All 45 tests validate:
- Text normalization (contractions, whitespace, Unicode, punctuation, symbol preservation).
- Tokenization & n-gram generation.
- Schema integrity of all 80 topics in the knowledge base.
- Deterministic regex intent classification.
- Multi-tier topic matching & acronym handling (CNN, RNN, SVM, YOLO, A*, RAG).
- Multi-turn conversation flows and contextual follow-up pronoun resolution.
- Safe unknown-query fallback behavior (ensuring no false answers are fabricated).

For complete testing documentation, see [docs/testing.md](file:///d:/Lingo_AI/docs/testing.md).

---

## 📂 Project Structure

```
d:\Lingo_AI\
├── app.py                      # Main Streamlit web application
├── requirements.txt            # Python dependencies manifest
├── .gitignore                  # Git exclusions
├── README.md                   # Project overview & documentation
├── knowledge_base/             # Structured JSON curriculum files
│   ├── module_a_fundamentals.json
│   ├── module_b_machine_learning.json
│   ├── module_c_deep_learning.json
│   ├── module_d_nlp.json
│   ├── module_e_computer_vision.json
│   ├── module_f_knowledge_based_ai.json
│   ├── module_g_search_planning.json
│   └── module_h_generative_ai.json
├── src/
│   ├── nlp/                    # Text Normalizer & Tokenizer
│   ├── engine/                 # Core Rule Engine, KnowledgeBase, Intent & Topic Matchers
│   └── ui/                     # CSS Styles, UI Components, Quiz Questions
├── tests/                      # Automated test suite (45 tests)
└── docs/                       # Technical architecture & knowledge base guides
```

---

## 💬 Example Conversations Supported

| User Query | KnowledgeBot Behavior |
| :--- | :--- |
| **"What is AI?"** | Returns formal definition, goals, and core branches of Artificial Intelligence. |
| **"What are its branches?"** | Resolves pronoun *"its"* to AI; details ML, DL, NLP, CV, Knowledge-Based AI, and Robotics. |
| **"Explain NLP."** | Defines Natural Language Processing and explains computational linguistics levels. |
| **"Difference between AI and ML?"** | Generates a structured side-by-side comparison table highlighting taxonomy and differences. |
| **"Give an example."** | Resolves follow-up context against active topic and outputs a real-world use case. |
| **"Compare CNN and RNN."** | Extracts both architectures and compares spatial vs temporal processing. |
| **"Explain A* search."** | Preserves `*` token, explains $f(n)=g(n)+h(n)$, and details admissibility criteria. |
| **"What is the weather today?"** | Transparent fallback: explains rule-based bounds and suggests relevant AI topics. |

---

## ⚖️ Limitations & Design Principles

- **Knowledge Boundary:** As a rule-based system, answers are limited to the topics in the knowledge base. It does not browse the live web or fabricate unverified claims.
- **Deterministic Rules:** Uses explicit regular expressions, grammatical patterns, and keyword scoring rather than stochastic neural generation.
- **Explainable by Design:** Decisions are 100% traceable to source rules and structured records.
