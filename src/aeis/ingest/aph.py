from __future__ import annotations

from pathlib import Path

import pandas as pd


APH_MEMBER_ALIASES = {
    "Name": "member_name",
    "Electorate": "seat_name",
    "Party": "party",
    "State": "state",
    "Chamber": "chamber",
}


def load_aph_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def normalise_member_reference(df: pd.DataFrame) -> pd.DataFrame:
    matching = {col: APH_MEMBER_ALIASES[col] for col in df.columns if col in APH_MEMBER_ALIASES}
    out = df.rename(columns=matching)
    preferred = [
        col
        for col in ["member_name", "seat_name", "party", "state", "chamber"]
        if col in out.columns
    ]
    if preferred:
        return out[preferred].drop_duplicates().copy()
    return out
