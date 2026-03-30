from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.aeis.domain.seat_reference import build_seat_reference
from src.aeis.io.resolvers import resolve_dataset_path


if __name__ == "__main__":
    members_path = resolve_dataset_path(
        processed="aph/current_members.csv",
        interim="aph/current_members_normalised.csv",
        reference=None,
    )
    divisions_path = resolve_dataset_path(
        processed="abs/commonwealth_electoral_divisions.csv",
        interim="abs/commonwealth_electoral_divisions_normalised.csv",
        reference=None,
    )

    if members_path is None:
        raise FileNotFoundError("Missing APH members dataset.")
    if divisions_path is None:
        raise FileNotFoundError("Missing ABS electoral divisions dataset.")

    members = pd.read_csv(members_path)
    divisions = pd.read_csv(divisions_path)
    seat_reference = build_seat_reference(members, divisions)

    output = Path("data") / "processed" / "core" / "seat_reference_v1.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    seat_reference.to_csv(output, index=False)
    print(f"Wrote {output}")
