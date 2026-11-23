from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from automation.observer import UIState


@dataclass(frozen=True)
class StateTransition:
    transition_id: str
    from_state: str
    to_state: str
    action_id: str
    action: str
    description: str
    changed: bool
    evidence: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "transition_id": self.transition_id,
            "from_state": self.from_state,
            "to_state": self.to_state,
            "action_id": self.action_id,
            "action": self.action,
            "description": self.description,
            "changed": self.changed,
            "evidence": self.evidence,
        }


def state_fingerprint(state: UIState) -> str:
    payload = "\n".join([state.url, state.title, state.body_hash, *state.headings, *state.controls])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def transition(before: UIState, after: UIState, *, action_id: str, action: str,
               evidence: dict[str, Any] | None = None) -> StateTransition:
    from_id, to_id = state_fingerprint(before), state_fingerprint(after)
    return StateTransition(
        transition_id=f"TR-{from_id}-{to_id}", from_state=from_id, to_state=to_id,
        action_id=action_id, action=action, description=_describe(before, after),
        changed=from_id != to_id, evidence=evidence or {},
    )


def state_record(state: UIState, *, state_id: str | None = None) -> dict[str, Any]:
    return {
        "state_id": state_id or state_fingerprint(state), "url": state.url,
        "title": state.title, "visible_text": state.visible_text,
        "body_hash": state.body_hash, "messages": list(state.messages),
        "headings": list(state.headings), "controls": list(state.controls),
    }


def _describe(before: UIState, after: UIState) -> str:
    changes = []
    if before.url != after.url:
        changes.append(f"a URL mudou de {before.url} para {after.url}")
    new_headings = [x for x in after.headings if x not in set(before.headings)]
    if new_headings:
        changes.append("novos títulos visíveis: " + ", ".join(new_headings[:4]))
    new_messages = [x for x in after.messages if x not in set(before.messages)]
    if new_messages:
        changes.append("nova mensagem visível: " + " | ".join(new_messages[:4]))
    new_controls = [x for x in after.controls if x not in set(before.controls)]
    if new_controls:
        changes.append("novos controles observados: " + ", ".join(new_controls[:4]))
    if not changes and before.body_hash != after.body_hash:
        changes.append("o conteúdo visível da interface foi alterado")
    return "; ".join(changes) if changes else "Nenhuma mudança visual relevante detectada."
