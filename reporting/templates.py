SCENARIO_SHEET = """# Ficha de Cenário

**ID do cenário:** {id}
**Domínio:** {domain}
**Nome do cenário:** {name}
**Ator:** {actor}
**Fluxo:** {flow}

## Pré-condição (estado inicial)

{precondition}

## Descrição do cenário

{description}

## Resultado observado (mudança de estado)

{result}

## Mensagens exibidas ao usuário

{messages}

## Dados manipulados

{data}

## Coerente com loja de sucos?

{coherent}

## Justificativa

{justification}

## Descrição funcional do cenário

{requirement}

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
{steps}
"""

DOMAIN_SHEET = """# Relatório do domínio {domain}

**Cenários executados:** {scenario_count}
**Cenários aprovados:** {passed_count}
**Status:** {status}

## Cenários

| ID | Cenário | Status | Comportamento observado |
|---|---|---|---|
{scenarios}

## Mensagens observadas

{messages}

## Rastreabilidade

Os comportamentos descritos neste relatório são derivados das evidências registradas
durante a execução dos cenários da Etapa 1. Não são criados artefatos END, COMP ou REQ
nesta etapa.
"""
