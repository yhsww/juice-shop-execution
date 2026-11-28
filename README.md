# Juice Shop Execution

Automação de testes funcionais do **OWASP Juice Shop** com execução na interface real, coleta de evidências, humanização opcional por LLM e geração de relatórios DOCX.

## 1. Objetivo

O objetivo do projeto é executar uma suíte de cenários funcionais do OWASP Juice Shop de forma **reprodutível, rastreável e baseada em evidências reais**.

A automação não considera apenas o resultado esperado do catálogo: cada cenário é executado na aplicação, suas ações e respostas observadas são registradas e o status é definido pelo executor.

A LLM é usada na etapa de **documentação/humanização**. Ela não decide se um cenário passou ou falhou.

### Fluxo

```text
Catálogo de cenários
        ↓
Execução na aplicação real
        ↓
Playwright + Chromium
        ↓
JSON de evidências + screenshots
        ↓
Humanização opcional por LLM
        ↓
DOCX por domínio + relatório geral
```

## 2. Escopo atual

A suíte possui **140 cenários funcionais**: 78 cenários-base e 62 complementares, que cobrem fluxos alternativos e comportamentos incoerentes com uma loja de sucos.

| Domínio | Base | Complementares | Total |
|---|---:|---:|---:|
| ADM — Administração | 3 | 5 | 8 |
| CAR — Carrinho de Compras | 7 | 8 | 15 |
| CAT — Catálogo | 17 | 12 | 29 |
| CHK — Checkout e Pedidos | 28 | 16 | 44 |
| IDT — Gestão de Identidade e Usuários | 17 | 11 | 28 |
| PER — Perfil | 6 | 10 | 16 |
| **Total** | **78** | **62** | **140** |

Os catálogos estão em:

```text
scenarios/scenarios.json              # 78 cenários-base
scenarios/scenarios_alternativos.json # 62 cenários complementares (gerado)
```

O runner, o humanizador e o gerador de DOCX leem **todos** os `*.json` da pasta `scenarios/` (exceto os iniciados por `_`). Os cenários complementares são detalhados na seção 2.1.

### 2.1 Cenários complementares (fluxos alternativos)

O arquivo `scenarios/scenarios_alternativos.json` é gerado por `tools/gerar_cenarios_alternativos.py`. Edite o gerador e rode o comando abaixo; não edite o JSON à mão:

```powershell
python tools/gerar_cenarios_alternativos.py
```

O gerador também grava as fichas no template da Etapa 1 em `docs/fichas_cenarios_alternativos.md`.

Cada cenário complementar traz campos extras:

| Campo | Significado |
|---|---|
| `flow_type` | Principal, Alternativo (formulário incompleto, ação sem login, dados inválidos, atualização…), Incoerente com loja de sucos ou Lacuna |
| `base_scenario` | Cenário-base do qual o fluxo deriva |
| `auth` | Estado de acesso antes do cenário: `none` (limpa cookies e storage e não autentica), `customer` (cliente comum, mesmo no domínio ADM) ou `admin` |
| `expected_confidence` | `observado` (critério escrito a partir da interface v20.3.0), `alta` ou `confirmado` (hipótese inicial confirmada na execução) |
| `scope` / `note` | Limites de escopo (regra 5 do guia) e o que observar na execução |

Última execução completa (`python run.py --all`, banco do Juice Shop v20.3.0 recém-reiniciado, 2026-11-28): **140/140 aprovados**.

Sem o campo `auth`, a heurística antiga de autenticação continua valendo, então os 78 cenários-base não mudam de comportamento.

## 3. Tecnologias utilizadas

### Automação

- **Python 3.10+** — linguagem principal.
- **Playwright** — automação do navegador e interação com a interface real.
- **Chromium** — navegador utilizado pelo Playwright.
- **pytest** — testes unitários e validações da base do projeto.

### Aplicação e infraestrutura

- **OWASP Juice Shop** — aplicação utilizada como alvo dos testes funcionais.
- **Docker** — execução isolada da aplicação.
- **Docker Compose** — inicialização e gerenciamento do Juice Shop.

### Evidências e relatórios

- **JSON** — evidências estruturadas da execução.
- **Screenshots PNG** — evidência visual complementar.
- **python-docx** — geração dos relatórios DOCX.
- **Markdown** — artefatos textuais intermediários, quando aplicável.

### Humanização com IA

- **Anthropic SDK** — integração com Claude.
- **OpenAI SDK** — suporte a provedores compatíveis.
- **LLM** — interpretação e organização funcional das evidências para documentação.
- A configuração atual validada do projeto utiliza **Claude** com saída estruturada.

As dependências estão declaradas em `requirements.txt`.

## 4. Estrutura principal

```text
juice-shop-execution/
├── automation/              # Executor e ações funcionais
├── reporting/               # Evidências, humanização e relatórios
│   └── llm/                 # Cliente e prompts da LLM
├── scenarios/               # Catálogos (78 base + 62 complementares)
├── tools/                   # Gerador dos cenários complementares
├── docs/                    # Fichas geradas dos cenários complementares
├── tests/                   # Testes automatizados do projeto
├── juice-shop/              # Docker Compose da aplicação alvo
├── reports/
│   ├── executions/          # Evidências das execuções
│   └── docx/                # DOCX finais da entrega
├── .env.example             # Modelo de variáveis de ambiente
├── requirements.txt         # Dependências Python
├── run.py                   # Entrada principal da execução
└── README.md
```

## 5. Pré-requisitos

Instale:

- Python 3.10 ou superior;
- Git;
- Docker Desktop (Windows/macOS) ou Docker Engine + Docker Compose v2 (Linux).

No Windows, os comandos abaixo podem ser executados pelo **PowerShell**.

Verifique:

```powershell
python --version
git --version
docker --version
docker compose version
```

## 6. Instalação

### 6.1 Clonar o repositório

```powershell
git clone https://github.com/yhsww/juice-shop-execution.git
cd juice-shop-execution
git pull --ff-only origin main
```

### 6.2 Criar o ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 6.3 Instalar dependências

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6.4 Instalar o Chromium

```powershell
python -m playwright install chromium
```

## 7. Configuração do ambiente

Crie o `.env`:

```powershell
Copy-Item .env.example .env
```

A execução utiliza o Juice Shop localmente:

```env
JUICE_SHOP_BASE_URL=http://127.0.0.1:3000
JUICE_SHOP_HEADLESS=false
```

Para humanização com Claude, configure o provedor e a chave no `.env`, por exemplo:

```env
REPORTING_LLM_PROVIDER=claude
ANTHROPIC_API_BASE_URL=https://api.anthropic.com
ANTHROPIC_API_KEY=SUA_CHAVE_AQUI
CLAUDE_LLM_MODEL=claude-sonnet-5
```

O modelo pode ser alterado para outro modelo Claude disponível na conta.

**Nunca versione `.env`, chaves de API, tokens ou credenciais reais.**

## 8. Iniciar o Juice Shop

O projeto possui o Compose em:

```text
juice-shop/docker-compose.yml
```

Para iniciar manualmente:

```powershell
docker compose -f juice-shop/docker-compose.yml up -d
```

Verifique:

```powershell
docker compose -f juice-shop/docker-compose.yml ps
```

A aplicação deve responder em:

```text
http://127.0.0.1:3000
```

Não é obrigatório iniciar o container manualmente: o `run.py` pode iniciar a aplicação com `--start-app`.

## 9. Executar os cenários

### 9.1 Um cenário

Com o Juice Shop já disponível:

```powershell
python run.py --scenario CEN-CAR-03
```

Ou deixando o executor iniciar a aplicação:

```powershell
python run.py --start-app --scenario CEN-CAR-03
```

### 9.2 Um domínio

Exemplo:

```powershell
python run.py --start-app --domain CHK
```

Também é possível selecionar mais de um domínio:

```powershell
python run.py --start-app --domain CHK --domain IDT
```

### 9.3 Todos os 140 cenários

Execução completa:

```powershell
python run.py --start-app --all
```

O terminal apresenta cada resultado e um resumo semelhante a:

```text
[summary] 140/140 cenários aprovados; 0 com falha.
```

Para iniciar e encerrar automaticamente o ambiente:

```powershell
python run.py --start-app --all --stop-app
```

## 10. Evidências de execução

Cada cenário executado deixa em `reports/executions/`:

| Arquivo | Conteúdo |
|---|---|
| `CEN-XXX-NN.json` | evidência estruturada: status, passos, dados, mensagens, resultado e resumo do tráfego de API por passo |
| `CEN-XXX-NN.md` | a mesma evidência em texto legível |
| `CEN-XXX-NN_step_NN.png` | captura de tela de cada passo |
| `CEN-XXX-NN.har` | tráfego HTTP de API (HAR 1.2, campo `_step` liga cada requisição ao passo); senhas, tokens, cookies e respostas de segurança mascarados, cartões reduzidos aos 4 últimos dígitos |

A execução é a fonte de verdade do resultado. As capturas e o HAR são evidência complementar. A coleta de rede pode ser desligada com `JUICE_SHOP_CAPTURE_NETWORK=false`.

## 11. Humanização com LLM

A humanização reescreve a evidência estruturada em prosa funcional. A LLM só redige: os fatos vêm da evidência e ela não pode acrescentar nada.

```text
catálogo do cenário + evidência da execução (CEN-XXX-NN.json/.md)
        ↓
      LLM  (Claude: só texto | Gemini: texto + capturas de tela)
        ↓
reports/humanized/CEN-XXX-NN.json
```

O provedor e o modelo são definidos no `.env` (`REPORTING_LLM_PROVIDER`, `CLAUDE_LLM_MODEL` etc.). Cada texto gravado leva uma impressão digital (catálogo + evidência + versão do prompt + modelo).

| Comando | O que faz |
|---|---|
| `python -m reporting.humanizer --all` | humaniza só o que falta; textos existentes são reaproveitados sem custo |
| `python -m reporting.humanizer --scenario CEN-XXX-NN --force` | regera um cenário (ex.: depois de reexecutá-lo) |
| `python -m reporting.humanizer --all --refresh-stale` | regera só os cuja evidência ou modelo mudou |
| `python -m reporting.humanizer --all --force` | regera todos (cobra de novo) |

## 12. Gerar os relatórios DOCX

```powershell
python -m reporting.docx_generator --humanize llm
```

Monta os DOCX a partir das evidências e dos textos de `reports/humanized/`. Se todos os textos já existem, não chama a LLM. Dentro de cada documento os cenários ficam agrupados por domínio e em ordem numérica (CHK-01, CHK-02 … CHK-44).

| Opção | Uso |
|---|---|
| `--humanize auto` | usa a LLM e recorre à descrição determinística se o provedor falhar |
| `--humanize deterministic` | sem LLM |
| `--output <pasta>` | grava em outra pasta (padrão: `reports/docx/`) |
| `--force-humanize` | regera todos os textos antes (cobra de novo) |

O gerador sempre grava os 7 arquivos; por isso não use `--scenario` para atualizar os relatórios oficiais (os documentos ficariam só com aquele cenário). Feche os DOCX no Word antes de gerar.

## 13. Relatórios finais

```text
reports/docx/
├── ADM_relatorio.docx   (8 cenários)
├── CAR_relatorio.docx   (15)
├── CAT_relatorio.docx   (29)
├── CHK_relatorio.docx   (44)
├── IDT_relatorio.docx   (28)
├── PER_relatorio.docx   (16)
└── JUICE_SHOP_RELATORIO_GERAL.docx   (140, por domínio)
```

Estrutura de cada cenário: Ficha de Ambiente, Guia de Domínio, Ficha de Cenário, Passos Executados e capturas de tela.

**Versão do catálogo `catalogo-v1`:** 140/140 cenários aprovados (Juice Shop v20.3.0, 2026-11-28); os 140 textos foram gerados pelo `claude-sonnet-5` com a mesma entrada (catálogo + evidência textual, sem imagens).

Rastreabilidade:

```text
DOCX → reports/humanized/CEN-XXX-NN.json → reports/executions/CEN-XXX-NN.{json,md,png,har}
```

## 14. Fluxo completo recomendado

```powershell
git pull
pip install -r requirements.txt
python -m playwright install chromium
Copy-Item .env.example .env   # só na primeira vez; preencha a chave da LLM
```

1. Executar os 140 cenários (Docker precisa estar rodando):

```powershell
python run.py --start-app --all
```

Esperado: `[summary] 140/140 cenários aprovados; 0 com falha.`

2. Humanizar (só o que falta):

```powershell
python -m reporting.humanizer --all
```

3. Gerar os DOCX:

```powershell
python -m reporting.docx_generator --humanize llm
```

## 15. Testes do projeto

Para executar os testes automatizados da própria base:

```powershell
python -m pytest -q
```

A suíte funcional completa do Juice Shop é executada com:

```powershell
python run.py --start-app --all
```

## 16. Princípios de funcionamento

### Evidência antes da expectativa

O catálogo define o objetivo do cenário. A execução registra o comportamento realmente observado.

### Separação entre execução e documentação

```text
Executor
   ↓
Evidências
   ↓
Humanizador
   ↓
DOCX
```

Uma falha da LLM não transforma um cenário real em `PASSED`.

### Correções genéricas

As correções no executor devem resolver padrões de comportamento da aplicação, evitando regras criadas exclusivamente para mascarar problemas de um cenário.

### Rastreabilidade

Cada relatório deve poder ser relacionado às evidências que o originaram.

## 17. Segurança

O OWASP Juice Shop é uma aplicação propositalmente vulnerável. Execute-o somente em ambiente controlado.

Não exponha o Juice Shop diretamente à Internet ou a redes não autorizadas.

Nunca envie para o Git:

- `.env`;
- chaves de API;
- tokens;
- credenciais reais;
- evidências com informações sensíveis.

## 18. Manutenção

A branch principal é:

```text
main
```

Antes de alterar o projeto:

```powershell
git pull --ff-only origin main
git status
```

Depois das alterações:

```powershell
git status
python -m pytest -q
```

Antes de uma entrega funcional, valide:

```powershell
python run.py --start-app --all
```

O estado esperado da suíte completa é:

```text
140/140 cenários aprovados; 0 com falha.
```

## 19. Aplicação alvo

O projeto utiliza o **OWASP Juice Shop** como aplicação alvo dos testes:

https://github.com/juice-shop/juice-shop
