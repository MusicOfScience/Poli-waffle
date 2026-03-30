import pandas as pd

from src.aeis.ingest.aec import add_source_metadata, normalise_house_candidate_results


def test_normalise_house_candidate_results_renames_known_columns():
    df = pd.DataFrame(
        {
            "DivisionNm": ["Kooyong"],
            "StateAb": ["VIC"],
            "CandidateNm": ["Example Candidate"],
            "PartyAb": ["IND"],
            "TotalVotes": [50000],
            "TotalPercentage": [50.5],
        }
    )

    result = normalise_house_candidate_results(df)

    assert "seat_name" in result.columns
    assert "state" in result.columns
    assert "candidate_name" in result.columns
    assert result.loc[0, "party"] == "IND"


def test_add_source_metadata_appends_columns():
    df = pd.DataFrame({"seat_name": ["Kooyong"]})
    result = add_source_metadata(df, source_name="AEC", file_name="house.csv")

    assert result.loc[0, "source_name"] == "AEC"
    assert result.loc[0, "source_file"] == "house.csv"
