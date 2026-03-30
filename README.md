# Australian Election Intelligence Streamlit Starter

A Streamlit-first starter repository for turning a dashboard-style political demo into a maintainable, testable, data-first research platform.

This project is designed as the **next step after a prototype**. It keeps the useful instinct from the original artefact — one place to see polling, seats, parliament, economics, and methodological notes — but replaces hard-coded assumptions with a structure that can grow into a real model.

## What this starter is for

This repository is meant to support:

- federal and state election analysis
- redistribution-aware seat tracking
- booth, SA1, and SA2-linked data workflows
- poll ingestion and aggregation
- final-two / TCP / 2CP contest detection
- backtesting and model diagnostics
- manual override files for edge cases and psephological judgement

## What this starter is **not**

This is **not** a finished forecasting engine.
It is a scaffold with:

- a working Streamlit multipage app
- a source registry
- example reference data
- override files
- placeholder model logic
- test scaffolding
- docs that define the architecture before the codebase sprawls

## Repository shape

```text
Poli-waffle/
├── streamlit_app.py
├── pages/
├── src/aeis/
│   ├── io/
│   ├── domain/
│   └── models/
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── reference/
├── overrides/
├── docs/
└── tests/
```

## Core design choices

### 1. Streamlit runs the front-end
This starter uses Streamlit as the application shell.

### 2. Data before visuals
Every chart or seat call should be traceable back to:
- a source
- a timestamp
- a transformation step
- an override if one exists

### 3. Geography is versioned
Seats change.
Boundaries move.
Names disappear.
The platform must treat **seat lineage** and **boundary versioning** as first-class data problems.

### 4. Manual judgement is explicit
Some edge cases are not solved by neat code.
Independent families, final-two contest overrides, candidate aliases, and redistribution quirks belong in human-readable YAML files.

## Recommended MVP phases

### Phase 1 — repository and data spine
- finalise source registry
- define seat/version IDs
- ingest official results and reference tables
- stand up Streamlit pages for audit and navigation

### Phase 2 — electoral intelligence
- final-two detection engine
- preference rules
- seat typing
- polling ingest
- notional carry-forward logic

### Phase 3 — modelling and testing
- national/state swing baselines
- seat-level residual model
- calibration and backtesting
- diagnostics dashboard

### Phase 4 — live operations
- live count tracker
- vote-type sensitivity tables
- scenario lab
- declaration vote monitoring
- map layers and booth monitoring

## Quick start

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run streamlit_app.py
```

## Streamlit Community Cloud

Set the app entrypoint to `streamlit_app.py`.

## Notes on the original prototype

The original artefact had a good instinctive product shape:
- polling
- electorates
- parliament
- economics
- rough preference logic

But it also had serious structural risks:
- hard-coded seat facts
- unversioned boundaries
- mixed source quality
- assumptions embedded directly in UI code
- no backtesting spine
- no canonical/advisory data hierarchy

This starter exists to fix that.
