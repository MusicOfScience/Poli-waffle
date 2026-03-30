import pandas as pd

from src.aeis.domain.seat_summary import build_seat_summary, bucket_party


def test_bucket_party_groups_major_families():
    assert bucket_party("ALP") == "ALP"
    assert bucket_party("LIB") == "Coalition"
    assert bucket_party("GRN") == "Greens"
    assert bucket_party("ONP") == "One Nation"
    assert bucket_party("IND") == "Independent"


def test_build_seat_summary_aggregates_votes_and_joins_reference():
    candidates = pd.DataFrame(
        {
            "state": ["VIC", "VIC", "VIC"],
            "seat_name": ["Kooyong", "Kooyong", "Kooyong"],
            "party": ["IND", "LIB", "ALP"],
            "total_votes": [52000, 50000, 15000],
        }
    )
    seat_reference = pd.DataFrame(
        {
            "state": ["VIC"],
            "seat_name": ["Kooyong"],
            "member_name": ["Monique Ryan"],
            "party": ["Independent"],
            "ced_code_2021": ["206"],
        }
    )

    result = build_seat_summary(candidates, seat_reference)

    assert len(result) == 1
    assert result.loc[0, "Independent"] == 52000
    assert result.loc[0, "Coalition"] == 50000
    assert result.loc[0, "ALP"] == 15000
    assert result.loc[0, "member_name"] == "Monique Ryan"
