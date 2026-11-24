from automation.observer import UIState
from recovery.behavior import extract_behaviors
from recovery.change_detector import diff
from recovery.data_generator import variants_for
from recovery.state_model import state_fingerprint, transition

def test_behavior_extraction_never_uses_expected_as_observed():
    behaviors = extract_behaviors(states=[], transitions=[], actions=[{'action_id': 'A-1', 'observed_result': 'Mensagem inválida exibida.', 'messages': ['Mensagem inválida'], 'expected': 'Login realizado com sucesso.'}])
    assert len(behaviors) == 1
    assert 'Login realizado' not in behaviors[0]['description']
    assert 'Mensagem inválida' in behaviors[0]['description']

def test_state_transition_is_evidence_backed():
    before = UIState(url='http://127.0.0.1:3000/#/login', title='Login', visible_text='Login', body_hash='a', headings=('Login',), controls=('button:login::',))
    after = UIState(url='http://127.0.0.1:3000/#/register', title='Register', visible_text='Register', body_hash='b', headings=('Register',), controls=('button:register::',))
    item = transition(before, after, action_id='A-1', action='CLICK')
    assert item.changed is True
    assert item.from_state == state_fingerprint(before)
    assert item.to_state == state_fingerprint(after)
    assert item.evidence == {}

def test_change_detector_captures_control_state_and_message_changes():
    before = {
        "url": "/#/register",
        "title": "Register",
        "visible_text": "Register",
        "messages": [],
        "controls": [{
            "key": "input|input|email",
            "enabled": True,
            "disabled": False,
            "required": True,
            "value": "",
        }],
        "interactive_fingerprint": "a",
        "visual_fingerprint": "a",
    }
    after = {
        **before,
        "visible_text": "Register Invalid email",
        "messages": ["Invalid email"],
        "controls": [{
            "key": "input|input|email",
            "enabled": False,
            "disabled": True,
            "required": True,
            "value": "x",
        }],
        "interactive_fingerprint": "b",
    }
    result = diff(before, after)
    assert result["changed"] is True
    assert "novas mensagens: Invalid email" in result["changes"]
    assert any(item["field"] in {"enabled", "disabled"} for item in result["control_state_changes"])


def test_input_variants_include_required_boundary_cases():
    variants = variants_for({
        "type": "number",
        "label": "Quantity",
        "min": "1",
        "max": "10",
    }, cap=6)
    values = {item.value for item in variants}
    assert "" in values
    assert "0" in values
    assert "-1" in values
    assert "1" in values


def test_control_target_is_semantic():
    from recovery.explorer import BehavioralExplorer

    target = BehavioralExplorer._action_target({
        "role": "input",
        "label": "Search",
        "name": "search",
        "placeholder": "Search...",
        "id": "search",
    })
    assert target == {
        "label": "Search",
        "name": "search",
        "placeholder": "Search...",
        "id": "search",
    }


def test_control_target_keeps_user_facing_role():
    from recovery.explorer import BehavioralExplorer

    target = BehavioralExplorer._action_target({
        "role": "button",
        "label": "Continue",
        "id": "continue",
    })
    assert target["role"] == "button"
    assert target["label"] == "Continue"
