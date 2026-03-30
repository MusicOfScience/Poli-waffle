## Data source hierarchy

### Tier 1 — canonical
Use these as the source of record wherever possible.

- Australian Electoral Commission (AEC)
- Australian Bureau of Statistics (ABS)
- Australian Parliament House / Parliamentary Handbook (APH)
- state and territory electoral commissions
- Reserve Bank of Australia (RBA) and ABS macro releases

### Tier 2 — advisory analytical sources
Useful for interpretation, seat context, and poll aggregation, but not the source of record.

- Poll Bludger / BludgerTrack
- Tally Room
- Antony Green / ABC election analysis
- individual pollsters and seat-modelling shops

### Tier 3 — project-maintained overrides
Use for explicit judgement calls that code alone cannot safely infer.

- seat lineage
- candidate aliases
- independent families
- contest overrides
- pollster house-effect adjustments

## Geographic recommendation

- **SA1** for atomic bridging and redistribution logic
- **SA2** for demographic storytelling and reporting
- **booth / PPVC / vote type** for operations and election-night analysis

## Minimum canonical feeds to ingest first

1. Federal results archive
2. Current and prior boundary files
3. SA1 allocations to electoral divisions
4. Polling-place and PPVC files
5. Candidate lists
6. Vote-type daily files where available
7. Enrolment statistics
8. Current parliamentarian reference data
