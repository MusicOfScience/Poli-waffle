import pandas as pd

from src.aeis.domain.seat_reference import build_seat_reference


def test_build_seat_reference_joins_members_to_divisions():
    members = pd.DataFrame(
        {
            "member_name": ["Monique Ryan"],
            "seat_name": ["Kooyong"],
            "party": ["Independent"],
            "state": ["VIC"],
            "chamber": ["House"],
        }
    )
    divisions = pd.DataFrame(
        {
            "ced_code_2021": ["206"],
            "ced_name_2021": ["Kooyong"],
            "state_name_2021": ["Victoria"],
        }
    )

    result = build_seat_reference(members, divisions)

    assert len(result) == 1
    assert result.loc[0, "member_name"] == "Monique Ryan"
    assert result.loc[0, "ced_code_2021"] == "206"
