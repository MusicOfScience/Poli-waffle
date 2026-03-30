from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.aeis.domain.polling_place_bridge import build_polling_place_bridge
from src.aeis.io.resolvers import resolve_dataset_path


if __name__ == "__main__":
    polling_places_path = resolve_dataset_path(
        processed="aec/polling_places_v2.csv",
        interim="aec/polling_places_normalised_v2.csv",
        reference=None,
    )
    correspondence_path = resolve_dataset_path(
        processed="abs/sa1_sa2_ced_correspondence.csv",
        interim="abs/sa1_sa2_ced_correspondence_normalised.csv",
        reference=None,
    )
    bridge_path = Path("data") / "raw" / "bridges" / "polling_place_to_sa1.csv"

    if polling_places_path is None:
        raise FileNotFoundError("Missing polling places dataset.")
    if correspondence_path is None:
        raise FileNotFoundError("Missing ABS correspondence dataset.")
    if not bridge_path.exists():
        raise FileNotFoundError(f"Missing manual bridge file: {bridge_path}")

    polling_places = pd.read_csv(polling_places_path)
    correspondence = pd.read_csv(correspondence_path)
    bridge = pd.read_csv(bridge_path)

    result = build_polling_place_bridge(polling_places, bridge, correspondence)
    output = Path("data") / "processed" / "core" / "polling_place_bridge_v1.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output, index=False)
    print(f"Wrote {output}")
