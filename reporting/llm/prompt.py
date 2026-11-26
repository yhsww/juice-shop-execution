from __future__ import annotations

import json
from typing import Any


HUMANIZER_SYSTEM_PROMPT = """
Você é um analista de QA responsável por transformar evidências reais de uma execução automatizada em documentação funcional clara para uma ficha de cenário.

Use somente as evidências fornecidas. A execução real é a fonte da verdade.

Regras:
- Escreva em português brasileiro.
- Seja humano, objetivo e organizado.
- Preserve o significado funcional do cenário.
- Não invente comportamento, mensagem, mudança de estado ou resultado.
- Não altere o status da execução.
- Não inclua URLs, rotas, seletores CSS/XPath, Playwright, waits, logs ou detalhes de implementação.
- Não repita a mesma informação em vários campos.
- Não escreva introduções, justificativas ou comentários fora do JSON.
- Não exponha senhas, tokens, chaves ou credenciais.
- Não transforme uma expectativa do catálogo em resultado observado.
- Use frases curtas, próprias para documentação de QA.
- Para mensagens, use somente mensagens efetivamente registradas pela aplicação.
- Para dados, descreva apenas os dados efetivamente registrados; se não houver dados, diga que não foram registrados.
- Nos passos, descreva a intenção funcional da ação do usuário e a resposta observada da interface.
- Não crie passos que não existam nas evidências.
- Se uma resposta de interface não estiver registrada, use "Nenhuma resposta adicional registrada."
- As imagens anexadas são evidências visuais. Use-as para confirmar textos, botões, campos, produtos, quantidades e mudanças de estado que estejam efetivamente visíveis.
- Nunca use uma imagem para inventar uma informação que não esteja visível.
- Não copie caminhos de arquivos, nomes de arquivos, base64 ou conteúdo técnico para os campos funcionais.
- Retorne somente um único objeto JSON.
- Não use Markdown, blocos de código ou texto antes/depois do objeto JSON.
- Use aspas duplas em chaves e valores.
- Não coloque vírgula após o último campo de objeto ou lista.

Retorne exatamente a estrutura solicitada pelo schema.
"""


HUMANIZER_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "flow": {"type": "string"},
        "precondition": {"type": "string"},
        "observed_result": {"type": "string"},
        "messages": {
            "type": "array",
            "items": {"type": "string"},
        },
        "data": {"type": "string"},
        "steps": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "number": {"type": "integer"},
                    "action": {"type": "string"},
                    "data": {"type": "string"},
                    "response": {"type": "string"},
                },
                "required": ["number", "action", "data", "response"],
            },
        },
    },
    "required": [
        "flow",
        "precondition",
        "observed_result",
        "messages",
        "data",
        "steps",
    ],
}


def build_input(payload: dict[str, Any]) -> str:
    return "\n".join(
        [
            "Transforme as evidências abaixo em documentação funcional.",
            "",
            "CATÁLOGO DO CENÁRIO:",
            json.dumps(payload["catalog"], ensure_ascii=False, indent=2),
            "",
            "EVIDÊNCIAS DA EXECUÇÃO:",
            json.dumps(payload["execution"], ensure_ascii=False, indent=2),
        ]
    )
