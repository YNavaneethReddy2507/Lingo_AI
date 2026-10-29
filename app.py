"""AI KnowledgeBot — Modern Educational Rule-Based AI Chatbot Frontend.

A fully local, deterministic rule-based chatbot application built with Streamlit.
"""
import os
import sys
from typing import Optional

import streamlit as st

# Ensure project root is on Python sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from src.engine.chatbot import AIKnowledgeBot
from src.ui.components import (
    export_conversation_json,
    export_conversation_txt,
    render_chat_message,
    render_header,
    render_welcome_hero,
)
from src.ui.quiz_data import QUIZ_QUESTIONS
from src.ui.styles import MAIN_CSS

# Page Configuration
st.set_page_config(
    page_title="AI KnowledgeBot — Rule-Based AI Chatbot",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom CSS Styles
st.markdown(MAIN_CSS, unsafe_allow_html=True)


# Initialize Session State
@st.cache_resource
def get_bot_instance() -> AIKnowledgeBot:
    """Instantiates and caches the AIKnowledgeBot engine and knowledge base."""
    return AIKnowledgeBot()


bot = get_bot_instance()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_query" not in st.session_state:
    st.session_state.pending_query = None

if "show_inspector" not in st.session_state:
    st.session_state.show_inspector = True

if "quiz_scores" not in st.session_state:
    st.session_state.quiz_scores = {}

# Top Navigation Header
render_header(
    total_topics=len(bot.kb.get_all_topics()),
    total_modules=len(bot.kb.get_all_modules())
)


# Sidebar Layout
with st.sidebar:
    st.markdown("### 🧭 Topic Navigator")

    # Search bar
    search_query = st.text_input("🔍 Search AI Topics", placeholder="e.g. CNN, A*, RAG, SVM, NER...")

    # Module selection
    module_options = ["All Modules"] + [m.name for m in bot.kb.get_all_modules()]
    selected_module_name = st.selectbox("📂 Filter by Category", module_options)

    # Filtered topics
    if search_query.strip():
        matching_topics = bot.kb.search_topics(search_query)
    elif selected_module_name != "All Modules":
        mod_id = next(m.id for m in bot.kb.get_all_modules() if m.name == selected_module_name)
        matching_topics = bot.kb.get_topics_by_module(mod_id)
    else:
        matching_topics = bot.kb.get_all_topics()

    topic_names = [f"{t.name} ({t.category_id})" for t in matching_topics]

    if topic_names:
        selected_topic_str = st.selectbox(
            f"📌 Select Topic ({len(matching_topics)} found)",
            topic_names,
            index=0
        )
        selected_topic_idx = topic_names.index(selected_topic_str)
        curr_topic = matching_topics[selected_topic_idx]

        # Topic Preview Card
        st.markdown(
            f"""
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 10px; padding: 0.85rem; margin-top: 0.5rem; font-size: 0.82rem;">
                <strong style="color: #f8fafc; font-size: 0.9rem;">{curr_topic.name}</strong><br>
                <span style="color: #818cf8;">{curr_topic.category}</span>
                <p style="color: #cbd5e1; margin-top: 0.4rem; margin-bottom: 0.4rem;">{curr_topic.definition[:140]}...</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        col_ask1, col_ask2 = st.columns(2)
        with col_ask1:
            if st.button("💬 Ask Bot", key="sidebar_ask_btn", use_container_width=True):
                st.session_state.pending_query = f"Explain {curr_topic.name}"
                st.rerun()
        with col_ask2:
            if st.button("💡 Example", key="sidebar_example_btn", use_container_width=True):
                st.session_state.pending_query = f"Give an example of {curr_topic.name}"
                st.rerun()
    else:
        st.info("No topics matched your search filter.")

    st.markdown("---")

    # Diagnostics and Controls
    st.markdown("### ⚙️ Engine Diagnostics")
    st.session_state.show_inspector = st.checkbox(
        "Show Rule Match Inspector",
        value=st.session_state.show_inspector,
        help="Displays rule pattern, intent, and match confidence details for every chatbot response."
    )

    # Session Stats
    unique_topics_seen = len(set(m.get("meta", {}).get("topic_id", "") for m in st.session_state.messages if m.get("role") == "bot"))
    st.markdown(
        f"""
        <div style="background: rgba(15, 23, 42, 0.6); padding: 0.75rem; border-radius: 8px; border: 1px solid rgba(148, 163, 184, 0.15); font-size: 0.8rem; color: #94a3b8;">
            <div>💬 <strong>User Turns:</strong> {len([m for m in st.session_state.messages if m['role'] == 'user'])}</div>
            <div>📖 <strong>Topics Explored:</strong> {unique_topics_seen} / {len(bot.kb.get_all_topics())}</div>
            <div>⚡ <strong>Rule Engine:</strong> Active & Deterministic</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # Export & Reset Options
    st.markdown("### 💾 Conversation Controls")
    if st.session_state.messages:
        export_col1, export_col2 = st.columns(2)
        with export_col1:
            json_data = export_conversation_json(bot.context.history)
            st.download_button(
                "📥 JSON",
                data=json_data,
                file_name="ai_knowledgebot_chat.json",
                mime="application/json",
                use_container_width=True
            )
        with export_col2:
            txt_data = export_conversation_txt(bot.context.history)
            st.download_button(
                "📥 Markdown",
                data=txt_data,
                file_name="ai_knowledgebot_chat.md",
                mime="text/markdown",
                use_container_width=True
            )

    if st.button("🗑️ Reset Conversation", use_container_width=True):
        bot.context.clear()
        st.session_state.messages.clear()
        st.session_state.pending_query = None
        st.rerun()


# Main Application Tabs
tab_chat, tab_compare, tab_quiz, tab_explorer = st.tabs([
    "💬 AI Knowledge Chat",
    "⚖️ Topic Comparison Tool",
    "🧠 Interactive AI Quiz",
    "📚 Curriculum Directory"
])


# -------------------------------------------------------------
# TAB 1: AI Knowledge Chat
# -------------------------------------------------------------
with tab_chat:
    # Check if there are no messages yet -> Render Hero Dashboard
    if not st.session_state.messages:
        starter_prompts = [
            "What is AI?",
            "Difference between AI and ML?",
            "What is an Expert System?",
            "Explain A* search",
            "What is Named Entity Recognition?",
            "Compare CNN and RNN",
            "Explain Word2Vec and GloVe",
            "What are the branches of AI?"
        ]
        clicked_hero_prompt = render_welcome_hero(starter_prompts)
        if clicked_hero_prompt:
            st.session_state.pending_query = clicked_hero_prompt
            st.rerun()

    # Render message history
    followup_clicked = None
    for msg_idx, msg in enumerate(st.session_state.messages):
        fup = render_chat_message(
            role=msg["role"],
            text=msg["content"],
            response_meta=msg.get("meta"),
            show_inspector=st.session_state.show_inspector
        )
        if fup:
            followup_clicked = fup

    if followup_clicked:
        st.session_state.pending_query = followup_clicked
        st.rerun()

    # Chat Input Form
    with st.form("chat_form", clear_on_submit=True):
        chat_col1, chat_col2 = st.columns([6, 1])
        with chat_col1:
            user_input = st.text_input(
                "Ask a question about AI...",
                placeholder="Ask about AI concepts, algorithms, formulas, or comparisons (e.g. 'What is TF-IDF?')...",
                label_visibility="collapsed"
            )
        with chat_col2:
            submitted = st.form_submit_button("Send 🚀", use_container_width=True)

    # Process query (either from form submission or pending click)
    query_to_process = None
    if submitted and user_input.strip():
        query_to_process = user_input.strip()
    elif st.session_state.pending_query:
        query_to_process = st.session_state.pending_query
        st.session_state.pending_query = None

    if query_to_process:
        # Append User Message
        st.session_state.messages.append({
            "role": "user",
            "content": query_to_process
        })

        # Process through Rule-Based AI Engine
        response = bot.process_message(query_to_process)

        # Append Bot Response with structured metadata
        st.session_state.messages.append({
            "role": "bot",
            "content": response.text,
            "meta": {
                "turn_id": bot.context.turn_count,
                "intent": response.intent.value,
                "topic_id": response.matched_topic.id if response.matched_topic else "none",
                "topic_name": response.matched_topic.name if response.matched_topic else "General Query",
                "category": response.matched_topic.category if response.matched_topic else "General AI",
                "confidence": response.confidence,
                "matched_rule": response.matched_rule,
                "context_used": response.context_used,
                "followups": response.suggested_followups
            }
        })
        st.rerun()


# -------------------------------------------------------------
# TAB 2: Topic Comparison Tool
# -------------------------------------------------------------
with tab_compare:
    st.markdown("### ⚖️ Automated Topic-to-Topic Comparison Engine")
    st.markdown(
        "Select any two topics from the knowledge base to inspect their definitions, strengths, "
        "limitations, and architectural differences side-by-side."
    )

    all_topics = bot.kb.get_all_topics()
    topic_labels = [f"{t.name} [{t.id}]" for t in all_topics]

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        # Default to AI
        default_idx1 = next((i for i, t in enumerate(all_topics) if t.id == "ai_definition"), 0)
        idx1 = st.selectbox("Select Topic A", range(len(topic_labels)), format_func=lambda i: topic_labels[i], index=default_idx1)
    with col_t2:
        # Default to ML
        default_idx2 = next((i for i, t in enumerate(all_topics) if t.id == "ml_definition"), 1)
        idx2 = st.selectbox("Select Topic B", range(len(topic_labels)), format_func=lambda i: topic_labels[i], index=default_idx2)

    top_a = all_topics[idx1]
    top_b = all_topics[idx2]

    if top_a.id == top_b.id:
        st.warning("Please choose two distinct topics to generate a meaningful comparative analysis.")
    else:
        comp_md = bot.generator.format_comparison(top_a, top_b)
        st.markdown(comp_md)

        if st.button(f"💬 Send Comparison to Chat Assistant", key="comp_to_chat_btn"):
            st.session_state.pending_query = f"Compare {top_a.name} and {top_b.name}"
            st.rerun()


# -------------------------------------------------------------
# TAB 3: Interactive AI Quiz Mode
# -------------------------------------------------------------
with tab_quiz:
    st.markdown("### 🧠 AI KnowledgeBot Interactive Mastery Quiz")
    st.markdown("Test your conceptual mastery across all 8 modules of Artificial Intelligence.")

    total_q = len(QUIZ_QUESTIONS)
    answered_count = len(st.session_state.quiz_scores)
    score_count = sum(1 for v in st.session_state.quiz_scores.values() if v.get("correct"))

    st.progress(answered_count / total_q)
    st.markdown(f"**Score:** `{score_count} / {answered_count}` answered correctly ({int(score_count / total_q * 100)}% overall progress)")

    for idx, q_data in enumerate(QUIZ_QUESTIONS):
        with st.container():
            st.markdown(f"#### Question {idx + 1} — `{q_data['module']}`")
            st.markdown(f"**{q_data['question']}**")

            q_key = f"quiz_{q_data['id']}"
            saved = st.session_state.quiz_scores.get(q_data["id"])

            selected_opt = st.radio(
                "Select your answer:",
                q_data["options"],
                key=q_key,
                index=saved["selected"] if saved else None,
                disabled=saved is not None
            )

            if saved is None:
                if st.button("Submit Answer", key=f"submit_{q_data['id']}"):
                    if selected_opt is not None:
                        sel_idx = q_data["options"].index(selected_opt)
                        is_correct = (sel_idx == q_data["answer_index"])
                        st.session_state.quiz_scores[q_data["id"]] = {
                            "selected": sel_idx,
                            "correct": is_correct
                        }
                        st.rerun()
            else:
                if saved["correct"]:
                    st.success("✅ **Correct!** " + q_data["explanation"])
                else:
                    correct_text = q_data["options"][q_data["answer_index"]]
                    st.error(f"❌ **Incorrect.** The correct answer is: **{correct_text}**\n\n💡 *Explanation:* {q_data['explanation']}")

            st.markdown("---")

    if st.button("🔄 Reset Quiz Scores"):
        st.session_state.quiz_scores.clear()
        st.rerun()


# -------------------------------------------------------------
# TAB 4: Curriculum Directory
# -------------------------------------------------------------
with tab_explorer:
    st.markdown("### 📚 AI Knowledge Base Curriculum Directory")
    st.markdown("Inspect all 80 verified topics structured by their respective academic modules.")

    for module in bot.kb.get_all_modules():
        topics_in_mod = bot.kb.get_topics_by_module(module.id)
        with st.expander(f"📁 {module.name} ({len(topics_in_mod)} Topics)", expanded=False):
            st.markdown(f"*{module.description}*")
            for t in topics_in_mod:
                st.markdown(f"#### 🔹 {t.name} (`{t.id}`)")
                st.markdown(f"**Definition:** {t.definition}")
                st.markdown(f"**Example:** {t.example}")
                if t.formula:
                    st.markdown(f"**Formula:** $${t.formula}$$")
                if t.advantages:
                    st.markdown(f"**Advantages:** {'; '.join(t.advantages)}")
                if t.limitations:
                    st.markdown(f"**Limitations:** {'; '.join(t.limitations)}")
                st.markdown("---")
