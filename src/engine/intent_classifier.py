"""Rule-based Intent Classifier for AI KnowledgeBot."""
import re
from typing import Tuple

from src.engine.models import Intent
from src.nlp.normalizer import TextNormalizer


class IntentClassifier:
    """Classifies user query intent using deterministic regular expressions and keyword rules."""

    # Ordered list of (Intent, list of regex patterns, priority)
    INTENT_RULES = [
        # Greetings
        (
            Intent.GREETING,
            [
                r"^(hi|hello|hey|howdy|greetings|good\s+(morning|afternoon|evening|day)|salutations)\b",
                r"^start\b",
                r"^who\s+are\s+you\b",
                r"^what\s+is\s+your\s+name\b",
            ]
        ),
        # Goodbyes
        (
            Intent.GOODBYE,
            [
                r"^(bye|goodbye|see\s+you|farewell|cya|exit|quit|later|have\s+a\s+good\s+day)\b",
            ]
        ),
        # Help
        (
            Intent.HELP,
            [
                r"^(help|commands|how\s+to\s+use|what\s+can\s+you\s+do|how\s+do\s+you\s+work|usage|menu)\b",
                r"\bhow\s+can\s+you\s+help\s+me\b",
                r"\bwhat\s+are\s+your\s+capabilities\b",
            ]
        ),
        # Comparison (High priority so "difference between X and Y" isn't swallowed by "what is")
        (
            Intent.COMPARE_TOPICS,
            [
                r"\b(difference\s+between|compare|contrast|versus|\bvs\.?\b|how\s+does\s+.+?\s+differ\s+from)\b",
            ]
        ),
        # List all modules
        (
            Intent.LIST_MODULES,
            [
                r"\b(list|show|view|all)\s+(modules|categories|branches|sections)\b",
                r"^what\s+(modules|categories)\s+(do\s+you\s+have|exist|are\s+there)\b",
                r"^(modules|categories)\b",
            ]
        ),
        # List topics (optionally in a module)
        (
            Intent.LIST_TOPICS,
            [
                r"\b(list|show|view|what\s+are)\s+(all\s+)?topics\b",
                r"\bshow\s+me\s+(.+?)\s+topics\b",
                r"\btopics\s+in\s+module\s+[a-h]\b",
                r"\btopics\s+in\s+(.+)\b",
                r"^topics\b",
            ]
        ),
        # Branches / Relationships
        (
            Intent.RELATIONSHIPS,
            [
                r"\b(what\s+are\s+its\s+branches|what\s+are\s+the\s+branches|branches\s+of\s+ai|branches\s+of\s+artificial\s+intelligence)\b",
                r"\bhow\s+is\s+.+?\s+related\s+to\s+.+\b",
                r"\bhow\s+are\s+.+?\s+and\s+.+?\s+related\b",
                r"\brelationship\s+between\s+.+?\s+and\s+.+\b",
            ]
        ),
        # Examples
        (
            Intent.GIVE_EXAMPLE,
            [
                r"^(give\s+(me\s+)?an?\s+example|show\s+(me\s+)?an?\s+example|example\s+please|can\s+you\s+give\s+an?\s+example)\b",
                r"\b(give\s+an?\s+example\s+of|example\s+of|real\s+world\s+example\s+of)\b",
                r"^example\b",
            ]
        ),
        # Advantages / Limitations / Pros and Cons
        (
            Intent.ADVANTAGES_LIMITATIONS,
            [
                r"\b(pros\s+and\s+cons|advantages\s+and\s+disadvantages|advantages\s+and\s+limitations|benefits\s+and\s+risks)\b",
                r"\b(what\s+are\s+its\s+advantages|what\s+are\s+its\s+limitations|what\s+are\s+its\s+pros|what\s+are\s+its\s+cons)\b",
                r"\b(advantages\s+of|disadvantages\s+of|limitations\s+of|pros\s+of|cons\s+of|benefits\s+of)\b",
            ]
        ),
        # Applications / Use Cases
        (
            Intent.APPLICATIONS,
            [
                r"\b(what\s+are\s+its\s+applications|where\s+is\s+it\s+used|how\s+is\s+it\s+used)\b",
                r"\b(applications\s+of|use\s+cases\s+of|practical\s+uses\s+of|where\s+is\s+.+?\s+used)\b",
                r"\breal-world\s+applications\b",
            ]
        ),
        # Formula / Equations
        (
            Intent.SHOW_FORMULA,
            [
                r"\b(formula\s+for|equation\s+for|math\s+behind|mathematical\s+formula|show\s+formula)\b",
                r"\bwhat\s+is\s+its\s+formula\b",
                r"^formula\b",
            ]
        ),
        # Algorithm / Steps
        (
            Intent.EXPLAIN_ALGORITHM,
            [
                r"\b(how\s+does\s+the\s+algorithm\s+work|steps\s+of|algorithm\s+steps|how\s+to\s+compute|pseudocode)\b",
                r"\b(algorithm\s+for|steps\s+for|how\s+does\s+.+?\s+algorithm\s+work)\b",
            ]
        ),
        # Recommendations
        (
            Intent.RECOMMEND_TOPIC,
            [
                r"\b(what\s+should\s+i\s+learn\s+next|recommend\s+(a\s+)?topic|suggest\s+(a\s+)?topic|next\s+topic|where\s+should\s+i\s+start)\b",
            ]
        ),
        # Repeat / Clarify
        (
            Intent.REPEAT_CLARIFY,
            [
                r"\b(repeat\s+(that|please)?|say\s+that\s+again|what\s+did\s+you\s+just\s+say|can\s+you\s+clarify|clarification)\b",
            ]
        ),
        # Definition
        (
            Intent.DEFINE_TOPIC,
            [
                r"^what\s+is\s+(an?\s+)?(.+)",
                r"^what\s+are\s+(the\s+)?(.+)",
                r"^define\s+(.+)",
                r"^definition\s+of\s+(.+)",
                r"^meaning\s+of\s+(.+)",
            ]
        ),
        # General explanation
        (
            Intent.EXPLAIN_TOPIC,
            [
                r"^explain\s+(.+)",
                r"^tell\s+me\s+about\s+(.+)",
                r"^how\s+does\s+(.+)\s+work",
                r"^overview\s+of\s+(.+)",
                r"^describe\s+(.+)",
                r"^teach\s+me\s+(.+)",
            ]
        ),
    ]

    @classmethod
    def classify(cls, query: str) -> Tuple[Intent, str]:
        """Classifies the user query into a known Intent.

        Returns: (Intent, rule_matched_description)
        """
        normalized = TextNormalizer.normalize(query)
        if not normalized:
            return Intent.UNKNOWN, "Empty input string"

        for intent, patterns in cls.INTENT_RULES:
            for pattern in patterns:
                if re.search(pattern, normalized, re.IGNORECASE):
                    return intent, f"Pattern matched: '{pattern}'"

        # If it's a bare noun phrase or single technical term (e.g. "NLP", "Machine Learning", "A*")
        # Treat as EXPLAIN_TOPIC by default rather than UNKNOWN
        words = normalized.split()
        if len(words) <= 4:
            return Intent.EXPLAIN_TOPIC, "Short keyword query defaulting to explanation"

        return Intent.UNKNOWN, "No intent rule pattern matched"
