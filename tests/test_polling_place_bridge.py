import pandas as pd

from src.aeis.domain.polling_place_bridge import build_polling_place_bridge


def test_build_polling_place_bridge_joins_sa1_and_ced_fields():
    polling_places = pd.DataFrame(
        {
            "polling_place_id": [101],
            "polling_place_name": ["Example Hall"],
            "seat_name": ["Kooyong"],
            "state": ["VIC"],
        }
    )
    bridge = pd.DataFrame(
        {
            "polling_place_id": [101],
            "sa1_code_2021": ["21111111111"],
        }
    )
    correspondence = pd.DataFrame(
        {
            "sa1_code_2021": ["21111111111"],
            "sa2_code_2021": ["206011001"],
            "ced_code_2021": ["206"],
            "ced_name_2021": ["Kooyong"],
            "state_name_2021": ["Victoria"],
        }
    )

    result = build_polling_place_bridge(polling_places, bridge, correspondence)

    assert len(result) == 1
    assert result.loc[0, "sa1_code_2021"] == "21111111111"
    assert result.loc[0, "ced_name_2021"] == "Kooyong"
