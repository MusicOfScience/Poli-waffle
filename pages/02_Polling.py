import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.title("Polling")

base = Path(__file__).resolve().parents[1]
polls = pd.read_csv(base / "data" / "reference" / "sample_polls.csv")
pollster = st.selectbox("Pollster", ["All"] + sorted(polls["pollster"].unique().tolist()))

if pollster != "All":
    polls = polls[polls["pollster"] == pollster]

fig = px.line(
    polls,
    x="date",
    y=["alp", "lnp", "grn", "onp", "other"],
    markers=True,
    title="Sample primary vote series",
)
st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
### Build notes

This page currently uses **sample data only**.

Real next steps:
- ingest polling as data rather than hard-coded arrays
- add field dates, sample modes, and state breakdown availability
- estimate or store house effects separately
- separate observed polling from modelled trend
"""
)
