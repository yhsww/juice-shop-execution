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

## Catálogo de cenários

O catálogo contém 78 cenários definidos nos domínios ADM, CAR, CAT, CHK, IDT e PER. A existência no inventário não significa que o cenário já tenha sido validado. Somente a execução real pode produzir resultado PASSED.

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

## Sem IA

O projeto não usa LLM, RAG, embeddings, ChromaDB, APIs de IA ou chaves de provedores. A execução usa regras determinísticas e observação da interface.