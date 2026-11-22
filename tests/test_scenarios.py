from pathlib import Path

from automation.runner import load_scenarios


def test_scenario_inventory_is_complete_and_unique():
    scenarios = load_scenarios(Path(__file__).resolve().parents[1] / "scenarios")
    ids = [scenario["id"] for scenario in scenarios]

    assert len(scenarios) == 69
    assert len(ids) == len(set(ids))

    domains = {scenario["domain"] for scenario in scenarios}
    assert {"ADM", "CAR", "CAT", "CHK", "IDT"} <= domains


def test_scenarios_have_manual_report_fields():
    scenarios = load_scenarios(Path(__file__).resolve().parents[1] / "scenarios")

    required = {"id", "domain", "name", "actor", "flow", "precondition", "data"}
    for scenario in scenarios:
        assert required <= scenario.keys()
        assert scenario["actions"]
