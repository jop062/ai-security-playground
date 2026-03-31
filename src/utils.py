from __future__ import annotations

import json
from pathlib import Path


def load_sample_attacks(path: str = "data/sample_attacks.json") -> list[dict]:
    file_path = Path(path)
    if not file_path.exists():
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
