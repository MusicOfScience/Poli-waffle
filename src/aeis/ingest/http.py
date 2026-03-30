from __future__ import annotations

from pathlib import Path
from urllib.request import urlopen


DEFAULT_USER_AGENT = "Poli-waffle/0.1"


def fetch_bytes(url: str, timeout: int = 30) -> bytes:
    request_headers = {"User-Agent": DEFAULT_USER_AGENT}
    with urlopen(url, timeout=timeout) as response:  # nosec B310
        return response.read()


def download_to_path(url: str, output_path: Path, timeout: int = 30) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data = fetch_bytes(url=url, timeout=timeout)
    output_path.write_bytes(data)
    return output_path
