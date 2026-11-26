# Juice Shop Execution

Automação de testes funcionais do **OWASP Juice Shop** utilizando a interface real da aplicação, Playwright, Python, Docker e geração de evidências e relatórios.

## 1. Objetivo do projeto

O objetivo deste projeto é automatizar a execução de cenários funcionais do OWASP Juice Shop de forma **reprodutível, rastreável e baseada em evidências reais da interface**.

A automação executa as ações do usuário na aplicação, registra o comportamento observado e gera evidências para cada cenário.

Fluxo geral:

```text
Cenário definido no catálogo
        ↓
Execução na interface real
        ↓
Playwright
        ↓
Evidências JSON + screenshots
        ↓
Relatório Markdown / DOCX
        ↓
Humanização opcional com LLM
```

A LLM é utilizada somente para **interpretar e organizar a documentação**. Ela não decide se um cenário passou ou falhou. O status da execução é determinado pelo executor e pelas evidências reais coletadas.

## 2. Escopo atual

A suíte principal possui **78 cenários funcionais**, incluindo o domínio PER:

| Domínio | Cenários |
|---|---:|
| ADM | 3 |
| CAR | 7 |
| CAT | 17 |
| CHK | 28 |
| IDT | 17 |
| PER | 6 |
| **Total** | **78** |

Os cenários são mantidos em:

```text
scenarios/scenarios.json
```

## 3. Tecnologias utilizadas

### Linguagem e execução

- **Python 3.10+** — linguagem principal da automação.
- **Playwright** — automação da interface web e interação com o navegador.
- **Chromium** — navegador utilizado pelos testes.
- **pytest** — infraestrutura de testes e validações do projeto.

### Ambiente da aplicação

- **OWASP Juice Shop** — aplicação web alvo dos testes.
- **Docker** — isolamento e execução da aplicação Juice Shop.
- **Docker Compose** — configuração e gerenciamento do container da aplicação.

### Configuração

- **python-dotenv** — carregamento das variáveis de ambiente a partir do arquivo `.env`.

### Evidências e documentação

- **python-docx** — geração dos relatórios DOCX.
- **JSON** — armazenamento estruturado das evidências de execução.
- **Markdown** — geração e leitura de relatórios intermediários.

### Humanização com IA

- **OpenAI SDK** — integração com provedores compatíveis com a API OpenAI.
- **Anthropic SDK** — suporte opcional ao Claude.
- **Gemini** — provedor recomendado atualmente para a humanização multimodal, utilizando a interface compatível com a API OpenAI.
- **LLM multimodal** — recebe as evidências textuais e screenshots para produzir descrições mais específicas dos comportamentos observados.

## 4. Estrutura do projeto

```text
juice-shop-execution/
├── automation/              # Executor e ações funcionais
├── config/                  # Configurações do ambiente
├── reporting/               # Evidências, relatórios e humanização
│   └── llm/                 # Cliente e prompt da LLM
├── scenarios/               # Catálogo dos 78 cenários
├── tests/                   # Testes do projeto
├── juice-shop/              # Docker Compose da aplicação alvo
├── reports/
│   ├── executions/          # JSONs e screenshots das execuções
│   ├── final/               # Relatórios Markdown
│   ├── humanized/           # Resultado da humanização pela LLM
│   └── docx/                # Relatórios DOCX
├── .env.example             # Modelo de configuração
├── requirements.txt         # Dependências Python
├── run.py                   # Ponto de entrada da execução
└── README.md
```

## 5. Passo a passo para executar

### Fluxo rápido

Se você já possui Python, Docker e o repositório configurados, a execução completa segue esta ordem:

1. Atualizar a branch `main`.
2. Ativar o ambiente virtual Python.
3. Instalar as dependências.
4. Instalar o Chromium do Playwright.
5. Configurar o `.env`.
6. Iniciar o Juice Shop pelo Docker.
7. Executar os cenários.
8. Conferir os JSONs, Markdown e screenshots em `reports/executions/`.
9. Gerar a humanização em `reports/humanized/`.
10. Gerar os DOCX finais em `reports/docx/`.

### Execução completa em sequência

```powershell
cd C:\Users\Asus\Desktop\juice-shop-execution-v2
git pull --ff-only origin main
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install chromium
python run.py --start-app --all
python -m reporting.humanizer --all --force
python -m reporting.docx_generator --humanize auto --force-humanize
```

Para uma execução do zero, os passos detalhados abaixo devem ser seguidos na ordem apresentada.


### Passo 1 — Pré-requisitos

Instale:

- Python 3.10 ou superior;
- Git;
- Docker Desktop no Windows/macOS ou Docker Engine + Docker Compose v2 no Linux.

No Windows, o projeto pode ser executado pelo **PowerShell**.

Verifique as instalações:

```powershell
python --version
git --version
docker --version
docker compose version
```

### Passo 2 — Clonar o projeto

```powershell
git clone https://github.com/yhsww/juice-shop-execution.git
cd juice-shop-execution
```

Para trabalhar sempre com a versão atual da branch principal:

```powershell
git pull --ff-only origin main
```

### Passo 3 — Criar o ambiente Python

É recomendado utilizar um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a ativação do ambiente virtual, ajuste a política somente para a sessão atual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois, ative novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Passo 4 — Instalar as dependências

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Passo 5 — Instalar o navegador do Playwright

```powershell
python -m playwright install chromium
```

### Passo 6 — Configurar o ambiente

Crie o arquivo `.env` a partir do modelo:

```powershell
Copy-Item .env.example .env
```

Configure, no mínimo, a URL da aplicação:

```env
JUICE_SHOP_BASE_URL=http://127.0.0.1:3000
JUICE_SHOP_HEADLESS=false
```

Para utilizar a humanização por LLM, configure também o provedor e a chave correspondente. Exemplo com Gemini:

```env
REPORTING_LLM_PROVIDER=gemini
GEMINI_API_KEY=SUA_CHAVE_AQUI
GEMINI_API_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
GEMINI_LLM_MODEL=gemini-3.5-flash-lite
```

**Nunca versione o arquivo `.env` nem chaves de API.**

### Passo 7 — Iniciar o Juice Shop

O projeto já possui um Docker Compose em:

```text
juice-shop/docker-compose.yml
```

É possível iniciar manualmente:

```powershell
docker compose -f juice-shop/docker-compose.yml up -d
```

Verifique se o container está executando:

```powershell
docker compose -f juice-shop/docker-compose.yml ps
```

A aplicação deve estar disponível em:

```text
http://127.0.0.1:3000
```

### Passo 8 — Executar um cenário específico

Com a aplicação já iniciada:

```powershell
python run.py --scenario CEN-CAR-03
```

O resultado será apresentado no terminal, por exemplo:

```text
[PASSED] CEN-CAR-03
```

Para deixar o próprio projeto responsável por iniciar a aplicação:

```powershell
python run.py --start-app --scenario CEN-CAR-03
```

### Passo 9 — Executar um domínio inteiro

Exemplo:

```powershell
python run.py --start-app --domain CHK
```

É possível executar mais de um domínio:

```powershell
python run.py --start-app --domain CHK --domain IDT
```

### Passo 10 — Executar todos os 78 cenários

Para executar a suíte completa:

```powershell
python run.py --start-app --all
```

O executor apresenta o resultado de cada cenário e, ao final, um resumo:

```text
[summary] X/78 cenários aprovados; Y com falha.
```

Para iniciar e encerrar automaticamente o ambiente Docker ao final:

```powershell
python run.py --start-app --all --stop-app
```

### Passo 11 — Verificar as evidências

Após a execução, consulte:

```text
reports/executions/
```

As evidências registram informações como:

- ID do cenário;
- status;
- ações executadas;
- dados utilizados;
- resultado observado;
- mensagens apresentadas pela interface;
- screenshots;
- informações de validação.

As screenshots são importantes para a documentação porque registram visualmente o estado da aplicação durante a execução.

### Passo 12 — Gerar a documentação humanizada

A humanização pode ser executada para um cenário específico:

```powershell
python -m reporting.humanizer --scenario CEN-CAR-03 --force
```

Ou para todos os cenários que possuem evidências:

```powershell
python -m reporting.humanizer --all --force
```

O resultado intermediário é armazenado em:

```text
reports/humanized/
```

A humanização considera as evidências estruturadas e as screenshots para produzir descrições funcionais mais detalhadas.

### Passo 13 — Gerar os relatórios DOCX

Para gerar os DOCX finais com as descrições humanizadas por LLM, use:

```powershell
python -m reporting.docx_generator --humanize llm --force-humanize
```

Esse é o comando recomendado para a entrega final: ele atualiza a humanização antes de montar os documentos DOCX.

Para gerar os DOCX usando humanização automática, permitindo fallback determinístico quando a LLM estiver indisponível:

```powershell
python -m reporting.docx_generator --humanize auto
```

Para gerar os DOCX sem LLM:

```powershell
python -m reporting.docx_generator --humanize deterministic
```

Essa opção utiliza apenas as evidências registradas pelo executor e não depende de um provedor externo.

Os documentos são gerados em:

```text
reports/docx/
```

O gerador cria **1 relatório geral consolidado com os 78 cenários** e **1 relatório separado para cada domínio** (ADM, CAR, CAT, CHK, IDT e PER). A versão do Juice Shop usada na ficha de ambiente é obtida da imagem configurada no `juice-shop/docker-compose.yml`, e o sistema operacional é identificado automaticamente durante a geração.

Para regenerar os documentos após uma nova execução, use:

```powershell
python -m reporting.docx_generator --humanize llm --force-humanize
```

O parâmetro `--force-humanize` força a atualização das descrições humanizadas antes da montagem do DOCX.

### Comando único recomendado para a entrega final

Depois que os 78 cenários forem executados e as evidências estiverem em `reports/executions/`:

```powershell
python -m reporting.humanizer --all --force
python -m reporting.docx_generator --humanize llm --force-humanize
```

Resultado esperado:

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

## 6. Fluxo completo recomendado

Para uma execução completa do projeto, a sequência recomendada é:

```powershell
cd C:\Users\Asus\Desktop\juice-shop-execution-v2

git pull --ff-only origin main

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python -m playwright install chromium

Copy-Item .env.example .env
```

Depois de configurar o `.env`:

```powershell
python run.py --start-app --all
```

Em seguida, gere a documentação:

```powershell
python -m reporting.docx_generator --humanize auto
```

Resultado esperado:

```text
Execução
   ↓
78 cenários
   ↓
JSON + screenshots
   ↓
Humanização
   ↓
DOCX final
```

## 7. Execução sem humanização por LLM

A LLM é opcional.

Para testar somente o executor:

```powershell
python run.py --start-app --all
```

Para gerar a documentação sem depender de uma API de IA:

```powershell
python -m reporting.docx_generator --humanize deterministic
```

Isso permite validar a execução e a geração do relatório mesmo sem uma chave de API configurada.

## 8. Documentação DOCX

A estrutura do DOCX é fixa e segue a ficha definida para o projeto. O gerador não cria seções adicionais de resumo, integridade ou detalhes técnicos de automação.


Cada relatório contém:

1. **Ficha de Ambiente**
2. **Guia de Domínio**
3. **Ficha de Cenário**
4. **Passos Executados**
5. Screenshots vinculadas às evidências dos passos

Os artefatos gerados ficam organizados em `reports/`:

- `reports/executions/` — JSONs e screenshots das execuções;
- `reports/final/` — relatórios Markdown;
- `reports/humanized/` — JSONs produzidos pela humanização;
- `reports/docx/` — documentos DOCX finais.

Quando esses artefatos forem versionados no repositório, não devem conter chaves, tokens, senhas reais ou outras informações sensíveis.

A ficha de cenário contempla:

- ID do cenário;
- domínio;
- nome do cenário;
- ator;
- fluxo;
- pré-condição;
- resultado observado;
- mensagens exibidas ao usuário;
- dados manipulados;
- coerência com a loja de sucos;
- justificativa;
- requisito candidato, quando aplicável.

A tabela de passos registra:

| Campo | Conteúdo |
|---|---|
| # | Número do passo |
| Ação do usuário | Ação funcional realizada |
| Dados informados | Dados utilizados na ação |
| Resposta da interface | Comportamento observado |

## 9. Humanização multimodal

Quando o provedor Gemini está configurado, o humanizador pode receber:

- evidências JSON;
- relatórios textuais;
- screenshots PNG;
- dados das ações executadas;
- resultados observados.

As imagens são analisadas para identificar elementos realmente visíveis, como:

- produtos;
- imagens;
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
- mudanças de estado.

A LLM deve interpretar as evidências, mas **não pode inventar fatos**. O executor continua sendo a fonte de verdade sobre o resultado do cenário.

## 10. Princípios de funcionamento

### Evidência antes da expectativa

O catálogo define o comportamento esperado. A execução registra o comportamento real.

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

## 11. Segurança

O OWASP Juice Shop é uma aplicação propositalmente vulnerável. Execute-o somente em ambiente controlado.

Não exponha o Juice Shop diretamente à Internet ou a redes não autorizadas.

Nunca envie para o Git:

- `.env`;
- chaves de API;
- tokens;
- credenciais reais;
- evidências que contenham informações sensíveis.

## 12. Manutenção

A branch principal do projeto é:

```text
main
```

Antes de alterar o código:

```powershell
git pull --ff-only origin main
git status
```

Após alterações:

```powershell
git status
```

Validação da suíte completa:

```powershell
python run.py --start-app --all
```

Validação rápida da documentação:

```powershell
python -m reporting.humanizer --scenario CEN-CAR-03 --force
```

## 13. Aplicação alvo

O projeto utiliza o **OWASP Juice Shop** como aplicação alvo dos testes.

```text
https://github.com/juice-shop/juice-shop
```
