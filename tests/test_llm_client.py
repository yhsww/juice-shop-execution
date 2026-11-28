import json

import pytest

from reporting.llm import client

VALID = {
    "flow": "f", "precondition": "p", "observed_result": "o",
    "messages": ["m"], "data": "d",
    "steps": [{"number": 1, "action": "a", "data": "d", "response": "r"}],
}
PAYLOAD = {"catalog": {}, "execution": {}}


def _fake(responses, calls):
    def fake_request(**kwargs):
        calls.append(kwargs["use_schema"])
        return responses.pop(0)
    return fake_request


def test_openai_compatible_returns_parsed_dict(monkeypatch):
    calls = []
    fenced = "```json\n" + json.dumps(VALID) + "\n```"
    monkeypatch.setattr(client, "_request_openai_compatible", _fake([fenced], calls))
    result = client._humanize_openai_compatible(PAYLOAD, "openai", "k", "u", "m")
    assert result == VALID
    assert calls == [True]


def test_openai_compatible_retries_without_schema(monkeypatch):
    calls = []
    monkeypatch.setattr(client, "_request_openai_compatible",
                        _fake(["desculpe, não sei", json.dumps(VALID)], calls))
    assert client._humanize_openai_compatible(PAYLOAD, "groq", "k", "u", "m") == VALID
    assert calls == [True, False]


def test_openai_compatible_raises_controlled_error(monkeypatch):
    calls = []
    monkeypatch.setattr(client, "_request_openai_compatible", _fake(["x", "y"], calls))
    with pytest.raises(client.LLMHumanizerError, match="não retornou JSON válido"):
        client._humanize_openai_compatible(PAYLOAD, "gemini", "k", "u", "m")
