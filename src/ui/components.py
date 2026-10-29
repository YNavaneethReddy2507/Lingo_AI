"""UI components and layout helpers for Streamlit frontend."""
import json
from typing import Any, Dict, List, Optional

import streamlit as st
from src.engine.models import ChatbotResponse, Topic


def render_header(total_topics: int, total_modules: int) -> None:
    """Renders top branding navigation bar with status badges."""
    st.markdown(
        f"""
        <div class="kb-header">
            <div>
                <div class="kb-brand-title">
                    <span>🧠</span> AI KnowledgeBot
                </div>
                <div style="font-size: 0.85rem; color: #94a3b8; margin-top: 0.2rem;">
                    Educational Rule-Based Artificial Intelligence Assistant & Curriculum Engine
                </div>
            </div>
            <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
                <span class="kb-badge kb-badge-green">● Local & Offline</span>
                <span class="kb-badge">8 Modules</span>
                <span class="kb-badge">{total_topics} Topics</span>
                <span class="kb-badge" style="border-color: #a855f7; color: #c084fc;">Deterministic Rules</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_welcome_hero(quick_prompts: List[str]) -> Optional[str]:
    """Renders welcome dashboard with introduction and interactive prompt cards."""
    st.markdown(
        """
        <div class="kb-hero">
            <h2>Welcome to the Artificial Intelligence Knowledge Explorer</h2>
            <p>
                This application is powered by an explicit <strong>Rule-Based AI Engine</strong> — not an LLM.
                Every response is derived deterministically from structured knowledge bases, regular expression rules,
                and syntactic intent matching. Experience <strong>zero hallucinations</strong>, transparent rule inspection,
                and complete auditability across all major branches of AI.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("##### ⚡ Quick Start Prompts (Click to Ask):")
    cols = st.columns(4)
    selected_prompt = None

    for idx, prompt in enumerate(quick_prompts):
        col = cols[idx % 4]
        with col:
            if st.button(prompt, key=f"quick_prompt_{idx}", use_container_width=True):
                selected_prompt = prompt

    return selected_prompt


def render_chat_message(role: str, text: str, response_meta: Optional[Dict[str, Any]] = None, show_inspector: bool = True) -> Optional[str]:
    """Renders a styled chat bubble with optional rule inspection metadata and follow-ups."""
    clicked_followup = None

    if role == "user":
        st.markdown(
            f"""
            <div class="user-msg-box">
                <div style="font-size: 0.75rem; color: #a5b4fc; margin-bottom: 0.25rem; font-weight: 600;">YOU</div>
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # Bot Message
        with st.container():
            # Metadata bar
            topic_name = response_meta.get("topic_name", "General AI") if response_meta else "General AI"
            category = response_meta.get("category", "General") if response_meta else "General"
            intent = response_meta.get("intent", "explain") if response_meta else "explain"
            conf = response_meta.get("confidence", 1.0) if response_meta else 1.0
            rule_desc = response_meta.get("matched_rule", "") if response_meta else ""
            context_used = response_meta.get("context_used", False) if response_meta else False

            meta_html = f"""
            <div class="meta-tag-bar">
                <span class="kb-badge" style="font-size: 0.7rem;">📘 {category}</span>
                <span class="kb-badge" style="font-size: 0.7rem; border-color: #38bdf8; color: #38bdf8;">🎯 {intent}</span>
                <span class="kb-badge" style="font-size: 0.7rem; border-color: #22c55e; color: #4ade80;">Confidence: {int(conf * 100)}%</span>
                {"<span class='kb-badge' style='font-size: 0.7rem; border-color: #f59e0b; color: #fbbf24;'>🔄 Context Follow-up</span>" if context_used else ""}
            </div>
            """
            st.markdown(
                f"""
                <div class="bot-msg-box">
                    {meta_html}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Markdown Content
            st.markdown(text)

            # Rule Inspector Accordion
            if show_inspector and rule_desc:
                with st.expander("🔍 Rule Engine Match Inspector", expanded=False):
                    st.markdown(
                        f"""
                        - **Triggered Rule / Pattern:** `{rule_desc}`
                        - **Active Intent:** `{intent}`
                        - **Target Topic:** `{topic_name}`
                        - **Confidence Score:** `{conf:.2f}`
                        - **Context Follow-up Resolved:** `{"Yes" if context_used else "No"}`
                        - **Engine Execution:** `100% Deterministic Symbolic Logic`
                        """
                    )

            # Suggested Follow-up Buttons
            followups = response_meta.get("followups", []) if response_meta else []
            if followups:
                st.markdown("<div style='font-size: 0.8rem; color: #94a3b8; margin-top: 0.5rem; margin-bottom: 0.25rem;'>💡 Suggested Next Questions:</div>", unsafe_allow_html=True)
                f_cols = st.columns(len(followups))
                for f_idx, followup in enumerate(followups):
                    with f_cols[f_idx]:
                        btn_key = f"fup_{response_meta.get('turn_id', 0)}_{f_idx}"
                        if st.button(f"👉 {followup}", key=btn_key, use_container_width=True):
                            clicked_followup = followup

    return clicked_followup


def export_conversation_json(history: List[Dict[str, Any]]) -> str:
    """Exports session conversation to JSON string."""
    return json.dumps(history, indent=2)


def export_conversation_txt(history: List[Dict[str, Any]]) -> str:
    """Exports session conversation to formatted Markdown / TXT string."""
    lines = ["# AI KnowledgeBot Conversation Export\n"]
    for turn in history:
        lines.append(f"### Turn {turn.get('turn', '1')}")
        lines.append(f"**User:** {turn.get('user', '')}")
        lines.append(f"**Intent:** `{turn.get('intent', '')}` | **Topic:** `{turn.get('topic_id', '')}`")
        lines.append(f"**KnowledgeBot:**\n{turn.get('bot', '')}\n")
        lines.append("-" * 50 + "\n")
    return "\n".join(lines)
