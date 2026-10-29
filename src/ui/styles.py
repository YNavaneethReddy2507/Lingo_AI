"""Custom CSS styles and design system for AI KnowledgeBot Streamlit frontend."""

MAIN_CSS = """
<style>
/* -------------------------------------------------------------
   AI KnowledgeBot Modern CSS Design System
   Palette: Dark Slate / Deep Navy (#0b0f19, #111827, #1f2937)
   Accents: Indigo / Violet (#6366f1, #8b5cf6, #38bdf8)
------------------------------------------------------------- */

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #e2e8f0;
}

/* Background gradient */
.stApp {
    background: radial-gradient(circle at 15% 15%, #131b2e 0%, #0a0e17 50%, #070a10 100%);
    background-attachment: fixed;
}

/* Main Container max width */
.block-container {
    max-width: 1280px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Header Banner */
.kb-header {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
    border: 1px solid rgba(99, 102, 241, 0.25);
    border-radius: 16px;
    padding: 1.25rem 1.75rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(12px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
}

.kb-brand-title {
    font-size: 1.6rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

.kb-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: rgba(99, 102, 241, 0.15);
    color: #818cf8;
    border: 1px solid rgba(99, 102, 241, 0.3);
    padding: 0.25rem 0.65rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.kb-badge-green {
    background: rgba(34, 197, 94, 0.15);
    color: #4ade80;
    border: 1px solid rgba(34, 197, 94, 0.3);
}

/* Welcome Hero Card */
.kb-hero {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.95) 100%);
    border: 1px solid rgba(148, 163, 184, 0.15);
    border-radius: 18px;
    padding: 1.75rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    position: relative;
    overflow: hidden;
}

.kb-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6366f1, #a855f7, #38bdf8);
}

.kb-hero h2 {
    font-size: 1.4rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.5rem;
}

.kb-hero p {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.5;
    margin-bottom: 1rem;
}

/* Prompt Card Grid */
.kb-card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 0.85rem;
    margin-top: 1rem;
}

.kb-prompt-card {
    background: rgba(30, 41, 59, 0.5);
    border: 1px solid rgba(148, 163, 184, 0.15);
    border-radius: 12px;
    padding: 1rem;
    transition: all 0.2s ease;
    cursor: pointer;
}

.kb-prompt-card:hover {
    background: rgba(49, 46, 129, 0.3);
    border-color: rgba(99, 102, 241, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(99, 102, 241, 0.15);
}

.kb-prompt-card strong {
    color: #f1f5f9;
    font-size: 0.9rem;
    display: block;
    margin-bottom: 0.25rem;
}

.kb-prompt-card span {
    color: #94a3b8;
    font-size: 0.8rem;
}

/* Chat bubble styling */
.user-msg-box {
    background: linear-gradient(135deg, #312e81 0%, #1e1b4b 100%);
    border: 1px solid rgba(99, 102, 241, 0.4);
    border-radius: 14px 14px 2px 14px;
    padding: 0.9rem 1.25rem;
    margin: 0.6rem 0;
    color: #ffffff;
    max-width: 85%;
    margin-left: auto;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    font-size: 0.95rem;
}

.bot-msg-box {
    background: rgba(17, 24, 39, 0.85);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 14px 14px 14px 2px;
    padding: 1.25rem 1.4rem;
    margin: 0.6rem 0;
    color: #e2e8f0;
    max-width: 95%;
    margin-right: auto;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
    line-height: 1.6;
}

/* Metadata tag container */
.meta-tag-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    align-items: center;
    margin-bottom: 0.75rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(148, 163, 184, 0.12);
}

/* Rule Inspector pill */
.rule-pill {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(99, 102, 241, 0.3);
    color: #a5b4fc;
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #0b1120 !important;
    border-right: 1px solid rgba(148, 163, 184, 0.12) !important;
}

[data-testid="stSidebar"] .stSelectbox, [data-testid="stSidebar"] .stTextInput {
    margin-bottom: 0.75rem;
}

/* Custom button accents */
.stButton>button {
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.2s ease;
    border: 1px solid rgba(99, 102, 241, 0.3);
}

.stButton>button:hover {
    border-color: #6366f1;
    background-color: rgba(99, 102, 241, 0.15);
    color: #ffffff;
}

/* Tab headers */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(15, 23, 42, 0.6);
    padding: 6px;
    border-radius: 12px;
    border: 1px solid rgba(148, 163, 184, 0.12);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    color: #94a3b8;
    font-weight: 600;
    padding: 8px 16px;
}

.stTabs [aria-selected="true"] {
    background-color: #312e81 !important;
    color: #ffffff !important;
}

/* Markdown tables */
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 1rem 0;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid rgba(148, 163, 184, 0.2);
}

th {
    background: rgba(30, 41, 59, 0.85);
    color: #f1f5f9;
    padding: 10px 14px;
    font-weight: 600;
    font-size: 0.85rem;
    border-bottom: 1px solid rgba(148, 163, 184, 0.2);
    text-align: left;
}

td {
    padding: 10px 14px;
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
    font-size: 0.85rem;
    color: #cbd5e1;
}

tr:nth-child(even) {
    background-color: rgba(15, 23, 42, 0.4);
}

tr:last-child td {
    border-bottom: none;
}
</style>
"""
