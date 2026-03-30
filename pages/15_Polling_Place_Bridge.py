import streamlit as st
import pandas as pd

from src.aeis.io.resolvers import resolve_dataset_path

st.title("Polling place bridge")

path = resolve_dataset_path(
    processed="core/polling_place_bridge_v1.csv",
    interim=None,
    reference=None,
)

if path is None:
    st.warning("No polling place bridge dataset found yet.")
    st.code("PYTHONPATH=. python scripts/build_polling_place_bridge_v1.py")
    st.write("Expected manual bridge file: `data/raw/bridges/polling_place_to_sa1.csv`")
    st.stop()

st.success(f"Using dataset: {path}")
df = pd.read_csv(path)

state_options = ["All"] + sorted(df["state"].dropna().unique().tolist()) if "state" in df.columns else ["All"]
state = st.selectbox("State", state_options)
if state != "All" and "state" in df.columns:
    df = df[df["state"] == state]

st.caption(f"Rows shown: {len(df):,}")
st.dataframe(df.head(500), use_container_width=True)
