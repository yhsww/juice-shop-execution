from automation.observer import UIState, meaningful_change


def test_url_change_is_meaningful():
    before = UIState("/#/", "Juice Shop", "home", "a")
    after = UIState("/#/login", "Juice Shop", "login", "a")
    assert meaningful_change(before, after)


def test_same_state_is_not_meaningful():
    state = UIState("/#/", "Juice Shop", "home", "a")
    assert not meaningful_change(state, state)
