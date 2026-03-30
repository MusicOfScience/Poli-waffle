import pandas as pd

from src.aeis.ingest.aec_extended import (
    normalise_house_members_elected,
    normalise_polling_places,
)


def test_normalise_house_members_elected_renames_fields():
    df = pd.DataFrame(
        {
            "DivisionNm": ["Kooyong"],
            "StateAb": ["VIC"],
            "CandidateNm": ["Monique Ryan"],
            "PartyAb": ["IND"],
            "Elected": ["Y"],
        }
    )

    result = normalise_house_members_elected(df)

    assert list(result.columns) == ["seat_name", "state", "member_name", "party", "elected_flag"]
    assert result.loc[0, "member_name"] == "Monique Ryan"


def test_normalise_polling_places_renames_fields():
    df = pd.DataFrame(
        {
            "PollingPlaceID": [101],
            "PollingPlaceNm": ["Example Hall"],
            "DivisionNm": ["Kooyong"],
            "StateAb": ["VIC"],
            "Latitude": [-37.8],
            "Longitude": [145.0],
            "Status": ["Open"],
        }
    )

    result = normalise_polling_places(df)

    assert "polling_place_id" in result.columns
    assert result.loc[0, "polling_place_name"] == "Example Hall"
