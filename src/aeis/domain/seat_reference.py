from __future__ import annotations

import pandas as pd


STATE_ABBREV_TO_NAME = {
    "NSW": "New South Wales",
    "VIC": "Victoria",
    "QLD": "Queensland",
    "WA": "Western Australia",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "ACT": "Australian Capital Territory",
    "NT": "Northern Territory",
}


def build_seat_reference(members: pd.DataFrame, divisions: pd.DataFrame) -> pd.DataFrame:
    members = members.copy()
    divisions = divisions.copy()

    members["state_name_join"] = members["state"].map(STATE_ABBREV_TO_NAME).fillna(members["state"])
    members["seat_name_join"] = members["seat_name"].str.strip().str.casefold()
    divisions["seat_name_join"] = divisions["ced_name_2021"].str.strip().str.casefold()
    divisions["state_name_join"] = divisions["state_name_2021"].str.strip()

    joined = members.merge(
        divisions,
        on=["seat_name_join", "state_name_join"],
        how="left",
        suffixes=("_member", "_division"),
    )

    columns = [
        col
        for col in [
            "seat_name",
            "state",
            "member_name",
            "party",
            "chamber",
            "ced_code_2021",
            "ced_name_2021",
            "state_name_2021",
        ]
        if col in joined.columns
    ]
    return joined[columns].drop_duplicates().copy()
