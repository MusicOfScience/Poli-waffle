from __future__ import annotations

from pathlib import Path
import json

from .sources import OFFICIAL_SOURCE_ENDPOINTS


def build_source_manifest() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for endpoint in OFFICIAL_SOURCE_ENDPOINTS:
        rows.append(
            {
                "name": endpoint.name,
                "host": endpoint.host,
                "path_hint": endpoint.path_hint,
                "tier": endpoint.tier,
                "notes": endpoint.notes,
            }
        )
    return rows


def write_source_manifest(output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(build_source_manifest(), indent=2), encoding="utf-8")
    return output_path
