from __future__ import annotations

import pandas as pd



def build_seat_detail(
    seat_reference: pd.DataFrame,
    seat_summary: pd.DataFrame | None = None,
    polling_place_summary: pd.DataFrame | None = None,
) -> pd.DataFrame:
    detail = seat_reference.copy()

    if seat_summary is not None and not seat_summary.empty:
        detail = detail.merge(
            seat_summary,
            on=[col for col in ["state", "seat_name"] if col in detail.columns and col in seat_summary.columns],
            how="left",
            suffixes=("", "_summary"),
        )

    if polling_place_summary is not None and not polling_place_summary.empty:
        pp = polling_place_summary.copy()
        pp_agg = (
            pp.groupby(["state", "seat_name"], dropna=False)
            .agg(
                polling_places_total=("polling_place_count", "sum"),
                bridged_polling_places=("bridged_polling_places", "max"),
                bridged_sa1_count=("bridged_sa1_count", "max"),
                bridged_sa2_count=("bridged_sa2_count", "max"),
            )
            .reset_index()
        )
        detail = detail.merge(
            pp_agg,
            on=[col for col in ["state", "seat_name"] if col in detail.columns and col in pp_agg.columns],
            how="left",
        )

    return detail.sort_values([col for col in ["state", "seat_name"] if col in detail.columns]).reset_index(drop=True)
