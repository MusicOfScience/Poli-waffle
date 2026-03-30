from __future__ import annotations

import pandas as pd


def apply_uniform_swing(df: pd.DataFrame, swing: float) -> pd.DataFrame:
    required = {"seat_name", "state", "alp_2cp"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = df.copy()
    out["alp_2cp_model"] = (out["alp_2cp"] + swing).clip(lower=0, upper=100)
    out["lnp_2cp_model"] = 100 - out["alp_2cp_model"]
    out["projected_winner"] = out["alp_2cp_model"].apply(
        lambda value: "ALP/ally" if value >= 50 else "Coalition/other"
    )
    return out


def classify_margin(alp_2cp: float) -> str:
    margin = abs(alp_2cp - 50)
    if margin < 2:
        return "ultra-marginal"
    if margin < 6:
        return "marginal"
    if margin < 10:
        return "fairly safe"
    return "safe"
