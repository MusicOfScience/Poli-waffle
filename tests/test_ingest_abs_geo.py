import pandas as pd

from src.aeis.ingest.abs_geo import normalise_correspondence, normalise_electoral_divisions


def test_normalise_correspondence_keeps_expected_fields():
    df = pd.DataFrame(
        {
            "SA1_CODE_2021": ["1001"],
            "SA2_CODE_2021": ["2002"],
            "CED_CODE_2021": ["3003"],
            "CED_NAME_2021": ["Kooyong"],
            "STATE_NAME_2021": ["Victoria"],
            "RATIO": [1.0],
        }
    )

    result = normalise_correspondence(df)
    assert list(result.columns) == [
        "sa1_code_2021",
        "sa2_code_2021",
        "ced_code_2021",
        "ced_name_2021",
        "state_name_2021",
        "allocation_ratio",
    ]


def test_normalise_electoral_divisions_deduplicates():
    df = pd.DataFrame(
        {
            "CED_CODE_2021": ["3003", "3003"],
            "CED_NAME_2021": ["Kooyong", "Kooyong"],
            "STE_CODE_2021": ["2", "2"],
            "STE_NAME_2021": ["Victoria", "Victoria"],
        }
    )

    result = normalise_electoral_divisions(df)
    assert len(result) == 1
