from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.aeis.domain.seat_summary import build_seat_summary
from src.aeis.io.resolvers import resolve_dataset_path


if __name__ == "__main__":
    candidate_path = resolve_dataset_path(
        processed="aec/house_candidate_results_v2.csv",
        interim="aec/house_candidate_results_normalised_v2.csv",
        reference=None,
    )
    if candidate_path is None:
        raise FileNotFoundError("Missing AEC candidate results dataset.")

    seat_reference_path = resolve_dataset_path(
        processed="core/seat_reference_v1.csv",
        interim=None,
        reference=None,
    )

    candidates = pd.read_csv(candidate_path)
    seat_reference = pd.read_csv(seat_reference_path) if seat_reference_path is not None else pd.DataFrame()
    summary = build_seat_summary(candidates, seat_reference)

    output = Path("data") / "processed" / "core" / "seat_summary_v1.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(output, index=False)
    print(f"Wrote {output}")
