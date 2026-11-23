from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class InputVariant:
    label: str
    value: str
    reason: str


def variants_for(control: dict[str, Any], cap: int = 6) -> list[InputVariant]:
    typ = str(control.get("type") or "text").lower()
    name = " ".join(str(control.get(k) or "") for k in ("label", "name", "placeholder", "aria_label")).lower()
    values: list[InputVariant] = [InputVariant("vazio", "", "campo sem valor")]
    if typ == "email" or "email" in name:
        values += [InputVariant("email inválido", "teste@", "formato incompleto"), InputVariant("email válido", "ambols.test@example.com", "formato válido")]
    elif typ == "number" or "quantity" in name or "quant" in name:
        values += [InputVariant("zero", "0", "valor limite"), InputVariant("negativo", "-1", "valor negativo"), InputVariant("válido", "1", "valor positivo")]
        if _int(control.get("min")) is not None: values.append(InputVariant("abaixo do mínimo", str(_int(control["min"]) - 1), "abaixo de min"))
        if _int(control.get("max")) is not None: values.append(InputVariant("acima do máximo", str(_int(control["max"]) + 1), "acima de max"))
    elif typ == "password" or "password" in name or "senha" in name:
        values += [InputVariant("curta", "a", "valor curto"), InputVariant("válida", "Ambols@Teste123!", "valor plausível")]
    elif "search" in name or "pesquisa" in name or "buscar" in name:
        values += [InputVariant("existente", "Apple", "produto conhecido"), InputVariant("inexistente", "AMBOLS-NAO-EXISTE", "termo sem correspondência")]
    elif "url" in name:
        values += [InputVariant("inválida", "not-a-url", "formato inválido"), InputVariant("válida", "https://example.com", "formato válido")]
    elif typ != "file":
        values += [InputVariant("curto", "A", "texto mínimo"), InputVariant("texto", "AMBOLS teste", "texto comum")]
    minlength, maxlength = _int(control.get("minlength")), _int(control.get("maxlength"))
    if minlength is not None: values.append(InputVariant("abaixo do mínimo", "a" * max(0, minlength - 1), "abaixo de minlength"))
    if maxlength is not None: values.append(InputVariant("limite máximo", "A" * maxlength, "no maxlength"))
    return _dedupe(values, cap)


def _int(value: Any) -> int | None:
    try: return int(value) if value not in (None, "") else None
    except (TypeError, ValueError): return None


def _dedupe(items: list[InputVariant], cap: int) -> list[InputVariant]:
    seen: set[str] = set()
    out: list[InputVariant] = []
    for item in items:
        if item.value in seen: continue
        seen.add(item.value)
        out.append(item)
        if len(out) >= cap: break
    return out
