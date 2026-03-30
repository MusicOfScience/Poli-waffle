from pathlib import Path

from src.aeis.ingest.catalog_download import download_targets_from_config


def test_download_targets_from_config_calls_download_helper(tmp_path, monkeypatch):
    config_path = tmp_path / "targets.yml"
    config_path.write_text(
        """
        targets:
          one:
            url: https://example.com/a.csv
            output: data/raw/aec/a.csv
        """,
        encoding="utf-8",
    )

    calls = []

    def fake_download(url: str, output_path: Path):
        calls.append((url, output_path))
        return output_path

    monkeypatch.setattr("src.aeis.ingest.catalog_download.download_to_path", fake_download)

    written = download_targets_from_config(config_path)

    assert len(written) == 1
    assert calls[0][0] == "https://example.com/a.csv"
    assert str(calls[0][1]) == "data/raw/aec/a.csv"
