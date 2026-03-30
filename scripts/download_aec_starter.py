from __future__ import annotations

from pathlib import Path

from src.aeis.ingest.catalog_download import download_targets_from_config


if __name__ == "__main__":
    config_path = Path("configs") / "aec_download_targets.yml"
    written = download_targets_from_config(config_path)
    for path in written:
        print(f"Downloaded {path}")
