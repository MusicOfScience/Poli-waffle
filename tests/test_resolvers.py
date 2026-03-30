from pathlib import Path

from src.aeis.io.resolvers import resolve_dataset_path


def test_resolve_dataset_path_prefers_processed(tmp_path, monkeypatch):
    project_root = tmp_path
    processed = project_root / "data" / "processed" / "aec" / "house_candidate_results.csv"
    interim = project_root / "data" / "interim" / "aec" / "house_candidate_results_normalised.csv"
    processed.parent.mkdir(parents=True, exist_ok=True)
    interim.parent.mkdir(parents=True, exist_ok=True)
    processed.write_text("x\n1\n", encoding="utf-8")
    interim.write_text("x\n2\n", encoding="utf-8")

    monkeypatch.setattr("src.aeis.io.resolvers.PROJECT_ROOT", project_root)

    resolved = resolve_dataset_path(
        processed="aec/house_candidate_results.csv",
        interim="aec/house_candidate_results_normalised.csv",
        reference=None,
    )

    assert resolved == processed


def test_resolve_dataset_path_falls_back_to_interim(tmp_path, monkeypatch):
    project_root = tmp_path
    interim = project_root / "data" / "interim" / "aph" / "current_members_normalised.csv"
    interim.parent.mkdir(parents=True, exist_ok=True)
    interim.write_text("x\n1\n", encoding="utf-8")

    monkeypatch.setattr("src.aeis.io.resolvers.PROJECT_ROOT", project_root)

    resolved = resolve_dataset_path(
        processed="aph/current_members.csv",
        interim="aph/current_members_normalised.csv",
        reference=None,
    )

    assert resolved == interim
