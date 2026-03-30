import streamlit as st
from pathlib import Path

st.title("Methods and sources")

base = Path(__file__).resolve().parents[1]

for doc_name in ["architecture.md", "data_sources.md", "rebuild_notes_from_claude.md"]:
    st.subheader(doc_name)
    st.markdown((base / "docs" / doc_name).read_text(encoding="utf-8"))
