import pandas as pd

from src.aeis.ingest.aph import normalise_member_reference


def test_normalise_member_reference_renames_and_selects_fields():
    df = pd.DataFrame(
        {
            "Name": ["Monique Ryan"],
            "Electorate": ["Kooyong"],
            "Party": ["Independent"],
            "State": ["VIC"],
            "Chamber": ["House"],
        }
    )

    result = normalise_member_reference(df)

    assert list(result.columns) == ["member_name", "seat_name", "party", "state", "chamber"]
    assert result.loc[0, "member_name"] == "Monique Ryan"
