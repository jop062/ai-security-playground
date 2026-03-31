from __future__ import annotations

import re
from typing import List, Tuple

from src.config import MAX_RISK_SCORE, RISK_WEIGHTS


PATTERNS = {
    "ignore_previous_instructions": [
        r"ignore (all )?previous instructions",
        r"disregard (all )?previous instructions",
        r"forget your instructions",
    ],
    "reveal_system_prompt": [
        r"reveal (your|the) system prompt",
        r"show (your|the) hidden instructions",
        r"print (your|the) system prompt",
    ],
    "role_override": [
        r"you are now",
        r"pretend to be",
        r"act as",
        r"roleplay as",
    ],
    "data_exfiltration": [
        r"show me confidential",
        r"dump all data",
        r"exfiltrate",
        r"export internal",
    ],
    "developer_override": [
        r"developer mode",
        r"admin mode",
        r"override safety",
    ],
    "policy_bypass": [
        r"bypass policy",
        r"ignore policy",
        r"without restrictions",
        r"no safety rules",
    ],
    "credential_request": [
        r"give me the password",
        r"show credentials",
        r"api key",
        r"secret token",
    ],
    "prompt_leak_attempt": [
        r"what are your hidden rules",
        r"what instructions are you following",
        r"repeat the exact instructions",
    ],
    "unsafe_tool_use": [
        r"run shell command",
        r"execute command",
        r"delete files",
        r"access the database directly",
    ],
}


def detect_risks(text: str) -> Tuple[int, List[str]]:
    """
    Returns:
        risk_score: int
        triggered_rules: list[str]
    """
    normalized = text.lower().strip()
    triggered: list[str] = []
    score = 0

    for rule_name, patterns in PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, normalized):
                triggered.append(rule_name)
                score += RISK_WEIGHTS.get(rule_name, 0)
                break

    score = min(score, MAX_RISK_SCORE)
    return score, triggered
