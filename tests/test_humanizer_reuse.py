import json

from reporting import humanizer

SCENARIO = {"id": "CEN-X-01", "name": "n", "actor": "a", "flow": "f", "precondition": "p", "data": "d"}
EXECUTION = {"scenario_id": "CEN-X-01", "status": "PASSED", "steps": []}
CONTENT = {"flow": "texto antigo", "precondition": "p", "observed_result": "o",
           "messages": [], "data": "d", "steps": []}


def _seed(tmp_path, fingerprint="outro-modelo"):
    (tmp_path / "CEN-X-01.json").write_text(
        json.dumps({"scenario_id": "CEN-X-01", "fingerprint": fingerprint, "content": CONTENT}),
        encoding="utf-8",
    )


def _no_llm(monkeypatch):
    calls = []
    monkeypatch.setattr(humanizer, "humanize", lambda payload: calls.append(1) or dict(CONTENT, flow="novo"))
    return calls


def test_existing_text_is_reused_even_if_model_changed(tmp_path, monkeypatch):
    _seed(tmp_path)
    calls = _no_llm(monkeypatch)
    out = humanizer.humanize_scenario(SCENARIO, EXECUTION, tmp_path, executions_dir=tmp_path)
    assert out["flow"] == "texto antigo"
    assert calls == []


def test_refresh_stale_regenerates_on_fingerprint_change(tmp_path, monkeypatch):
    _seed(tmp_path)
    calls = _no_llm(monkeypatch)
    humanizer.humanize_scenario(SCENARIO, EXECUTION, tmp_path, executions_dir=tmp_path, reuse_existing=False)
    assert calls == [1]


def test_missing_or_corrupt_file_is_generated(tmp_path, monkeypatch):
    (tmp_path / "CEN-X-01.json").write_text("{corrompido", encoding="utf-8")
    calls = _no_llm(monkeypatch)
    humanizer.humanize_scenario(SCENARIO, EXECUTION, tmp_path, executions_dir=tmp_path)
    assert calls == [1]
