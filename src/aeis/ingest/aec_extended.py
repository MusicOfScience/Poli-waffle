from __future__ import annotations

from pathlib import Path

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

AEC_MEMBERS_ELECTED_ALIASES = {
    "DivisionNm": "seat_name",
    "StateAb": "state",
    "CandidateNm": "member_name",
    "PartyAb": "party",
    "Elected": "elected_flag",
}

AEC_POLLING_PLACE_ALIASES = {
    "PollingPlaceID": "polling_place_id",
    "PollingPlaceNm": "polling_place_name",
    "DivisionNm": "seat_name",
    "StateAb": "state",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "Status": "status",
}


def load_aec_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def _rename(df: pd.DataFrame, aliases: dict[str, str]) -> pd.DataFrame:
    matching = {col: aliases[col] for col in df.columns if col in aliases}
    return df.rename(columns=matching)


def normalise_house_candidate_results(df: pd.DataFrame) -> pd.DataFrame:
    out = _rename(df.copy(), AEC_RESULT_COLUMN_ALIASES)
    preferred = [
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
    return out[preferred].copy() if preferred else out


def normalise_house_members_elected(df: pd.DataFrame) -> pd.DataFrame:
    out = _rename(df.copy(), AEC_MEMBERS_ELECTED_ALIASES)
    preferred = [
        col
        for col in ["seat_name", "state", "member_name", "party", "elected_flag"]
        if col in out.columns
    ]
    return out[preferred].drop_duplicates().copy() if preferred else out


def normalise_polling_places(df: pd.DataFrame) -> pd.DataFrame:
    out = _rename(df.copy(), AEC_POLLING_PLACE_ALIASES)
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
        ]
        if col in out.columns
    ]
    return out[preferred].drop_duplicates().copy() if preferred else out


def add_source_metadata(df: pd.DataFrame, *, source_name: str, file_name: str) -> pd.DataFrame:
    out = df.copy()
    out["source_name"] = source_name
    out["source_file"] = file_name
    return out
