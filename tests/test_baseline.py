import pandas as pd

from src.aeis.models.baseline import apply_uniform_swing, classify_margin


def test_apply_uniform_swing_shifts_and_clips():
    df = pd.DataFrame(
        {
            "seat_name": ["Example"],
            "state": ["VIC"],
            "alp_2cp": [49.0],
        }
    )

    result = apply_uniform_swing(df, swing=3.0)

    assert result.loc[0, "alp_2cp_model"] == 52.0
    assert result.loc[0, "lnp_2cp_model"] == 48.0
    assert result.loc[0, "projected_winner"] == "ALP/ally"


def test_classify_margin_bands():
    assert classify_margin(50.5) == "ultra-marginal"
    assert classify_margin(53.0) == "marginal"
    assert classify_margin(57.0) == "fairly safe"
    assert classify_margin(62.0) == "safe"
