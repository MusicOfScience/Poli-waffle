## Architecture

This project should be built in layers.

### 1. Canonical data layer
Official results, boundaries, enrolment, candidates, vote-type returns, and parliamentary reference material.

### 2. Derived analytical layer
Notional boundaries, seat typologies, poll aggregates, contest classes, and model features.

### 3. Override layer
Human-readable YAML files for:
- seat lineage exceptions
- independent families
- candidate aliases
- final-two contest overrides
- house-effect overrides

### 4. Application layer
A Streamlit interface for:
- data QA
- polling
- geography
- seat pages
- model lab
- methods and source audit

### 5. Testing layer
Every non-trivial transformation should become testable.
That includes:
- seat lineage
- final-two detection
- preference rules
- swing application
- file validation
