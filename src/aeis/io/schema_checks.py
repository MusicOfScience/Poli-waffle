from __future__ import annotations

from collections.abc import Iterable

import pandas as pd


class SchemaError(ValueError):
    """Raised when a dataframe does not contain required columns."""



def require_columns(df: pd.DataFrame, required: Iterable[str], *, dataset_name: str) -> None:
    required = list(required)
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise SchemaError(
            f"{dataset_name} is missing required columns: {missing}. Available columns: {list(df.columns)}"
        )
