import streamlit as st
import pandas as pd
from pathlib import Path


def apply_uniform_swing(df: pd.DataFrame, swing: float) -> pd.DataFrame:
    out = df.copy()
    out["alp_2cp_model"] = (out["alp_2cp"] + swing).clip(lower=0, upper=100)
    out["lnp_2cp_model"] = (100 - out["alp_2cp_model"]).clip(lower=0, upper=100)
    out["projected_winner"] = out["alp_2cp_model"].apply(lambda x: "ALP/ally" if x >= 50 else "Coalition/other")
    return out[[
        "seat_name",
        "state",
        "alp_2cp",
        "alp_2cp_model",
        "lnp_2cp_model",
        "projected_winner",
    ]]


st.title("Model lab")

base = Path(__file__).resolve().parents[1]
seats = pd.read_csv(base / "data" / "reference" / "sample_seats.csv")

swing = st.slider("National ALP swing (%)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
modelled = apply_uniform_swing(seats.copy(), swing=swing)

st.dataframe(modelled, use_container_width=True)

st.warning(
    "This is a placeholder baseline only. A serious model must distinguish between national swing, state swing, seat residuals, final-two contest shape, redistribution effects, and independents."
)
