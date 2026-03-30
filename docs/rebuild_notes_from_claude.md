## Rebuild notes from the original artefact

### Keep
- the broad product idea
- the visible tabs for polling / seats / parliament / economics
- the intuition that final-two contests are not always Labor vs Coalition
- the desire to combine polling, psephology, and count operations

### Replace
- hard-coded seat facts in UI code
- hard-coded polling arrays as the long-term storage pattern
- static seat naming without versioning
- preference assumptions hidden inside rendering code
- undocumented judgments
- unsourced economic snapshots

### Add
- source registry
- seat/version IDs
- lineage tracking
- booth + SA1 + SA2 integration
- backtesting
- diagnostics
- override files
- data validation
