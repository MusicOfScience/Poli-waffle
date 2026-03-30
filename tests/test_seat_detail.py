import pandas as pd

from src.aeis.domain.seat_detail import build_seat_detail


def test_build_seat_detail_merges_reference_summary_and_polling_place_stats():
    seat_reference = pd.DataFrame(
        {
            "state": ["VIC"],
            "seat_name": ["Kooyong"],
            "member_name": ["Monique Ryan"],
        }
    )
    seat_summary = pd.DataFrame(
        {
            "state": ["VIC"],
            "seat_name": ["Kooyong"],
            "Independent": [52000],
        }
    )
    polling_place_summary = pd.DataFrame(
        {
            "state": ["VIC"],
            "seat_name": ["Kooyong"],
            "polling_place_count": [12],
            "bridged_polling_places": [10],
            "bridged_sa1_count": [24],
            "bridged_sa2_count": [5],
        }
    )

    result = build_seat_detail(seat_reference, seat_summary, polling_place_summary)

    assert len(result) == 1
    assert result.loc[0, "member_name"] == "Monique Ryan"
    assert result.loc[0, "Independent"] == 52000
    assert result.loc[0, "polling_places_total"] == 12
    assert result.loc[0, "bridged_sa2_count"] == 5
