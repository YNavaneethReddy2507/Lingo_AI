"""Domain models for AI KnowledgeBot rule-based engine."""
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class Intent(Enum):
    """Supported chatbot intents."""
    GREETING = "greeting"
    GOODBYE = "goodbye"
    HELP = "help"
    LIST_MODULES = "list_modules"
    LIST_TOPICS = "list_topics"
    DEFINE_TOPIC = "define_topic"
    EXPLAIN_TOPIC = "explain_topic"
    GIVE_EXAMPLE = "give_example"
    COMPARE_TOPICS = "compare_topics"
    ADVANTAGES_LIMITATIONS = "advantages_limitations"
    APPLICATIONS = "applications"
    EXPLAIN_ALGORITHM = "explain_algorithm"
    SHOW_FORMULA = "show_formula"
    RELATIONSHIPS = "relationships"
    RECOMMEND_TOPIC = "recommend_topic"
    REPEAT_CLARIFY = "repeat_clarify"
    UNKNOWN = "unknown"


@dataclass
class Topic:
    """Represents an individual AI educational topic in the knowledge base."""
    id: str
    name: str
    category: str
    category_id: str
    aliases: List[str]
    keywords: List[str]
    definition: str
    explanation: str
    example: str
    formula: str = ""
    algorithm_steps: List[str] = field(default_factory=list)
    advantages: List[str] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)
    applications: List[str] = field(default_factory=list)
    related_topics: List[str] = field(default_factory=list)
    suggested_followups: List[str] = field(default_factory=list)


@dataclass
class Module:
    """Represents a major knowledge base category / module."""
    id: str
    name: str
    description: str
    topic_ids: List[str] = field(default_factory=list)


@dataclass
class ChatbotResponse:
    """Encapsulates the structured answer produced by the rule engine."""
    text: str
    intent: Intent
    matched_topic: Optional[Topic] = None
    secondary_topic: Optional[Topic] = None
    confidence: float = 1.0
    matched_rule: str = ""
    suggested_followups: List[str] = field(default_factory=list)
    context_used: bool = False
    turn_id: int = 0
