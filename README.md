# 🧠 AI KnowledgeBot — Rule-Based Artificial Intelligence Chatbot

> **A complete, deterministic educational AI chatbot and curriculum dashboard built with Python and Streamlit.**
>
> ⚡ **100% Rule-Based AI Engine** — Zero OpenAI / LLM API dependencies, zero cloud subscriptions, zero hallucinations, fully verifiable symbolic execution, and complete local offline support.

---

## 🌟 Key Features

### 1. Deterministic Rule-Based Response Engine
- **Syntactic & Pattern Matching:** Powered by explicit regular expressions, tokenization, n-gram windows, and multi-tier alias matching.
- **Context-Aware Follow-Up Handling:** Resolves pronoun and contextual queries like *"Give an example"*, *"What are its branches?"*, *"What are its limitations?"*, and *"Explain it"* against the preceding conversation topic.
- **Zero Hallucination Guarantee:** Responses strictly derive from structured, curated knowledge bases. Out-of-scope questions receive graceful educational fallbacks with topic recommendations.
- **Rule Engine Match Inspector:** Every assistant answer displays the active intent, triggered rule pattern, confidence score, and context resolution flag for complete auditability.

### 2. Comprehensive AI Curriculum (10 Modules, 117 In-Depth Topics)
- **Module A — AI Fundamentals & Problem Solving (7 topics):** Scratch block programming, Turing Test, Narrow AI vs AGI vs ASI, PEAS Agent framework, Rational Agents, Ethics & Bias.
- **Module B — Machine Learning Foundations (18 topics):** Supervised, Unsupervised, Reinforcement Learning, Decision Trees, Random Forests, XGBoost/Gradient Boosting, SVM, KNN, Naive Bayes, K-Means, Hierarchical Clustering, PCA, Feature Engineering, Evaluation Metrics, Bias-Variance Tradeoff.
- **Module C — Deep Learning & Neural Networks (11 topics):** Perceptrons, MLPs, Activation Functions, Forward & Backpropagation, Loss Functions, Optimizers (SGD, Adam), Regularization (Dropout, L1/L2), BatchNorm vs LayerNorm, RNNs, LSTMs/GRUs, Transformers.
- **Module D — Natural Language Processing (19 topics):** Text Preprocessing, Tokenization (BPE/WordPiece), Stemming & Lemmatization, Stopwords/POS, TF-IDF, Word2Vec, GloVe, Seq2Seq, Attention Mechanisms, Transformer Architecture, BERT, GPT, NER, Sentiment Analysis, Machine Translation, Summarization, Question Answering, Prompt Engineering, BLEU/ROUGE.
- **Module E — Computer Vision (7 topics):** Image Processing Fundamentals, Edge Detection & Filters, CNN Architecture, YOLO Object Detection, Semantic Segmentation (U-Net), Transfer Learning, ResNet & Residual Connections.
- **Module F — Knowledge-Based AI & Symbolic Reasoning (9 topics):** Expert Systems (MYCIN), Knowledge Representation, Forward Chaining, Backward Chaining, Rule Engines, Semantic Networks, Ontologies & OWL, Fuzzy Logic, Case-Based Reasoning.
- **Module G — Search, Planning & Robotics (8 topics):** BFS & DFS, Heuristic A* Search, Minimax Algorithm, Alpha-Beta Pruning, Constraint Satisfaction (CSP), Markov Decision Processes (MDP), Q-Learning, Robot Kinematics & SLAM.
- **Module H — Generative AI, LLMs & Exhaustive GANs (28 topics):**
  - **GAN Deep Dive:** Foundations & Minimax Game, Non-Saturating Loss, Mode Collapse & Vanishing Gradients, DCGAN, Wasserstein GAN (Earth Mover's Distance), WGAN-GP (Gradient Penalty), Conditional GANs (cGAN), Pix2Pix, CycleGAN, StyleGAN (AdaIN & latent spaces), Progressive GAN, PyTorch Training Workflow, DiffAugment, Inception Score & FID Evaluation, Deepfake Forensics & Ethics.
  - **Variational & Diffusion Models:** VAEs, Latent Spaces, Autoregressive Models, Diffusion (DDPM), Latent Diffusion Models (Stable Diffusion).
  - **LLMs & Multimodal:** Multimodal CLIP & DALL-E, Pretraining & Fine-Tuning, LoRA & PEFT, RAG Architecture, Hallucination Mitigation.
- **Module I — Mathematics & Data Foundations for AI (4 topics):** Linear Algebra (Vectors, Matrices, SVD), Multivariable Calculus & Gradient Descent, Probability & Statistics (Bayes' Theorem, Distributions), Python for AI (NumPy, Pandas, PyTorch).
- **Module J — Autonomous Agents, Multimodal & MLOps (6 topics):** ReAct Prompting & Tool Calling, Multi-Agent Coordination, Vision-Language Models, MLOps Pipelines & CI/CD, Model Quantization & Serving (ONNX, TensorRT), AI Safety & Adversarial Robustness.

### 3. Modern Interactive UI (Streamlit)
- **💬 AI Knowledge Chat:** Modern dark navy/slate dashboard with quick-start prompt cards, chat bubbles, clickable follow-up chips, and expandable rule match inspector.
- **⚖️ Automated Topic Comparison Tool:** Select any two topics from the 117-topic directory to generate instant side-by-side comparison tables.
- **🧠 Interactive AI Quiz Mode:** 12 curriculum multiple-choice questions with instant scoring, feedback, and pedagogical explanations.
- **📚 Curriculum Explorer:** Full directory browser across all 10 modules and 117 topics with KaTeX mathematical formulas and algorithm steps.
- **💾 Conversation Export:** Download the conversation history as formatted **JSON** or **Markdown/TXT**.

---

## 🚀 How to Run the Project

### Prerequisites
- **Python 3.10+** (Python 3.11, 3.12, or 3.13 tested and supported)
- Standard PowerShell / Command Prompt on Windows (or Bash on macOS/Linux)

---

### Step 1: Open Terminal & Navigate to the Project
```powershell
cd d:\Lingo_AI
```
*(On macOS/Linux: `cd /path/to/Lingo_AI`)*

---

### Step 2: (Recommended) Create and Activate Virtual Environment
On Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
*(If script execution is disabled in PowerShell, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Step 3: Install Required Dependencies
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

### Step 4: Run the Streamlit Web Application
```powershell
python -m streamlit run app.py
```
Or simply:
```powershell
streamlit run app.py
```

The app will start and automatically open in your default browser:
👉 **`http://localhost:8501`**

---

### Step 5: (Optional) Run via Interactive CLI Mode
You can also interact directly with the rule-based knowledge engine in your terminal:
```powershell
python -m src.cli
```
Type any AI query (e.g., `What is DCGAN?`, `Explain Mode Collapse`, `Difference between CNN and RNN`), or type `quit` to exit.

---

## 🧪 Running Automated Tests

Run the full automated test suite with pytest:

On Windows (PowerShell):
```powershell
$env:PYTHONIOENCODING="utf-8"
python -m pytest -v
```

On macOS/Linux:
```bash
python -m pytest -v
```

### What the 46 Tests Validate:
1. **Text Normalization:** Contractions expansion, whitespace trimming, Unicode accents, punctuation handling, and compound/symbol preservation (`A*`, `C++`, `L1/L2`).
2. **Tokenizer & N-grams:** Unigrams, bigrams, trigrams, 4-grams, and stopword filtering.
3. **Knowledge Base Schema & Integrity:** All 10 modules and 117 topics checked for non-empty definitions, explanations, examples, formulas, and relationship mappings.
4. **Intent Classifier:** 10 core intents (greeting, goodbye, help, list, define, explain, example, compare, formula, unknown).
5. **Topic Matcher & Regex Precedence:** Acronym handling (GAN, DCGAN, WGAN, VAE, CNN, RNN, SVM, YOLO, RAG) and prevention of greedy false positives.
6. **GAN Queries & Contextual Multi-Turn Flows:** Conversational pronoun resolution (`"explain it"`, `"give an example"`, `"how does it train"`).
7. **Zero-Hallucination Boundaries:** Graceful out-of-domain query handling with suggested topic alternatives.

---

## 📂 Project Structure

```
d:\Lingo_AI\
├── app.py                             # Streamlit modern frontend application
├── requirements.txt                   # Project dependencies (streamlit, pytest)
├── README.md                          # Complete overview and execution guide
├── .gitignore                         # Version control exclusions
│
├── knowledge_base/                    # Modular JSON Knowledge Bases (117 topics)
│   ├── module_a_fundamentals.json
│   ├── module_b_machine_learning.json
│   ├── module_c_deep_learning.json
│   ├── module_d_nlp.json
│   ├── module_e_computer_vision.json
│   ├── module_f_knowledge_based_ai.json
│   ├── module_g_search_planning.json
│   ├── module_h_generative_ai.json    # Exhaustive GANs, VAEs, Diffusion, LLMs
│   ├── module_i_mathematics_data_foundations.json
│   └── module_j_agents_multimodal_mlops.json
│
├── src/
│   ├── cli.py                         # Standalone interactive terminal chatbot
│   ├── engine/                        # Core Deterministic Rule Engine
│   │   ├── chatbot.py                 # Central orchestrator & dialog manager
│   │   ├── conversation_manager.py    # Conversation state & pronoun resolver
│   │   ├── intent_classifier.py       # Regex rule intent detection
│   │   ├── knowledge_base.py          # Knowledge loader, search & verification
│   │   ├── response_generator.py      # Structured template response composer
│   │   └── topic_matcher.py           # Multi-tier topic matcher & regex rules
│   ├── nlp/
│   │   ├── normalizer.py              # Text cleaning & symbol normalizer
│   │   └── tokenizer.py               # Tokenization & n-gram extractor
│   └── ui/
│       ├── quiz_data.py               # 12 interactive multiple-choice questions
│       └── styles.py                  # Modern Dark Navy design system CSS
│
├── tests/                             # Automated test suite (46 pytest tests)
│   ├── test_chatbot_engine.py
│   ├── test_intent_classifier.py
│   ├── test_knowledge_base.py
│   ├── test_normalizer.py
│   ├── test_tokenizer.py
│   └── test_topic_matcher.py
│
└── docs/                              # Detailed Technical Documentation
    ├── architecture.md                # System design & pipeline specification
    ├── AI_CURRICULUM_AUDIT.md         # Curriculum audit matrix across 17 domains
    ├── knowledge-base.md              # JSON schema specification & guide
    └── testing.md                     # Test strategy & validation cases
```

---

## 💬 Example Queries Supported

| User Query | Engine Intent | Behavior |
| :--- | :--- | :--- |
| **"What is AI?"** | `define` | Returns definition, history, and core branches of Artificial Intelligence. |
| **"What are its branches?"** | `explain` (Contextual) | Resolves *"its"* to AI; details ML, DL, NLP, CV, Symbolic AI, and Robotics. |
| **"Explain GANs."** | `explain` | Details Generator vs Discriminator minimax game, equations, and applications. |
| **"What is Mode Collapse in GANs?"**| `define` | Explains generator output diversity failure, math, and mitigation techniques. |
| **"Explain Wasserstein GAN."** | `explain` | Explains Earth Mover's Distance, 1-Lipschitz continuity, and WGAN-GP. |
| **"Difference between CNN and RNN?"**| `compare` | Generates a structured comparison table (spatial vs sequential processing). |
| **"Explain A* search."** | `explain` | Preserves `*` token; explains $f(n)=g(n)+h(n)$ and admissibility. |
| **"What is ReAct in AI agents?"** | `explain` | Details Reason + Act loop, tool-calling, and reasoning traces. |
| **"What is the weather today?"** | `unknown` | Transparent fallback: explains boundaries and suggests relevant AI topics. |

---

## ⚖️ Limitations & Design Principles

- **Zero-Cloud & Zero-Hallucination:** Operates completely offline without external API keys or cloud tokens.
- **Explainability:** Every generated answer displays an expandable Rule Match Inspector showing the detected intent, matched pattern, confidence score, and contextual resolution status.
- **Deterministic Bounds:** If a topic falls outside the 117 curriculum topics, the bot gracefully informs the user and provides actionable topic recommendations instead of fabricating untruthful content.

---

## 📄 License

This project is released under the **MIT License**.
