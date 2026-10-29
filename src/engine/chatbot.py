"""Core orchestrator for AI KnowledgeBot rule-based chatbot engine."""
import re
from typing import Optional

from src.engine.context_manager import ConversationContext
from src.engine.intent_classifier import IntentClassifier
from src.engine.knowledge_base import KnowledgeBase
from src.engine.models import ChatbotResponse, Intent, Topic
from src.engine.response_generator import ResponseGenerator
from src.engine.topic_matcher import TopicMatcher
from src.nlp.normalizer import TextNormalizer


class AIKnowledgeBot:
    """Complete rule-based chatbot engine for Artificial Intelligence education."""

    def __init__(self, kb_dir: Optional[str] = None):
        self.kb = KnowledgeBase(kb_dir=kb_dir)
        self.matcher = TopicMatcher(self.kb)
        self.generator = ResponseGenerator(self.kb)
        self.context = ConversationContext()

    def process_message(self, user_input: str) -> ChatbotResponse:
        """Processes a user message through the rule-based pipeline and returns a structured response."""
        raw_text = user_input.strip() if user_input else ""
        if not raw_text:
            return ChatbotResponse(
                text="Please type an AI question or topic! For example: **\"What is AI?\"** or **\"Explain Neural Networks\"**.",
                intent=Intent.UNKNOWN,
                confidence=0.0,
                matched_rule="Empty or whitespace-only input rule",
                suggested_followups=["What is AI?", "Explain Machine Learning", "List all modules"]
            )

        norm_text = TextNormalizer.normalize(raw_text)

        # 1. Intent Detection
        detected_intent, intent_rule = IntentClassifier.classify(norm_text)

        # 2. Handle Standalone Conversational Intents
        if detected_intent == Intent.GREETING:
            text = self.generator.format_greeting()
            resp = ChatbotResponse(
                text=text,
                intent=Intent.GREETING,
                confidence=1.0,
                matched_rule=intent_rule,
                suggested_followups=["What is AI?", "Difference between AI and ML?", "List all modules"]
            )
            self.context.record_turn(raw_text, text, Intent.GREETING)
            return resp

        if detected_intent == Intent.GOODBYE:
            text = self.generator.format_goodbye()
            resp = ChatbotResponse(
                text=text,
                intent=Intent.GOODBYE,
                confidence=1.0,
                matched_rule=intent_rule,
                suggested_followups=[]
            )
            self.context.record_turn(raw_text, text, Intent.GOODBYE)
            return resp

        if detected_intent == Intent.HELP:
            text = self.generator.format_help()
            resp = ChatbotResponse(
                text=text,
                intent=Intent.HELP,
                confidence=1.0,
                matched_rule=intent_rule,
                suggested_followups=["What is AI?", "Compare CNN and RNN", "Show topics in NLP"]
            )
            self.context.record_turn(raw_text, text, Intent.HELP)
            return resp

        if detected_intent == Intent.LIST_MODULES:
            text = self.generator.format_module_list()
            resp = ChatbotResponse(
                text=text,
                intent=Intent.LIST_MODULES,
                confidence=1.0,
                matched_rule=intent_rule,
                suggested_followups=["Show topics in Module A", "Show topics in Deep Learning", "Explain A* search"]
            )
            self.context.record_turn(raw_text, text, Intent.LIST_MODULES)
            return resp

        if detected_intent == Intent.LIST_TOPICS:
            # Check if a specific module was mentioned in the query
            mod_filter = None
            module_keywords = {
                "module_c": ["deep learning", "module c"],
                "module_b": ["machine learning", "module b"],
                "module_d": ["natural language processing", "nlp", "module d"],
                "module_e": ["computer vision", "module e"],
                "module_f": ["knowledge-based", "expert systems", "module f"],
                "module_g": ["search", "planning", "robotics", "module g"],
                "module_h": ["generative ai", "genai", "module h"],
                "module_a": ["fundamentals", "history", "module a"],
            }
            for mid, kws in module_keywords.items():
                if any(kw in norm_text for kw in kws):
                    mod_filter = mid
                    break
            if not mod_filter:
                for mod in self.kb.get_all_modules():
                    if mod.id in norm_text:
                        mod_filter = mod.id
                        break
            text = self.generator.format_topic_list(mod_filter)
            resp = ChatbotResponse(
                text=text,
                intent=Intent.LIST_TOPICS,
                confidence=1.0,
                matched_rule=f"List topics rule (filter={mod_filter})",
                suggested_followups=["Explain Supervised Learning", "What is TF-IDF?", "What is YOLO?"]
            )
            self.context.record_turn(raw_text, text, Intent.LIST_TOPICS)
            return resp

        if detected_intent == Intent.REPEAT_CLARIFY:
            text = self.generator.format_repeat(self.context.last_response_text)
            resp = ChatbotResponse(
                text=text,
                intent=Intent.REPEAT_CLARIFY,
                confidence=1.0,
                matched_rule="Repeat previous response rule",
                context_used=True,
                suggested_followups=["Give an example", "What are its limitations?"]
            )
            self.context.record_turn(raw_text, text, Intent.REPEAT_CLARIFY)
            return resp

        if detected_intent == Intent.RECOMMEND_TOPIC:
            text = self.generator.format_recommendation(self.context.last_topic)
            resp = ChatbotResponse(
                text=text,
                intent=Intent.RECOMMEND_TOPIC,
                confidence=1.0,
                matched_rule="Topic recommendation rule",
                suggested_followups=["Explain Machine Learning", "What is RAG?", "Explain Backpropagation"]
            )
            self.context.record_turn(raw_text, text, Intent.RECOMMEND_TOPIC)
            return resp

        # 3. Handle Comparisons ("difference between X and Y", "compare X and Y", "X vs Y")
        if detected_intent == Intent.COMPARE_TOPICS or " vs " in norm_text or " versus " in norm_text or "difference between" in norm_text:
            t1, t2, comp_rule = self.matcher.match_two_topics_for_comparison(norm_text)
            if t1 and t2:
                text = self.generator.format_comparison(t1, t2)
                resp = ChatbotResponse(
                    text=text,
                    intent=Intent.COMPARE_TOPICS,
                    matched_topic=t1,
                    secondary_topic=t2,
                    confidence=0.95,
                    matched_rule=f"Comparison rule: {comp_rule}",
                    suggested_followups=[
                        f"Give an example of {t1.name}",
                        f"Give an example of {t2.name}",
                        f"What are the limitations of {t1.name}?"
                    ]
                )
                self.context.record_turn(raw_text, text, Intent.COMPARE_TOPICS, topic=t1, secondary_topic=t2)
                return resp

        # 4. Contextual Follow-up Resolution
        active_topic: Optional[Topic] = None
        context_used = False
        topic_match_rule = ""
        topic_conf = 0.0

        if self.context.is_contextual_followup(norm_text) and self.context.last_topic is not None:
            active_topic = self.context.last_topic
            context_used = True
            topic_match_rule = f"Contextual resolution to previous topic '{active_topic.name}'"
            topic_conf = 0.95
        else:
            # Match topic directly from query text
            active_topic, topic_conf, topic_match_rule = self.matcher.match_topic(norm_text)

        # 5. Route by Intent with Matched Topic
        if active_topic is not None:
            # Special check for branches of AI
            if "branch" in norm_text or detected_intent == Intent.RELATIONSHIPS:
                text = self.generator.format_relationships(active_topic)
                intent = Intent.RELATIONSHIPS
            elif detected_intent == Intent.GIVE_EXAMPLE:
                text = self.generator.format_example(active_topic)
                intent = Intent.GIVE_EXAMPLE
            elif detected_intent == Intent.ADVANTAGES_LIMITATIONS:
                text = self.generator.format_advantages_limitations(active_topic)
                intent = Intent.ADVANTAGES_LIMITATIONS
            elif detected_intent == Intent.APPLICATIONS:
                text = self.generator.format_applications(active_topic)
                intent = Intent.APPLICATIONS
            elif detected_intent == Intent.SHOW_FORMULA:
                text = self.generator.format_formula(active_topic)
                intent = Intent.SHOW_FORMULA
            elif detected_intent == Intent.EXPLAIN_ALGORITHM:
                text = self.generator.format_algorithm(active_topic)
                intent = Intent.EXPLAIN_ALGORITHM
            elif detected_intent == Intent.DEFINE_TOPIC:
                text = self.generator.format_topic_definition(active_topic)
                intent = Intent.DEFINE_TOPIC
            else:
                # Default comprehensive explanation
                text = self.generator.format_topic_explanation(active_topic)
                intent = Intent.EXPLAIN_TOPIC

            followups = list(active_topic.suggested_followups) if active_topic.suggested_followups else [
                "Give an example", "What are its limitations?", "What should I learn next?"
            ]

            resp = ChatbotResponse(
                text=text,
                intent=intent,
                matched_topic=active_topic,
                confidence=topic_conf,
                matched_rule=f"{intent_rule} | {topic_match_rule}",
                suggested_followups=followups,
                context_used=context_used,
            )
            self.context.record_turn(raw_text, text, intent, topic=active_topic)
            return resp

        # 6. Fallback for Unknown / Unsupported Questions
        fallback_text = self.generator.format_unknown_fallback(raw_text)
        resp = ChatbotResponse(
            text=fallback_text,
            intent=Intent.UNKNOWN,
            confidence=0.1,
            matched_rule="Rule-based fallback: No topic or intent pattern met minimum threshold",
            suggested_followups=["What is AI?", "Difference between AI and ML?", "List all modules"]
        )
        self.context.record_turn(raw_text, fallback_text, Intent.UNKNOWN)
        return resp
