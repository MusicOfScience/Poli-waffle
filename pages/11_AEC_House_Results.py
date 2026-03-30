import streamlit as st
import pandas as pd

from src.aeis.io.resolvers import resolve_dataset_path

st.title("AEC House results explorer")

path = resolve_dataset_path(
    processed="aec/house_candidate_results.csv",
    interim="aec/house_candidate_results_normalised.csv",
    reference=None,
)

if path is None:
    st.warning("No AEC House result dataset found yet. Run the AEC download and pipeline scripts first.")
    st.stop()

st.success(f"Using dataset: {path}")
df = pd.read_csv(path)

state_options = ["All"] + sorted(df["state"].dropna().unique().tolist()) if "state" in df.columns else ["All"]
state = st.selectbox("State", state_options)

if state != "All" and "state" in df.columns:
    df = df[df["state"] == state]

if "seat_name" in df.columns:
    seat_options = ["All"] + sorted(df["seat_name"].dropna().unique().tolist())
    seat = st.selectbox("Seat", seat_options)
    if seat != "All":
        df = df[df["seat_name"] == seat]

st.caption(f"Rows shown: {len(df):,}")
st.dataframe(df.head(500), use_container_width=True)
