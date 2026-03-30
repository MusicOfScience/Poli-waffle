import pandas as pd

from src.aeis.domain.polling_place_summary import build_polling_place_summary


def test_build_polling_place_summary_counts_and_bridge_stats():
    polling_places = pd.DataFrame(
        {
            "state": ["VIC", "VIC"],
            "seat_name": ["Kooyong", "Kooyong"],
            "status": ["Open", "Open"],
            "polling_place_id": [101, 102],
        }
    )
    bridge = pd.DataFrame(
        {
            "state": ["VIC", "VIC"],
            "seat_name": ["Kooyong", "Kooyong"],
            "polling_place_id": [101, 102],
            "sa1_code_2021": ["1", "2"],
            "sa2_code_2021": ["10", "10"],
        }
    )

    result = build_polling_place_summary(polling_places, bridge)

    assert len(result) == 1
    assert result.loc[0, "polling_place_count"] == 2
    assert result.loc[0, "bridged_polling_places"] == 2
    assert result.loc[0, "bridged_sa1_count"] == 2
    assert result.loc[0, "bridged_sa2_count"] == 1
