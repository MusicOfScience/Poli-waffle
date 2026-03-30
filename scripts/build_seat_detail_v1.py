from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.aeis.domain.seat_detail import build_seat_detail
from src.aeis.io.resolvers import resolve_dataset_path


if __name__ == "__main__":
    seat_reference_path = resolve_dataset_path(
        processed="core/seat_reference_v1.csv",
        interim=None,
        reference=None,
    )
    if seat_reference_path is None:
        raise FileNotFoundError("Missing seat reference dataset.")

    seat_summary_path = resolve_dataset_path(
        processed="core/seat_summary_v1.csv",
        interim=None,
        reference=None,
    )
    polling_place_summary_path = resolve_dataset_path(
        processed="core/polling_place_summary_v1.csv",
        interim=None,
        reference=None,
    )

    seat_reference = pd.read_csv(seat_reference_path)
    seat_summary = pd.read_csv(seat_summary_path) if seat_summary_path is not None else pd.DataFrame()
    polling_place_summary = pd.read_csv(polling_place_summary_path) if polling_place_summary_path is not None else pd.DataFrame()

    detail = build_seat_detail(seat_reference, seat_summary, polling_place_summary)
    output = Path("data") / "processed" / "core" / "seat_detail_v1.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    detail.to_csv(output, index=False)
    print(f"Wrote {output}")
