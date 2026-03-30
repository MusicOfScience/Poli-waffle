import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Data status")

base = Path(__file__).resolve().parents[1]
source_registry = pd.read_csv(base / "data" / "reference" / "source_registry.csv")
seat_sample = pd.read_csv(base / "data" / "reference" / "sample_seats.csv")

st.subheader("Source registry")
st.dataframe(source_registry, use_container_width=True)

st.subheader("Example seat reference data")
st.dataframe(seat_sample, use_container_width=True)

st.markdown(
    """
### What this page is for

This page is an audit surface.

Before any serious modelling work happens, the team should be able to answer:

- what data source is being used
- whether it is canonical or advisory
- how often it updates
- what geography it uses
- whether it is suitable for modelling, QA, or commentary only
"""
)
