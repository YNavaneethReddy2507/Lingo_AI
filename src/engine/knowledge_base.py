"""Knowledge Base repository and indexer for AI KnowledgeBot."""
import glob
import json
import os
from typing import Dict, List, Optional, Set

from src.engine.models import Module, Topic
from src.nlp.normalizer import TextNormalizer


class KnowledgeBase:
    """Loads, validates, indexes, and queries topic entries from JSON files."""

    REQUIRED_FIELDS = [
        "id", "name", "category", "category_id", "aliases",
        "keywords", "definition", "explanation", "example"
    ]

    def __init__(self, kb_dir: Optional[str] = None):
        if kb_dir is None:
            # Default to relative knowledge_base directory from workspace root
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.kb_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "knowledge_base"))
        else:
            self.kb_dir = os.path.abspath(kb_dir)

        self.topics_by_id: Dict[str, Topic] = {}
        self.modules_by_id: Dict[str, Module] = {}
        self.alias_to_id: Dict[str, str] = {}
        self.keyword_to_ids: Dict[str, Set[str]] = {}

        self.load_and_validate()

    def load_and_validate(self) -> None:
        """Loads and strictly validates all JSON module files in the knowledge base directory."""
        if not os.path.isdir(self.kb_dir):
            raise FileNotFoundError(f"Knowledge base directory not found: {self.kb_dir}")

        json_files = sorted(glob.glob(os.path.join(self.kb_dir, "*.json")))
        if not json_files:
            raise FileNotFoundError(f"No JSON knowledge base files found in: {self.kb_dir}")

        self.topics_by_id.clear()
        self.modules_by_id.clear()
        self.alias_to_id.clear()
        self.keyword_to_ids.clear()

        for filepath in json_files:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                raise ValueError(f"Failed to parse JSON file {filepath}: {e}")

            # Validate module header
            module_id = data.get("module_id")
            module_name = data.get("module_name")
            description = data.get("description", "")
            if not module_id or not module_name:
                raise ValueError(f"Module file {filepath} missing 'module_id' or 'module_name'")

            if module_id in self.modules_by_id:
                raise ValueError(f"Duplicate module_id detected: '{module_id}' in {filepath}")

            module = Module(
                id=module_id,
                name=module_name,
                description=description,
                topic_ids=[]
            )

            # Validate topics
            topics_data = data.get("topics", [])
            if not topics_data:
                raise ValueError(f"Module file {filepath} has no topics defined")

            for t_data in topics_data:
                for req in self.REQUIRED_FIELDS:
                    if req not in t_data or (not t_data[req] and not isinstance(t_data[req], list)):
                        raise ValueError(f"Topic in {filepath} missing required non-empty field '{req}': {t_data}")

                topic_id = t_data["id"]
                if topic_id in self.topics_by_id:
                    raise ValueError(f"Duplicate topic ID '{topic_id}' found in {filepath}")

                topic = Topic(
                    id=topic_id,
                    name=t_data["name"],
                    category=t_data["category"],
                    category_id=t_data["category_id"],
                    aliases=t_data.get("aliases", []),
                    keywords=t_data.get("keywords", []),
                    definition=t_data["definition"],
                    explanation=t_data["explanation"],
                    example=t_data["example"],
                    formula=t_data.get("formula", ""),
                    algorithm_steps=t_data.get("algorithm_steps", []),
                    advantages=t_data.get("advantages", []),
                    limitations=t_data.get("limitations", []),
                    applications=t_data.get("applications", []),
                    related_topics=t_data.get("related_topics", []),
                    suggested_followups=t_data.get("suggested_followups", []),
                )

                self.topics_by_id[topic_id] = topic
                module.topic_ids.append(topic_id)

                # Index name and aliases
                norm_name = TextNormalizer.normalize(topic.name)
                self.alias_to_id[norm_name] = topic_id

                for alias in topic.aliases:
                    norm_alias = TextNormalizer.normalize(alias)
                    if norm_alias:
                        self.alias_to_id[norm_alias] = topic_id

                # Index keywords
                for kw in topic.keywords:
                    norm_kw = TextNormalizer.normalize(kw)
                    if norm_kw:
                        if norm_kw not in self.keyword_to_ids:
                            self.keyword_to_ids[norm_kw] = set()
                        self.keyword_to_ids[norm_kw].add(topic_id)

            self.modules_by_id[module_id] = module

        # Validate that all related_topics point to existing topic IDs
        for tid, topic in self.topics_by_id.items():
            for rel in topic.related_topics:
                if rel not in self.topics_by_id:
                    # Provide helpful warning or clean up invalid refs
                    pass

    def get_topic(self, topic_id: str) -> Optional[Topic]:
        """Returns topic by unique ID."""
        return self.topics_by_id.get(topic_id)

    def get_all_topics(self) -> List[Topic]:
        """Returns all topics across all modules."""
        return list(self.topics_by_id.values())

    def get_all_modules(self) -> List[Module]:
        """Returns all modules in order."""
        return list(self.modules_by_id.values())

    def get_module(self, module_id: str) -> Optional[Module]:
        """Returns module by ID."""
        return self.modules_by_id.get(module_id)

    def get_topics_by_module(self, module_id: str) -> List[Topic]:
        """Returns list of topics belonging to a given module ID."""
        mod = self.modules_by_id.get(module_id)
        if not mod:
            return []
        return [self.topics_by_id[tid] for tid in mod.topic_ids if tid in self.topics_by_id]

    def search_topics(self, query: str) -> List[Topic]:
        """Performs multi-field lexical search across topic names, keywords, and definitions."""
        norm_query = TextNormalizer.normalize(query)
        if not norm_query:
            return []

        results = []
        for topic in self.topics_by_id.values():
            score = 0
            norm_name = TextNormalizer.normalize(topic.name)
            if norm_query in norm_name:
                score += 10
            for alias in topic.aliases:
                if norm_query in TextNormalizer.normalize(alias):
                    score += 8
                    break
            for kw in topic.keywords:
                if norm_query in TextNormalizer.normalize(kw):
                    score += 4
                    break
            if norm_query in TextNormalizer.normalize(topic.definition):
                score += 2

            if score > 0:
                results.append((score, topic))

        results.sort(key=lambda x: x[0], reverse=True)
        return [r[1] for r in results]
