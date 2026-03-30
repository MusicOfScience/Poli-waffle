from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml



def load_yaml_file(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}
