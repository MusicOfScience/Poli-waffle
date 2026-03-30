# Manual bridge inputs

This folder holds manually prepared bridge files that connect operational election files to geographic reference layers.

## Current expected file

### `polling_place_to_sa1.csv`
Required columns:
- `polling_place_id`
- `sa1_code_2021`

## Why this exists
The starter repo does not yet perform a full geospatial point-in-polygon join from polling-place coordinates into SA1 boundaries.

Until that is added, the bridge file makes the dependency explicit rather than burying ad hoc manual joins elsewhere.
