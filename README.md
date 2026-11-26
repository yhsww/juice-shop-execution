# Juice Shop Execution

Automação de testes funcionais do **OWASP Juice Shop** usando a interface real da aplicação, Playwright, Docker e geração de evidências e relatórios.

## Objetivo

O projeto executa cenários funcionais de forma reproduzível e rastreável.

O fluxo principal é:

```text
Cenário
   ↓
Playwright + interface real
   ↓
Evidências JSON + screenshots
   ↓
Relatório Markdown / DOCX
   ↓
Humanização opcional com LLM
```

A LLM atua somente na documentação. **O resultado do teste é determinado pelo executor e pelas evidências reais.**

## Status atual

A suíte principal contém **72 cenários**:

| Domínio | Cenários |
|---|---:|
| ADM | 3 |
| CAR | 7 |
| CAT | 17 |
| CHK | 28 |
| IDT | 17 |
| **Total** | **72** |

A implementação consolidada está na branch `main`.

## Tecnologias

- Python 3.10+
- Playwright
- Chromium
- Docker / Docker Compose
- OWASP Juice Shop
- pytest
- python-dotenv
- python-docx
- OpenAI SDK — usado também para provedores compatíveis com a API OpenAI
- Anthropic SDK — suporte opcional ao Claude

## Estrutura

```text
juice-shop-execution/
├── automation/              # Executor e ações funcionais
├── config/                  # Configurações de ambiente
├── reporting/               # Evidências, relatórios e humanização
│   └── llm/                 # Cliente e prompt da LLM
├── scenarios/               # Catálogo dos 72 cenários
├── tests/                   # Testes do projeto
├── juice-shop/              # Docker Compose do ambiente alvo
├── reports/
│   ├── executions/          # Evidências JSON e screenshots
│   ├── final/               # Relatórios Markdown
│   ├── humanized/           # Cache da documentação humanizada
│   └── docx/                # DOCX gerados
├── screenshots/             # Diretório reservado para evidências visuais
├── .env.example             # Modelo de configuração
├── requirements.txt
├── run.py                   # Ponto de entrada
└── README.md
```

## Requisitos

Instale:

- Python 3.10 ou superior;
- Docker Desktop no Windows/macOS ou Docker Engine + Compose v2 no Linux;
- Git.

No Windows, PowerShell é recomendado.

## Instalação

Clone o projeto:

```powershell
git clone https://github.com/yhsww/juice-shop-execution.git
cd juice-shop-execution
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

Instale o Chromium:

```powershell
python -m playwright install chromium
```

Crie o arquivo de ambiente:

```powershell
Copy-Item .env.example .env
```

Edite `.env` e informe as configurações locais necessárias.

**Nunca versione o arquivo `.env` nem chaves de API.**

## Configuração

As principais variáveis do Juice Shop são:

```env
JUICE_SHOP_BASE_URL=http://127.0.0.1:3000
JUICE_SHOP_HEADLESS=false
JUICE_SHOP_ACTION_TIMEOUT_MS=10000
JUICE_SHOP_NAVIGATION_TIMEOUT_MS=15000
JUICE_SHOP_SCENARIO_TIMEOUT_SECONDS=180
JUICE_SHOP_MAX_STEPS=30
```

O projeto utiliza por padrão:

- usuário de teste para os cenários de identidade;
- credenciais administrativas da instância local do Juice Shop;
- screenshots e evidências em `reports/executions/`.

## LLM para documentação

A humanização é opcional e não participa da aprovação dos cenários.

O provedor recomendado atualmente é **Gemini**, principalmente porque o humanizador envia as screenshots ao modelo para análise multimodal.

Configuração:

```env
REPORTING_LLM_PROVIDER=gemini

GEMINI_API_KEY=
GEMINI_API_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
GEMINI_LLM_MODEL=gemini-3.5-flash-lite
```

Também existe suporte configurável para:

- Groq;
- OpenAI;
- Kimi;
- Claude.

As chaves e os modelos devem ser configurados no `.env`.

### Como a LLM recebe as evidências

```text
Execução real
    ↓
JSON de evidências
    ↓
Normalização dos dados funcionais
    ↓
Screenshots PNG + evidências textuais
    ↓
Gemini multimodal
    ↓
JSON estruturado
    ↓
DOCX
```

As screenshots são enviadas como imagens para o Gemini. O prompt exige que o modelo analise visualmente os elementos realmente visíveis, incluindo:

- produtos;
- imagens dos produtos;
- preços;
- quantidades;
- botões;
- campos;
- títulos;
- menus;
- cartões;
- mensagens;
- alertas;
- resultados de pesquisa;
- mudanças de estado entre screenshots.

A LLM não pode inventar informações que não estejam nas evidências.

## Executando os cenários

### Um cenário

```powershell
python run.py --start-app --scenario CEN-CAR-03
```

### Um domínio

```powershell
python run.py --start-app --domain CHK
```

### Mais de um domínio

```powershell
python run.py --start-app --domain CHK --domain IDT
```

### Suíte completa

```powershell
python run.py --start-app --all
```

### Iniciar e encerrar o Docker automaticamente

```powershell
python run.py --start-app --all --stop-app
```

Se o Juice Shop já estiver rodando em `http://127.0.0.1:3000`, não é necessário usar `--start-app`.

## Docker

Para iniciar manualmente:

```powershell
docker compose -f juice-shop/docker-compose.yml up -d
```

Verificar:

```powershell
docker compose -f juice-shop/docker-compose.yml ps
```

Logs:

```powershell
docker compose -f juice-shop/docker-compose.yml logs -f
```

Encerrar:

```powershell
docker compose -f juice-shop/docker-compose.yml down
```

A aplicação é vinculada localmente em `127.0.0.1`.

## Evidências

Cada execução gera evidências estruturadas em:

```text
reports/executions/
```

As evidências podem conter:

- ID do cenário;
- status;
- ação realizada;
- descrição funcional da ação;
- dados utilizados;
- estado visual antes e depois;
- resultado observado;
- mensagens;
- URL;
- screenshot;
- informações de validação.

As screenshots são capturadas durante as etapas e utilizadas também pelo humanizador multimodal.

## Humanização de um cenário

Depois que o cenário foi executado, gere a documentação humanizada:

```powershell
python -m reporting.humanizer --scenario CEN-CAR-03 --force
```

O resultado fica em:

```text
reports/humanized/CEN-CAR-03.json
```

Para humanizar todos os cenários que possuem evidência:

```powershell
python -m reporting.humanizer --all --force
```

### Por que usar `--force`

Os arquivos em `reports/humanized/` funcionam como cache. O `--force` força uma nova chamada à LLM e é recomendado depois de alterar o prompt ou a forma de preparação das evidências.

## Relatórios DOCX

A estrutura do DOCX é fixa e segue a ficha definida para o projeto.

Cada cenário contém:

1. **Ficha de Ambiente**
2. **Guia de Domínio**
3. **Ficha de Cenário**
4. **Passos Executados**
5. Screenshots vinculadas às evidências dos passos

A ficha de cenário utiliza:

- ID do cenário;
- domínio;
- nome;
- ator;
- fluxo;
- pré-condição;
- resultado observado;
- mensagens;
- dados manipulados;
- coerência com a loja de sucos;
- justificativa;
- requisito candidato;
- tabela de ações, dados e respostas da interface.

### Gerar DOCX com humanização automática

```powershell
python -m reporting.docx_generator --humanize auto
```

### Exigir LLM

```powershell
python -m reporting.docx_generator --humanize llm
```

### Gerar sem LLM

```powershell
python -m reporting.docx_generator --humanize deterministic
```

Os arquivos são gerados em:

```text
reports/docx/
```

Os DOCX e os arquivos humanizados são artefatos gerados e não são versionados.

## Catálogo de cenários

O catálogo está em:

```text
scenarios/scenarios.json
```

Cada cenário possui informações como:

- identificador;
- domínio;
- nome;
- ator;
- fluxo;
- pré-condição;
- ações;
- dados;
- comportamento esperado;
- validação.

O catálogo é separado do executor para permitir evolução dos cenários sem acoplar cada caso ao código do motor.

## Princípios de engenharia

### Evidência antes da expectativa

O executor deve validar o comportamento real da aplicação. O catálogo descreve o que deve acontecer; a evidência registra o que aconteceu.

### Correções genéricas

Correções no executor devem resolver padrões de comportamento da aplicação, e não criar regras específicas para um único cenário.

### Sem mascaramento de falhas

Timeouts, exceções ou ações alternativas não devem transformar uma falha funcional em `PASSED`.

### Separação entre execução e documentação

O executor produz as evidências. O humanizador apenas transforma essas evidências em documentação legível.

```text
Executor
   ↓
Evidência
   ↓
Humanizador
   ↓
DOCX
```

Uma falha na LLM não deve alterar o resultado real da execução.

### Rastreabilidade

A documentação deve permitir relacionar:

```text
DOCX
 ↓
JSON humanizado
 ↓
JSON da execução
 ↓
ações e screenshots reais
```

## Segurança

O OWASP Juice Shop é uma aplicação propositalmente vulnerável.

Execute-o somente em ambiente controlado.

Não exponha o Juice Shop diretamente à Internet ou a redes não autorizadas.

Nunca envie para o Git:

- `.env`;
- chaves de API;
- tokens;
- credenciais reais;
- evidências contendo informações sensíveis.

## Manutenção

A branch oficial é:

```text
main
```

Antes de uma alteração:

```powershell
git pull --ff-only origin main
git status
```

Depois de alterar o código:

```powershell
git status
```

Para validar a suíte:

```powershell
python run.py --start-app --all
```

Para validar somente a documentação após mudanças no reporting, prefira primeiro um cenário:

```powershell
python -m reporting.humanizer --scenario CEN-CAR-03 --force
```

Isso permite verificar a qualidade da humanização sem executar novamente toda a suíte.

## OWASP Juice Shop

Aplicação alvo:

https://github.com/juice-shop/juice-shop
