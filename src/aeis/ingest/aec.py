from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


AEC_RESULT_COLUMN_ALIASES = {
    "DivisionNm": "seat_name",
    "DivisionID": "seat_id_numeric",
    "StateAb": "state",
    "CandidateNm": "candidate_name",
    "PartyAb": "party",
    "OrdinaryVotes": "ordinary_votes",
    "AbsentVotes": "absent_votes",
    "ProvisionalVotes": "provisional_votes",
    "PostalVotes": "postal_votes",
    "TotalVotes": "total_votes",
    "TotalPercentage": "total_pct",
    "Swing": "swing",
}


def _rename_known_columns(df: pd.DataFrame, aliases: dict[str, str]) -> pd.DataFrame:
    matching = {col: aliases[col] for col in df.columns if col in aliases}
    return df.rename(columns=matching)


def load_aec_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def normalise_house_candidate_results(df: pd.DataFrame) -> pd.DataFrame:
    out = _rename_known_columns(df.copy(), AEC_RESULT_COLUMN_ALIASES)
    wanted = [
        col
        for col in [
            "seat_name",
            "seat_id_numeric",
            "state",
            "candidate_name",
            "party",
            "ordinary_votes",
            "absent_votes",
            "provisional_votes",
            "postal_votes",
            "total_votes",
            "total_pct",
            "swing",
        ]
        if col in out.columns
    ]
    if not wanted:
        return out
    return out[wanted].copy()


def add_source_metadata(df: pd.DataFrame, *, source_name: str, file_name: str) -> pd.DataFrame:
    out = df.copy()
    out["source_name"] = source_name
    out["source_file"] = file_name
    return out


def combine_frames(frames: Iterable[pd.DataFrame]) -> pd.DataFrame:
    frames = list(frames)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)
