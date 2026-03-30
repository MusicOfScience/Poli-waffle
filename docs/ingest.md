## Ingest scaffold

This repository now includes a **real ingest scaffold**, but not yet a full production pipeline.

### What exists
- a lightweight ingest package under `src/aeis/ingest/`
- a source registry module for official sources
- a thin HTTP helper
- a manifest writer
- a script entrypoint at `scripts/ingest_reference.py`

### What it does right now
Right now the ingest step is intentionally conservative.
It writes a manifest of the official source endpoints and path hints that the project expects to use.

This is useful because it separates:
- source governance
- source discovery
- download logic
- later parsing logic

### What it does not do yet
- authenticate against anything
- scrape dynamic pages aggressively
- parse PDFs or spreadsheets
- harmonise election results into processed tables
- map booth files into SA1 or SA2 bridges

### Why this is still useful
A lot of political projects go wrong because source choice is implicit.
This scaffold makes the source layer explicit before the transformation layer gets messy.

### Next steps
1. turn the official source manifest into a richer registry with file types and refresh cadence
2. add downloader functions for stable CSV and XLSX endpoints
3. create validation checks on expected columns
4. write parsed outputs into `data/interim/`
5. only then promote cleaned files into `data/processed/`
