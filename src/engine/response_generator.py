"""Template and structured response generation for AI KnowledgeBot."""
from typing import List, Optional

from src.engine.knowledge_base import KnowledgeBase
from src.engine.models import Intent, Module, Topic


class ResponseGenerator:
    """Generates structured educational markdown responses using predefined templates and knowledge entries."""

    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def format_greeting(self) -> str:
        """Welcome greeting introducing the bot and rule-based architecture."""
        return (
            "### 👋 Welcome to AI KnowledgeBot!\n\n"
            "I am a **100% Rule-Based Artificial Intelligence Educational Assistant**. "
            "Unlike large language models, my answers are generated using **explicit deterministic rules**, "
            "syntactic parsing, keyword matching, and a curated structured knowledge base — "
            "guaranteeing **zero hallucinations** and complete explainability!\n\n"
            "#### 📚 What I Cover (8 Core AI Modules):\n"
            "1. **Module A** — AI Fundamentals & History\n"
            "2. **Module B** — Machine Learning (Supervised, Unsupervised, RL)\n"
            "3. **Module C** — Deep Learning (ANN, CNN, RNN, Transformers)\n"
            "4. **Module D** — Natural Language Processing (Tokenization, NER, TF-IDF)\n"
            "5. **Module E** — Computer Vision (Classification, YOLO, Segmentation)\n"
            "6. **Module F** — Knowledge-Based AI (Expert Systems, Logic, Chaining)\n"
            "7. **Module G** — Search, Planning & Robotics (A*, Heuristics, SLAM)\n"
            "8. **Module H** — Generative AI (LLMs, Prompt Engineering, RAG)\n\n"
            "💡 *Try asking:* **\"What is AI?\"**, **\"Difference between AI and ML?\"**, or **\"Explain A* search\"**."
        )

    def format_goodbye(self) -> str:
        """Goodbye message."""
        return (
            "### 👋 Goodbye!\n\n"
            "Thank you for exploring Artificial Intelligence with **AI KnowledgeBot**. "
            "Come back anytime to study algorithms, formulas, or compare AI paradigms!"
        )

    def format_help(self) -> str:
        """Detailed help guide explaining syntax and supported queries."""
        return (
            "### 📖 AI KnowledgeBot User Guide\n\n"
            "You can query me using natural language phrases, keywords, or explicit commands:\n\n"
            "| Query Type | Example Prompt |\n"
            "| :--- | :--- |\n"
            "| **Definitions** | `What is AI?`, `Define Named Entity Recognition` |\n"
            "| **Explanations** | `Explain Machine Learning`, `Tell me about Transformers` |\n"
            "| **Comparisons** | `Difference between AI and ML?`, `Compare CNN and RNN` |\n"
            "| **Examples** | `Give an example`, `Example of Supervised Learning` |\n"
            "| **Formulas** | `Show formula for TF-IDF`, `Equation for A* search` |\n"
            "| **Algorithms** | `How does K-Means algorithm work?`, `Steps of BFS` |\n"
            "| **Pros & Cons** | `Advantages of Rule-Based AI`, `Limitations of Deep Learning` |\n"
            "| **Applications** | `Applications of Computer Vision`, `Where is YOLO used?` |\n"
            "| **Branches** | `What are its branches?`, `Branches of AI` |\n"
            "| **Listings** | `List all modules`, `Show topics in Deep Learning` |\n"
            "| **Recommendations**| `What should I learn next?`, `Recommend a topic` |\n\n"
            "💡 *Contextual follow-ups are supported:* After asking *\"What is AI?\"*, you can simply say *\"Give an example\"* or *\"What are its branches?\"*."
        )

    def format_module_list(self) -> str:
        """Lists all 8 knowledge base modules."""
        modules = self.kb.get_all_modules()
        lines = ["### 🗂️ Artificial Intelligence Curriculum Modules\n"]
        for mod in modules:
            topic_count = len(mod.topic_ids)
            lines.append(f"#### 🔹 {mod.name} ({topic_count} Topics)")
            lines.append(f"{mod.description}\n")
        lines.append("👉 *To view topics in any category, type:* **`Show topics in Module A`** or **`List Deep Learning topics`**.")
        return "\n".join(lines)

    def format_topic_list(self, module_filter: Optional[str] = None) -> str:
        """Lists topics, optionally filtered by module name or ID."""
        if module_filter:
            # Find matching module
            norm_filter = module_filter.lower()
            matched_mod = None
            for mod in self.kb.get_all_modules():
                if norm_filter in mod.id.lower() or norm_filter in mod.name.lower():
                    matched_mod = mod
                    break

            if matched_mod:
                topics = self.kb.get_topics_by_module(matched_mod.id)
                lines = [f"### 📋 Topics in {matched_mod.name}\n"]
                for t in topics:
                    lines.append(f"- **{t.name}** (`{t.id}`): {t.definition}")
                return "\n".join(lines)

        # List all modules and topics summarized
        lines = ["### 📋 Complete AI KnowledgeBot Topic Directory\n"]
        for mod in self.kb.get_all_modules():
            topics = self.kb.get_topics_by_module(mod.id)
            lines.append(f"**{mod.name}** ({len(topics)} topics):")
            topic_names = [f"`{t.name}`" for t in topics]
            lines.append(", ".join(topic_names) + "\n")
        return "\n".join(lines)

    def format_topic_definition(self, topic: Topic) -> str:
        """Formats a concise definition for a topic."""
        lines = [
            f"### 📌 {topic.name}",
            f"**Category:** `{topic.category}`\n",
            f"**Definition:** {topic.definition}\n",
            f"**Quick Explanation:** {topic.explanation.split('.')[0] + '.'}\n",
            f"💡 **Example:** {topic.example}"
        ]
        return "\n".join(lines)

    def format_topic_explanation(self, topic: Topic) -> str:
        """Formats an in-depth educational topic explanation."""
        lines = [
            f"### 🎓 {topic.name}",
            f"🏷️ **Category:** `{topic.category}` | 🆔 `{topic.id}`\n",
            f"#### 📖 Definition",
            f"{topic.definition}\n",
            f"#### 🔍 Detailed Explanation",
            f"{topic.explanation}\n",
            f"#### 💡 Real-World Example",
            f"{topic.example}\n",
        ]

        if topic.formula:
            lines.extend([
                f"#### 🧮 Mathematical / Formal Representation",
                f"$$\n{topic.formula}\n$$\n"
            ])

        if topic.algorithm_steps:
            lines.append(f"#### ⚙️ Algorithm Steps")
            for idx, step in enumerate(topic.algorithm_steps, 1):
                lines.append(f"{idx}. {step}")
            lines.append("")

        if topic.advantages:
            lines.append(f"#### ✅ Key Advantages")
            for adv in topic.advantages:
                lines.append(f"- {adv}")
            lines.append("")

        if topic.limitations:
            lines.append(f"#### ⚠️ Key Limitations")
            for lim in topic.limitations:
                lines.append(f"- {lim}")
            lines.append("")

        if topic.applications:
            lines.append(f"#### 🚀 Real-World Applications")
            for app in topic.applications:
                lines.append(f"- {app}")
            lines.append("")

        # Related topics
        related_names = []
        for rel_id in topic.related_topics:
            rel_t = self.kb.get_topic(rel_id)
            if rel_t:
                related_names.append(f"`{rel_t.name}`")
        if related_names:
            lines.append(f"🔗 **Related Topics:** {', '.join(related_names)}")

        return "\n".join(lines)

    def format_example(self, topic: Topic) -> str:
        """Formats the concrete real-world example for a topic."""
        return (
            f"### 💡 Example: {topic.name}\n\n"
            f"**Topic:** `{topic.name}` ({topic.category})\n\n"
            f"**Concrete Real-World Case:**\n"
            f"> {topic.example}\n\n"
            f"*Context:* {topic.definition}"
        )

    def format_advantages_limitations(self, topic: Topic) -> str:
        """Formats the pros and cons of a topic."""
        lines = [
            f"### ⚖️ Advantages & Limitations: {topic.name}\n",
            f"#### ✅ Advantages",
        ]
        if topic.advantages:
            for adv in topic.advantages:
                lines.append(f"- {adv}")
        else:
            lines.append("- High efficiency within domain bounds.")

        lines.append("\n#### ⚠️ Limitations & Challenges")
        if topic.limitations:
            for lim in topic.limitations:
                lines.append(f"- {lim}")
        else:
            lines.append("- Subject to data quality and computational constraints.")

        return "\n".join(lines)

    def format_applications(self, topic: Topic) -> str:
        """Formats applications and use cases for a topic."""
        lines = [
            f"### 🚀 Applications of {topic.name}\n",
            f"**Domain:** `{topic.category}`\n",
        ]
        if topic.applications:
            for app in topic.applications:
                lines.append(f"- **{app.split(':')[0] if ':' in app else app}**")
                if ":" in app:
                    lines.append(f"  {app.split(':', 1)[1].strip()}")
        else:
            lines.append(f"- Practical deployments in automated reasoning and machine intelligence.")

        lines.append(f"\n💡 *Example:* {topic.example}")
        return "\n".join(lines)

    def format_formula(self, topic: Topic) -> str:
        """Formats mathematical formula or formal representation for a topic."""
        if not topic.formula:
            return (
                f"### 🧮 Formula: {topic.name}\n\n"
                f"The topic **{topic.name}** is primarily conceptual or qualitative rather than governed by a single closed-form mathematical formula.\n\n"
                f"**Key formal principle:**\n"
                f"{topic.definition}"
            )
        return (
            f"### 🧮 Mathematical Formula: {topic.name}\n\n"
            f"**Topic:** `{topic.name}`\n\n"
            f"$$\n{topic.formula}\n$$\n\n"
            f"**Theoretical Context:**\n"
            f"{topic.explanation}"
        )

    def format_algorithm(self, topic: Topic) -> str:
        """Formats algorithm execution steps."""
        if not topic.algorithm_steps:
            return (
                f"### ⚙️ Algorithm Steps: {topic.name}\n\n"
                f"**{topic.name}** is a foundational paradigm rather than a standalone procedural algorithm.\n\n"
                f"**Operational Mechanism:**\n"
                f"{topic.explanation}"
            )
        lines = [
            f"### ⚙️ Algorithm Steps: {topic.name}\n",
            f"**Methodology:** `{topic.name}` ({topic.category})\n",
        ]
        for idx, step in enumerate(topic.algorithm_steps, 1):
            lines.append(f"{idx}. **Step {idx}:** {step}")
        lines.append(f"\n💡 **Implementation Example:**\n> {topic.example}")
        return "\n".join(lines)

    def format_relationships(self, topic: Topic) -> str:
        """Explains branches and architectural relationships for a topic."""
        if topic.id == "ai_definition":
            return (
                "### 🌳 Branches of Artificial Intelligence\n\n"
                "Artificial Intelligence comprises several interconnected major subfields:\n\n"
                "1. **Machine Learning (ML):** Systems that learn predictive patterns from empirical data.\n"
                "2. **Deep Learning (DL):** Multi-layered neural network architectures learning hierarchical representations.\n"
                "3. **Natural Language Processing (NLP):** Computational linguistics enabling human speech and text understanding.\n"
                "4. **Computer Vision (CV):** Visual perception, image classification, and object detection.\n"
                "5. **Knowledge-Based & Expert Systems:** Symbolic reasoning using explicit facts and IF-THEN production rules.\n"
                "6. **Search, Planning & Robotics:** State-space heuristic navigation (A*) and physical autonomous agents.\n"
                "7. **Generative AI:** Large Language Models and diffusion models synthesizing novel media.\n\n"
                "👉 *Ask about any branch: e.g.* **`Explain Machine Learning`** *or* **`What is Knowledge-Based AI?`**"
            )

        lines = [
            f"### 🔗 Conceptual Relationships: {topic.name}\n",
            f"**Category:** `{topic.category}`\n",
            f"**Core Role:** {topic.definition}\n",
            f"#### Related Topics in Knowledge Base:"
        ]
        for rel_id in topic.related_topics:
            rel_t = self.kb.get_topic(rel_id)
            if rel_t:
                lines.append(f"- **{rel_t.name}** (`{rel_t.id}`): {rel_t.definition}")

        return "\n".join(lines)

    def format_comparison(self, topic1: Topic, topic2: Topic) -> str:
        """Generates a structured side-by-side comparison markdown table."""
        lines = [
            f"### ⚖️ Comparison: {topic1.name} vs {topic2.name}\n",
            f"| Dimension | **{topic1.name}** | **{topic2.name}** |",
            f"| :--- | :--- | :--- |",
            f"| **Category** | `{topic1.category}` | `{topic2.category}` |",
            f"| **Core Definition** | {topic1.definition} | {topic2.definition} |",
            f"| **Primary Example** | {topic1.example} | {topic2.example} |",
        ]

        # Key advantage comparison
        adv1 = topic1.advantages[0] if topic1.advantages else "Specialized performance"
        adv2 = topic2.advantages[0] if topic2.advantages else "Specialized performance"
        lines.append(f"| **Main Advantage** | {adv1} | {adv2} |")

        # Key limitation comparison
        lim1 = topic1.limitations[0] if topic1.limitations else "Boundary limits"
        lim2 = topic2.limitations[0] if topic2.limitations else "Boundary limits"
        lines.append(f"| **Main Limitation** | {lim1} | {lim2} |")

        # Synthesis summary
        lines.extend([
            f"\n#### 🎯 Key Takeaway",
            f"- **{topic1.name}** emphasizes: {topic1.explanation.split('.')[0]}.",
            f"- **{topic2.name}** emphasizes: {topic2.explanation.split('.')[0]}.",
            f"- They often work together in modern AI architectures."
        ])

        return "\n".join(lines)

    def format_recommendation(self, current_topic: Optional[Topic] = None) -> str:
        """Recommends next topics to study."""
        if current_topic and current_topic.related_topics:
            rec_id = current_topic.related_topics[0]
            rec_topic = self.kb.get_topic(rec_id)
            if rec_topic:
                return (
                    f"### 💡 Recommended Next Topic: {rec_topic.name}\n\n"
                    f"Since you are studying **{current_topic.name}**, a natural progression is **{rec_topic.name}** (`{rec_topic.category}`).\n\n"
                    f"> {rec_topic.definition}\n\n"
                    f"👉 *Type:* **`Explain {rec_topic.name}`** to continue your learning journey!"
                )

        return (
            "### 💡 Recommended Starting Topics\n\n"
            "Here are recommended foundational topics across our modules:\n\n"
            "1. **AI Fundamentals:** `What is AI?`\n"
            "2. **Machine Learning:** `Explain Supervised Learning`\n"
            "3. **Deep Learning:** `What is Backpropagation?`\n"
            "4. **Natural Language Processing:** `What is TF-IDF?`\n"
            "5. **Computer Vision:** `Explain YOLO`\n"
            "6. **Knowledge-Based AI:** `What is an Expert System?`\n"
            "7. **Search & Planning:** `Explain A* Search`\n"
            "8. **Generative AI:** `What is Retrieval-Augmented Generation (RAG)?`"
        )

    def format_repeat(self, previous_response: str) -> str:
        """Repeats or clarifies the previous turn."""
        if not previous_response:
            return "I haven't said anything yet in this session! Ask me any question about Artificial Intelligence to get started."
        return f"### 🔄 Here is what I shared previously:\n\n{previous_response}"

    def format_unknown_fallback(self, query: str) -> str:
        """Helpful fallback for out-of-scope or unparseable queries with topic suggestions."""
        # Find partial candidate matches
        candidates = self.kb.search_topics(query)
        suggestions = []
        if candidates:
            suggestions = [f"- **`Explain {t.name}`** ({t.category})" for t in candidates[:4]]

        suggestion_text = ""
        if suggestions:
            suggestion_text = "\n\n#### 🔍 Did you mean one of these topics?\n" + "\n".join(suggestions)

        return (
            f"### 🤖 I couldn't find an exact rule match for: *\"{query}\"*\n\n"
            f"As a **deterministic rule-based educational chatbot**, I only provide verified answers "
            f"from my curated Artificial Intelligence knowledge base without fabricating answers or hallucinating.{suggestion_text}\n\n"
            f"#### 💡 Quick suggestions you can ask:\n"
            f"- **`What is AI?`**\n"
            f"- **`Difference between AI and ML?`**\n"
            f"- **`Explain Named Entity Recognition`**\n"
            f"- **`What is an Expert System?`**\n"
            f"- **`Explain A* search`**\n"
            f"- **`List all modules`**"
        )
