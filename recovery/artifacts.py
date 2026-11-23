from __future__ import annotations

import json
from pathlib import Path

from automation.observer import UIState

def state_record(state: UIState) -> dict:
    return {'url': state.url, 'title': state.title, 'visible_text': state.visible_text, 'body_hash': state.body_hash, 'messages': list(state.messages), 'headings': list(state.headings), 'controls': list(state.controls)}

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')

def write_jsonl(path: Path, rows: list[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows), encoding='utf-8')

def route_key(url: str) -> str:
    marker = url.find('/#/')
    return url[marker:] if marker >= 0 else url

def evidence_index(*, states: list[dict], transitions: list[dict], behaviors: list[dict], network: list[dict]) -> dict:
    return {'stage': 'ETAPA_1', 'evidence_policy': {'ui_primary': True, 'network_supporting': True, 'expected_is_not_evidence': True, 'creates_end_comp_req': False}, 'counts': {'states': len(states), 'transitions': len(transitions), 'behaviors': len(behaviors), 'network_events': len(network)}, 'states': states, 'transitions': transitions, 'behaviors': behaviors}