from __future__ import annotations

from pathlib import Path

from src.aeis.ingest.catalog_download import download_targets_from_config
from scripts.build_interim_tables_v2 import (
    build_house_candidates,
    build_members_elected,
    build_polling_places,
)
from scripts.build_processed_tables_v2 import (
    build_processed_house_candidates,
    build_processed_members_elected,
    build_processed_polling_places,
)


if __name__ == "__main__":
    config_path = Path("configs") / "aec_download_targets.yml"
    written = download_targets_from_config(config_path)
    for path in written:
        print(f"Downloaded {path}")
    build_house_candidates()
    build_members_elected()
    build_polling_places()
    build_processed_house_candidates()
    build_processed_members_elected()
    build_processed_polling_places()
    print("Finished AEC v2 raw -> interim -> processed pipeline.")
