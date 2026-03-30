from __future__ import annotations

from pathlib import Path

from src.aeis.ingest.aec_extended import (
    add_source_metadata,
    load_aec_csv,
    normalise_house_candidate_results,
    normalise_house_members_elected,
    normalise_polling_places,
)


RAW = Path("data") / "raw" / "aec"
INTERIM = Path("data") / "interim" / "aec"


def _safe_write(df, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Wrote {path}")


def build_house_candidates() -> None:
    path = RAW / "house_candidate_results.csv"
    if not path.exists():
        print(f"Skip house candidate results: missing {path}")
        return
    df = load_aec_csv(path)
    df = normalise_house_candidate_results(df)
    df = add_source_metadata(df, source_name="AEC", file_name=path.name)
    _safe_write(df, INTERIM / "house_candidate_results_normalised_v2.csv")


def build_members_elected() -> None:
    path = RAW / "house_members_elected.csv"
    if not path.exists():
        print(f"Skip members elected: missing {path}")
        return
    df = load_aec_csv(path)
    df = normalise_house_members_elected(df)
    df = add_source_metadata(df, source_name="AEC", file_name=path.name)
    _safe_write(df, INTERIM / "house_members_elected_normalised_v2.csv")


def build_polling_places() -> None:
    path = RAW / "polling_places.csv"
    if not path.exists():
        print(f"Skip polling places: missing {path}")
        return
    df = load_aec_csv(path)
    df = normalise_polling_places(df)
    df = add_source_metadata(df, source_name="AEC", file_name=path.name)
    _safe_write(df, INTERIM / "polling_places_normalised_v2.csv")


if __name__ == "__main__":
    build_house_candidates()
    build_members_elected()
    build_polling_places()
