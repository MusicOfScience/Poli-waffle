import streamlit as st
import pandas as pd

from src.aeis.io.resolvers import resolve_dataset_path

st.title("Seat reference")

path = resolve_dataset_path(
    processed="core/seat_reference_v1.csv",
    interim=None,
    reference=None,
)

if path is None:
    st.warning("No seat reference dataset found yet. Run the seat reference build script first.")
    st.code("PYTHONPATH=. python scripts/build_seat_reference_v1.py")
    st.stop()

st.success(f"Using dataset: {path}")
df = pd.read_csv(path)
state_options = ["All"] + sorted(df["state"].dropna().unique().tolist()) if "state" in df.columns else ["All"]
state = st.selectbox("State", state_options)

if state != "All" and "state" in df.columns:
    df = df[df["state"] == state]

st.caption(f"Rows shown: {len(df):,}")
st.dataframe(df, use_container_width=True)
