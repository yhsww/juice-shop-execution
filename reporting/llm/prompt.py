from __future__ import annotations

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

Retorne exatamente a estrutura solicitada pelo schema.
""";

export const HUMANIZER_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    flow: { type: "string" },
    precondition: { type: "string" },
    observed_result: { type: "string" },
    messages: {
      type: "array",
      items: { type: "string" }
    },
    data: { type: "string" },
    steps: {
      type: "array",
      items: {
        type: "object",
        additionalProperties: false,
        properties: {
          number: { type: "integer" },
          action: { type: "string" },
          data: { type: "string" },
          response: { type: "string" }
        },
        required: ["number", "action", "data", "response"]
      }
    }
  },
  required: [
    "flow",
    "precondition",
    "observed_result",
    "messages",
    "data",
    "steps"
  ]
};

export function buildInput(payload: Record<string, unknown>): string {
  return [
    "Transforme as evidências abaixo em documentação funcional.",
    "",
    "CATÁLOGO DO CENÁRIO:",
    JSON.stringify(payload.catalog, null, 2),
    "",
    "EVIDÊNCIAS DA EXECUÇÃO:",
    JSON.stringify(payload.execution, null, 2),
  ].join("\n");
}
