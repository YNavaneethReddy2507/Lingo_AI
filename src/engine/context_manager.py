"""Context manager for tracking conversational state and resolving rule-based follow-ups."""
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from src.engine.models import Intent, Topic


@dataclass
class ConversationContext:
    """Maintains active conversation state across conversational turns."""
    last_topic: Optional[Topic] = None
    last_secondary_topic: Optional[Topic] = None
    last_intent: Optional[Intent] = None
    last_response_text: str = ""
    turn_count: int = 0
    history: List[Dict[str, str]] = field(default_factory=list)

    def record_turn(
        self,
        user_query: str,
        bot_response: str,
        intent: Intent,
        topic: Optional[Topic] = None,
        secondary_topic: Optional[Topic] = None,
    ) -> None:
        """Updates the conversation context after an interaction."""
        self.turn_count += 1
        self.last_intent = intent
        self.last_response_text = bot_response
        if topic is not None:
            self.last_topic = topic
        if secondary_topic is not None:
            self.last_secondary_topic = secondary_topic

        self.history.append({
            "turn": str(self.turn_count),
            "user": user_query,
            "bot": bot_response,
            "intent": intent.value,
            "topic_id": topic.id if topic else "",
        })

    def is_contextual_followup(self, query: str) -> bool:
        """Determines whether a query is an anaphoric follow-up dependent on prior context.

        Examples:
        - "Give an example"
        - "What are its branches?"
        - "What are its limitations?"
        - "What are its applications?"
        - "Show me its formula"
        - "How does it work?"
        - "Explain it"
        """
        q = query.lower().strip()
        pronoun_triggers = [
            "its branches", "branches of it", "give an example",
            "show an example", "example please", "give me an example",
            "what are its", "its limitations", "its advantages",
            "its formula", "how does it work", "explain it",
            "pros and cons of it", "its applications", "use cases of it"
        ]
        if any(trig in q for trig in pronoun_triggers):
            return True

        if q in {"give an example", "example", "formula", "steps", "applications", "limitations", "pros and cons"}:
            return True

        return False

    def clear(self) -> None:
        """Resets the context for a fresh conversation session."""
        self.last_topic = None
        self.last_secondary_topic = None
        self.last_intent = None
        self.last_response_text = ""
        self.turn_count = 0
        self.history.clear()
