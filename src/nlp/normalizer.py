"""Text normalization for rule-based chatbot input processing."""
import re
import unicodedata


class TextNormalizer:
    """Normalizes user input text deterministically using explicit rules."""

    CONTRACTIONS = {
        r"\bwhat's\b": "what is",
        r"\bwhat're\b": "what are",
        r"\bwho's\b": "who is",
        r"\bhow's\b": "how is",
        r"\bwhere's\b": "where is",
        r"\bthere's\b": "there is",
        r"\bit's\b": "it is",
        r"\bthat's\b": "that is",
        r"\bdon't\b": "do not",
        r"\bdoesn't\b": "does not",
        r"\bdidn't\b": "did not",
        r"\bcan't\b": "cannot",
        r"\bcouldn't\b": "could not",
        r"\bwon't\b": "will not",
        r"\bwouldn't\b": "would not",
        r"\bshouldn't\b": "should not",
        r"\bisn't\b": "is not",
        r"\baren't\b": "are not",
        r"\bwasn't\b": "was not",
        r"\bweren't\b": "were not",
        r"\bhasn't\b": "has not",
        r"\bhaven't\b": "have not",
        r"\bhadn't\b": "had not",
        r"\bi'm\b": "i am",
        r"\byou're\b": "you are",
        r"\bwe're\b": "we are",
        r"\bthey're\b": "they are",
        r"\bi've\b": "i have",
        r"\byou've\b": "you have",
        r"\bwe've\b": "we have",
        r"\bthey've\b": "they have",
        r"\bi'll\b": "i will",
        r"\byou'll\b": "you will",
        r"\bhe'll\b": "he will",
        r"\bshe'll\b": "she will",
        r"\bwe'll\b": "we will",
        r"\bthey'll\b": "they will",
        r"\blet's\b": "let us",
        r"\bai's\b": "ai",
        r"\bml's\b": "ml",
        r"\bdl's\b": "dl",
        r"\bnlp's\b": "nlp",
    }

    # Replace typographical smart quotes and dashes with ASCII equivalents
    SMART_CHARACTERS = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": " - ",
        "\u2026": "...",
    }

    @classmethod
    def normalize(cls, text: str) -> str:
        """Fully normalizes text for downstream tokenization and rule matching.

        Steps:
        1. Handle null or whitespace-only strings.
        2. Replace typographic smart characters.
        3. Unicode normalize (NFKD) to separate diacritics.
        4. Lowercase.
        5. Expand standard English contractions.
        6. Strip non-essential punctuation (preserving letters, digits, spaces, hyphens, and asterisk for A*).
        7. Collapse repeated whitespaces.
        """
        if not text:
            return ""

        # Replace smart quotes and dashes
        for orig, replacement in cls.SMART_CHARACTERS.items():
            text = text.replace(orig, replacement)

        # Unicode decomposition to strip accents
        text = unicodedata.normalize("NFKD", text)
        text = "".join(ch for ch in text if not unicodedata.combining(ch))

        # Lowercase
        text = text.lower()

        # Expand contractions
        for pattern, replacement in cls.CONTRACTIONS.items():
            text = re.sub(pattern, replacement, text)

        # Normalize special symbols: preserve '*' in 'a*' but drop elsewhere
        # Replace punctuation except hyphens, asterisks attached to 'a', and basic alphanumeric
        # Turn other punctuation into space
        cleaned_chars = []
        i = 0
        n = len(text)
        while i < n:
            ch = text[i]
            if ch.isalnum() or ch == " " or ch == "-":
                cleaned_chars.append(ch)
            elif ch == "*":
                # Keep '*' only if preceded by 'a' (for A* search)
                if i > 0 and text[i - 1] == "a":
                    cleaned_chars.append(ch)
                else:
                    cleaned_chars.append(" ")
            elif ch in "?!.,;:()[]{}\"'/\\_":
                cleaned_chars.append(" ")
            else:
                cleaned_chars.append(" ")
            i += 1

        text = "".join(cleaned_chars)

        # Collapse multiple spaces and trim
        text = re.sub(r"\s+", " ", text).strip()
        return text

    @classmethod
    def clean_query_for_topic_extraction(cls, text: str) -> str:
        """Removes common conversational question framing to isolate topic phrases.

        E.g., "what is the difference between supervised and unsupervised" ->
        "difference between supervised and unsupervised"
        """
        norm = cls.normalize(text)
        # Strip common question prefixes
        prefixes = [
            r"^(can you please |could you please |please |kindly )",
            r"^(can you |could you |would you |will you )",
            r"^(tell me about |talk about |give me information on |give me info on )",
            r"^(what can you tell me about |what do you know about )",
            r"^(i want to know about |i would like to know about |i need to know about )",
            r"^(what is |what are |what was |what were |who is |who are )",
            r"^(explain to me |explain |describe |define )",
            r"^(give me an example of |give an example of |show me an example of |example of )",
            r"^(what is the definition of |give the definition of |definition of )",
            r"^(show me the formula for |what is the formula for |formula for )",
            r"^(how does |how do |how can )",
        ]
        for p in prefixes:
            norm = re.sub(p, "", norm).strip()

        # Strip trailing filler
        norm = re.sub(r"( please| in ai| in machine learning| in nlp| in deep learning)$", "", norm).strip()
        return norm
