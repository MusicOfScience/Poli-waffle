from __future__ import annotations

from pathlib import Path

from src.aeis.ingest.manifests import write_source_manifest


if __name__ == "__main__":
    output = Path("data") / "raw" / "manifests" / "official_sources.json"
    path = write_source_manifest(output)
    print(f"Wrote manifest to {path}")
