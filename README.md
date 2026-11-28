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

Após executar os cenários, as evidências ficam em:

```text
reports/executions/
```

Os artefatos podem incluir:

- ID do cenário;
- status;
- ações executadas;
- dados utilizados;
- resultado observado;
- mensagens apresentadas pela interface;
- screenshots;
- informações de validação.

A execução é a fonte de verdade do resultado do cenário.

As screenshots são evidências visuais complementares e não devem ser utilizadas para inventar fatos que não foram registrados pela execução.

## 11. Humanização com Claude

A humanização transforma as evidências estruturadas em documentação funcional mais natural.

O fluxo é:

```text
JSON da execução
      +
screenshots
      +
catálogo do cenário
        ↓
      Claude
        ↓
JSON humanizado
```

Os JSONs humanizados são artefatos intermediários da geração dos relatórios e não fazem parte da entrega final versionada. A entrega final mantém os DOCX consolidados em `reports/docx/`.

### Humanizar um cenário

```powershell
python -m reporting.humanizer --scenario CEN-CAR-03 --force
```

### Humanizar todos os cenários

```powershell
python -m reporting.humanizer --all --force
```

O humanizador utiliza fingerprint do conteúdo e do modelo para evitar reutilizar uma documentação incompatível quando a evidência ou o modelo muda.

A LLM deve **interpretar as evidências sem inventar fatos**. URLs, seletores, waits e outros detalhes técnicos são tratados como artefatos de execução e não devem ser transformados em narrativa funcional.

## 12. Gerar os relatórios DOCX

O gerador pode montar os documentos a partir das evidências e dos JSONs humanizados.

### Gerar os DOCX usando humanização LLM

```powershell
python -m reporting.docx_generator --humanize llm --force-humanize
```

### Gerar automaticamente

```powershell
python -m reporting.docx_generator --humanize auto
```

No modo `auto`, o gerador tenta utilizar a LLM e pode recorrer à descrição determinística quando o provedor não estiver disponível.

### Gerar sem LLM

```powershell
python -m reporting.docx_generator --humanize deterministic
```

Esse modo usa as evidências disponíveis sem depender de uma API de IA.

### Gerar um único cenário

```powershell
python -m reporting.docx_generator --scenario CEN-ADM-01 --humanize llm --force-humanize
```

### Gerar todos os relatórios a partir dos humanizados existentes

Se os 140 JSONs humanizados já estiverem disponíveis localmente, os DOCX podem ser recriados em uma pasta de trabalho e, após validação, consolidados em `reports/docx/`.

A árvore versionada final não mantém os JSONs humanizados intermediários; mantém somente os relatórios DOCX finais e as evidências de execução.

## 13. Relatórios finais

A entrega final validada contém **7 DOCX**, versionados em:

```text
reports/docx/
├── ADM_relatorio.docx
├── CAR_relatorio.docx
├── CAT_relatorio.docx
├── CHK_relatorio.docx
├── IDT_relatorio.docx
├── PER_relatorio.docx
└── JUICE_SHOP_RELATORIO_GERAL.docx
```

Os relatórios foram gerados e validados com **Claude** e consolidados em seis relatórios por domínio mais um relatório geral.

São gerados:

- 1 relatório para cada um dos 6 domínios;
- 1 relatório geral consolidando todos os cenários do catálogo (140 com os complementares; os DOCX versionados hoje ainda refletem os 78 cenários-base até serem regenerados).

O relatório geral reúne os mesmos cenários dos relatórios por domínio.

A estrutura dos DOCX contempla:

1. **Ficha de Ambiente**
2. **Guia de Domínio**
3. **Ficha de Cenário**
4. **Passos Executados**
5. Screenshots vinculadas às evidências dos passos

A documentação mantém a rastreabilidade:

```text
DOCX
 ↓
JSON humanizado
 ↓
JSON da execução
 ↓
ações + resultados + screenshots
```

## 14. Fluxo completo recomendado

Para uma execução completa desde o ambiente local:

```powershell
git pull --ff-only origin main

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python -m playwright install chromium

Copy-Item .env.example .env
```

Configure o `.env` e depois execute:

```powershell
python run.py --start-app --all
```

Valide o resumo final. Para a entrega com Claude:

```powershell
python -m reporting.humanizer --all --force
python -m reporting.docx_generator --humanize llm --force-humanize --output .\reports\docx
```

Se a humanização dos 140 cenários já estiver pronta e apenas os DOCX precisarem ser recriados:

```powershell
python -m reporting.docx_generator --output .\reports\docx
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
