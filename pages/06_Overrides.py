import streamlit as st
from pathlib import Path

st.title("Overrides")

base = Path(__file__).resolve().parents[1]
override_files = [
    "seat_lineage.yml",
    "contest_overrides.yml",
    "candidate_aliases.yml",
    "independent_families.yml",
]

st.markdown(
    """
These files are where explicit political judgement belongs.

That is healthier than burying assumptions in chart code or model functions.
"""
)

for filename in override_files:
    path = base / "overrides" / filename
    st.subheader(filename)
    st.code(path.read_text(encoding="utf-8"), language="yaml")
