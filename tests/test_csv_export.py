import csv

from reporting.csv_export import STEP_COLUMNS, SCENARIO_COLUMNS, build_rows, write_csv

SCENARIO = {"id": "CEN-CAR-02", "domain": "CAR", "name": "Adicionar; remover", "actor": "Cliente",
            "precondition": "p", "flow": "f", "data": "d"}


def test_rows_combine_catalog_execution_and_humanized_text(tmp_path):
    (tmp_path / "CEN-CAR-02.json").write_text(
        '{"status": "PASSED", "steps": [{"step": "1", "action": "CLICK", "success": true,'
        ' "network": ["POST /api/BasketItems/ -> 200"], "screenshot": "C:/x/CEN-CAR-02_step_01.png"}]}',
        encoding="utf-8",
    )
    humanized = tmp_path / "h"
    humanized.mkdir()
    (humanized / "CEN-CAR-02.json").write_text(
        '{"content": {"observed_result": "texto", "messages": ["a", "b"],'
        ' "steps": [{"number": 1, "action": "clicou", "data": "", "response": "ok"}]}}',
        encoding="utf-8",
    )
    scenarios, steps = build_rows([SCENARIO], tmp_path, humanized)
    assert scenarios[0]["status"] == "PASSED"
    assert scenarios[0]["mensagens"] == "a | b"
    assert scenarios[0]["requisicoes_api"] == "1"
    assert steps[0]["acao"] == "clicou"
    assert steps[0]["captura"] == "CEN-CAR-02_step_01.png"

    write_csv(tmp_path / "c.csv", SCENARIO_COLUMNS, scenarios)
    write_csv(tmp_path / "p.csv", STEP_COLUMNS, steps)
    raw = (tmp_path / "c.csv").read_bytes()
    assert raw.startswith(b"\xef\xbb\xbf")  # BOM para o Excel
    rows = list(csv.DictReader((tmp_path / "c.csv").open(encoding="utf-8-sig"), delimiter=";"))
    assert rows[0]["nome"] == "Adicionar; remover"  # ";" no texto não quebra a coluna
