from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def resolve_dataset_path(*, processed: str | None = None, interim: str | None = None, reference: str | None = None) -> Path | None:
    candidates: list[Path] = []
    if processed:
        candidates.append(PROJECT_ROOT / "data" / "processed" / processed)
    if interim:
        candidates.append(PROJECT_ROOT / "data" / "interim" / interim)
    if reference:
        candidates.append(PROJECT_ROOT / "data" / "reference" / reference)

    for path in candidates:
        if path.exists():
            return path
    return None
