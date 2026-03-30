import streamlit as st

st.set_page_config(
    page_title="Poli-waffle",
    page_icon="🗳️",
    layout="wide",
)

st.title("Poli-waffle")
st.caption("Browser-first Streamlit scaffold for Australian political and election intelligence work.")

st.markdown(
    """
This is the **home page** of the repository scaffold.

The point of this first version is not to pretend we already have a serious forecast engine.
It is to give the project a clean shell while the real work happens in:

- source governance
- polling ingestion
- seat lineage and redistribution handling
- booth, SA1 and SA2 geography
- final-two contest logic
- backtesting and diagnostics

Use the sidebar to move through the pages.
"""
)

col1, col2, col3 = st.columns(3)
col1.metric("Reference source groups", "5")
col2.metric("Sample reference seats", "8")
col3.metric("Immediate next milestone", "Real ingest")

st.info(
    "This starter is intentionally modest. The next serious step is replacing sample files with real AEC, ABS, APH and state commission inputs."
)
