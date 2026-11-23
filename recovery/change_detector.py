from __future__ import annotations

import hashlib
from typing import Any


def fingerprint(snapshot: dict[str, Any]) -> str:
    material = "\n".join([
        str(snapshot.get("url", "")),
        str(snapshot.get("title", "")),
        str(snapshot.get("visible_text", "")),
        str(snapshot.get("interactive_fingerprint", "")),
        str(snapshot.get("visual_fingerprint", "")),
    ])
    return hashlib.sha256(material.encode("utf-8")).hexdigest()[:20]


def diff(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    changes: list[str] = []
    for field, label in (
        ("url", "URL"),
        ("title", "título"),
        ("visible_text", "texto visível"),
        ("interactive_fingerprint", "controles/estados de interação"),
        ("visual_fingerprint", "estado visual/estrutura visual"),
    ):
        if before.get(field) != after.get(field):
            changes.append(f"{label} alterada" if field == "url" else f"{label} alterado")

    bmsg, amsg = set(before.get("messages", [])), set(after.get("messages", []))
    added, removed = sorted(amsg - bmsg), sorted(bmsg - amsg)
    if added:
        changes.append("novas mensagens: " + " | ".join(added[:8]))
    if removed:
        changes.append("mensagens removidas: " + " | ".join(removed[:8]))

    def keyed(items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
        return {str(x.get("key")): x for x in items if x.get("key")}

    b, a = keyed(before.get("controls", [])), keyed(after.get("controls", []))
    added_controls = [a[k] for k in a.keys() - b.keys()]
    removed_controls = [b[k] for k in b.keys() - a.keys()]

    state_changes = []
    for key in a.keys() & b.keys():
        for field in ("visible", "enabled", "disabled", "required", "checked", "selected", "value"):
            if b[key].get(field) != a[key].get(field):
                state_changes.append({
                    "key": key,
                    "field": field,
                    "before": b[key].get(field),
                    "after": a[key].get(field),
                })

    if added_controls:
        changes.append(f"{len(added_controls)} controle(s) apareceu(ram)")
    if removed_controls:
        changes.append(f"{len(removed_controls)} controle(s) desapareceu(ram)")
    if state_changes:
        changes.append(f"{len(state_changes)} estado(s) de controle alterado(s)")

    return {
        "changed": bool(changes),
        "changes": changes,
        "messages_added": added,
        "messages_removed": removed,
        "controls_added": added_controls,
        "controls_removed": removed_controls,
        "control_state_changes": state_changes,
    }
