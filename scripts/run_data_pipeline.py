from __future__ import annotations

from scripts.build_interim_tables import build_aec, build_abs, build_aph
from scripts.build_processed_tables import (
    build_processed_aec_house,
    build_processed_abs,
    build_processed_aph,
)


if __name__ == "__main__":
    build_aec()
    build_abs()
    build_aph()
    build_processed_aec_house()
    build_processed_abs()
    build_processed_aph()
    print("Finished interim and processed pipeline.")
