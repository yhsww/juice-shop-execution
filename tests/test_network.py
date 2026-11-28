import json

from automation.network import (
    NetworkRecorder,
    assign_step,
    is_api_call,
    redact,
    redact_query,
    redact_text,
)

BASE = "http://127.0.0.1:3000"


def test_redact_masks_credentials_and_card_numbers():
    payload = {
        "email": "cliente@example.com",
        "password": "Teste@12345",
        "passwordRepeat": "Teste@12345",
        "securityAnswer": "a",
        "authentication": {"token": "eyJ...", "bid": 7},
        "cardNum": 4000000000000002,
        "items": [{"quantity": 2}],
    }
    out = redact(payload)
    assert out["email"] == "cliente@example.com"
    assert out["password"] == out["passwordRepeat"] == out["securityAnswer"] == "***"
    assert out["authentication"] == "***"
    assert out["cardNum"] == "****0002"
    assert out["items"] == [{"quantity": 2}]


def test_redact_text_keeps_non_json_and_truncates():
    assert json.loads(redact_text('{"password": "x", "q": 1}')) == {"password": "***", "q": 1}
    assert redact_text("plain") == "plain"
    assert len(redact_text("x" * 5000)) == 2000


def test_change_password_query_is_masked():
    path, query = redact_query(f"{BASE}/rest/user/change-password?current=a&new=b&repeat=b")
    assert path == "/rest/user/change-password"
    assert {item["value"] for item in query} == {"***"}


def test_only_api_calls_are_recorded():
    assert is_api_call(f"{BASE}/rest/products/search?q=", "xhr", BASE)
    assert is_api_call(f"{BASE}/api/BasketItems/", "fetch", BASE)
    assert not is_api_call(f"{BASE}/assets/public/images/x.png", "image", BASE)
    assert not is_api_call(f"{BASE}/main.js", "script", BASE)
    assert not is_api_call("https://example.org/api/x", "fetch", BASE)


def test_requests_are_assigned_to_the_step_that_triggered_them():
    windows = [(1, 100.0, 101.0), (2, 102.0, 103.0)]
    assert assign_step(99.0, windows) == 0      # pré-condição
    assert assign_step(100.5, windows) == 1
    assert assign_step(101.5, windows) == 1     # resposta tardia do passo 1
    assert assign_step(102.2, windows) == 2
    assert assign_step(200.0, windows) == 2


def test_build_produces_har_with_step_and_summary():
    recorder = NetworkRecorder(BASE)
    recorder.mark_step(1, 100.0, 101.0)
    recorder.entries.append({
        "_started": 100.5, "_failure": None,
        "request": {"method": "POST", "url": f"{BASE}/api/BasketItems/", "path": "/api/BasketItems/",
                    "queryString": [], "headers": [], "postData": None},
        "response": {"status": 200, "statusText": "OK", "content": {"mimeType": "application/json", "text": "{}"}},
    })
    har, per_step = recorder.build()
    assert har["log"]["version"] == "1.2"
    assert har["log"]["entries"][0]["_step"] == 1
    assert "postData" not in har["log"]["entries"][0]["request"]
    assert per_step == {1: ["POST /api/BasketItems/ -> 200"]}
