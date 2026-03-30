from __future__ import annotations

from scripts.build_seat_reference_v1 import __name__ as _unused1
from scripts.build_seat_summary_v1 import __name__ as _unused2
from scripts.build_polling_place_summary_v1 import __name__ as _unused3
from scripts.build_seat_detail_v1 import __name__ as _unused4

from pathlib import Path
import subprocess
import sys


SCRIPTS = [
    "scripts/build_seat_reference_v1.py",
    "scripts/build_seat_summary_v1.py",
    "scripts/build_polling_place_summary_v1.py",
    "scripts/build_seat_detail_v1.py",
]


if __name__ == "__main__":
    for script in SCRIPTS:
        print(f"Running {script}")
        completed = subprocess.run([sys.executable, script], check=False)
        if completed.returncode != 0:
            raise SystemExit(f"Build failed for {script}")
    print("Finished core table build chain.")
