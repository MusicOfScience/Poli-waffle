import streamlit as st
from pathlib import Path

from src.aeis.io.yaml_loader import load_yaml_file

st.title("Official source catalog")

base = Path(__file__).resolve().parents[1]
catalog = load_yaml_file(base / "configs" / "source_catalog.yml")

st.markdown(
    """
This page lists the official source endpoints currently wired into the scaffold.

These are the **canonical discovery points** for the first-pass federal pipeline.
"""
)

for source_group, entries in catalog.get("sources", {}).items():
    st.subheader(source_group.upper())
    for label, value in entries.items():
        st.write(f"- **{label}**: {value}")
