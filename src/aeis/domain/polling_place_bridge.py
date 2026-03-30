from __future__ import annotations

import pandas as pd


def build_polling_place_bridge(
    polling_places: pd.DataFrame,
    bridge_to_sa1: pd.DataFrame,
    correspondence: pd.DataFrame,
) -> pd.DataFrame:
    pp = polling_places.copy()
    bridge = bridge_to_sa1.copy()
    corr = correspondence.copy()

    pp["polling_place_id_join"] = pp["polling_place_id"].astype(str)
    bridge["polling_place_id_join"] = bridge["polling_place_id"].astype(str)
    bridge["sa1_code_2021"] = bridge["sa1_code_2021"].astype(str)
    corr["sa1_code_2021"] = corr["sa1_code_2021"].astype(str)

    joined = pp.merge(
        bridge[["polling_place_id_join", "sa1_code_2021"]],
        on="polling_place_id_join",
        how="left",
    )
    joined = joined.merge(
        corr[["sa1_code_2021", "sa2_code_2021", "ced_code_2021", "ced_name_2021", "state_name_2021"]],
        on="sa1_code_2021",
        how="left",
    )

    preferred = [
        col
        for col in [
            "polling_place_id",
            "polling_place_name",
            "seat_name",
            "state",
            "latitude",
            "longitude",
            "status",
            "sa1_code_2021",
            "sa2_code_2021",
            "ced_code_2021",
            "ced_name_2021",
            "state_name_2021",
        ]
        if col in joined.columns
    ]
    return joined[preferred].drop_duplicates().copy()
