from __future__ import annotations

from scripts.download_aec_starter import download_targets_from_config, Path as _Path
from scripts.build_interim_tables import build_aec
from scripts.build_processed_tables import build_processed_aec_house


if __name__ == "__main__":
    config_path = _Path("configs") / "aec_download_targets.yml"
    written = download_targets_from_config(config_path)
    for path in written:
        print(f"Downloaded {path}")
    build_aec()
    build_processed_aec_house()
    print("Finished AEC raw -> interim -> processed pipeline.")
