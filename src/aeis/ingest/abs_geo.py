from __future__ import annotations

from pathlib import Path

import pandas as pd


ABS_CORRESPONDENCE_ALIASES = {
    "SA1_CODE_2021": "sa1_code_2021",
    "SA2_CODE_2021": "sa2_code_2021",
    "CED_CODE_2021": "ced_code_2021",
    "CED_NAME_2021": "ced_name_2021",
    "STATE_NAME_2021": "state_name_2021",
    "RATIO": "allocation_ratio",
}


ELECTORAL_DIVISION_ALIASES = {
    "CED_CODE_2021": "ced_code_2021",
    "CED_NAME_2021": "ced_name_2021",
    "STE_CODE_2021": "state_code_2021",
    "STE_NAME_2021": "state_name_2021",
}


def load_abs_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def _rename(df: pd.DataFrame, aliases: dict[str, str]) -> pd.DataFrame:
    matching = {col: aliases[col] for col in df.columns if col in aliases}
    return df.rename(columns=matching)


def normalise_correspondence(df: pd.DataFrame) -> pd.DataFrame:
    out = _rename(df.copy(), ABS_CORRESPONDENCE_ALIASES)
    preferred = [
        col
        for col in [
            "sa1_code_2021",
            "sa2_code_2021",
            "ced_code_2021",
            "ced_name_2021",
            "state_name_2021",
            "allocation_ratio",
        ]
        if col in out.columns
    ]
    if preferred:
        return out[preferred].copy()
    return out


def normalise_electoral_divisions(df: pd.DataFrame) -> pd.DataFrame:
    out = _rename(df.copy(), ELECTORAL_DIVISION_ALIASES)
    preferred = [
        col
        for col in [
            "ced_code_2021",
            "ced_name_2021",
            "state_code_2021",
            "state_name_2021",
        ]
        if col in out.columns
    ]
    if preferred:
        return out[preferred].drop_duplicates().copy()
    return out
