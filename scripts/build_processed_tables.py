from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.aeis.io.schema_checks import require_columns


INTERIM = Path("data") / "interim"
PROCESSED = Path("data") / "processed"


def _safe_write(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Wrote {path}")


def build_processed_aec_house() -> None:
    path = INTERIM / "aec" / "house_candidate_results_normalised.csv"
    if not path.exists():
        print(f"Skip processed AEC: missing {path}")
        return

    df = pd.read_csv(path)
    require_columns(
        df,
        ["seat_name", "state", "candidate_name", "party", "source_name", "source_file"],
        dataset_name="AEC interim house candidate results",
    )
    _safe_write(df, PROCESSED / "aec" / "house_candidate_results.csv")


def build_processed_abs() -> None:
    corr = INTERIM / "abs" / "sa1_sa2_ced_correspondence_normalised.csv"
    divs = INTERIM / "abs" / "commonwealth_electoral_divisions_normalised.csv"

    if corr.exists():
        df = pd.read_csv(corr)
        require_columns(
            df,
            ["sa1_code_2021", "sa2_code_2021", "ced_code_2021", "ced_name_2021"],
            dataset_name="ABS interim correspondence",
        )
        _safe_write(df, PROCESSED / "abs" / "sa1_sa2_ced_correspondence.csv")
    else:
        print(f"Skip processed ABS correspondence: missing {corr}")

    if divs.exists():
        df = pd.read_csv(divs)
        require_columns(
            df,
            ["ced_code_2021", "ced_name_2021", "state_name_2021"],
            dataset_name="ABS interim electoral divisions",
        )
        _safe_write(df, PROCESSED / "abs" / "commonwealth_electoral_divisions.csv")
    else:
        print(f"Skip processed ABS divisions: missing {divs}")


def build_processed_aph() -> None:
    path = INTERIM / "aph" / "current_members_normalised.csv"
    if not path.exists():
        print(f"Skip processed APH: missing {path}")
        return

    df = pd.read_csv(path)
    require_columns(
        df,
        ["member_name", "seat_name", "party", "state", "chamber"],
        dataset_name="APH interim current members",
    )
    _safe_write(df, PROCESSED / "aph" / "current_members.csv")


if __name__ == "__main__":
    build_processed_aec_house()
    build_processed_abs()
    build_processed_aph()
