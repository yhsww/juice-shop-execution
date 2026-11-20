SCENARIO_SHEET = """# Ficha de Cenário

**ID do cenário:** {id}
**Domínio:** {domain}
**Nome do cenário:** {name}
**Ator:** {actor}
**Fluxo:** {flow}

## Pré-condição (estado inicial)

{precondition}

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

## Requisito candidato (opcional)

{requirement}

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
{steps}
"""
