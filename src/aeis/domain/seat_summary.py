from __future__ import annotations

import pandas as pd


PARTY_BUCKETS = {
    "ALP": "ALP",
    "LIB": "Coalition",
    "LP": "Coalition",
    "LNP": "Coalition",
    "NP": "Coalition",
    "NAT": "Coalition",
    "GRN": "Greens",
    "ONP": "One Nation",
    "IND": "Independent",
    "CA": "Independent",
    "KAP": "Other",
}


def bucket_party(value: str | float | None) -> str:
    if value is None or pd.isna(value):
        return "Other"
    text = str(value).strip().upper()
    return PARTY_BUCKETS.get(text, "Other")


def build_seat_summary(candidate_results: pd.DataFrame, seat_reference: pd.DataFrame | None = None) -> pd.DataFrame:
    df = candidate_results.copy()
    if "party" in df.columns:
        df["party_bucket"] = df["party"].apply(bucket_party)
    else:
        df["party_bucket"] = "Other"

    if "total_votes" in df.columns:
        numeric_votes = pd.to_numeric(df["total_votes"], errors="coerce").fillna(0)
    else:
        numeric_votes = pd.Series([0] * len(df), index=df.index)
    df["total_votes_num"] = numeric_votes

    grouped = (
        df.groupby(["state", "seat_name", "party_bucket"], dropna=False)["total_votes_num"]
        .sum()
        .reset_index()
    )

    pivot = grouped.pivot_table(
        index=["state", "seat_name"],
        columns="party_bucket",
        values="total_votes_num",
        fill_value=0,
        aggfunc="sum",
    ).reset_index()

    pivot.columns.name = None
    pivot = pivot.rename_axis(None, axis=1)

    vote_columns = [col for col in pivot.columns if col not in {"state", "seat_name"}]
    pivot["total_votes_all"] = pivot[vote_columns].sum(axis=1)

    for col in vote_columns:
        pct_col = f"{col.lower().replace(' ', '_')}_pct"
        pivot[pct_col] = pivot.apply(
            lambda row: (row[col] / row["total_votes_all"] * 100) if row["total_votes_all"] else 0,
            axis=1,
        )

    if seat_reference is not None and not seat_reference.empty:
        join_cols = [col for col in ["state", "seat_name", "member_name", "party", "ced_code_2021"] if col in seat_reference.columns]
        seat_ref = seat_reference[join_cols].drop_duplicates()
        pivot = pivot.merge(seat_ref, on=["state", "seat_name"], how="left")

    return pivot.sort_values(["state", "seat_name"]).reset_index(drop=True)
