from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import json

from automation.observer import UIState


def state_record(state: UIState) -> dict:
    return {
        "url": state.url,
        "title": state.title,
        "visible_text": state.visible_text,
        "body_hash": state.body_hash,
        "messages": list(state.messages),
        "headings": list(state.headings),
        "controls": list(state.controls),
    }


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def route_key(url: str) -> str:
    marker = url.find("/#/")
    return url[marker:] if marker >= 0 else url
