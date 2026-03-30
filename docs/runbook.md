## Operator runbook

### First local setup
1. Install dependencies
2. Run tests
3. Generate the source manifest
4. Check raw file layout
5. Build interim tables
6. Run Streamlit

### Suggested command sequence
```bash
make install
make test
make manifest
make check-raw
make build-interim
make run
```

### What to do when a file is missing
- do not improvise a replacement inside `data/interim/`
- place the original file under `data/raw/`
- keep the source filename stable when possible
- document any naming mismatch in a note or issue

### What to do when parsing breaks
- inspect the raw source columns
- update the alias maps in the ingest modules
- add or update a test that captures the new column pattern
- rerun `make test` and `make build-interim`

### What belongs in overrides
- contest exceptions
- candidate aliases
- independent families
- seat lineage decisions

### What does not belong in overrides
- missing raw data
- ad hoc manual aggregates that should be derived
- values that should come from canonical source files
