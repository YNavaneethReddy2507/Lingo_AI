# Knowledge Base Guide: Schema, Coverage & Contribution

## 1. Overview

The AI KnowledgeBot knowledge base is structured into modular JSON files stored in `knowledge_base/`. Each file corresponds to one of the 10 academic modules specified in the curriculum (117 total topics).

At startup, the knowledge base is validated:
- Schema completeness.
- Unique topic and module IDs.
- Non-empty definitions, explanations, and examples.
- Bidirectional or referenced topic relationship integrity.

---

## 2. Topic Schema Definition

Every topic entry in a module JSON file must adhere to this schema:

```json
{
  "id": "nlp_ner",
  "name": "Named Entity Recognition (NER)",
  "category": "Module D — Natural Language Processing",
  "category_id": "module_d",
  "aliases": [
    "ner",
    "named entity recognition",
    "entity extraction",
    "entity recognition"
  ],
  "keywords": [
    "ner",
    "named entity recognition",
    "entity",
    "person",
    "organization",
    "location",
    "iob tagging",
    "bio"
  ],
  "definition": "Named Entity Recognition is an information extraction subtask that identifies and classifies key entity mentions in unstructured text into predefined categories.",
  "explanation": "NER formulates entity detection as a sequence labeling problem...",
  "example": "In \"Google opened an office in Hyderabad on Monday\", NER identifies [Google: ORGANIZATION], [Hyderabad: LOCATION], and [Monday: DATE].",
  "formula": "\\hat{y} = \\arg\\max_y \\sum_{i=1}^n (A_{y_{i-1}, y_i} + P_{i, y_i})",
  "algorithm_steps": [
    "Preprocess and tokenize input text",
    "Extract linguistic features",
    "Predict entity boundary and class tag (BIO format)",
    "Assemble contiguous entity chunks"
  ],
  "advantages": [
    "Transforms raw unstructured text into structured relational entities"
  ],
  "limitations": [
    "Entity ambiguity (e.g. 'Washington' person vs state)"
  ],
  "applications": [
    "Financial intelligence",
    "Biomedical literature mining"
  ],
  "related_topics": [
    "nlp_rule_based_ner",
    "nlp_information_extraction",
    "nlp_pos"
  ],
  "suggested_followups": [
    "What is Rule-based NER?",
    "Explain the BIO tagging scheme.",
    "What is Information Extraction?"
  ]
}
```

---

## 3. Curriculum Modules & Topics (117 Topics Total across 10 Modules)

### Module A — AI Fundamentals (`module_a_fundamentals.json`)
- `ai_definition`: Definition, Goals, and Branches of AI
- `ai_history`: History & Evolution (Turing Test, Dartmouth 1956, AI Winters)
- `ai_narrow_vs_general`: Narrow AI (ANI) vs General AI (AGI) vs Superintelligence (ASI)
- `ai_agents_environments`: Intelligent Agents & PEAS Framework
- `ai_rational_agents`: Rational Agents & Expected Utility
- `ai_ethics_limitations`: Applications, Limitations, and Ethical Concerns

### Module B — Machine Learning (`module_b_machine_learning.json`)
- `ml_definition`: Definition & Relationship between AI and ML
- `ml_supervised`: Supervised Learning Paradigm
- `ml_unsupervised`: Unsupervised Learning Paradigm
- `ml_semi_supervised`: Semi-Supervised Learning & Pseudo-labeling
- `ml_reinforcement`: Reinforcement Learning, MDPs, and Q-Learning
- `ml_classification_regression`: Classification vs Regression
- `ml_clustering`: Clustering Foundations
- `ml_decision_trees`: Decision Trees, Entropy, and Gini Impurity
- `ml_naive_bayes`: Naive Bayes & Conditional Independence
- `ml_svm`: Support Vector Machines & Kernel Trick
- `ml_kmeans`: K-Means Clustering & Centroid Updates
- `ml_train_val_test`: Training, Validation, and Testing Splits
- `ml_overfitting_evaluation`: Overfitting, Underfitting, Bias-Variance, ROC-AUC

### Module C — Deep Learning (`module_c_deep_learning.json`)
- `dl_ann`: Artificial Neural Networks & Universal Approximation
- `dl_neurons_layers`: Neurons, Layers, Weights, and Biases
- `dl_activation_functions`: Activation Functions (ReLU, Sigmoid, Tanh, Softmax)
- `dl_forward_prop`: Forward Propagation Pipeline
- `dl_backprop`: Backpropagation & Calculus Chain Rule
- `dl_gradient_descent`: Gradient Descent & Adaptive Optimizers (SGD, Adam)
- `dl_cnn`: Convolutional Neural Networks Architecture
- `dl_rnn`: Recurrent Neural Networks & Temporal Modeling
- `dl_lstm_gru`: LSTM, GRU, and Gating Mechanisms
- `dl_transformers_attention`: Transformers & Scaled Dot-Product Attention
- `dl_applications_limitations`: Deep Learning Applications & Opacity

### Module D — Natural Language Processing (`module_d_nlp.json`)
- `nlp_fundamentals`: NLP Foundations & Linguistic Levels
- `nlp_corpus`: Corpus Construction & Inter-Annotator Agreement
- `nlp_normalization_segmentation`: Text Normalization, Stemming & Lemmatization
- `nlp_tokenization`: Tokenization & Subword Methods (BPE, WordPiece)
- `nlp_regex`: Regular Expressions in NLP
- `nlp_pos`: Part-of-Speech (POS) Tagging & Tagsets
- `nlp_ner`: Named Entity Recognition (NER)
- `nlp_rule_based_ner`: Rule-Based NER & Gazetteers
- `nlp_hmm`: Hidden Markov Models & Viterbi Decoding
- `nlp_ngrams_smoothing`: N-gram Language Modeling & Smoothing
- `nlp_word2vec_glove`: Word Embeddings (Word2Vec, Skip-Gram, CBOW, GloVe)
- `nlp_vector_space_model`: Vector Space Model & Term-Document Matrices
- `nlp_tfidf`: TF-IDF Term Weighting
- `nlp_cosine_similarity`: Cosine Similarity Metric
- `nlp_text_classification`: Text Classification Algorithms
- `nlp_text_clustering`: Text Clustering & Topic Discovery (LDA)
- `nlp_text_summarization`: Extractive vs Abstractive Summarization
- `nlp_information_extraction`: Information Extraction & Relation Triples
- `nlp_sentiment_analysis`: Sentiment Analysis & Opinion Mining (VADER)

### Module E — Computer Vision (`module_e_computer_vision.json`)
- `cv_image_classification`: Image Classification & ImageNet
- `cv_object_detection`: Object Detection & Bounding Boxes
- `cv_image_segmentation`: Semantic vs Instance vs Panoptic Segmentation (U-Net)
- `cv_cnn`: Convolutional Feature Extraction in CV
- `cv_yolo`: YOLO (You Only Look Once) Real-Time Detection
- `cv_preprocessing`: Image Preprocessing & Data Augmentation
- `cv_applications_limitations`: Vision Applications & Adversarial Vulnerabilities

### Module F — Knowledge-Based AI (`module_f_knowledge_based_ai.json`)
- `kb_knowledge_representation`: Knowledge Representation & Semantic Nets
- `kb_rule_based_systems`: Rule-Based Systems Architecture
- `kb_expert_systems`: Expert Systems & MYCIN History
- `kb_facts_and_rules`: Facts, Rules, and Working Memory
- `kb_inference_engines`: Inference Engines & Pattern Matching
- `kb_forward_chaining`: Forward Chaining (Data-Driven Reasoning)
- `kb_backward_chaining`: Backward Chaining (Goal-Driven Reasoning)
- `kb_logic`: Propositional and First-Order Predicate Logic
- `kb_rule_based_pros_cons`: Advantages & Limitations of Rule-Based AI

### Module G — Search, Planning, and Robotics (`module_g_search_planning.json`)
- `search_state_space`: State-Space Problem Formulation
- `search_bfs`: Breadth-First Search (BFS)
- `search_dfs`: Depth-First Search (DFS)
- `search_ucs`: Uniform-Cost Search (UCS / Dijkstra)
- `search_greedy_best_first`: Greedy Best-First Search
- `search_astar`: A* Search & Admissible Heuristics
- `search_planning`: Automated Planning (STRIPS & PDDL)
- `search_robotics`: Robotics, SLAM, and Autonomous Physical Agents

### Module H — Generative AI, LLMs & Advanced Architectures (`module_h_generative_ai.json` - 28 Topics)
- **GAN Suite:** `genai_gan_foundations`, `gan_mode_collapse`, `gan_dcgan`, `gan_wgan`, `gan_wgan_gp`, `gan_cgan`, `gan_pix2pix`, `gan_cyclegan`, `gan_stylegan`, `gan_pytorch_workflow`, `gan_diffaugment`, `gan_evaluation_metrics`, `gan_ethics_deepfakes`.
- **VAEs & Diffusion:** `genai_vae_foundations`, `genai_latent_spaces`, `genai_autoregressive`, `genai_diffusion_models`, `genai_latent_diffusion`.
- **Multimodal & LLMs:** `genai_multimodal_clip`, `genai_multimodal_dalle`, `genai_llm_pretraining_finetuning`, `genai_lora_peft`, `genai_rag_architecture`, `genai_hallucination_mitigation`.

### Module I — Mathematics & Data Foundations (`module_i_mathematics_data_foundations.json` - 4 Topics)
- `math_linear_algebra`: Vectors, Matrices, Eigenvalues, SVD, Tensors.
- `math_calculus_optimization`: Partial Derivatives, Gradients, Jacobians, Optimization.
- `math_probability_statistics`: Probability Distributions, Bayes' Theorem, MLE.
- `python_ai_foundations`: NumPy Vectorization, Pandas, PyTorch Tensors.

### Module J — Autonomous Agents, Multimodal & MLOps (`module_j_agents_multimodal_mlops.json` - 6 Topics)
- `agents_react_tool_calling`: ReAct Prompting & Tool Calling.
- `agents_multi_agent`: Multi-Agent Systems & Coordination.
- `multimodal_vision_language`: Vision-Language Foundation Models.
- `mlops_foundations`: MLOps CI/CD, Experiment Tracking, Model Registries.
- `mlops_optimization_serving`: ONNX, TensorRT, Quantization & Serving.
- `safety_adversarial_jailbreaks`: Adversarial Robustness, Red-Teaming & Guardrails.

---

## 4. How to Add or Edit Topics

1. Open the relevant JSON file in `knowledge_base/`.
2. Ensure the new topic ID is unique across all modules.
3. Populate all required fields (`id`, `name`, `category`, `category_id`, `aliases`, `keywords`, `definition`, `explanation`, `example`).
4. Optionally provide `formula`, `algorithm_steps`, `advantages`, `limitations`, `applications`, `related_topics`, and `suggested_followups`.
5. Run the validation test suite:
   ```powershell
   $env:PYTHONIOENCODING="utf-8"; python -m pytest tests/test_knowledge_base.py
   ```
