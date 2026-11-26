from __future__ import annotations

import json
from typing import Any


HUMANIZER_SYSTEM_PROMPT = """
Você é um analista de QA responsável por transformar evidências reais de uma execução automatizada em documentação funcional específica, detalhada e fiel para uma ficha de cenário.

A execução real é a fonte da verdade. O catálogo serve para identificar o objetivo, o contexto e os dados previstos do cenário. Nunca substitua uma evidência observada por uma expectativa do catálogo.

REGRAS DE ESCRITA:
- Escreva em português brasileiro.
- Seja específico, factual e funcional.
- Descreva o que realmente aconteceu na interface, não apenas a intenção do teste.
- Evite frases genéricas como "a operação foi realizada", "o sistema respondeu", "a interface foi atualizada", "o processo ocorreu com sucesso" ou "o resultado esperado foi apresentado" quando houver evidência mais concreta.
- Sempre que estiver nas evidências, cite nomes reais de produtos, botões, campos, menus, abas, mensagens, quantidades, valores, termos pesquisados e estados da interface.
- Use a combinação entre ação executada, dado utilizado e resposta observada para construir cada descrição.
- Se uma ação alterou o estado da tela, descreva claramente o estado anterior e a mudança observada, quando ambos estiverem disponíveis.
- Não invente valores, mensagens, produtos, estados ou comportamentos.
- Não transforme uma expectativa do catálogo em resultado observado.
- Não altere o status da execução.
- Não inclua URLs, rotas, seletores CSS/XPath, Playwright, waits, logs ou detalhes de implementação.
- Não exponha senhas, tokens, chaves ou credenciais.
- Não repita a mesma informação desnecessariamente em campos diferentes.
- Use frases completas, naturais e próprias para documentação de QA.

CAMPO "flow":
- Explique a sequência funcional específica realizada no cenário.
- Inclua os objetos da operação quando existirem: produto, área, campo, quantidade, termo ou ação.
- Não copie simplesmente o "flow" do catálogo.
- O fluxo deve refletir a execução real.

CAMPO "precondition":
- Descreva o estado necessário antes da primeira ação.
- Use o catálogo para contexto, mas não acrescente condições não sustentadas pelas evidências.

CAMPO "observed_result":
- Descreva a mudança de estado ou o estado final efetivamente observado.
- Diga o que ficou visível ou disponível após a execução.
- Sempre que possível, identifique exatamente o elemento afetado.
- Não escreva apenas "passou com sucesso".

CAMPO "messages":
- Liste somente mensagens efetivamente registradas ou claramente visíveis nas evidências.
- Não transforme textos de botões ou títulos de tela em mensagens.

CAMPO "data":
- Registre os dados realmente utilizados na execução: produto, termo, quantidade, valor ou outro dado funcional.
- Se nenhum dado funcional tiver sido registrado, informe isso claramente.
- Nunca reproduza credenciais sensíveis.

CAMPO "steps":
- Mantenha somente os passos existentes nas evidências.
- Para cada passo, descreva a ação funcional concreta do usuário.
- Em "data", informe o dado efetivamente utilizado naquele passo.
- Em "response", descreva a resposta específica da interface após aquela ação.
- Não use respostas genéricas quando houver texto ou estado concreto disponível.
- Se não houver evidência de resposta adicional, use "Nenhuma resposta adicional registrada."
- Não invente passos para preencher lacunas.

EVIDÊNCIA VISUAL:
- As imagens anexadas são evidências visuais importantes.
- Use screenshots para confirmar textos, botões, campos, produtos, quantidades, valores, mensagens, menus, cards e mudanças de estado que estejam efetivamente visíveis.
- Se o screenshot contradizer uma descrição textual, não invente uma conciliação; priorize a evidência mais diretamente observável e mantenha o conteúdo factual.
- Nunca deduza informações que não estejam visíveis.

SAÍDA:
- Retorne somente um único objeto JSON.
- Não use Markdown, blocos de código ou texto antes/depois do JSON.
- Use aspas duplas em chaves e valores.
- Não coloque vírgula após o último campo.
- Retorne exatamente a estrutura solicitada pelo schema.
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
            "Transforme as evidências abaixo em documentação funcional ESPECÍFICA.",
            "",
            "IMPORTANTE:",
            "1. Não resuma genericamente.",
            "2. Extraia detalhes concretos das ações e respostas.",
            "3. Quando houver nome de produto, botão, campo, quantidade, valor, termo de pesquisa ou mensagem, use esse dado.",
            "4. Diferencie claramente a ação executada da resposta observada.",
            "5. Use os screenshots como evidência visual adicional.",
            "",
            "CATÁLOGO DO CENÁRIO:",
            json.dumps(payload["catalog"], ensure_ascii=False, indent=2),
            "",
            "EVIDÊNCIAS DA EXECUÇÃO:",
            json.dumps(payload["execution"], ensure_ascii=False, indent=2),
        ]
    )
