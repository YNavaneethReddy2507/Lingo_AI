"""Topic matching algorithms for AI KnowledgeBot rule-based engine."""
import re
from typing import List, Optional, Tuple

from src.engine.knowledge_base import KnowledgeBase
from src.engine.models import Topic
from src.nlp.normalizer import TextNormalizer
from src.nlp.tokenizer import Tokenizer


class TopicMatcher:
    """Matches user queries to knowledge base topics using multi-tier deterministic rules."""

    # Explicit regex patterns for specific acronyms and short terms to prevent false positives
    SPECIAL_TERM_PATTERNS = {
        "search_astar": [r"\ba\*(?:\s+(?:search|algorithm))?", r"\ba\s+star\b", r"\bastar\b"],
        "dl_cnn": [r"\bcnn\b", r"\bcnns\b", r"\bconvnets?\b", r"\bconvolutional\s+neural\s+networks?\b"],
        "dl_rnn": [r"\brnn\b", r"\brnns\b", r"\brecurrent\s+neural\s+networks?\b"],
        "dl_ann": [r"\bann\b", r"\banns\b", r"\bneural\s+networks?\b", r"\bdeep\s+learning\b"],
        "nlp_ner": [r"\bner\b", r"\bnamed\s+entity\s+recogni[sz]ation\b"],
        "nlp_pos": [r"\bpos\b", r"\bpos\s+tagging\b", r"\bpart\s+of\s+speech\b"],
        "nlp_tfidf": [r"\btf-?idf\b", r"\bterm\s+frequency\b"],
        "nlp_word2vec_glove": [r"\bword2vec\b", r"\bglove\b", r"\bword\s+embeddings?\b"],
        "ml_svm": [r"\bsvm\b", r"\bsvms\b", r"\bsupport\s+vector\s+machines?\b"],
        "ml_kmeans": [r"\bk-?means\b", r"\bk\s+means\b"],
        "cv_yolo": [r"\byolo\b", r"\byolov\d+\b", r"\byou\s+only\s+look\s+once\b"],
        "genai_rag": [r"\brag\b", r"\bretrieval\s+augmented\s+generation\b", r"\bretrieval-augmented\b"],
        "genai_llms": [r"\bllms?\b", r"\blarge\s+language\s+models?\b", r"\bchatgpt\b"],
        "nlp_fundamentals": [r"\bnlp\b", r"\bnatural\s+language\s+processing\b"],
        "dl_lstm_gru": [r"\blstm\b", r"\bgru\b", r"\blong\s+short\s+term\s+memory\b"],
        "nlp_hmm": [r"\bhmm\b", r"\bhmms\b", r"\bhidden\s+markov\s+models?\b"],
        "search_bfs": [r"\bbfs\b", r"\bbreadth\s+first\s+search\b", r"\bbreadth-first\b"],
        "search_dfs": [r"\bdfs\b", r"\bdepth\s+first\s+search\b", r"\bdepth-first\b"],
        "search_ucs": [r"\bucs\b", r"\buniform\s+cost\s+search\b", r"\buniform-cost\b"],
        # GANs and Generative AI
        "gan_dcgan": [r"\bdcgan\b", r"\bdeep\s+convolutional\s+gan\b"],
        "gan_wgan_gp": [r"\bwgan-?gp\b", r"\bgradient\s+penalty\b"],
        "gan_wgan": [r"\bwgan\b", r"\bwasserstein\s+gan\b", r"\bearth\s+mover\b"],
        "gan_cgan": [r"\bcgan\b", r"\bconditional\s+gan\b"],
        "gan_pix2pix": [r"\bpix2pix\b", r"\bpatchgan\b", r"\bpaired\s+image\s+translation\b"],
        "gan_cyclegan": [r"\bcyclegan\b", r"\bcycle\s+consistency\b", r"\bunpaired\s+image\s+translation\b"],
        "gan_stylegan": [r"\bstylegan\d?\b", r"\badain\b", r"\bprogressive\s+growing\b"],
        "gan_training_instability": [r"\bmode\s+collapse\b", r"\bgan\s+instability\b", r"\bvanishing\s+gradients?\s+in\s+gans?\b"],
        "gan_architectures": [r"\bgenerator\s+and\s+discriminator\b", r"\bgenerator\s+architecture\b", r"\bdiscriminator\s+architecture\b"],
        "gan_adversarial_training": [r"\badversarial\s+training\b", r"\balternating\s+optimization\b"],
        "gan_loss_functions": [r"\bgan\s+loss\b", r"\bminimax\s+loss\b", r"\bnon-saturating\s+loss\b"],
        "gan_evaluation_metrics": [r"\binception\s+score\b", r"\bfid\b", r"\bfrechet\s+inception\s+distance\b"],
        "gan_training_workflow_pytorch": [r"\bpytorch\s+gan\b", r"\bgan\s+pytorch\b", r"\bgan\s+implementation\b", r"\bgan\s+training\s+workflow\b"],
        "gan_dataset_prep_augmentation": [r"\bdiffaugment\b", r"\bdifferentiable\s+augmentation\b", r"\bdata\s+augmentation\s+for\s+gans\b"],
        "gan_applications_ethics": [r"\bdeepfakes?\b", r"\bbiometric\s+spoofing\b", r"\bsynthetic\s+data\s+risks?\b", r"\bgan\s+ethics\b"],
        "gan_fundamentals": [r"\bgans?\b", r"\bgenerative\s+adversarial\s+networks?\b"],
        "genai_vae": [r"\bvaes?\b", r"\bvariational\s+autoencoders?\b", r"\breparameterization\s+trick\b", r"\belbo\b"],
        "genai_diffusion_models": [r"\bdiffusion\s+models?\b", r"\bddpm\b", r"\bdenoising\s+diffusion\b", r"\bscore-based\s+models?\b"],
        "genai_autoregressive": [r"\bautoregressive\s+models?\b", r"\bpixelcnn\b", r"\bcausal\s+language\s+modeling\b"],
        "genai_multimodal_image": [r"\bclip\b", r"\bdall-?e\d?\b", r"\btext-to-image\b", r"\bmultimodal\s+generative\b"],
        "genai_finetuning_inference": [r"\blora\b", r"\bqlora\b", r"\bpeft\b", r"\bkv-?cache\b"],
        # Machine Learning & Ensembles
        "ml_random_forests": [r"\brandom\s+forests?\b", r"\bbagging\b", r"\bbootstrap\s+aggregating\b"],
        "ml_gradient_boosting_xgboost": [r"\bxgboost\b", r"\bgradient\s+boosting\b", r"\bgbdt\b", r"\blightgbm\b", r"\bcatboost\b"],
        "ml_pca": [r"\bpca\b", r"\bprincipal\s+component\s+analysis\b"],
        "ds_feature_engineering": [r"\bfeature\s+engineering\b", r"\bsmote\b", r"\bimbalanced\s+data\b", r"\bstandardscaler\b"],
        # Agents, Multimodal & MLOps
        "agents_react_tool_calling": [r"\breact\b", r"\btool\s+calling\b", r"\bfunction\s+calling\b", r"\bai\s+agents?\b", r"\bagentic\s+ai\b", r"\bautonomous\s+agents?\b"],
        "agents_multi_agent": [r"\bmulti-?agent\b", r"\bautogen\b", r"\bcrewai\b"],
        "multimodal_vision_language": [r"\bvlms?\b", r"\bvision\s+language\s+models?\b", r"\bllava\b"],
        "mlops_foundations": [r"\bmlops\b", r"\bmodel\s+registry\b", r"\bdata\s+drift\b", r"\bconcept\s+drift\b"],
        "mlops_optimization_serving": [r"\bquantization\b", r"\bonnx\b", r"\bvllm\b", r"\btensorrt\b", r"\bpagedattention\b"],
        "safety_adversarial_jailbreaks": [r"\bjailbreaks?\b", r"\bprompt\s+injection\b", r"\bred\s+teaming\b"],
        # Mathematics & Foundations
        "math_linear_algebra": [r"\blinear\s+algebra\b", r"\beigenvalues?\b", r"\beigenvectors?\b", r"\bsvd\b"],
        "math_calculus_optimization": [r"\bcalculus\b", r"\bpartial\s+derivatives?\b", r"\bhessian\b", r"\bjacobian\b"],
        "math_probability_statistics": [r"\bprobability\b", r"\bmaximum\s+likelihood\b", r"\bmle\b", r"\bmap\s+estimation\b"],
        "python_ai_foundations": [r"\bpython\s+for\s+ai\b", r"\bnumpy\b", r"\bvectorization\b", r"\bbroadcasting\b"],
        "ai_scratch_computational": [r"\bscratch\s+ai\b", r"\bcomputational\s+thinking\b", r"\bteachable\s+machine\b"],
        # General Broad Concepts (Checked Last)
        "ml_definition": [r"\bmachine\s+learning\b", r"\bml\b"],
        "ai_definition": [r"\bartificial\s+intelligence\b", r"\bai\b"],
    }

    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def match_topic(self, query: str) -> Tuple[Optional[Topic], float, str]:
        """Matches a single query to the best topic in the knowledge base.

        Returns: (Topic or None, confidence_score, match_reason)
        """
        normalized_query = TextNormalizer.normalize(query)
        if not normalized_query:
            return None, 0.0, "Empty query"

        # Tier 1: Direct exact alias or topic name match
        cleaned_query = TextNormalizer.clean_query_for_topic_extraction(query)
        if cleaned_query in self.kb.alias_to_id:
            tid = self.kb.alias_to_id[cleaned_query]
            return self.kb.get_topic(tid), 1.0, f"Exact alias match for '{cleaned_query}'"

        if normalized_query in self.kb.alias_to_id:
            tid = self.kb.alias_to_id[normalized_query]
            return self.kb.get_topic(tid), 1.0, f"Exact query match for '{normalized_query}'"

        # Tier 2: Check explicit special acronym patterns
        for tid, patterns in self.SPECIAL_TERM_PATTERNS.items():
            for pat in patterns:
                # Disambiguate short 'ai' and 'ml' so they don't greedily match subwords
                if re.search(pat, normalized_query, re.IGNORECASE):
                    # Check if there is a more specific term in query (e.g. 'ai vs ml')
                    topic = self.kb.get_topic(tid)
                    if topic:
                        return topic, 0.95, f"Matched specialized technical pattern '{pat}'"

        # Tier 3: Multi-word N-Gram matching against aliases (from longest 4-gram down to 1-gram)
        tokens = Tokenizer.tokenize(normalized_query)
        ngrams = Tokenizer.get_all_ngrams(tokens, max_n=4)
        for gram in ngrams:
            # Skip generic 1-letter or pure stop words
            if len(gram) < 2 or gram in Tokenizer.STANDARD_STOPWORDS:
                continue
            if gram in self.kb.alias_to_id:
                tid = self.kb.alias_to_id[gram]
                return self.kb.get_topic(tid), 0.90, f"N-gram match on alias '{gram}'"

        # Tier 4: Keyword frequency scoring
        filtered_tokens = Tokenizer.filter_stopwords(tokens, preserve_intent_words=False)
        if filtered_tokens:
            scores = {}
            for tok in filtered_tokens:
                if tok in self.kb.keyword_to_ids:
                    for tid in self.kb.keyword_to_ids[tok]:
                        scores[tid] = scores.get(tid, 0) + 1

            if scores:
                best_tid = max(scores, key=scores.get)
                max_score = scores[best_tid]
                # Confidence proportional to keyword count
                confidence = min(0.85, 0.40 + (max_score * 0.15))
                return self.kb.get_topic(best_tid), confidence, f"Keyword overlap score ({max_score} terms)"

        # Tier 5: Fallback partial search across names
        candidates = self.kb.search_topics(cleaned_query)
        if candidates:
            return candidates[0], 0.60, "Fuzzy name/definition search match"

        return None, 0.0, "No matching topic found"

    def match_two_topics_for_comparison(self, query: str) -> Tuple[Optional[Topic], Optional[Topic], str]:
        """Extracts two distinct topics from a comparative query.

        Examples:
        - "difference between AI and ML"
        - "compare CNN and RNN"
        - "AI vs ML"
        - "supervised vs unsupervised"
        """
        normalized = TextNormalizer.normalize(query)

        # Regex patterns to split comparative queries
        split_patterns = [
            r"\bdifference\s+between\s+(.+?)\s+and\s+(.+)$",
            r"\bcompare\s+(.+?)\s+and\s+(.+)$",
            r"\bcompare\s+(.+?)\s+with\s+(.+)$",
            r"\bcontrast\s+(.+?)\s+and\s+(.+)$",
            r"(.+?)\s+\bvs\.?\b\s+(.+)$",
            r"(.+?)\s+\bversus\b\s+(.+)$",
            r"\bhow\s+does\s+(.+?)\s+differ\s+from\s+(.+)$",
            r"\bwhat\s+is\s+the\s+difference\s+between\s+(.+?)\s+and\s+(.+)$",
        ]

        part1, part2 = None, None
        for pat in split_patterns:
            m = re.search(pat, normalized)
            if m:
                part1 = m.group(1).strip()
                part2 = m.group(2).strip()
                break

        if part1 and part2:
            t1, _, _ = self.match_topic(part1)
            t2, _, _ = self.match_topic(part2)
            if t1 and t2 and t1.id != t2.id:
                return t1, t2, f"Extracted comparison parts: '{part1}' vs '{part2}'"

        # Fallback: scan for all special term patterns or aliases appearing in the query
        detected_topics = []
        # Check special patterns first
        for tid, patterns in self.SPECIAL_TERM_PATTERNS.items():
            for pat in patterns:
                if re.search(pat, normalized):
                    top = self.kb.get_topic(tid)
                    if top and top not in detected_topics:
                        detected_topics.append(top)
                        break

        if len(detected_topics) >= 2:
            return detected_topics[0], detected_topics[1], "Matched two distinct topics in query text"

        return None, None, "Could not extract two distinct topics for comparison"
