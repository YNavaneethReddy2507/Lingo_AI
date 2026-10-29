"""
Script to generate a highly professional, 35-slide widescreen presentation (16:9)
covering NLP foundations (Slides 1-25) and AI KnowledgeBot Project Workflow (Slides 26-35).
"""
import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # Blank slide

    # Theme Colors
    BG_DARK = RGBColor(15, 23, 42)        # Slate 900
    BG_CARD = RGBColor(30, 41, 59)        # Slate 800
    BG_LIGHT_CARD = RGBColor(241, 245, 249) # Slate 100
    TEXT_DARK = RGBColor(15, 23, 42)      # Slate 900
    TEXT_MUTED = RGBColor(100, 116, 139)  # Slate 500
    TEXT_WHITE = RGBColor(255, 255, 255)
    PRIMARY_BLUE = RGBColor(37, 99, 235)  # Blue 600
    ACCENT_CYAN = RGBColor(6, 182, 212)   # Cyan 500
    ACCENT_EMERALD = RGBColor(16, 185, 129) # Emerald 500
    ACCENT_AMBER = RGBColor(245, 158, 11) # Amber 500
    BORDER_COLOR = RGBColor(203, 213, 225) # Slate 300
    ACCENT_INDIGO = RGBColor(79, 70, 229) # Indigo 600

    def add_header(slide, slide_num, category, title, is_dark=False):
        # Top banner background accent line
        line = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12)
        )
        line.fill.solid()
        line.fill.fore_color.rgb = ACCENT_CYAN if is_dark else PRIMARY_BLUE
        line.line.color.rgb = ACCENT_CYAN if is_dark else PRIMARY_BLUE

        # Category pill & Slide number badge
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.733), Inches(0.4))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = f"{category.upper()}  |  SLIDE {slide_num} OF 35"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN if is_dark else PRIMARY_BLUE

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.733), Inches(0.65))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE if is_dark else TEXT_DARK

    def add_card(slide, left, top, width, height, bg_color=RGBColor(255, 255, 255), border_color=BORDER_COLOR):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.2)
        else:
            card.line.fill.background()
        return card

    def add_content_block(slide, left, top, width, height, title, items, badge="", bg_color=RGBColor(255, 255, 255), border_color=BORDER_COLOR, title_color=PRIMARY_BLUE):
        add_card(slide, left, top, width, height, bg_color, border_color)

        # Title / Header
        tb = slide.shapes.add_textbox(left + Inches(0.3), top + Inches(0.25), width - Inches(0.6), Inches(0.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        if badge:
            p.text = f"[{badge}]  {title}"
        else:
            p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = title_color

        # Body items
        body_box = slide.shapes.add_textbox(left + Inches(0.3), top + Inches(0.8), width - Inches(0.6), height - Inches(1.0))
        tf_b = body_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0

        for i, item in enumerate(items):
            p_b = tf_b.add_paragraph() if i > 0 else tf_b.paragraphs[0]
            p_b.space_after = Pt(7)
            if isinstance(item, tuple):
                # (heading, desc)
                run1 = p_b.add_run()
                run1.text = f"• {item[0]}: "
                run1.font.bold = True
                run1.font.size = Pt(11.5)
                run1.font.color.rgb = TEXT_DARK
                run2 = p_b.add_run()
                run2.text = item[1]
                run2.font.bold = False
                run2.font.size = Pt(11)
                run2.font.color.rgb = RGBColor(51, 65, 85)
            else:
                p_b.text = f"• {item}"
                p_b.font.size = Pt(11)
                p_b.font.color.rgb = RGBColor(51, 65, 85)

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    # =========================================================================
    # SLIDE 1: Text Normalization
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, RGBColor(248, 250, 252))
    add_header(s1, 1, "Module 1: NLP Fundamentals", "Text Normalization: Transforming Raw Text into Canonical Forms")
    add_content_block(s1, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Core Normalization Techniques",
        [
            ("Case Folding", "Converting all text to lowercase to prevent vocabulary fragmentation (e.g., 'Model', 'model', 'MODEL' -> 'model')."),
            ("Noise Removal", "Stripping HTML tags, URLs, special control characters, emojis, and unprintable ASCII codes using regular expressions."),
            ("Contraction Expansion", "Restoring colloquial forms into formal equivalents (e.g., \"don't\" -> \"do not\", \"can't\" -> \"cannot\")."),
            ("Unicode Normalization", "Applying NFKD/NFC transformations to convert accents and diacritics (e.g., 'café' -> 'cafe', smart quotes to straight quotes)."),
            ("Special Token Protection", "Preserving domain-specific mathematical or technical tokens (e.g., 'A*', 'C++', 'L1/L2') during symbol sanitization.")
        ],
        badge="TECHNIQUES", title_color=PRIMARY_BLUE
    )
    add_content_block(s1, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Stemming vs. Lemmatization Comparison",
        [
            ("Stemming Concept", "Crude heuristic rule-based affix chopping that strips word prefixes and suffixes without morphological awareness."),
            ("Stemming Examples", "Porter / Lancaster Stemmer: 'studies' -> 'studi', 'meeting' -> 'meet', 'university' -> 'univers' (often non-words)."),
            ("Lemmatization Concept", "Morphological analysis utilizing vocabulary lookup and Part-of-Speech tags to return true dictionary root forms (lemmas)."),
            ("Lemmatization Examples", "WordNet Lemmatizer: 'better' (with POS=a) -> 'good', 'saw' (POS=v) -> 'see', 'corpora' -> 'corpus'."),
            ("Tradeoff Analysis", "Stemming is extremely fast with low memory overhead; Lemmatization is linguistically accurate but requires lexicon lookup and POS context.")
        ],
        badge="STEMMING VS LEMMA", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 2: Text Segmentation
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, RGBColor(248, 250, 252))
    add_header(s2, 2, "Module 1: NLP Fundamentals", "Text Segmentation: Sentence Boundaries and Tokenization Paradigms")
    add_content_block(s2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Sentence Segmentation & Word Tokenization",
        [
            ("Sentence Boundary Disambiguation (SBD)", "Detecting end-of-sentence punctuation ('.', '!', '?') while disambiguating abbreviations (Dr., e.g., U.S.A.) and numerical decimals ($3.50)."),
            ("Rule-Based Heuristics", "Regular expression lookaheads checking whether a period is followed by whitespace and an uppercase character."),
            ("Whitespace & Word Tokenization", "Splitting raw streams into discrete word tokens while preserving compound hyphenated entities ('state-of-the-art', 'decision-tree')."),
            ("Punctuation Handling", "Isolating punctuation marks as standalone tokens without corrupting contraction clitics (e.g., \"they're\" -> [\"they\", \"'re\"])."),
            ("Non-Segmenting Languages", "Languages such as Chinese and Japanese lack explicit whitespace, necessitating dictionary longest-match or character lattice segmentation.")
        ],
        badge="WORD & SENTENCE", title_color=PRIMARY_BLUE
    )
    add_content_block(s2, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Subword Tokenization Algorithms",
        [
            ("Out-of-Vocabulary (OOV) Dilemma", "Traditional word-level vocabularies suffer from huge memory footprints and failure when encountering unseen words."),
            ("Byte-Pair Encoding (BPE)", "Starts with character alphabet; iteratively counts and merges the most frequent adjacent character pairs (used in GPT-2, RoBERTa)."),
            ("WordPiece Tokenizer", "Maximizes the language model likelihood when adding merged subwords, using '##' prefixes for continuation tokens (used in BERT)."),
            ("SentencePiece / Unigram", "Treats whitespace as an ordinary character ('_'), enabling language-independent lossless tokenization without pre-segmentation."),
            ("Subword Example", "'unhappiness' -> ['un', '##happi', '##ness']; unseen word 'bioengineering' -> ['bio', '##engineer', '##ing'].")
        ],
        badge="SUBWORD ALGORITHMS", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 3: Corpus and Corpus Construction
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, RGBColor(248, 250, 252))
    add_header(s3, 3, "Module 2: Linguistic Data", "Corpus Foundations: Typologies, Design Principles, and Representativeness")
    add_content_block(s3, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Corpus Definition & Core Typologies",
        [
            ("Corpus Definition", "A large, curated, machine-readable collection of authentic, structured texts assembled according to rigorous sampling criteria."),
            ("Monolingual vs. Multilingual", "Single language (e.g., British National Corpus) vs Parallel aligned sentence pairs (e.g., Europarl for Machine Translation)."),
            ("Synchronic vs. Diachronic", "Capturing language at a specific slice in time vs tracking linguistic and lexical evolution across historical eras."),
            ("Balanced / General Corpora", "Proportionally sampled across diverse genres (news, fiction, academic, spoken, web) to model language generally (e.g., Brown Corpus)."),
            ("Domain-Specific Corpora", "Targeted collections optimized for niche tasks: PubMed for biomedicine, SEC EDGAR for finance, arXiv for computer science.")
        ],
        badge="TYPOLOGY", title_color=PRIMARY_BLUE
    )
    add_content_block(s3, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Corpus Construction Best Practices",
        [
            ("Domain Definition & Scope", "Formulating boundary constraints on document genre, target registers, geographic dialects, and temporal boundaries."),
            ("Sampling & Stratification", "Selecting representative texts across publications and authors to prevent over-representation of outlier writing styles."),
            ("Deduplication & Hygiene", "MinHash LSH and exact text fingerprinting to remove scraped boilerplate, duplicate articles, and copyright disclaimers."),
            ("Metadata Association", "Attaching author, date, source URL, genre, reading grade level, and language tags to every text document."),
            ("Legal & Ethical Compliance", "Verifying licensing, fair use exemptions, user privacy scrubbing (PII redaction), and copyright restrictions.")
        ],
        badge="PIPELINE", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 4: Corpus Annotation & Agreement
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, RGBColor(248, 250, 252))
    add_header(s4, 4, "Module 2: Linguistic Data", "Corpus Annotation Pipelines and Inter-Annotator Agreement")
    add_content_block(s4, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Annotation Hierarchy & Guidelines",
        [
            ("Annotation Layers", "Enriching raw text across structural strata: POS tags, syntactic parse trees, named entities, coreference, and semantic roles."),
            ("Annotation Guidelines", "Comprehensive documentation defining boundary edge cases, disambiguation rules, and operational examples for annotators."),
            ("Dual Annotation Workflow", "Independent labeling of the identical text by multiple expert annotators to measure consistency and ambiguity."),
            ("Adjudication Process", "A senior linguist or curator resolves conflicts where annotators disagree, finalizing ground-truth benchmark datasets."),
            ("Active Learning in Annotation", "Training preliminary models to identify low-confidence examples, prioritizing human labeling where uncertainty is greatest.")
        ],
        badge="WORKFLOW", title_color=PRIMARY_BLUE
    )
    add_content_block(s4, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Inter-Annotator Agreement: Cohen's Kappa",
        [
            ("Agreement Objective", "Quantifying annotation reliability beyond chance agreement between independent raters."),
            ("Cohen's Kappa Formula", "kappa = (P_o - P_e) / (1 - P_e), where P_o is observed proportion of agreement and P_e is chance agreement."),
            ("Observed Agreement (P_o)", "Sum of diagonal cells in confusion matrix divided by total annotated instances: P_o = sum(C_ii) / N."),
            ("Expected Agreement (P_e)", "Sum of products of marginal probabilities for each category: P_e = sum(p_i1 * p_i2)."),
            ("Interpretation Standards", "kappa < 0: Poor; 0.21-0.40: Fair; 0.61-0.80: Substantial; 0.81-1.00: Near Perfect agreement. Crucial for benchmark validity.")
        ],
        badge="COHEN'S KAPPA", title_color=ACCENT_AMBER
    )

    # =========================================================================
    # SLIDE 5: Regular Expressions in NLP
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, RGBColor(248, 250, 252))
    add_header(s5, 5, "Module 3: Pattern Matching", "Regular Expressions (Regex) in NLP: Syntax, Quantifiers, and Rule Patterns")
    add_content_block(s5, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Metacharacters, Anchors & Character Classes",
        [
            ("Anchors (^, $)", "'^' asserts start of string/line; '$' asserts end of string/line (e.g., ^[A-Z] matches sentences starting with capital)."),
            ("Word Boundaries (\\b)", "Asserts position between a word character (\\w) and non-word character (\\W). Essential for exact keyword matching (\\bAI\\b vs 'AIR')."),
            ("Predefined Character Classes", "\\d (digit [0-9]), \\w (alphanumeric [a-zA-Z0-9_]), \\s (whitespace [ \\t\\r\\n\\f])."),
            ("Custom Character Sets", "[a-zA-Z] matches any alphabet letter; [^0-9] negates digits; [-+] matches signs."),
            ("Disjunction / Alternation (|)", "(cat|dog|bird) matches any alternative in the grouping.")
        ],
        badge="SYNTAX & ANCHORS", title_color=PRIMARY_BLUE
    )
    add_content_block(s5, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Quantifiers, Capturing Groups & Lookarounds",
        [
            ("Greedy vs. Lazy Quantifiers", "* (0+), + (1+), ? (0 or 1), {m,n} (between m and n times). Append '?' for lazy/non-greedy matching (*? or +?)."),
            ("Capturing vs Non-Capturing Groups", "(pattern) captures matched substring into group indices; (?:pattern) matches without capturing overhead."),
            ("Positive Lookahead (?=...)", "Asserts regex matches only if followed by subpattern: '\\d+(?=\\s*USD)' matches '500' in '500 USD'."),
            ("Negative Lookahead (?!...)", "Asserts regex matches only if NOT followed by subpattern: 'apple(?!\\s*pie)' matches 'apple' if not 'apple pie'."),
            ("Entity Extraction Regex Example", "Date extraction: r'\\b(19|20)\\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])\\b'.")
        ],
        badge="ADVANCED REGEX", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 6: Information Extraction (IE)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, RGBColor(248, 250, 252))
    add_header(s6, 6, "Module 3: Pattern Matching", "Information Extraction: Transforming Unstructured Text into Structured Knowledge")
    add_content_block(s6, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "The Information Extraction Pipeline",
        [
            ("Objective of IE", "Extracting predefined types of facts, entities, and relationships from unconstrained natural text into relational tables."),
            ("Named Entity Detection", "Locating mentions of people, companies, geographical locations, monetary quantities, and temporal expressions."),
            ("Entity Linking & Disambiguation", "Mapping text surface strings to canonical knowledge graph nodes (e.g., 'Apple' to NASDAQ:AAPL vs the fruit)."),
            ("Co-reference Resolution", "Connecting pronouns and alternative mentions to the primary entity ('Sundar Pichai was appointed CEO. He said...')."),
            ("Template Filling", "Populating fixed schema slots for events (e.g., Acquisition Template: Buyer, Target, Value, Date, Advisors).")
        ],
        badge="IE PIPELINE", title_color=PRIMARY_BLUE
    )
    add_content_block(s6, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Relation Extraction Paradigms",
        [
            ("Relation Definition", "Identifying semantic predicates binding entity pairs: Rel(Entity1, Entity2) (e.g., FoundedBy(Google, Larry Page))."),
            ("Hearst Patterns (Lexico-Syntactic)", "Hand-crafted regex rules detecting hyponymy/hypernymy: 'X such as Y', 'X including Y, Z' -> is-a(Y, X)."),
            ("Supervised Classification", "Training classifiers (SVM, BiLSTM, BERT) on annotated sentence paths between entity mention spans."),
            ("Distant Supervision (Mintz et al.)", "Aligning a known knowledge graph relation triple with all text sentences co-mentioning both entities to auto-generate training data."),
            ("Open Information Extraction (OpenIE)", "Domain-independent extraction of arbitrary relational tuples (Subject, Predicate, Object) without predefined schemata.")
        ],
        badge="RELATION EXTRACTION", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 7: Part-of-Speech (POS) Tagging
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, RGBColor(248, 250, 252))
    add_header(s7, 7, "Module 4: Syntactic Analysis", "Part-of-Speech (POS) Tagging: Syntactic Categories and Lexical Ambiguity")
    add_content_block(s7, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Grammatical Categories & Tagsets",
        [
            ("Definition of POS Tagging", "Assigning a specific grammatical category tag (noun, verb, adjective, preposition) to each token in a sentence."),
            ("Penn Treebank 45-Tag Tagset", "Standard benchmark tagset: NN (singular noun), NNS (plural noun), NNP (proper noun), VB (base verb), VBD (past verb), JJ (adjective), IN (preposition)."),
            ("Universal Dependencies Tagset (UPOS)", "17 coarse universal tags across languages: NOUN, VERB, ADJ, ADV, PRON, DET, ADP, CONJ, NUM, PUNCT."),
            ("Syntactic Utility", "Serves as prerequisite input for dependency parsers, named entity recognition, text-to-speech phoneme selection, and phrase chunking."),
            ("Morphological Enrichment", "In morphologically rich languages, tags also encode gender, number, case, tense, and aspect.")
        ],
        badge="TAGSETS & ROLE", title_color=PRIMARY_BLUE
    )
    add_content_block(s7, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Lexical Ambiguity & Disambiguation",
        [
            ("The Ambiguity Challenge", "A massive proportion of English words function across multiple grammatical categories depending entirely on contextual syntax."),
            ("Classic POS Ambiguity Example", "'Time flies like an arrow':\n• 'Time' can be Noun, Verb, or Adjective.\n• 'flies' can be Plural Noun or Verb.\n• 'like' can be Preposition, Verb, or Conjunction."),
            ("Frequency-Based Baseline", "Assigning each word its most frequent tag from a training corpus achieves ~90% accuracy; remaining 10% requires sequence context."),
            ("Syntactic Context Resolution", "Determining that 'book' after 'a' is a noun (NN), while 'book' after 'to' is a verb (VB)."),
            ("Capitalization & Affix Clues", "Capitalization indicates NNP; suffixes '-tion', '-ment' signal NN; '-ly' indicates RB (adverb).")
        ],
        badge="AMBIGUITY", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 8: POS Tagging Approaches
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, RGBColor(248, 250, 252))
    add_header(s8, 8, "Module 4: Syntactic Analysis", "POS Tagging Approaches: Rule-Based, Transformation-Based, and Statistical")
    add_content_block(s8, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Rule-Based & Transformation-Based (TBL)",
        [
            ("Two-Stage Rule-Based Tagger", "1. Lexicon lookup assigns every word all possible candidate tags.\n2. Disambiguation rules eliminate invalid tags based on neighboring context."),
            ("Hand-Crafted Constraint Grammar", "Example rule: If word is ambiguous between verb and noun and immediately preceded by a possessive pronoun ('my book'), eliminate verb tag."),
            ("Brill's Transformation-Based Learning", "Learns error-correcting rules automatically from a tagged corpus starting from a simple baseline tagger."),
            ("TBL Rule Template", "Change tag from A to B if predecessor is tagged C (e.g., Change NN to VB if previous word is 'to' [TO])."),
            ("TBL Advantages", "Produces human-interpretable linguistic rule sets; small footprint; resistant to over-fitting on small lexicons.")
        ],
        badge="RULE & TBL", title_color=PRIMARY_BLUE
    )
    add_content_block(s8, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Statistical, Generative & Neural Taggers",
        [
            ("Stochastic HMM Taggers", "Generative sequence model optimizing joint probability P(Words, Tags) via transition and emission probabilities."),
            ("Maximum Entropy Markov Models (MEMM)", "Discriminative log-linear model supporting arbitrary overlapping features; suffers from label bias problem."),
            ("Linear-Chain Conditional Random Fields (CRF)", "Global normalization avoids label bias; state-of-the-art for traditional feature-engineered sequence labeling."),
            ("BiLSTM-CRF Neural Tagger", "Bidirectional LSTM encodes character/word representations; CRF layer enforces global tag transition constraints."),
            ("Transformer-Based Tagging (BERT)", "Token-classification head over contextual transformer representations; achieves >97.5% Penn Treebank accuracy.")
        ],
        badge="STATISTICAL & DL", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 9: Hidden Markov Models (HMM) Architecture
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, RGBColor(248, 250, 252))
    add_header(s9, 9, "Module 5: Sequence Modeling", "Hidden Markov Models (HMM): Mathematical Framework for Sequence Labeling")
    add_content_block(s9, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "HMM Five-Tuple Formal Definition",
        [
            ("States (S)", "Set of hidden states S = {s1, s2, ..., sN}. In POS tagging, hidden states correspond to POS tags (NN, VB, JJ)."),
            ("Observations (V)", "Vocabulary of observable symbols V = {v1, v2, ..., vM}. In NLP, observations are raw tokenized words in text."),
            ("Transition Probability Matrix (A)", "A = {a_ij}, where a_ij = P(q_t = s_j | q_{t-1} = s_i). Probability of transitioning from tag s_i to tag s_j."),
            ("Emission Probability Matrix (B)", "B = {b_j(k)}, where b_j(k) = P(o_t = v_k | q_t = s_j). Probability that tag s_j emits observed word v_k."),
            ("Initial State Distribution (pi)", "pi = {pi_i}, where pi_i = P(q_1 = s_i). Probability of the sequence starting in state s_i.")
        ],
        badge="HMM 5-TUPLE", title_color=PRIMARY_BLUE
    )
    add_content_block(s9, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Two Fundamental Markov Assumptions",
        [
            ("1. First-Order Markov Property", "The current state depends solely on the immediately preceding state: P(q_t | q_1, ..., q_{t-1}) = P(q_t | q_{t-1})."),
            ("2. Output Independence Assumption", "The observed token at time t depends only on the current hidden state at time t: P(o_t | q_1, ..., q_t, o_1, ..., o_{t-1}) = P(o_t | q_t)."),
            ("Joint Probability Formulation", "P(O, Q) = pi_{q_1} * b_{q_1}(o_1) * prod_{t=2}^T a_{q_{t-1}, q_t} * b_{q_t}(o_t)."),
            ("MLE Estimation from Tagged Corpus", "a_ij = Count(s_i, s_j) / Count(s_i);  b_j(k) = Count(s_j, v_k) / Count(s_j)."),
            ("Out-of-Vocabulary Emission Handling", "Assigning uniform floor probability or smoothing based on morphological prefixes/suffixes for unseen words.")
        ],
        badge="MATHEMATICS", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 10: Three HMM Problems & Viterbi Decoding
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, RGBColor(248, 250, 252))
    add_header(s10, 10, "Module 5: Sequence Modeling", "The 3 HMM Problems and the Viterbi Dynamic Programming Algorithm")
    add_content_block(s10, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "The 3 Classical HMM Problems",
        [
            ("Problem 1: Evaluation (Likelihood)", "Given model lambda=(A, B, pi) and observation sequence O, compute P(O|lambda). Solved via Forward-Backward Algorithm in O(N^2 * T) time."),
            ("Problem 2: Decoding (Inference)", "Given model lambda and observation sequence O, discover the optimal hidden state sequence Q* that best explains O. Solved via Viterbi Algorithm."),
            ("Problem 3: Learning (Training)", "Given observation sequence O (unlabeled), adjust model parameters lambda to maximize P(O|lambda). Solved via Baum-Welch (EM) Algorithm."),
            ("Computational Bottleneck", "Naive brute-force path evaluation requires O(N^T) operations, which is computationally intractable for realistic sentence lengths.")
        ],
        badge="3 PROBLEMS", title_color=PRIMARY_BLUE
    )
    add_content_block(s10, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Viterbi Decoding Algorithm & Recurrence",
        [
            ("Viterbi Trellis Variable v_t(j)", "Represents maximum probability of observing o_1...o_t along single best path terminating in state s_j at time t."),
            ("Initialization (t = 1)", "v_1(j) = pi_j * b_j(o_1);  backpointer ptr_1(j) = 0 for all j."),
            ("Induction Step (t = 2 to T)", "v_t(j) = max_{1 <= i <= N} [ v_{t-1}(i) * a_ij ] * b_j(o_t)."),
            ("Backpointer Matrix Storage", "ptr_t(j) = argmax_{1 <= i <= N} [ v_{t-1}(i) * a_ij ]. Tracks winning predecessor state for backward path recovery."),
            ("Termination & Backtracking", "Best final state q_T* = argmax_i v_T(i). Trace backwards: q_t* = ptr_{t+1}(q_{t+1}*). Complexity: O(N^2 * T).")
        ],
        badge="VITERBI ALGORITHM", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 11: N-gram Language Modeling
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, RGBColor(248, 250, 252))
    add_header(s11, 11, "Module 6: Language Modeling", "N-gram Language Modeling: Probability Estimation and the Markov Chain")
    add_content_block(s11, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Probabilistic Language Modeling Formulation",
        [
            ("Goal of Language Modeling", "Assigning a probability P(W) to a sequence of words W = (w1, w2, ..., wm) and predicting the next word P(w_{k} | w_1, ..., w_{k-1})."),
            ("Probability Chain Rule (Exact)", "P(w_1, w_2, ..., w_m) = prod_{k=1}^m P(w_k | w_1, w_2, ..., w_{k-1}). Exponentially unmanageable history."),
            ("Markov Assumption (Order n-1)", "Assume probability of the current word depends solely on preceding n-1 words: P(w_k | w_1, ..., w_{k-1}) approx P(w_k | w_{k-n+1}, ..., w_{k-1})."),
            ("Unigram Model (n = 1)", "Assumes complete word independence: P(W) = prod_{i=1}^m P(w_i) = prod C(w_i)/N."),
            ("Bigram Model (n = 2)", "Conditioned on immediate predecessor: P(W) = prod_{i=1}^m P(w_i | w_{i-1}).")
        ],
        badge="FOUNDATIONS", title_color=PRIMARY_BLUE
    )
    add_content_block(s11, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Maximum Likelihood Estimation & Perplexity",
        [
            ("Bigram MLE Formula", "P_MLE(w_i | w_{i-1}) = Count(w_{i-1}, w_i) / Count(w_{i-1})."),
            ("Trigram MLE Formula", "P_MLE(w_i | w_{i-2}, w_{i-1}) = Count(w_{i-2}, w_{i-1}, w_i) / Count(w_{i-2}, w_{i-1})."),
            ("Sentence Probability Example", "P('<s> AI KnowledgeBot is interactive </s>') = P(AI|<s>) * P(KnowledgeBot|AI) * P(is|KnowledgeBot) * P(interactive|is) * P(</s>|interactive)."),
            ("Perplexity (PPL) Metric", "PP(W) = P(w_1, ..., w_m)^{-1/m} = exp(- 1/m sum ln P(w_i | w_{<i}))."),
            ("Perplexity Interpretation", "Geometric average branching factor. Lower perplexity indicates superior predictive power and tighter probability fit.")
        ],
        badge="MLE & PERPLEXITY", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 12: Zero-Probability Problem & Smoothing
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12, RGBColor(248, 250, 252))
    add_header(s12, 12, "Module 6: Language Modeling", "The Zero-Probability Problem and Additive Laplace Smoothing")
    add_content_block(s12, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "The Zero-Probability Bottleneck (Sparsity)",
        [
            ("The Zero-Frequency Phenomenon", "Even massive corpora contain only a fraction of valid n-grams. If Count(w_{i-1}, w_i) = 0, then P_MLE(w_i | w_{i-1}) = 0."),
            ("Catastrophic Product Nullification", "Because sentence probability multiplies conditional probabilities, a single unseen bigram zeroes the entire sentence probability: P(W) = 0!"),
            ("Perplexity Divergence", "Zero probability causes log(0) = -infinity, causing perplexity to diverge to infinity, making model evaluation impossible."),
            ("Concept of Smoothing (Discounting)", "Stealing probability mass from frequent n-grams and reallocating it to zero-count and rare events."),
            ("Zipf's Law Rationale", "A tiny number of words occur frequently, while vast numbers of words and combinations occur rarely or never.")
        ],
        badge="THE PROBLEM", title_color=PRIMARY_BLUE
    )
    add_content_block(s12, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Laplace (Add-1) & Lidstone (Add-k) Smoothing",
        [
            ("Laplace (Add-1) Formula", "P_Laplace(w_i | w_{i-1}) = [ Count(w_{i-1}, w_i) + 1 ] / [ Count(w_{i-1}) + |V| ], where |V| is vocabulary size."),
            ("Normalizing Denominator", "Adding 1 to every possible continuation word requires adding |V| to denominator to ensure sum_{w in V} P(w|w_{i-1}) = 1."),
            ("Lidstone (Add-k) Formula", "P_Add-k(w_i | w_{i-1}) = [ Count(w_{i-1}, w_i) + k ] / [ Count(w_{i-1}) + k*|V| ], where 0 < k < 1 (e.g., k = 0.05)."),
            ("Shortcoming of Laplace", "When |V| is large (e.g., 100,000 words), Add-1 allocates far too much probability mass to unseen events, severely degrading known probabilities."),
            ("Practical Role", "Useful baseline for naive Bayes text classification; largely superseded by Kneser-Ney in acoustic and language modeling.")
        ],
        badge="ADDITIVE SMOOTHING", title_color=ACCENT_AMBER
    )

    # =========================================================================
    # SLIDE 13: Advanced Smoothing Techniques
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13, RGBColor(248, 250, 252))
    add_header(s13, 13, "Module 6: Language Modeling", "Advanced Smoothing Techniques: Good-Turing, Backoff, and Kneser-Ney")
    add_content_block(s13, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Good-Turing & Jelinek-Mercer Interpolation",
        [
            ("Good-Turing Intuition", "Re-estimates frequency of things seen r times based on frequency of things seen r+1 times: r* = (r+1) * [N_{r+1} / N_r]."),
            ("Probability of Unseen Events in GT", "Total probability mass for zero-count items is P_0 = N_1 / N (proportion of singletons/hapax legomena)."),
            ("Jelinek-Mercer Interpolation", "Linearly blends trigram, bigram, and unigram probabilities using learned weights lambda:\nP_JM(w_i | w_{i-2}, w_{i-1}) = lambda_3 * P_MLE(w_i | w_{i-2}, w_{i-1}) + lambda_2 * P_MLE(w_i | w_{i-1}) + lambda_1 * P_MLE(w_i)."),
            ("Interpolation Invariant", "sum lambda_i = 1; ensures valid probability distribution while falling back smoothly when higher-order counts are sparse.")
        ],
        badge="GOOD-TURING & JM", title_color=PRIMARY_BLUE
    )
    add_content_block(s13, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Katz Backoff & Modified Kneser-Ney",
        [
            ("Katz Backoff Philosophy", "Uses MLE probability if count > 0; otherwise backs off to lower-order smoothed distribution scaled by normalization alpha."),
            ("Kneser-Ney Breakthrough", "Recognizes that lower-order unigram should reflect how likely a word is to complete a novel context, not just raw unigram frequency."),
            ("Classic 'Francisco' Example", "'San Francisco' is very frequent, making 'Francisco' have high unigram count. But 'Francisco' almost exclusively follows 'San' and should NOT be suggested in random contexts!"),
            ("Continuation Probability P_cont", "P_cont(w) = |{w_{i-1} : Count(w_{i-1}, w) > 0}| / sum_{w'} |{w_{i-1} : Count(w_{i-1}, w') > 0}|."),
            ("Kneser-Ney Interpolated Formula", "P_KN(w_i | w_{i-1}) = max(Count(w_{i-1}, w_i) - d, 0)/Count(w_{i-1}) + lambda(w_{i-1}) * P_cont(w_i). State of the art.")
        ],
        badge="KNESER-NEY", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 14: Named Entity Recognition (NER)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14, RGBColor(248, 250, 252))
    add_header(s14, 14, "Module 7: Entity Extraction", "Named Entity Recognition (NER): Task Definition, Taxonomy, and Tag Schemes")
    add_content_block(s14, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "NER Task Definition & Entity Taxonomies",
        [
            ("Definition of NER", "Information extraction subtask identifying and categorizing named entity spans in unstructured text into predefined semantic classes."),
            ("MUC Standard Categories", "PERSON (Alan Turing), ORGANIZATION (Google, DeepMind), LOCATION (London, California)."),
            ("CoNLL & OntoNotes Categories", "Extended to 18 classes: DATE, TIME, MONEY, PERCENT, GPE (geopolitical entities), NORP (nationalities/religions), FACILITY, PRODUCT."),
            ("Biomedical Domain NER", "Specialized entities: GENE, PROTEIN, DISEASE, CHEMICAL, DRUG (e.g., 'Metformin', 'BRCA1')."),
            ("Dual Subtask Formulation", "1. Entity Boundary Detection (where does the mention begin and end?)\n2. Entity Classification (what type of entity is it?).")
        ],
        badge="TAXONOMY", title_color=PRIMARY_BLUE
    )
    add_content_block(s14, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Sequence Tagging Schemes: IOB, BIOES & BILOU",
        [
            ("Sequence Labeling Formulation", "Transforms span extraction into token-level classification using positional boundary prefixes."),
            ("IOB / BIO Tagging Scheme", "• B (Begin): First token of multi-token entity span.\n• I (Inside): Subsequent tokens inside entity span.\n• O (Outside): Tokens not belonging to any entity."),
            ("Concrete BIO Example", "\"Google [B-ORG] DeepMind [I-ORG] opened [O] an [O] office [O] in [O] London [B-LOC] on [O] Monday [B-DATE]\"."),
            ("BIOES / BILOU Extension", "Adds E/L (End/Last) token and S/U (Single/Unit) token. Helps models explicitly learn transitions for single-token versus multi-token spans."),
            ("Evaluation Metrics", "Precision, Recall, and Strict Micro F1-Score requiring both exact entity boundary span AND correct semantic class.")
        ],
        badge="BIO TAGGING", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 15: Rule-Based NER
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15, RGBColor(248, 250, 252))
    add_header(s15, 15, "Module 7: Entity Extraction", "Rule-Based NER: Gazetteers, Contextual Clues, and Deterministic Heuristics")
    add_content_block(s15, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Gazetteers & Dictionary Matching",
        [
            ("Gazetteer Lists", "Curated white-lists containing millions of known entity instances (e.g., country lists, company registry databases, drug dictionaries)."),
            ("Aho-Corasick Algorithm", "Trie-based string matching that searches across millions of dictionary entries in O(Text Length + Matches) time."),
            ("Lexical Variation Challenges", "Fails on unseen spelling variations, nicknames, acronyms, or novel entities not in pre-compiled lists."),
            ("Case Sensitivity Matching", "Differentiating 'May' (Month/Person) vs 'may' (modal verb); 'Apple' (Company) vs 'apple' (fruit)."),
            ("Hybrid Gazetteer Features", "Feeding gazetteer hit binary flags as input features into statistical models (CRF, BiLSTM) to bridge rule-based and machine learning.")
        ],
        badge="GAZETTEERS", title_color=PRIMARY_BLUE
    )
    add_content_block(s15, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Contextual Heuristics & Pros / Cons",
        [
            ("Contextual Trigger Words", "Preceding or trailing trigger keywords signaling entity classes (e.g., 'CEO of [ORG]', 'Dr. [PERSON]', 'Inc.', 'Ltd.', 'River', 'Avenue')."),
            ("Capitalization & POS Patterns", "Proper noun sequences [NNP]+ followed by corporate designators: r'\\b[A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*\\s+(?:Inc\\.|Corp\\.|LLC)\\b'."),
            ("Advantages of Rule-Based NER", "100% deterministic, fully explainable, zero training annotations required, instant domain adaptation via list editing."),
            ("Limitations of Rule-Based NER", "High maintenance cost, brittle against spelling mistakes, unable to handle complex context-dependent ambiguity."),
            ("Modern Industry Use Cases", "Ideal for high-precision regulatory extraction (PII, SSN, Tax IDs, IP addresses, clinical trial codes).")
        ],
        badge="HEURISTICS & TRADEOFFS", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 16: Vector Space Model (VSM)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16, RGBColor(248, 250, 252))
    add_header(s16, 16, "Module 8: Text Representation", "Vector Space Model (VSM): Algebraic Representation of Documents and Terms")
    add_content_block(s16, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Salton's Vector Space Model Foundations",
        [
            ("Foundational Concept (Gerard Salton)", "Documents and search queries are represented as multidimensional vectors in a shared vector space: d_j = (w_{1j}, w_{2j}, ..., w_{Vj})^T."),
            ("Dimensionality |V|", "Each unique vocabulary term constitutes an independent orthogonal basis dimension in the geometric space."),
            ("Term-Document Matrix (TDM)", "A matrix X of size |V| x |D|, where cell X_{ij} contains the weight of term i in document j."),
            ("Bag-of-Words (BoW) Assumption", "Disregards word grammar, syntax, and sequence order, retaining only word occurrence frequency."),
            ("Geometric Retrieval Principle", "Documents judged semantically relevant to a user query lie closer in the vector space, measured by angular orientation.")
        ],
        badge="SALTON'S MODEL", title_color=PRIMARY_BLUE
    )
    add_content_block(s16, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Sparsity & Weighting Schemes in VSM",
        [
            ("Matrix Sparsity Challenge", "Real-world vocabularies contain 50,000+ words, but typical documents contain a few hundred words; matrices are >99% sparse."),
            ("Binary Weighting", "w_{ij} in {0, 1} indicating mere presence or absence of term in document."),
            ("Raw Term Frequency (TF)", "w_{ij} = count(t_i, d_j). Over-rewards excessively repeated words."),
            ("Logarithmic Term Frequency", "w_{ij} = 1 + log(TF_{ij}) if TF > 0, else 0. Dampens impact of repeated terms."),
            ("Matrix Storage Solutions", "Compressed Sparse Row (CSR) and Compressed Sparse Column (CSC) formats to store only non-zero coordinates in memory.")
        ],
        badge="SPARSITY & WEIGHTING", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 17: TF-IDF Term Weighting
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17, RGBColor(248, 250, 252))
    add_header(s17, 17, "Module 8: Text Representation", "TF-IDF Term Weighting: Balancing Local Importance with Corpus Specificity")
    add_content_block(s17, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Mathematical Formulation of TF-IDF",
        [
            ("Core Motivation", "A term appearing frequently in a specific document is important (high TF), but a term appearing across almost every document in corpus carries low informational value (low IDF)."),
            ("Term Frequency (TF)", "TF(t, d) = f_{t,d} / sum_{t' in d} f_{t',d}  (normalized local count)."),
            ("Inverse Document Frequency (IDF)", "IDF(t, D) = log [ N / (1 + |{d in D : t in d}|) ], where N is total documents and denominator counts document frequency."),
            ("TF-IDF Product", "TF-IDF(t, d, D) = TF(t, d) * IDF(t, D). High score means term is frequent locally and rare globally."),
            ("L2 Euclidean Normalization", "w'_i = w_i / sqrt(sum w_j^2). Eliminates bias favoring longer documents over concise ones.")
        ],
        badge="FORMULATION", title_color=PRIMARY_BLUE
    )
    add_content_block(s17, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Behavioral Dynamics & Stopword Suppression",
        [
            ("Stopword Elimination without Lists", "Common grammatical function words ('the', 'is', 'at') appear in 100% of documents; IDF = log(N/N) = log(1) = 0, automatically nullifying them!"),
            ("Signature Keyword Discovery", "Domain-specific terms ('transformer', 'mitochondria') appear concentrated in few documents, yielding high IDF and strong discriminative power."),
            ("Search Query Scoring", "Score(Query, Document) = sum_{t in Q} TF-IDF(t, d). Serves as classical search relevance backbone."),
            ("BM25 Evolution", "Okapi BM25 refines TF-IDF with non-linear asymptotic TF saturation and explicit document length normalization parameters (k1, b).")
        ],
        badge="DYNAMICS & BM25", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 18: Cosine Similarity Metric
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_background(s18, RGBColor(248, 250, 252))
    add_header(s18, 18, "Module 9: Similarity & Geometry", "Cosine Similarity: Mathematical Formulation and Geometric Properties")
    add_content_block(s18, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Cosine Similarity Mathematical Definition",
        [
            ("Definition", "Cosine similarity measures the cosine of the angle theta between two non-zero vectors u and v in an inner product space."),
            ("Dot Product Formulation", "cos(theta) = (u . v) / (||u||_2 * ||v||_2)."),
            ("Expanded Formula", "cos(theta) = [ sum_{i=1}^n u_i * v_i ] / [ sqrt(sum_{i=1}^n u_i^2) * sqrt(sum_{i=1}^n v_i^2) ]."),
            ("Value Range in Text Spaces", "Since term frequencies and TF-IDF weights are non-negative (u_i >= 0), cosine similarity is bounded in [0, 1]."),
            ("Geometric Interpretation", "• cos(theta) = 1 (theta = 0 deg): Identical direction / perfect similarity.\n• cos(theta) = 0 (theta = 90 deg): Orthogonal vectors / zero shared vocabulary.")
        ],
        badge="FORMULA", title_color=PRIMARY_BLUE
    )
    add_content_block(s18, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Why Cosine Beats Euclidean Distance in Text",
        [
            ("The Document Length Bias Problem", "Euclidean distance ||u - v|| = sqrt(sum (u_i - v_i)^2) is heavily distorted by document length. A short article and its long expanded version would have huge Euclidean distance."),
            ("Length Invariance of Cosine", "Cosine evaluates the angle (directional orientation) rather than vector magnitude (length). Concatenating a document with itself doubles its length but leaves its cosine angle unchanged!"),
            ("Cosine Distance Relationship", "Cosine Distance = 1 - Cosine Similarity. Note: Cosine distance is technically a semimetric (does not strictly satisfy triangle inequality)."),
            ("Computational Efficiency", "For unit-normalized vectors (||u|| = 1, ||v|| = 1), cosine similarity simplifies to pure dot product: cos(theta) = u . v.")
        ],
        badge="ADVANTAGES", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 19: Cosine Similarity Numerical Problem
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    set_slide_background(s19, RGBColor(248, 250, 252))
    add_header(s19, 19, "Module 9: Similarity & Geometry", "Worked Numerical Problem: Calculating Cosine Similarity Step-by-Step")
    add_content_block(s19, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Problem Setup & Vector Representations",
        [
            ("Given Documents", "D1: 'AI agents learn AI models'\nD2: 'models learn data patterns'"),
            ("Shared Vocabulary |V| = 6", "Index mapping: [1: 'AI', 2: 'agents', 3: 'learn', 4: 'models', 5: 'data', 6: 'patterns']"),
            ("Vector d1 (Term Frequency Counts)", "d1 = [2, 1, 1, 1, 0, 0]  (AI: 2, agents: 1, learn: 1, models: 1)"),
            ("Vector d2 (Term Frequency Counts)", "d2 = [0, 0, 1, 1, 1, 1]  (learn: 1, models: 1, data: 1, patterns: 1)"),
            ("Objective", "Calculate the exact cosine similarity cos(theta) between document vectors d1 and d2.")
        ],
        badge="STEP 1: SETUP", title_color=PRIMARY_BLUE
    )
    add_content_block(s19, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Step-by-Step Numerical Computation",
        [
            ("Step 2: Calculate Dot Product (d1 . d2)", "d1 . d2 = (2*0) + (1*0) + (1*1) + (1*1) + (0*1) + (0*1)\n= 0 + 0 + 1 + 1 + 0 + 0 = 2."),
            ("Step 3: Calculate L2 Norm ||d1||", "||d1|| = sqrt(2^2 + 1^2 + 1^2 + 1^2 + 0^2 + 0^2)\n= sqrt(4 + 1 + 1 + 1) = sqrt(7) approx 2.6458."),
            ("Step 4: Calculate L2 Norm ||d2||", "||d2|| = sqrt(0^2 + 0^2 + 1^2 + 1^2 + 1^2 + 1^2)\n= sqrt(1 + 1 + 1 + 1) = sqrt(4) = 2.0000."),
            ("Step 5: Compute Cosine Ratio", "cos(theta) = 2 / (sqrt(7) * 2) = 1 / sqrt(7) = 1 / 2.6458\napprox 0.3780 (37.8% similarity)."),
            ("Interpretation", "Documents share 2 terms ('learn', 'models') out of 6 vocabulary terms, resulting in a moderate semantic alignment score of 0.378.")
        ],
        badge="STEP 2-5: SOLUTION", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 20: Word Embeddings — Word2Vec
    # =========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    set_slide_background(s20, RGBColor(248, 250, 252))
    add_header(s20, 20, "Module 10: Distributed Representations", "Word2Vec: Continuous Distributed Semantic Representations (Mikolov 2013)")
    add_content_block(s20, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Distributional Hypothesis & Architectures",
        [
            ("Firth's Distributional Hypothesis (1957)", "\"You shall know a word by the company it keeps.\" Words occurring in similar linguistic contexts share semantic properties."),
            ("From Sparse to Dense Vectors", "Replaces sparse |V|-dimensional one-hot vectors with dense, low-dimensional continuous vectors in R^d (d in [100, 300])."),
            ("Continuous Bag-of-Words (CBOW)", "Predicts target center word w_t given context window words (w_{t-c}, ..., w_{t+c}). Smoother for frequent words, faster training."),
            ("Continuous Skip-Gram Architecture", "Predicts surrounding context words given target center word w_t. Superior representation for rare words and smaller datasets."),
            ("Sliding Context Window", "A symmetrical window of size c (e.g., c = 5) slides across corpus, generating millions of (center, context) training pairs.")
        ],
        badge="ARCHITECTURES", title_color=PRIMARY_BLUE
    )
    add_content_block(s20, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Negative Sampling & Optimization",
        [
            ("The Softmax Computational Bottleneck", "Full softmax denominator sum_{w' in V} exp(v'_{w'} . v_w) requires computing over all |V| words for every single gradient step: O(|V|)."),
            ("Negative Sampling (SGNS) Formulation", "Reformulates multi-class prediction into binary logistic regression: Is pair (w, c) a real corpus pair or sampled noise?"),
            ("SGNS Objective Function", "L = log sigma(v'_c . v_w) + sum_{i=1}^k E_{w_i ~ P_n(w)} [ log sigma(- v'_{w_i} . v_w) ], where k is negative samples (5-20)."),
            ("Noise Distribution P_n(w)", "Unigram distribution raised to the 3/4 power: P_n(w) proportional to U(w)^{0.75}. Balances frequency, boosting selection of rare words."),
            ("Hierarchical Softmax Alternative", "Huffman tree structure reducing computation to O(log_2 |V|).")
        ],
        badge="NEGATIVE SAMPLING", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 21: Word Embeddings — GloVe
    # =========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    set_slide_background(s21, RGBColor(248, 250, 252))
    add_header(s21, 21, "Module 10: Distributed Representations", "GloVe: Global Vectors for Word Representation (Pennington et al. 2014)")
    add_content_block(s21, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Global Co-occurrence vs. Local Windows",
        [
            ("Bridging Two Major Paradigms", "GloVe combines the benefits of global matrix factorization methods (LSA) with local window-based predictive models (Word2Vec)."),
            ("Global Co-occurrence Matrix X", "X_{ij} counts how often word j appears in the context of word i across the entire corpus."),
            ("Ratio of Co-occurrence Probabilities", "Let P_{ik} = X_{ik} / X_i. The ratio P_{ik} / P_{jk} isolates relevant words from noise."),
            ("Ice vs. Steam Canonical Example", "• k = 'solid': P(solid|ice)/P(solid|steam) is very large (~8.9).\n• k = 'gas': P(gas|ice)/P(gas|steam) is very small (~0.085).\n• k = 'water': Ratio is near 1.0 (equally relevant to both).\n• k = 'fashion': Ratio is near 1.0 (equally irrelevant).")
        ],
        badge="GLOBAL RATIOS", title_color=PRIMARY_BLUE
    )
    add_content_block(s21, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "GloVe Objective Function & Weighting",
        [
            ("GloVe Log-Bilinear Objective Function", "J = sum_{i,j=1}^V f(X_{ij}) * ( w_i^T * w_tilde_j + b_i + b_tilde_j - log X_{ij} )^2."),
            ("Soft Constraints on Dot Product", "Forces dot product of word vectors to approximate log probability of co-occurrence: w_i^T * w_tilde_j approx log(P_{ij})."),
            ("Weighting Function f(X_{ij})", "f(x) = (x / x_max)^alpha if x < x_max else 1.0 (typically alpha = 0.75, x_max = 100)."),
            ("Purpose of Weighting Function", "Prevents rare co-occurrences from dominating noise while preventing ultra-frequent co-occurrences ('the', 'of') from overwhelming model."),
            ("Vector Combination", "Final word embedding is typically the sum: W_final = w_i + w_tilde_i, boosting geometric robustness.")
        ],
        badge="OBJECTIVE & WEIGHTS", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 22: Word Vectors & Document Similarity
    # =========================================================================
    s22 = prs.slides.add_slide(blank_layout)
    set_slide_background(s22, RGBColor(248, 250, 252))
    add_header(s22, 22, "Module 11: Semantic Operations", "Word Vector Properties, Analogies, and Document Similarity")
    add_content_block(s22, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Vector Arithmetic & Semantic Analogies",
        [
            ("Linear Substructure of Word Vectors", "Semantic and grammatical relationships emerge as consistent displacement vectors in vector space."),
            ("Gender & Royalty Analogy", "v('king') - v('man') + v('woman') approx v('queen'). Cosine similarity discovers 'queen' as closest vector."),
            ("Capital Cities & Geopolitics", "v('Paris') - v('France') + v('Japan') approx v('Tokyo'); v('Rome') - v('Italy') + v('Germany') approx v('Berlin')."),
            ("Grammatical / Morphological Shifts", "v('walking') - v('walk') + v('swim') approx v('swimming'); v('bigger') - v('big') + v('fast') approx v('faster')."),
            ("Cosine Neighborhoods", "K-Nearest Neighbors (KNN) in embedding space retrieve synonym clusters and semantic relatives.")
        ],
        badge="ANALOGY ARITHMETIC", title_color=PRIMARY_BLUE
    )
    add_content_block(s22, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Document Embeddings & Semantic Similarity",
        [
            ("Word Centroid (Average Embedding)", "d = (1/|D|) sum_{w in D} v_w. Simple, highly competitive baseline for document representation."),
            ("TF-IDF Weighted Word Centroid", "d = sum_{w in D} [ TF-IDF(w) * v_w ] / sum TF-IDF(w). Down-weights stopwords, amplifying core content words."),
            ("Word Mover's Distance (WMD)", "Formulates document distance as Earth Mover's Distance (transportation problem): minimum cumulative distance words in D1 must travel to reach words in D2."),
            ("Doc2Vec (Paragraph Vector - Le & Mikolov)", "Distributed Memory (PV-DM) and Distributed BoW (PV-DBOW) learning explicit document-level tokens during training."),
            ("Sentence-BERT (Bi-Encoder Embeddings)", "Fine-tuned Siamese transformer generating fixed 768-d semantic sentence vectors optimized directly for cosine similarity.")
        ],
        badge="DOCUMENT VECTORS", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 23: Text Classification
    # =========================================================================
    s23 = prs.slides.add_slide(blank_layout)
    set_slide_background(s23, RGBColor(248, 250, 252))
    add_header(s23, 23, "Module 12: Supervised NLP", "Text Classification: Pipeline, Generative vs. Discriminative, and Naive Bayes")
    add_content_block(s23, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "The Text Classification Pipeline",
        [
            ("Definition", "Supervised learning task mapping input text documents x into one or more discrete predefined categories c in C."),
            ("Key Industry Applications", "Spam filtering, sentiment analysis, customer ticket routing, toxic speech moderation, legal document discovery."),
            ("Stage 1: Preprocessing & Tokenization", "Text cleaning, contraction expansion, tokenization, stopword removal."),
            ("Stage 2: Feature Extraction", "Transforming text into numerical features via BoW, TF-IDF, N-grams, or dense pretrained embeddings."),
            ("Stage 3: Classifier Training", "Optimizing decision boundaries using labeled training examples (x_i, c_i).")
        ],
        badge="PIPELINE", title_color=PRIMARY_BLUE
    )
    add_content_block(s23, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Multinomial Naive Bayes Classifier",
        [
            ("Bayes' Rule Formulation", "P(c | d) = [ P(c) * P(d | c) ] / P(d). Class c* = argmax_{c in C} P(c) * P(d | c)."),
            ("Conditional Independence Assumption", "Assumes all words w_i are conditionally independent given class c: P(d | c) = prod_{i=1}^n P(w_i | c)."),
            ("Class Prior Probability P(c)", "P(c) = Count(docs in class c) / Total documents."),
            ("Smoothed Likelihood Estimation", "P(w_i | c) = [ Count(w_i, c) + alpha ] / [ sum_{w in V} Count(w, c) + alpha * |V| ] (Laplace alpha = 1)."),
            ("Log-Space Calculation", "c* = argmax_c [ log P(c) + sum_{i=1}^n log P(w_i | c) ]. Prevents floating-point underflow.")
        ],
        badge="NAIVE BAYES", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 24: Discriminative Text Classifiers & Metrics
    # =========================================================================
    s24 = prs.slides.add_slide(blank_layout)
    set_slide_background(s24, RGBColor(248, 250, 252))
    add_header(s24, 24, "Module 12: Supervised NLP", "Discriminative Text Classifiers (SVM, Logistic Regression) & Evaluation Metrics")
    add_content_block(s24, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Support Vector Machines & Logistic Regression",
        [
            ("Linear SVM for Text", "Finds maximum-margin hyperplane w^T x + b = 0 separating classes. Highly effective in high-dimensional sparse text spaces without overfitting."),
            ("Hinge Loss & Regularization", "L = max(0, 1 - y_i(w^T x_i + b)) + lambda ||w||_2^2. Linear kernel is almost universally preferred over RBF in text."),
            ("Logistic Regression (Log-Linear)", "Models posterior probability directly via sigmoid P(y=1|x) = 1 / (1 + exp(-w^T x)). Provides calibrated probability scores."),
            ("L1 vs. L2 Feature Regularization", "L1 (Lasso) drives non-informative word weights to exact 0, performing automatic feature selection; L2 (Ridge) prevents weight explosion."),
            ("Pretrained Fine-Tuning (BERT/RoBERTa)", "Places classification head [CLS] over transformer encoder; fine-tunes all layers with cross-entropy loss.")
        ],
        badge="DISCRIMINATIVE MODELS", title_color=PRIMARY_BLUE
    )
    add_content_block(s24, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Evaluation Metrics: Precision, Recall, F1",
        [
            ("Confusion Matrix", "True Positives (TP), False Positives (FP), True Negatives (TN), False Negatives (FN)."),
            ("Precision (P)", "P = TP / (TP + FP). Out of all documents predicted as class C, how many were actually correct? Crucial for spam filtering."),
            ("Recall (R)", "R = TP / (TP + FN). Out of all actual documents in class C, how many did the model find? Crucial for legal e-discovery and medical diagnostics."),
            ("F1-Score (Harmonic Mean)", "F1 = 2 * (Precision * Recall) / (Precision + Recall). Balances precision and recall, especially on imbalanced datasets."),
            ("Macro vs. Micro Averaging", "Macro F1 calculates unweighted average across classes (highlights minority classes); Micro F1 pools global TP/FP/FN (dominated by majority).")
        ],
        badge="EVALUATION METRICS", title_color=ACCENT_AMBER
    )

    # =========================================================================
    # SLIDE 25: Text Summarization & Clustering
    # =========================================================================
    s25 = prs.slides.add_slide(blank_layout)
    set_slide_background(s25, RGBColor(248, 250, 252))
    add_header(s25, 25, "Module 13: Summarization & Clustering", "Text Summarization Paradigms and Unsupervised Document Clustering")
    add_content_block(s25, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Extractive vs. Abstractive Summarization",
        [
            ("Extractive Summarization", "Identifies, scores, and extracts the most salient verbatim sentences directly from the original source text."),
            ("TextRank / LexRank Algorithm", "Constructs a graph where nodes are sentences and edges are weighted by lexical similarity; applies PageRank centrality to rank sentences."),
            ("Abstractive Summarization", "Generates novel paraphrased sentences conveying core meaning, mimicking human synthesizers using encoder-decoder transformers (BART, T5)."),
            ("ROUGE Evaluation Metrics", "• ROUGE-1 / ROUGE-2: Unigram and bigram overlap with human reference summaries.\n• ROUGE-L: Longest Common Subsequence (captures sentence-level structure)."),
            ("Faithfulness & Hallucination", "Primary challenge in abstractive summarization: generating non-factual claims unsupported by source text.")
        ],
        badge="SUMMARIZATION", title_color=PRIMARY_BLUE
    )
    add_content_block(s25, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Text Clustering & Evaluation Measures",
        [
            ("Unsupervised Clustering in NLP", "Partitioning unannotated document collections into coherent topical groups without human labels."),
            ("K-Means for Text", "Iteratively assigns documents to closest centroid (via cosine similarity) and updates centroids to mean vector. Fast: O(t * k * n * d)."),
            ("Cluster Cohesion & Silhouette Score", "s(i) = [ b(i) - a(i) ] / max(a(i), b(i)), where a(i) is mean intra-cluster distance and b(i) is mean nearest-cluster distance."),
            ("Davies-Bouldin Index (DBI)", "Measures ratio of within-cluster spread to between-cluster separation. Lower DBI values indicate tighter, better-separated clusters."),
            ("Topic Modeling (LDA)", "Latent Dirichlet Allocation: Generative probabilistic model viewing documents as distributions over topics, and topics as distributions over words.")
        ],
        badge="CLUSTERING & METRICS", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 26: Project Overview — AI KnowledgeBot
    # =========================================================================
    s26 = prs.slides.add_slide(blank_layout)
    set_slide_background(s26, BG_DARK)
    add_header(s26, 26, "Project Architecture", "AI KnowledgeBot: Deterministic Rule-Based Educational System", is_dark=True)
    add_content_block(s26, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Project Philosophy & Core Pillars",
        [
            ("Zero Hallucinations Guarantee", "Strictly deterministic rule-based execution. Every single response is generated from verified educational knowledge bases, never fabricated."),
            ("Zero Cloud & API Subscriptions", "100% offline, privacy-preserving execution on local hardware. Zero dependency on OpenAI, Anthropic, or external LLM tokens."),
            ("Symbolic Verifiability", "Every assistant response exposes an expandable Rule Match Inspector showing the exact intent, regex pattern, and confidence score."),
            ("Comprehensive Academic Curriculum", "Curated coverage of 10 complete modules and 117 topics from Scratch fundamentals to cutting-edge Generative AI & MLOps."),
            ("Modern Production Engineering", "Structured Python backend, modular JSON data layer, Streamlit frontend, and automated Pytest test suite.")
        ],
        badge="CORE PRINCIPLES", bg_color=BG_CARD, border_color=ACCENT_CYAN, title_color=ACCENT_CYAN
    )
    add_content_block(s26, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Curriculum Coverage at a Glance",
        [
            ("Module A: Fundamentals (7 topics)", "Scratch block programming, Turing Test, Narrow AI vs AGI vs ASI, Rational Agents, Ethics."),
            ("Module B: Machine Learning (18 topics)", "Supervised, Unsupervised, RL, Ensembles (Random Forest, XGBoost), PCA, Feature Engineering."),
            ("Module C: Deep Learning (11 topics)", "Perceptrons, Backpropagation, Optimizers (Adam), Activations, BatchNorm/LayerNorm, Transformers."),
            ("Module D: NLP (19 topics)", "Tokenization, POS, NER, HMM, N-grams, Word2Vec, GloVe, BERT, Translation, Summarization."),
            ("Module E-G: Vision, KBS, Search (24 topics)", "YOLO, ResNet, Expert Systems, Forward/Backward Chaining, A* Search, Minimax, Robotics SLAM."),
            ("Module H-J: GenAI, Math, MLOps (38 topics)", "Exhaustive GANs, VAEs, Diffusion, Linear Algebra, Calculus, ReAct Agents, MLOps Serving.")
        ],
        badge="10 MODULES / 117 TOPICS", bg_color=BG_CARD, border_color=ACCENT_EMERALD, title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 27: System End-to-End Workflow & Pipeline Architecture
    # =========================================================================
    s27 = prs.slides.add_slide(blank_layout)
    set_slide_background(s27, RGBColor(248, 250, 252))
    add_header(s27, 27, "Project Architecture", "System End-to-End Execution Pipeline: From User Input to Rendered UI")
    add_content_block(s27, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2),
        "Stage 1: Ingestion & NLP",
        [
            ("Step 1: User Query Ingestion", "Raw string received via Streamlit UI or terminal CLI interface."),
            ("Step 2: Normalization", "Whitespace collapse, Unicode NFKD conversion, contraction expansion via regex."),
            ("Step 3: Symbol Protection", "Preserves technical compounds like 'A*', 'C++', 'L1/L2' from regex corruption."),
            ("Step 4: Tokenization & N-grams", "Extracts unigrams, bigrams, trigrams, and 4-grams for multi-word phrase detection.")
        ],
        badge="STAGE 1", title_color=PRIMARY_BLUE
    )
    add_content_block(s27, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2),
        "Stage 2: Intent & Matcher",
        [
            ("Step 5: Intent Classification", "Evaluates 10 deterministic regex rules to identify user action (define, compare, example, etc.)."),
            ("Step 6: Acronym Pre-scan", "Evaluates boundary-isolated acronyms (GAN, CNN, RNN, SVM, YOLO, RAG) with exact precedence."),
            ("Step 7: Multi-tier Topic Match", "Checks exact aliases, stemmed tokens, and keyword set intersections against 117 topics."),
            ("Step 8: Context Resolution", "Resolves pronouns ('it', 'its', 'example') against conversation history session state.")
        ],
        badge="STAGE 2", title_color=ACCENT_INDIGO
    )
    add_content_block(s27, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2),
        "Stage 3: Response & UI",
        [
            ("Step 9: Template Assembly", "Retrieves structured topic records and populates definition, explanation, example, math formula."),
            ("Step 10: Comparison Engine", "Extracts dual entities and synthesizes structured markdown comparison table."),
            ("Step 11: Follow-up Suggestions", "Generates interactive clickable chips linking to prerequisite or advanced topics."),
            ("Step 12: Streamlit Rendering", "Renders chat bubble, KaTeX math formulas, and expandable Rule Match Inspector.")
        ],
        badge="STAGE 3", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 28: Text Normalization & Tokenization Subsystem
    # =========================================================================
    s28 = prs.slides.add_slide(blank_layout)
    set_slide_background(s28, RGBColor(248, 250, 252))
    add_header(s28, 28, "NLP Engine Details", "Text Normalization & Tokenization Subsystem Implementation")
    add_content_block(s28, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "src/nlp/normalizer.py Architecture",
        [
            ("Contraction Expansion Dictionary", "Maps 25+ contractions (e.g., \"what's\" -> \"what is\", \"can't\" -> \"cannot\", \"it's\" -> \"it is\") using case-insensitive regex boundaries."),
            ("Unicode Accent Flattening", "Applies unicodedata.normalize('NFKD', text) and strips non-spacing combining marks (e.g., 'résumé' -> 'resume')."),
            ("Special Compound Protection", "Temporarily maps tokens like 'A*', 'C++', 'L1/L2' to placeholder keys before punctuation stripping, then restores them: r'\\ba\\*(?:\\s+(?:search|algorithm))?'."),
            ("Punctuation & Whitespace Hygiene", "Replaces non-alphanumeric noise with single spaces while preserving valid internal hyphens."),
            ("Deterministic Clean Strings", "Outputs sanitized lowercase string guaranteed to match rule patterns reliably.")
        ],
        badge="NORMALIZER.PY", title_color=PRIMARY_BLUE
    )
    add_content_block(s28, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "src/nlp/tokenizer.py Architecture",
        [
            ("Deterministic Regex Tokenizer", "Splits normalized text on whitespace and punctuation boundaries using compiled regex: r'[\\w\\*\\+\\-]+'."),
            ("Stopword Filtering", "Maintains an in-memory set of 120+ English grammatical stopwords; produces both raw tokens and filtered content tokens."),
            ("Sliding Window N-gram Extractor", "Generates unigrams, bigrams, trigrams, and 4-grams by sliding window across token list: [tokens[i:i+n] for i in range(len-n+1)]."),
            ("Significance for Topic Matching", "Multi-word concepts ('generative adversarial networks', 'named entity recognition') match instantly via trigrams/4-grams."),
            ("Performance Benchmark", "Completes tokenization and n-gram generation in sub-millisecond execution times (<0.2 ms).")
        ],
        badge="TOKENIZER.PY", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 29: Deterministic Intent Classification Engine
    # =========================================================================
    s29 = prs.slides.add_slide(blank_layout)
    set_slide_background(s29, RGBColor(248, 250, 252))
    add_header(s29, 29, "Core Engine Details", "Deterministic Intent Classification Engine: Regex Rules and Priority Scoring")
    add_content_block(s29, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Ten Intent Classes & Regex Patterns",
        [
            ("1. GREETING", "r'\\b(hi|hello|hey|greetings|good morning|good evening)\\b'"),
            ("2. GOODBYE", "r'\\b(bye|goodbye|see you|exit|quit|farewell)\\b'"),
            ("3. HELP", "r'\\b(help|what can you do|how to use|commands|features)\\b'"),
            ("4. LIST_MODULES", "r'\\b(modules|curriculum|topics|what do you know|syllabus)\\b'"),
            ("5. COMPARE", "r'\\b(difference between|compare|vs|versus|contrast)\\b'"),
            ("6. DEFINE", "r'\\b(what is|define|definition of|meaning of)\\b'"),
            ("7. EXPLAIN", "r'\\b(explain|tell me about|how does .* work|deep dive)\\b'"),
            ("8. EXAMPLE", "r'\\b(example of|give an example|use case|sample code)\\b'"),
            ("9. FORMULA", "r'\\b(formula|equation|math|algorithm steps|loss function)\\b'"),
            ("10. UNKNOWN", "Fallback triggered when confidence falls below certainty threshold.")
        ],
        badge="INTENT CLASSES", title_color=PRIMARY_BLUE
    )
    add_content_block(s29, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Priority Weighting & Rule Evaluation",
        [
            ("Pattern Weighting & Specificity", "Explicit multi-word phrases receive higher confidence scores (1.0) than single keyword triggers (0.7)."),
            ("Precedence Architecture", "Comparison and Formula intents take precedence over general Explain intents to avoid false generic answers."),
            ("Confidence Scoring Metric", "Calculates match length / query length ratio combined with pattern specificity weights."),
            ("Zero Machine Learning Stochastics", "No temperature parameters, no floating-point weights, no stochastic drift. 100% repeatable outputs."),
            ("Rule Match Audit Trail", "Outputs IntentMatch dataclass containing matched intent name, rule pattern string, and assigned confidence score.")
        ],
        badge="RULE EVALUATION", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 30: Topic Matcher & Contextual Resolution
    # =========================================================================
    s30 = prs.slides.add_slide(blank_layout)
    set_slide_background(s30, RGBColor(248, 250, 252))
    add_header(s30, 30, "Core Engine Details", "Multi-Tier Topic Matcher and Contextual Conversation Resolution")
    add_content_block(s30, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Multi-Tier Topic Matching Hierarchy",
        [
            ("Tier 1: Acronym & Boundary Matching", "Scans pre-compiled regex for ambiguous technical acronyms (GAN, DCGAN, WGAN, VAE, CNN, RNN, SVM, YOLO, RAG, A*)."),
            ("Preemption Prevention", "Short broad patterns (e.g., '\\bai\\b', '\\bml\\b') are placed at the bottom of evaluation to prevent stealing matches from specific terms like 'Python for AI'."),
            ("Tier 2: Exact Alias & N-gram Matching", "Compares generated 4-grams, trigrams, and bigrams against 1,000+ topic aliases indexed in lookup map."),
            ("Tier 3: Keyword Set Intersection", "Calculates Jaccard overlap between filtered query tokens and curated topic keywords."),
            ("Comparison Extraction", "Splits comparison queries via ' vs ', ' and ', ' or ' to resolve two distinct topic entities simultaneously.")
        ],
        badge="TOPIC MATCHER", title_color=PRIMARY_BLUE
    )
    add_content_block(s30, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Contextual Pronoun Resolution Workflow",
        [
            ("The Multi-Turn Conversation Problem", "Users frequently ask follow-ups using pronouns: \"What is it?\", \"Give an example\", \"What are its limitations?\", \"Explain its formula\"."),
            ("Session State History Tracking", "ConversationManager stores active topic ID, module ID, and turn stack across user interactions."),
            ("Pronoun Detection Regex", "Detects referential terms: r'\\b(it|its|this|that|these|the model|the algorithm)\\b'."),
            ("Contextual Substitution Engine", "If query lacks explicit topic but contains pronoun or follow-up trigger ('example', 'formula'), the engine binds query to last active topic."),
            ("Context Indicator Badge", "Displays '[Context Resolved: Topic Name]' badge in Rule Inspector to inform user of antecedent resolution.")
        ],
        badge="CONTEXT RESOLUTION", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 31: Structured Knowledge Base Schema
    # =========================================================================
    s31 = prs.slides.add_slide(blank_layout)
    set_slide_background(s31, RGBColor(248, 250, 252))
    add_header(s31, 31, "Data Architecture", "Modular JSON Knowledge Base: Schema Invariants and Verification Engine")
    add_content_block(s31, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Topic Schema Invariants (knowledge_base/)",
        [
            ("id (String)", "Unique kebab/snake-case identifier (e.g., 'gan_wgan_gp', 'nlp_ner')."),
            ("name (String)", "Formal pedagogical title with standard acronyms."),
            ("category & category_id", "Maps topic directly to one of the 10 academic curriculum modules."),
            ("aliases (List[String])", "Extensive list of alternate names, acronyms, and common colloquial phrasing."),
            ("keywords (List[String])", "Linguistic tokens for set-overlap scoring."),
            ("definition & explanation", "Formal textbook definition and detailed architectural explanation."),
            ("example (String)", "Concrete real-world case study or code snippet."),
            ("formula & algorithm_steps", "LaTeX mathematical equations and ordered step-by-step procedures.")
        ],
        badge="SCHEMA DEFINITION", title_color=PRIMARY_BLUE
    )
    add_content_block(s31, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Startup Validation & Integrity Engine",
        [
            ("Automated Schema Verification", "KnowledgeBase loader iterates across all 10 module JSON files during application startup."),
            ("Invariant 1: Unique Topic IDs", "Raises fatal exception if duplicate topic IDs exist across any module files."),
            ("Invariant 2: Required Field Integrity", "Enforces non-empty strings for definition, explanation, and example across all 117 topics."),
            ("Invariant 3: Relational Reference Validity", "Validates that every entry in 'related_topics' points to a legitimately registered topic ID."),
            ("Blazing Fast In-Memory Indexing", "Pre-computes lowercase alias maps and module indices in memory for O(1) instant topic lookups.")
        ],
        badge="VALIDATION ENGINE", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 32: Response Generation & Rule Inspector
    # =========================================================================
    s32 = prs.slides.add_slide(blank_layout)
    set_slide_background(s32, RGBColor(248, 250, 252))
    add_header(s32, 32, "Response Generation", "Structured Response Composition and the Rule Match Inspector")
    add_content_block(s32, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Dynamic Response Templates",
        [
            ("Definition Template", "Delivers formal definition, category banner, bulleted core principles, and follow-up prompts."),
            ("Explanation Template", "Expands on underlying mechanisms, algorithmic workflows, advantages, and limitations."),
            ("Comparison Template", "Generates side-by-side Markdown comparison table covering: Category, Primary Paradigm, Input/Representation, Strengths, Weaknesses, Applications."),
            ("Formula / Math Template", "Renders clean KaTeX mathematical equations (e.g., Minimax game, Earth Mover's Distance, Bayes Rule) and step-by-step numbered algorithms."),
            ("Graceful Fallback Template", "When query is out of bounds, transparently acknowledges scope and suggests 3-5 relevant curriculum topics.")
        ],
        badge="TEMPLATES", title_color=PRIMARY_BLUE
    )
    add_content_block(s32, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Rule Match Inspector Component",
        [
            ("Pedagogical Auditability", "Every assistant response features an expandable 'Rule Match Inspector' drawer in the UI."),
            ("Audit Metadata Displayed", "• Active User Intent: [e.g., EXPLAIN]\n• Matched Regex Rule: [e.g., r'\\b(explain|tell me about)\\b']\n• Matched Topic ID: [e.g., gan_dcgan]\n• Match Confidence: [e.g., 0.95 / 1.0]\n• Context Resolved: [True/False]."),
            ("Educational Benefit", "Allows students and evaluators to understand the deterministic reasoning path of the chatbot."),
            ("Follow-Up Chip Generation", "Dynamically attaches suggested follow-up query chips, encouraging interactive exploratory learning.")
        ],
        badge="RULE INSPECTOR", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 33: Streamlit Interactive UI/UX Architecture
    # =========================================================================
    s33 = prs.slides.add_slide(blank_layout)
    set_slide_background(s33, RGBColor(248, 250, 252))
    add_header(s33, 33, "Frontend Architecture", "Streamlit Interactive UI/UX Architecture & Multi-Modal Views")
    add_content_block(s33, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Modern Dark Navy Design System (src/ui/styles.py)",
        [
            ("Curated Color Palette", "Sleek Dark Navy theme: Primary Background `#0F172A`, Card Surfaces `#1E293B`, Electric Blue `#3B82F6`, Cyan `#06B6D4`, Emerald `#10B981`."),
            ("Typography & Modern Cards", "System fonts with clean line-heights, subtle border glow effects, rounded containers (border-radius 12px), and smooth hover transitions."),
            ("Quick-Start Prompt Cards", "Interactive clickable cards on home tab allowing one-click execution of starter queries ('What is AI?', 'Explain GANs', 'Compare CNN vs RNN')."),
            ("Chat History Export", "Download full conversation transcripts in formatted JSON or Markdown/TXT directly from sidebar."),
            ("Responsive Two-Column Layout", "Sidebar module navigator with live topic counters and system health diagnostics.")
        ],
        badge="DESIGN SYSTEM", title_color=PRIMARY_BLUE
    )
    add_content_block(s33, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Four Integrated Dashboard Modes",
        [
            ("1. AI Knowledge Chat Tab", "Full conversational interface with message history, stream simulation, and Rule Match Inspectors."),
            ("2. Curriculum Explorer Tab", "Directory browser filtering across all 10 modules and 117 topics with search bar, KaTeX math cards, and algorithm lists."),
            ("3. Topic Comparison Tool Tab", "Interactive dual-dropdown tool enabling instant side-by-side comparison tables between any two selected curriculum topics."),
            ("4. Interactive AI Quiz Mode Tab", "12 curriculum multiple-choice questions with instant scoring, feedback, and comprehensive pedagogical explanations.")
        ],
        badge="DASHBOARD MODES", title_color=ACCENT_EMERALD
    )

    # =========================================================================
    # SLIDE 34: Verification, Testing Strategy & QA
    # =========================================================================
    s34 = prs.slides.add_slide(blank_layout)
    set_slide_background(s34, RGBColor(248, 250, 252))
    add_header(s34, 34, "Quality Assurance", "Comprehensive Testing Strategy: 46 Automated Tests & Invariants")
    add_content_block(s34, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Pytest Test Suite Overview (tests/)",
        [
            ("test_normalizer.py (7 tests)", "Validates contraction expansion, whitespace hygiene, Unicode NFKD accents, and symbol protection ('A*', 'C++')."),
            ("test_tokenizer.py (5 tests)", "Validates compound token preservation, stopword filtering, unigram/bigram/trigram generation order."),
            ("test_knowledge_base.py (5 tests)", "Enforces 10 modules, 117 topics, zero empty fields, valid search results, and raises errors on malformed JSON or duplicate IDs."),
            ("test_intent_classifier.py (9 tests)", "Validates deterministic detection of all 10 intents and empty/unknown query fallback."),
            ("test_topic_matcher.py (4 tests)", "Tests exact aliases, acronym matching, comparison extraction, and unknown topic handling."),
            ("test_chatbot_engine.py (16 tests)", "Tests end-to-end multi-turn conversations, pronoun resolution, GAN queries, and edge cases.")
        ],
        badge="46 TESTS (100% PASS)", title_color=PRIMARY_BLUE
    )
    add_content_block(s34, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Edge Case & Non-Regression Invariants",
        [
            ("Unicode & Malformed Strings", "Tests execution against emojis, Japanese characters, non-breaking spaces, and empty/whitespace queries without crashing."),
            ("Multi-Turn Contextual Integrity", "Verifies that 'What is it?' correctly inherits active topic from prior conversation turn."),
            ("Zero-Hallucination Fallback", "Verifies that out-of-scope queries ('What is the weather?') trigger transparent educational fallbacks without fabricating fake answers."),
            ("Regex Non-Preemption Invariant", "Ensures broad patterns ('ai', 'ml') never preempt specific compound terms ('ReAct in AI agents', 'Python for AI')."),
            ("Execution Speed", "All 46 tests execute in under 2.0 seconds.")
        ],
        badge="EDGE CASES & QA", title_color=ACCENT_INDIGO
    )

    # =========================================================================
    # SLIDE 35: Project Execution Guide & Deployment Workflow
    # =========================================================================
    s35 = prs.slides.add_slide(blank_layout)
    set_slide_background(s35, BG_DARK)
    add_header(s35, 35, "Deployment & Execution", "Project Execution Guide, Deployment Workflow, and Git Repository", is_dark=True)
    add_content_block(s35, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "How to Run AI KnowledgeBot Locally",
        [
            ("Prerequisites", "Python 3.10+ (tested on Python 3.11, 3.12, 3.13) on Windows, macOS, or Linux."),
            ("Step 1: Clone Repository", "git clone https://github.com/YNavaneethReddy2507/Lingo_AI.git\ncd Lingo_AI"),
            ("Step 2: Virtual Environment", "python -m venv .venv\n.\\.venv\\Scripts\\Activate.ps1  (or source .venv/bin/activate)"),
            ("Step 3: Install Dependencies", "pip install -r requirements.txt  (installs streamlit & pytest)"),
            ("Step 4: Launch Web Dashboard", "streamlit run app.py  -> Opens at http://localhost:8501"),
            ("Step 5: Launch Terminal CLI", "python -m src.cli  -> Interactive terminal chatbot session"),
            ("Step 6: Run Automated Tests", "$env:PYTHONIOENCODING=\"utf-8\"; pytest tests/ -v")
        ],
        badge="LOCAL SETUP GUIDE", bg_color=BG_CARD, border_color=ACCENT_CYAN, title_color=ACCENT_CYAN
    )
    add_content_block(s35, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2),
        "Production Git Repository & CI/CD",
        [
            ("Remote Git Repository", "https://github.com/YNavaneethReddy2507/Lingo_AI.git (Main Branch)."),
            ("Clean Project Layout", "Adheres to clean architecture separation: src/engine, src/nlp, src/ui, knowledge_base/, tests/, docs/."),
            ("Zero Cloud Secret Exposure", "Requires no .env keys, API tokens, or external database credentials."),
            ("Full Documentation Suite", "• README.md: Getting started & execution guide.\n• docs/AI_CURRICULUM_AUDIT.md: 17-domain audit.\n• docs/architecture.md: Pipeline specifications.\n• docs/knowledge-base.md: Schema standards."),
            ("Production Readiness", "Engine is fully deterministic, self-contained, and ready for deployment on Streamlit Community Cloud or Docker.")
        ],
        badge="PRODUCTION REPO", bg_color=BG_CARD, border_color=ACCENT_EMERALD, title_color=ACCENT_EMERALD
    )

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "AI_KnowledgeBot_NLP_Curriculum_35_Slides.pptx")
    prs.save(output_path)
    print(f"Successfully generated 35-slide presentation at: {output_path}")

if __name__ == "__main__":
    create_deck()
