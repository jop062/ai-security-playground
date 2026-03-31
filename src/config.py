RISK_WEIGHTS = {
    "ignore_previous_instructions": 30,
    "reveal_system_prompt": 25,
    "role_override": 20,
    "data_exfiltration": 25,
    "developer_override": 20,
    "policy_bypass": 20,
    "credential_request": 30,
    "prompt_leak_attempt": 25,
    "unsafe_tool_use": 20,
}

MAX_RISK_SCORE = 100

BLOCK_THRESHOLD = 60
WARN_THRESHOLD = 30

SAFE_KNOWLEDGE_BASE = {
    "password reset": "To reset your password, use the internal password reset portal or contact IT support.",
    "vpn access": "VPN access is managed through the company VPN portal. Contact IT if access is unavailable.",
    "software install": "Software installation requests should be submitted through the internal IT request process.",
    "mfa": "Multi-factor authentication helps protect accounts by requiring a second verification factor.",
}
