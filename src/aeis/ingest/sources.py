from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceEndpoint:
    name: str
    host: str
    path_hint: str
    tier: str
    notes: str


OFFICIAL_SOURCE_ENDPOINTS = [
    SourceEndpoint(
        name="AEC downloads and statistics",
        host="aec.gov.au",
        path_hint="2025 federal election downloads and statistics",
        tier="canonical",
        notes="Federal election result and operations landing page.",
    ),
    SourceEndpoint(
        name="AEC maps and spatial data",
        host="aec.gov.au",
        path_hint="electorates maps and spatial data",
        tier="canonical",
        notes="Current divisions, spatial files, and SA1 allocations.",
    ),
    SourceEndpoint(
        name="ABS ASGS latest release",
        host="abs.gov.au",
        path_hint="ASGS Edition 3 latest release",
        tier="canonical",
        notes="Geographic reference layer for SA1 and SA2 work.",
    ),
    SourceEndpoint(
        name="ABS correspondences",
        host="abs.gov.au",
        path_hint="ASGS correspondences",
        tier="canonical",
        notes="Geographic bridging and correspondence files.",
    ),
    SourceEndpoint(
        name="APH members reference",
        host="aph.gov.au",
        path_hint="senators and members",
        tier="canonical",
        notes="Current parliamentarian reference layer.",
    ),
    SourceEndpoint(
        name="VEC results",
        host="vec.vic.gov.au",
        path_hint="results",
        tier="canonical",
        notes="Victorian election results landing page.",
    ),
]
