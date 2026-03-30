import streamlit as st
from pathlib import Path
import pandas as pd

from src.aeis.io.resolvers import resolve_dataset_path

st.title("Preferred datasets")

catalog = {
    "House candidate results": {
        "processed": "aec/house_candidate_results.csv",
        "interim": "aec/house_candidate_results_normalised.csv",
        "reference": None,
    },
    "ABS correspondence": {
        "processed": "abs/sa1_sa2_ced_correspondence.csv",
        "interim": "abs/sa1_sa2_ced_correspondence_normalised.csv",
        "reference": None,
    },
    "ABS electoral divisions": {
        "processed": "abs/commonwealth_electoral_divisions.csv",
        "interim": "abs/commonwealth_electoral_divisions_normalised.csv",
        "reference": None,
    },
    "APH current members": {
        "processed": "aph/current_members.csv",
        "interim": "aph/current_members_normalised.csv",
        "reference": None,
    },
    "Sample seats": {
        "processed": None,
        "interim": None,
        "reference": "sample_seats.csv",
    },
}

for label, paths in catalog.items():
    st.subheader(label)
    chosen = resolve_dataset_path(
        processed=paths["processed"],
        interim=paths["interim"],
        reference=paths["reference"],
    )
    if chosen is None:
        st.warning("No dataset found in processed, interim, or reference layers.")
        continue

    st.success(f"Using `{chosen}`")
    if chosen.suffix.lower() == ".csv":
        df = pd.read_csv(chosen)
        st.caption(f"Rows: {len(df):,} · Columns: {len(df.columns)}")
        st.dataframe(df.head(10), use_container_width=True)
