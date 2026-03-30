from __future__ import annotations

import pandas as pd


def build_polling_place_summary(
    polling_places: pd.DataFrame,
    polling_place_bridge: pd.DataFrame | None = None,
) -> pd.DataFrame:
    pp = polling_places.copy()

    if "state" not in pp.columns:
        pp["state"] = None
    if "seat_name" not in pp.columns:
        pp["seat_name"] = None
    if "status" not in pp.columns:
        pp["status"] = None

    summary = (
        pp.groupby(["state", "seat_name", "status"], dropna=False)
        .size()
        .reset_index(name="polling_place_count")
    )

    if polling_place_bridge is not None and not polling_place_bridge.empty:
        bridge = polling_place_bridge.copy()
        bridge_summary = (
            bridge.groupby(["state", "seat_name"], dropna=False)
            .agg(
                bridged_polling_places=("polling_place_id", "nunique"),
                bridged_sa1_count=("sa1_code_2021", "nunique"),
                bridged_sa2_count=("sa2_code_2021", "nunique"),
            )
            .reset_index()
        )
        summary = summary.merge(bridge_summary, on=["state", "seat_name"], how="left")

    return summary.sort_values(["state", "seat_name", "status"]).reset_index(drop=True)
