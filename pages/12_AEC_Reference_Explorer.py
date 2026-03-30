import streamlit as st
import pandas as pd

from src.aeis.io.resolvers import resolve_dataset_path

st.title("AEC reference explorer")

members_path = resolve_dataset_path(
    processed="aec/house_members_elected_v2.csv",
    interim="aec/house_members_elected_normalised_v2.csv",
    reference=None,
)
polling_places_path = resolve_dataset_path(
    processed="aec/polling_places_v2.csv",
    interim="aec/polling_places_normalised_v2.csv",
    reference=None,
)

st.subheader("Members elected")
if members_path is None:
    st.warning("No members-elected dataset found yet. Run the v2 AEC pipeline first.")
else:
    st.success(f"Using dataset: {members_path}")
    members = pd.read_csv(members_path)
    st.caption(f"Rows: {len(members):,}")
    st.dataframe(members.head(200), use_container_width=True)

st.subheader("Polling places")
if polling_places_path is None:
    st.warning("No polling-places dataset found yet. Run the v2 AEC pipeline first.")
else:
    st.success(f"Using dataset: {polling_places_path}")
    polling_places = pd.read_csv(polling_places_path)
    state_options = ["All"] + sorted(polling_places["state"].dropna().unique().tolist()) if "state" in polling_places.columns else ["All"]
    state = st.selectbox("Polling places state", state_options)
    if state != "All" and "state" in polling_places.columns:
        polling_places = polling_places[polling_places["state"] == state]
    st.caption(f"Rows shown: {len(polling_places):,}")
    st.dataframe(polling_places.head(500), use_container_width=True)
