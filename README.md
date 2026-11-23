# Juice Shop Execution

Automação determinística de cenários de teste no OWASP Juice Shop usando a interface real da aplicação.

## Organização dos repositórios

Este repositório reúne o executor dos testes e a configuração Docker usada para subir a aplicação sob teste:

- `automation/`, `scenarios/` e `reporting/`: automação, catálogo de cenários e relatórios.
- `juice-shop/`: configuração de execução local derivada de `https://github.com/yhsww/juice-shop`.
- `juice-shop/docker-compose.yml`: inicia a imagem `bkimminich/juice-shop:v20.3.0`, fixada para manter o ambiente reprodutível.

O diretório `juice-shop/` incorpora a configuração de ambiente Docker e scripts de inicialização do repositório separado. Não copia o código-fonte integral da aplicação: o serviço é fornecido pela imagem Docker versionada.

## Requisitos

- Python 3.10+ (recomendado 3.12)
- Docker Desktop no Windows/macOS ou Docker Engine + Docker Compose v2 no Linux
- Playwright Chromium

## Instalação

```powershell
pip install -r requirements.txt
python -m playwright install chromium
Copy-Item .env.example .env
```

## Execução

Para executar um cenário e iniciar o Docker automaticamente quando o serviço ainda não estiver disponível:

```powershell
python run.py --start-app --scenario CEN-IDT-01
```

Para executar um domínio inteiro e facilitar a investigação por área:

```powershell
python run.py --start-app --domain CHK
python run.py --start-app --domain IDT
```

É possível repetir `--domain` para executar mais de um domínio:

```powershell
python run.py --start-app --domain CHK --domain IDT
```

Para executar um cenário específico:

```powershell
python run.py --start-app --scenario CEN-CHK-03
```

Para iniciar o ambiente e executar todos os cenários cadastrados:

```powershell
python run.py --start-app --all
```

Para encerrar o container ao fim da execução:

```powershell
python run.py --start-app --all --stop-app
```

Se o serviço já estiver rodando em `http://127.0.0.1:3000`, o executor reutiliza essa instância e não sobe outra.

Também é possível controlar o container manualmente:

```powershell
docker compose -f juice-shop/docker-compose.yml up -d
docker compose -f juice-shop/docker-compose.yml ps
docker compose -f juice-shop/docker-compose.yml logs -f
docker compose -f juice-shop/docker-compose.yml down
```

## Engenharia reversa AMBOLS

Esta branch adiciona uma etapa determinística de exploração comportamental. Ela usa os cenários AMBOLS como guia, executa o fluxo real na interface e, a partir do estado observado, explora controles, entradas e interações adicionais para descobrir comportamentos e cenários alternativos.

Execução da exploração:

```powershell
python run.py --reverse-engineer --start-app
python run.py --reverse-engineer --start-app --recovery-domain CAT
python run.py --reverse-engineer --start-app --recovery-scenario CEN-CAT-01
```

Artefatos gerados em `reports/recovery/`:

- `ETAPA_1.md` e `ETAPA_1.json`: relatório consolidado da Etapa 1.
- `stage1-scenarios.json`: execução observacional por cenário.
- `behaviors.json`: comportamentos derivados das mudanças observadas.
- `discovered-scenarios.json`: caminhos alternativos descobertos.
- `evidence-index.json`: índice metodológico das evidências.

A abordagem é deliberadamente determinística e conservadora: o campo `expected` do catálogo não é tratado como evidência. O comportamento relatado precisa ser sustentado por observação da UI. Network/ZAP podem complementar a evidência, mas não substituem a observação da interface. Esta etapa não produz END, COMP ou REQ.

## Catálogo de cenários

O catálogo contém 69 cenários definidos nos domínios ADM, CAR, CAT, CHK e IDT. A existência no inventário não significa que o cenário já tenha sido validado. Somente a execução real pode produzir resultado PASSED.

| Domínio | Quantidade |
|---|---:|
| ADM | 3 |
| CAR | 7 |
| CAT | 17 |
| CHK | 28 |
| IDT | 17 |
| PER | 6 |
| **Total** | **78** |

## Princípio da automação

1. Verifica se o Juice Shop responde no endereço local.
2. Quando `--start-app` é informado, inicia o serviço a partir do Docker Compose incorporado.
3. Abre a aplicação com Playwright.
4. Observa o estado inicial, executa as ações e observa novamente a interface.
5. Valida mudanças observáveis, captura screenshots e registra evidências.
6. Gera uma Ficha de Cenário em Markdown e um registro JSON.

Resultados, mensagens e respostas da interface devem refletir o que foi observado. O sistema não deve inventar observações para completar um relatório.

## Segurança

O Juice Shop é intencionalmente vulnerável. A porta do container é vinculada somente a `127.0.0.1`. Não altere para exposição pública e utilize o ambiente apenas localmente ou em ambiente autorizado.

## Uso de IA na Etapa 1

A execução da Etapa 1 é determinística. Não depende de LLM para decidir o que foi observado, evitando que um modelo invente comportamentos ausentes da evidência. Modelos de IA podem ser usados posteriormente para revisão ou refinamento textual, mas a evidência primária permanece a execução real da UI.