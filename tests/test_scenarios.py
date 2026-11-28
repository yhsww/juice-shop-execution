from pathlib import Path

from automation.runner import load_scenarios


def test_scenario_inventory_is_complete_and_unique():
    scenarios = load_scenarios(Path(__file__).resolve().parents[1] / "scenarios")
    ids = [scenario["id"] for scenario in scenarios]

    # 78 cenários-base (scenarios.json) + 62 complementares (scenarios_alternativos.json)
    assert len(scenarios) == 140
    assert len(ids) == len(set(ids))

    domains = {scenario["domain"] for scenario in scenarios}
    assert {"ADM", "CAR", "CAT", "CHK", "IDT", "PER"} <= domains


def test_scenarios_have_manual_report_fields():
    scenarios = load_scenarios(Path(__file__).resolve().parents[1] / "scenarios")

    required = {"id", "domain", "name", "actor", "flow", "precondition", "data"}
    for scenario in scenarios:
        assert required <= scenario.keys()
        assert scenario["actions"]


def test_alternative_scenarios_declare_access_state_and_flow_type():
    scenarios = load_scenarios(Path(__file__).resolve().parents[1] / "scenarios")
    alternatives = [s for s in scenarios if "flow_type" in s]

    assert len(alternatives) == 62
    for scenario in alternatives:
        assert scenario["auth"] in {"none", "customer", "admin"}
        assert scenario["expected"], scenario["id"]


def test_explicit_auth_mode_overrides_domain_heuristic():
    from automation.preconditions import needs_authentication

    # CHK/PER são autenticados pela heurística; "none" precisa vencer.
    assert needs_authentication({"domain": "CHK", "auth": "none", "actions": []}) is False
    assert needs_authentication({"domain": "PER", "auth": "none", "actions": []}) is False
    assert needs_authentication({"domain": "CAT", "auth": "customer", "actions": []}) is True
    # Sem o campo, o comportamento antigo é preservado.
    assert needs_authentication({"domain": "CHK", "precondition": "", "actions": []}) is True
    assert needs_authentication({"domain": "CAT", "precondition": "", "actions": [{"route": "/#/"}]}) is False


def test_reporting_loads_every_catalog_file():
    from reporting.docx_generator import load_scenarios as docx_load
    from reporting.humanizer import load_catalog

    folder = Path(__file__).resolve().parents[1] / "scenarios"
    assert len(docx_load(folder)) == len(load_catalog(folder)) == 140
