from __future__ import annotations

import json
from pathlib import Path

def build_stage1_report(result: dict) -> str:
    lines = ['# Engenharia reversa — Etapa 1', '', '**Método:** execução observável da interface do Juice Shop com captura de estados, transições e evidências de rede.', '', '## Comportamentos observados', '', '| ID | Tipo | Ação | Comportamento observado |', '|---|---|---|---|']
    for item in result.get('behaviors', []):
        description = ' '.join(str(item.get('description') or '').split()).replace('|', '\\|')
        lines.append(f"| {item.get('behavior_id','')} | {item.get('type','')} | {item.get('action_id','')} | {description[:1200]} |")
    lines.extend(['', '## Estados observados', '', '| Estado | URL | Título |', '|---|---|---|'])
    for state in result.get('states', []):
        lines.append(f"| {state.get('state_id','')} | {state.get('url','')} | {state.get('title','')} |")
    lines.extend(['', '## Transições', '', '| ID | Origem | Destino | Ação | Evidência |', '|---|---|---|---|---|'])
    for item in result.get('transitions', []):
        evidence = ' '.join(str(item.get('description') or '').split()).replace('|', '\\|')
        lines.append(f"| {item.get('transition_id','')} | {item.get('from_state','')} | {item.get('to_state','')} | {item.get('action','')} | {evidence[:800]} |")
    lines.extend(['', '## Rastreabilidade e limites', '', 'Os comportamentos acima são derivados exclusivamente de observações registradas durante a execução. Tráfego HTTP é evidência técnica complementar e não é convertido, isoladamente, em requisito. Esta etapa não produz END, COMP ou REQ.', ''])
    return '\n'.join(lines)

def save_stage1_report(output_dir: Path, result: dict) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / 'ETAPA_1.md').write_text(build_stage1_report(result), encoding='utf-8')
    (output_dir / 'ETAPA_1.json').write_text(json.dumps({'stage': 'ETAPA_1', 'behaviors': result.get('behaviors', []), 'states': result.get('states', []), 'transitions': result.get('transitions', []), 'network_summary': result.get('network_summary', {})}, ensure_ascii=False, indent=2), encoding='utf-8')