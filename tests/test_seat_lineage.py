from src.aeis.domain.seat_lineage import (
    find_current_version,
    lineage_by_seat_id,
    parse_seat_lineage,
)


def test_parse_and_group_seat_lineage():
    payload = {
        "seat_lineage": [
            {
                "seat_id": "fed_vic_kooyong",
                "seat_version": "fed_2022_vic_kooyong",
                "seat_name": "Kooyong",
                "state": "VIC",
                "boundary_date": "2022-01-01",
                "predecessor_version": None,
            },
            {
                "seat_id": "fed_vic_kooyong",
                "seat_version": "fed_2025_vic_kooyong",
                "seat_name": "Kooyong",
                "state": "VIC",
                "boundary_date": "2025-03-04",
                "predecessor_version": "fed_2022_vic_kooyong",
            },
        ]
    }

    records = parse_seat_lineage(payload)
    grouped = lineage_by_seat_id(records)

    assert len(records) == 2
    assert len(grouped["fed_vic_kooyong"]) == 2


def test_find_current_version_returns_latest_boundary_date():
    payload = {
        "seat_lineage": [
            {
                "seat_id": "fed_vic_kooyong",
                "seat_version": "fed_2022_vic_kooyong",
                "seat_name": "Kooyong",
                "state": "VIC",
                "boundary_date": "2022-01-01",
                "predecessor_version": None,
            },
            {
                "seat_id": "fed_vic_kooyong",
                "seat_version": "fed_2025_vic_kooyong",
                "seat_name": "Kooyong",
                "state": "VIC",
                "boundary_date": "2025-03-04",
                "predecessor_version": "fed_2022_vic_kooyong",
            },
        ]
    }

    records = parse_seat_lineage(payload)
    current = find_current_version(records, "fed_vic_kooyong")

    assert current is not None
    assert current.seat_version == "fed_2025_vic_kooyong"
