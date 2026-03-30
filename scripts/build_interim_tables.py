from __future__ import annotations

from pathlib import Path

from src.aeis.ingest.aec import add_source_metadata, load_aec_csv, normalise_house_candidate_results
from src.aeis.ingest.abs_geo import load_abs_csv, normalise_correspondence, normalise_electoral_divisions
from src.aeis.ingest.aph import load_aph_csv, normalise_member_reference


RAW = Path("data") / "raw"
INTERIM = Path("data") / "interim"


def _safe_write(df, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Wrote {path}")


def build_aec() -> None:
    path = RAW / "aec" / "house_candidate_results.csv"
    if not path.exists():
        print(f"Skip AEC: missing {path}")
        return
    df = load_aec_csv(path)
    df = normalise_house_candidate_results(df)
    df = add_source_metadata(df, source_name="AEC", file_name=path.name)
    _safe_write(df, INTERIM / "aec" / "house_candidate_results_normalised.csv")


def build_abs() -> None:
    correspondence = RAW / "abs" / "sa1_sa2_ced_correspondence.csv"
    divisions = RAW / "abs" / "commonwealth_electoral_divisions.csv"

    if correspondence.exists():
        df = load_abs_csv(correspondence)
        df = normalise_correspondence(df)
        _safe_write(df, INTERIM / "abs" / "sa1_sa2_ced_correspondence_normalised.csv")
    else:
        print(f"Skip ABS correspondence: missing {correspondence}")

    if divisions.exists():
        df = load_abs_csv(divisions)
        df = normalise_electoral_divisions(df)
        _safe_write(df, INTERIM / "abs" / "commonwealth_electoral_divisions_normalised.csv")
    else:
        print(f"Skip ABS divisions: missing {divisions}")


def build_aph() -> None:
    path = RAW / "aph" / "current_members.csv"
    if not path.exists():
        print(f"Skip APH: missing {path}")
        return
    df = load_aph_csv(path)
    df = normalise_member_reference(df)
    _safe_write(df, INTERIM / "aph" / "current_members_normalised.csv")


if __name__ == "__main__":
    build_aec()
    build_abs()
    build_aph()
