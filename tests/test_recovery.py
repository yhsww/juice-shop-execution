from recovery.discover import _candidate_requirements


def test_candidate_requirements_are_evidence_backed():
    states = [{"url": "http://127.0.0.1:3000/#/login", "controls": ["button:login::"]}]
    transitions = [{"from_route": "/#/login", "to_route": "/#/register", "changed": True}]
    requirements = _candidate_requirements(states, transitions)
    assert requirements
    assert all(item["evidence"] for item in requirements)
    assert all(item["source"] in {"ui-observation", "ui-transition"} for item in requirements)
