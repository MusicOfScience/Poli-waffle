from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_REFERENCE = PROJECT_ROOT / "data" / "reference"
OVERRIDES_DIR = PROJECT_ROOT / "overrides"


def project_root() -> Path:
    return PROJECT_ROOT


def load_reference_csv(filename: str) -> pd.DataFrame:
    path = DATA_REFERENCE / filename
    if not path.exists():
        raise FileNotFoundError(f"Reference CSV not found: {path}")
    return pd.read_csv(path)


def load_yaml(filename: str) -> dict[str, Any]:
    path = OVERRIDES_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Override YAML not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
