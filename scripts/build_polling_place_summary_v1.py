from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.aeis.domain.polling_place_summary import build_polling_place_summary
from src.aeis.io.resolvers import resolve_dataset_path


if __name__ == "__main__":
    polling_places_path = resolve_dataset_path(
        processed="aec/polling_places_v2.csv",
        interim="aec/polling_places_normalised_v2.csv",
        reference=None,
    )
    if polling_places_path is None:
        raise FileNotFoundError("Missing polling places dataset.")

    bridge_path = resolve_dataset_path(
        processed="core/polling_place_bridge_v1.csv",
        interim=None,
        reference=None,
    )

    polling_places = pd.read_csv(polling_places_path)
    bridge = pd.read_csv(bridge_path) if bridge_path is not None else pd.DataFrame()

    summary = build_polling_place_summary(polling_places, bridge)
    output = Path("data") / "processed" / "core" / "polling_place_summary_v1.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(output, index=False)
    print(f"Wrote {output}")
