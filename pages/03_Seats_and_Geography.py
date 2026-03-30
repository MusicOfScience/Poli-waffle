import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Seats and geography")

base = Path(__file__).resolve().parents[1]
seats = pd.read_csv(base / "data" / "reference" / "sample_seats.csv")
lineage = (base / "overrides" / "seat_lineage.yml").read_text(encoding="utf-8")

state = st.selectbox("State", ["All"] + sorted(seats["state"].unique().tolist()))
if state != "All":
    seats = seats[seats["state"] == state]

st.subheader("Seat sample")
st.dataframe(seats, use_container_width=True)

st.subheader("Why geography must be versioned")
st.markdown(
    """
A seat is not just a label.
A serious platform needs to distinguish between:

- `seat_id` — the enduring conceptual seat key
- `seat_version` — a specific boundary and naming instance
- `boundary_date` — when that version took effect
- `notional_source` — how legacy votes were carried across

The raw prototype treated seats as if the name was stable and sufficient.
It is not.
"""
)

with st.expander("Seat lineage override file"):
    st.code(lineage, language="yaml")
