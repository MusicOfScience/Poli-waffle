import streamlit as st
from pathlib import Path
import pandas as pd

st.title("Processed data")

base = Path(__file__).resolve().parents[1]
processed_root = base / "data" / "processed"

expected = {
    "AEC House candidate results": processed_root / "aec" / "house_candidate_results.csv",
    "ABS correspondence": processed_root / "abs" / "sa1_sa2_ced_correspondence.csv",
    "ABS electoral divisions": processed_root / "abs" / "commonwealth_electoral_divisions.csv",
    "APH current members": processed_root / "aph" / "current_members.csv",
}

for label, path in expected.items():
    st.subheader(label)
    if path.exists():
        st.success(f"Found {path.relative_to(base)}")
        df = pd.read_csv(path)
        st.caption(f"Rows: {len(df):,} · Columns: {len(df.columns)}")
        st.dataframe(df.head(20), use_container_width=True)
    else:
        st.warning(f"Missing {path.relative_to(base)}")
