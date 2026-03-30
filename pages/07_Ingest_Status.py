import streamlit as st
from pathlib import Path

st.title("Ingest status")

base = Path(__file__).resolve().parents[1]
raw_root = base / "data" / "raw"
interim_root = base / "data" / "interim"

expected_files = {
    "AEC": [raw_root / "aec" / "house_candidate_results.csv"],
    "ABS": [
        raw_root / "abs" / "sa1_sa2_ced_correspondence.csv",
        raw_root / "abs" / "commonwealth_electoral_divisions.csv",
    ],
    "APH": [raw_root / "aph" / "current_members.csv"],
}

st.markdown(
    """
This page is here to answer a blunt operational question:

**Do we actually have the files we think we have?**

It tracks the first pass of raw files expected by the interim build scripts.
"""
)

for source_name, files in expected_files.items():
    st.subheader(source_name)
    for file_path in files:
        exists = file_path.exists()
        label = "Present" if exists else "Missing"
        icon = "✅" if exists else "⚠️"
        st.write(f"{icon} `{file_path.relative_to(base)}` — {label}")

st.subheader("Interim output directory")
if interim_root.exists():
    paths = [p for p in interim_root.rglob("*.csv")]
    if paths:
        for path in paths:
            st.write(f"✅ `{path.relative_to(base)}`")
    else:
        st.write("No interim CSV outputs yet.")
else:
    st.write("Interim directory not created yet.")
