import pandas as pd
import pytest

from src.aeis.io.schema_checks import SchemaError, require_columns


def test_require_columns_passes_when_columns_exist():
    df = pd.DataFrame({"a": [1], "b": [2]})
    require_columns(df, ["a", "b"], dataset_name="example")


def test_require_columns_raises_when_missing():
    df = pd.DataFrame({"a": [1]})
    with pytest.raises(SchemaError):
        require_columns(df, ["a", "b"], dataset_name="example")
