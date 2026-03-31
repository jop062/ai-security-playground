from __future__ import annotations

import streamlit as st

from src.detector import detect_risks
from src.filters import classify_risk
from src.simulator import secured_llm_response, vulnerable_llm_response
from src.utils import load_sample_attacks


st.set_page_config(page_title="AI Security Playground", layout="wide")


def risk_badge(level: str) -> str:
    if level == "high":
        return "🔴 High"
    if level == "medium":
        return "🟠 Medium"
    return "🟢 Low"


def main() -> None:
    st.title("AI Security Playground")
    st.subheader("Prompt Injection, Guardrails, and Safer LLM Workflows")

    st.markdown(
        """
This demo shows the difference between:
- a **vulnerable AI assistant**
- a **secured AI assistant** with basic guardrails

Use the sample attacks or type your own prompt.
"""
    )

    attacks = load_sample_attacks()
    sample_names = ["Custom Prompt"] + [item["name"] for item in attacks]

    selected = st.selectbox("Choose a sample attack", sample_names)

    default_prompt = ""
    if selected != "Custom Prompt":
        matched = next((item for item in attacks if item["name"] == selected), None)
        if matched:
            default_prompt = matched["prompt"]

    user_input = st.text_area(
        "Enter prompt",
        value=default_prompt,
        height=180,
        placeholder="Type a user prompt here..."
    )

    if st.button("Analyze Prompt", use_container_width=True):
        if not user_input.strip():
            st.warning("Please enter a prompt.")
            return

        score, triggered_rules = detect_risks(user_input)
        level = classify_risk(score)

        vulnerable = vulnerable_llm_response(user_input)
        secured = secured_llm_response(user_input, score, triggered_rules)

        c1, c2, c3 = st.columns(3)
        c1.metric("Risk Score", score)
        c2.metric("Risk Level", risk_badge(level))
        c3.metric("Rules Triggered", len(triggered_rules))

        st.markdown("---")

        left, right = st.columns(2)

        with left:
            st.markdown("### Vulnerable Mode")
            st.code(vulnerable, language="text")

        with right:
            st.markdown("### Secure Mode")
            st.code(secured, language="text")

        st.markdown("### Triggered Rules")
        if triggered_rules:
            for rule in triggered_rules:
                st.write(f"- {rule}")
        else:
            st.write("- No risky patterns detected")

        st.markdown("### Why this matters")
        if level == "high":
            st.error(
                "This prompt looks like an injection or sensitive-data extraction attempt. "
                "A secure assistant should block it."
            )
        elif level == "medium":
            st.warning(
                "This prompt contains suspicious instruction patterns. "
                "A secure assistant should limit behavior and answer only from approved knowledge."
            )
        else:
            st.success(
                "This prompt appears low risk. A secure assistant can answer normally in grounded mode."
            )


if __name__ == "__main__":
    main()
