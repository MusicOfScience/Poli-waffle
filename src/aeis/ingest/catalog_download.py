from __future__ import annotations

from pathlib import Path
from typing import Any

from src.aeis.io.yaml_loader import load_yaml_file

from .http import download_to_path



def download_targets_from_config(config_path: str | Path) -> list[Path]:
    config = load_yaml_file(config_path)
    targets: dict[str, dict[str, Any]] = config.get("targets", {})
    written: list[Path] = []

    for _, target in targets.items():
        url = target["url"]
        output = Path(target["output"])
        written.append(download_to_path(url, output))

    return written
