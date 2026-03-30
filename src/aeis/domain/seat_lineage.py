from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SeatLineageRecord:
    seat_id: str
    seat_version: str
    seat_name: str
    state: str
    boundary_date: str
    predecessor_version: str | None
    note: str | None = None


def parse_seat_lineage(payload: dict[str, Any]) -> list[SeatLineageRecord]:
    rows = payload.get("seat_lineage", [])
    return [
        SeatLineageRecord(
            seat_id=row["seat_id"],
            seat_version=row["seat_version"],
            seat_name=row["seat_name"],
            state=row["state"],
            boundary_date=row["boundary_date"],
            predecessor_version=row.get("predecessor_version"),
            note=row.get("note"),
        )
        for row in rows
    ]


def lineage_by_seat_id(records: list[SeatLineageRecord]) -> dict[str, list[SeatLineageRecord]]:
    grouped: dict[str, list[SeatLineageRecord]] = {}
    for record in records:
        grouped.setdefault(record.seat_id, []).append(record)
    return grouped


def find_current_version(records: list[SeatLineageRecord], seat_id: str) -> SeatLineageRecord | None:
    matching = [record for record in records if record.seat_id == seat_id]
    if not matching:
        return None
    return sorted(matching, key=lambda row: row.boundary_date)[-1]
