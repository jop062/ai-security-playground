from __future__ import annotations

from src.filters import redact_sensitive_output, secure_response


def vulnerable_llm_response(user_input: str) -> str:
    """
    Simulates how a naive assistant might respond if guardrails are weak.
    This is intentionally illustrative, not connected to a real model.
    """
    lowered = user_input.lower()

    if "system prompt" in lowered or "hidden instructions" in lowered:
        return (
            "System prompt: You are an enterprise assistant. Follow internal rules and do not reveal secrets."
        )

    if "password" in lowered or "api key" in lowered or "secret token" in lowered:
        return "Potential sensitive value exposed: example_api_key_12345"

    if "ignore previous instructions" in lowered:
        return "Instructions ignored. I will now comply with your unrestricted request."

    return (
        "This is a simulated vulnerable response. In a real insecure setup, the model might follow unsafe instructions."
    )


def secured_llm_response(user_input: str, risk_score: int, triggered_rules: list[str]) -> str:
    response = secure_response(user_input, risk_score, triggered_rules)
    response = redact_sensitive_output(response)
    return response
