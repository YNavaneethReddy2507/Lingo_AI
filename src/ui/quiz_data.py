"""Curated rule-based quiz bank for AI KnowledgeBot educational testing."""

QUIZ_QUESTIONS = [
    {
        "id": "q1",
        "module": "Module A — AI Fundamentals",
        "question": "What is the primary distinction between Narrow AI (ANI) and General AI (AGI)?",
        "options": [
            "Narrow AI is rule-based, while General AI uses neural networks.",
            "Narrow AI excels at a single specific task, while General AI possesses human-level cognitive flexibility across all domains.",
            "Narrow AI runs in the cloud, while General AI runs on edge devices.",
            "Narrow AI requires reinforcement learning, while General AI does not."
        ],
        "answer_index": 1,
        "explanation": "Current AI is Narrow AI (ANI), performing dedicated bounded tasks like chess or speech recognition. General AI (AGI) refers to hypothetical systems capable of learning and abstract reasoning across any domain like a human."
    },
    {
        "id": "q2",
        "module": "Module B — Machine Learning",
        "question": "Why is the Naive Bayes classifier called 'Naive'?",
        "options": [
            "It does not use probability theory.",
            "It assumes all input features are conditionally independent given the class label.",
            "It cannot be used for text classification.",
            "It requires zero training data."
        ],
        "answer_index": 1,
        "explanation": "It naively assumes feature conditional independence P(X|C) = prod P(x_i|C), which rarely holds in real-world data (e.g. words in a sentence correlate strongly)."
    },
    {
        "id": "q3",
        "module": "Module C — Deep Learning",
        "question": "What mathematical principle enables backpropagation to compute gradients efficiently across deep layers?",
        "options": [
            "Bayes Theorem",
            "The Chain Rule of calculus",
            "Euler's formula",
            "Central Limit Theorem"
        ],
        "answer_index": 1,
        "explanation": "Backpropagation uses the calculus Chain Rule to compute partial derivatives of loss with respect to all weights and biases via reverse-mode automatic differentiation in linear time."
    },
    {
        "id": "q4",
        "module": "Module D — Natural Language Processing",
        "question": "In TF-IDF, what happens to the weight of common stopwords like 'the' and 'is'?",
        "options": [
            "Their weight is doubled because they appear frequently.",
            "Their IDF value approaches zero because they appear in almost every document, effectively penalizing them.",
            "They cause division by zero errors.",
            "They are converted to dense vector embeddings."
        ],
        "answer_index": 1,
        "explanation": "IDF = log(N / DF). When document frequency DF approaches total document count N, N/DF approaches 1, and log(1) = 0, mathematically neutralizing ubiquitous uninformative words."
    },
    {
        "id": "q5",
        "module": "Module E — Computer Vision",
        "question": "How does YOLO achieve real-time object detection speed compared to Faster R-CNN?",
        "options": [
            "YOLO only detects one object per image.",
            "YOLO frames detection as a single regression pass over an SxS grid, eliminating the slow separate region proposal step.",
            "YOLO converts images to grayscale before convolution.",
            "YOLO uses decision trees instead of neural networks."
        ],
        "answer_index": 1,
        "explanation": "Single-stage YOLO processes the entire image in one unified neural forward pass, predicting bounding boxes and class probabilities simultaneously at up to 60-150+ FPS."
    },
    {
        "id": "q6",
        "module": "Module F — Knowledge-Based AI",
        "question": "Which reasoning strategy begins with a target hypothesis and works backward to locate supporting facts?",
        "options": [
            "Forward Chaining",
            "Backward Chaining",
            "Gradient Descent",
            "Breadth-First Search"
        ],
        "answer_index": 1,
        "explanation": "Backward Chaining is goal-driven (top-down), verifying hypotheses by setting antecedents as subgoals, foundational in diagnostic expert systems and Prolog."
    },
    {
        "id": "q7",
        "module": "Module G — Search, Planning & Robotics",
        "question": "Under what condition is A* graph search guaranteed to return the optimal lowest-cost path?",
        "options": [
            "When the heuristic h(n) is consistent (monotonic) and never overestimates the true remaining cost (admissible).",
            "When the branching factor b is equal to 1.",
            "When the search is unguided without heuristics.",
            "When using a LIFO stack frontier."
        ],
        "answer_index": 0,
        "explanation": "Admissibility (h(n) <= h*(n)) ensures optimality in tree search; consistency (satisfying triangle inequality) ensures optimality in graph search without reopening closed nodes."
    },
    {
        "id": "q8",
        "module": "Module H — Generative AI",
        "question": "What is the primary objective of Retrieval-Augmented Generation (RAG)?",
        "options": [
            "To train a new foundation model from scratch using reinforcement learning.",
            "To retrieve authoritative source documents from an external vector store to ground LLM generation and mitigate hallucinations.",
            "To convert text prompt tokens into high-resolution images.",
            "To eliminate the need for vector databases."
        ],
        "answer_index": 1,
        "explanation": "RAG injects relevant real-time or proprietary knowledge passages directly into the prompt context, grounding language models in verified facts and eliminating confabulations."
    }
]
