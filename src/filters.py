from __future__ import annotations

from src.config import BLOCK_THRESHOLD, SAFE_KNOWLEDGE_BASE, WARN_THRESHOLD


def classify_risk(score: int) -> str:
    if score >= BLOCK_THRESHOLD:
        return "high"
    if score >= WARN_THRESHOLD:
        return "medium"
    return "low"


def grounded_response(user_input: str) -> str:
    """
    Very simple grounded-answer mode for demonstration.
    Only answers with known safe topics.
    """
    lowered = user_input.lower()

    for key, value in SAFE_KNOWLEDGE_BASE.items():
        if key in lowered:
            return value

    return (
        "I can only provide grounded answers for approved topics in this demo. "
        "Try asking about password reset, VPN access, software install, or MFA."
    )


def secure_response(user_input: str, risk_score: int, triggered_rules: list[str]) -> str:
    level = classify_risk(risk_score)

    if level == "high":
        return (
            "Request blocked: this prompt appears to contain prompt injection, policy bypass, "
            "or sensitive-information extraction behavior."
        )

    if level == "medium":
        return (
            "Warning: your request includes potentially unsafe instruction patterns. "
            "Proceeding in grounded-answer mode.\n\n"
            + grounded_response(user_input)
        )

    return grounded_response(user_input)


def redact_sensitive_output(text: str) -> str:
    """
    Placeholder output filter.
    """
    banned_terms = ["system prompt", "api key", "secret token", "password"]
    filtered = text

    for term in banned_terms:
        filtered = filtered.replace(term, "[REDACTED]")

    return filtered
