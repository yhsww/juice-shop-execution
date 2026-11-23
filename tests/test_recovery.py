from automation.observer import UIState
from recovery.behavior import extract_behaviors
from recovery.discover import _candidate_requirements
from recovery.state_model import state_fingerprint, transition

def test_candidate_requirements_are_evidence_backed():
    states = [{'url': 'http://127.0.0.1:3000/#/login', 'controls': ['button:login::']}]
    transitions = [{'from_route': '/#/login', 'to_route': '/#/register', 'changed': True}]
    requirements = _candidate_requirements(states, transitions)
    assert requirements
    assert all(item['evidence'] for item in requirements)
    assert all(item['source'] in {'ui-observation', 'ui-transition'} for item in requirements)

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