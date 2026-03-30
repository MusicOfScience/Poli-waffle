## AEC starter pipeline

This project now has a first-pass AEC pipeline.

### Source shape
The starter downloader is based on the 2025 House downloads menu and targets a small set of stable CSV files:
- national House candidates
- members elected
- first preferences by candidate by vote type
- polling places reference

### Commands
Use the clean one-shot runner:

```bash
PYTHONPATH=. python scripts/run_aec_pipeline_clean.py
```

Or step through manually:

```bash
PYTHONPATH=. python scripts/download_aec_starter.py
PYTHONPATH=. python scripts/build_interim_tables.py
PYTHONPATH=. python scripts/build_processed_tables.py
```

### What it produces
- raw files under `data/raw/aec/`
- interim normalised candidate results under `data/interim/aec/`
- processed candidate results under `data/processed/aec/`

### Limits of the current version
- only a narrow starter subset is wired
- does not yet parse every House download file
- does not yet join polling places to booths, SA1, or SA2
- does not yet create final-two or swing analytics from live official files
