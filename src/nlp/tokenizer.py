"""Tokenizer and n-gram extraction for rule-based NLP."""
import re
from typing import List


class Tokenizer:
    """Tokenizes normalized text into word tokens and n-grams."""

    # Structural words that should NOT be stripped as stopwords
    PRESERVED_KEYWORDS = {
        "vs", "versus", "between", "difference", "and", "or", "not",
        "what", "why", "how", "define", "explain", "example",
        "formula", "algorithm", "steps", "pros", "cons", "advantages",
        "disadvantages", "limitations", "applications", "branches",
        "compare", "comparison", "list", "all", "topics", "modules",
        "a*", "q-learning", "k-means", "tf-idf"
    }

    # Standard English stopwords to filter during pure content keyword extraction
    STANDARD_STOPWORDS = {
        "a", "about", "above", "after", "again", "against", "all", "am", "an",
        "any", "are", "as", "at", "be", "because", "been", "before", "being",
        "below", "both", "but", "by", "could", "did", "do", "does", "doing",
        "down", "during", "each", "few", "for", "from", "further", "had", "has",
        "have", "having", "he", "her", "here", "hers", "herself", "him", "himself",
        "his", "i", "if", "in", "into", "is", "it", "its", "itself", "me", "more",
        "most", "my", "myself", "no", "nor", "of", "off", "on", "once", "only",
        "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same",
        "she", "should", "so", "some", "such", "than", "that", "the", "their",
        "theirs", "them", "themselves", "then", "there", "these", "they", "this",
        "those", "through", "to", "too", "under", "until", "up", "very", "was",
        "we", "were", "what", "when", "where", "which", "while", "who", "whom",
        "with", "would", "you", "your", "yours", "yourself", "yourselves"
    }

    @classmethod
    def tokenize(cls, text: str) -> List[str]:
        """Splits normalized text into tokens while preserving hyphenated compounds and special tokens like 'a*'."""
        if not text:
            return []
        # Match 'a*' or words with hyphens (e.g. 'k-means', 'tf-idf') or standard alphanumeric words
        tokens = re.findall(r"\ba\*|[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*", text)
        return tokens

    @classmethod
    def filter_stopwords(cls, tokens: List[str], preserve_intent_words: bool = True) -> List[str]:
        """Removes stopwords from a token list while optionally preserving intent-bearing keywords."""
        filtered = []
        for t in tokens:
            t_lower = t.lower()
            if preserve_intent_words and t_lower in cls.PRESERVED_KEYWORDS:
                filtered.append(t)
            elif t_lower not in cls.STANDARD_STOPWORDS:
                filtered.append(t)
        return filtered

    @classmethod
    def get_ngrams(cls, tokens: List[str], n: int) -> List[str]:
        """Generates consecutive n-grams joined by a space from a list of tokens."""
        if not tokens or n < 1:
            return []
        if len(tokens) < n:
            return []
        return [" ".join(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]

    @classmethod
    def get_all_ngrams(cls, tokens: List[str], max_n: int = 4) -> List[str]:
        """Returns all n-grams from size 1 up to max_n, ordered from longest to shortest."""
        all_grams = []
        for n in range(min(max_n, len(tokens)), 0, -1):
            all_grams.extend(cls.get_ngrams(tokens, n))
        return all_grams
