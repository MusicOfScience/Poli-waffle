from __future__ import annotations

from pathlib import Path


BASE = Path("data") / "raw"
EXPECTED = {
    "AEC": [BASE / "aec" / "house_candidate_results.csv"],
    "ABS": [
        BASE / "abs" / "sa1_sa2_ced_correspondence.csv",
        BASE / "abs" / "commonwealth_electoral_divisions.csv",
    ],
    "APH": [BASE / "aph" / "current_members.csv"],
}


if __name__ == "__main__":
    missing_count = 0
    for source_name, paths in EXPECTED.items():
        print(f"[{source_name}]")
        for path in paths:
            if path.exists():
                print(f"  OK   {path}")
            else:
                print(f"  MISS {path}")
                missing_count += 1
    print()
    print(f"Missing files: {missing_count}")
