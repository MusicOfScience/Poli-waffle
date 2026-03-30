from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.aeis.io.schema_checks import require_columns


INTERIM = Path("data") / "interim" / "aec"
PROCESSED = Path("data") / "processed" / "aec"


def _safe_write(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Wrote {path}")


def build_processed_house_candidates() -> None:
    path = INTERIM / "house_candidate_results_normalised_v2.csv"
    if not path.exists():
        print(f"Skip processed house candidate results: missing {path}")
        return
    df = pd.read_csv(path)
    require_columns(
        df,
        ["seat_name", "state", "candidate_name", "party", "source_name", "source_file"],
        dataset_name="AEC v2 interim house candidate results",
    )
    _safe_write(df, PROCESSED / "house_candidate_results_v2.csv")


def build_processed_members_elected() -> None:
    path = INTERIM / "house_members_elected_normalised_v2.csv"
    if not path.exists():
        print(f"Skip processed members elected: missing {path}")
        return
    df = pd.read_csv(path)
    require_columns(
        df,
        ["seat_name", "state", "member_name", "party", "source_name", "source_file"],
        dataset_name="AEC v2 interim members elected",
    )
    _safe_write(df, PROCESSED / "house_members_elected_v2.csv")


def build_processed_polling_places() -> None:
    path = INTERIM / "polling_places_normalised_v2.csv"
    if not path.exists():
        print(f"Skip processed polling places: missing {path}")
        return
    df = pd.read_csv(path)
    require_columns(
        df,
        ["polling_place_id", "polling_place_name", "seat_name", "state", "source_name", "source_file"],
        dataset_name="AEC v2 interim polling places",
    )
    _safe_write(df, PROCESSED / "polling_places_v2.csv")


if __name__ == "__main__":
    build_processed_house_candidates()
    build_processed_members_elected()
    build_processed_polling_places()
