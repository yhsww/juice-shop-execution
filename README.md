# Juice Shop Execution

Automação de testes funcionais no [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) usando a interface real da aplicação, com Playwright, execução reproduzível em Docker e geração de evidências e relatórios.

## Objetivo

Este projeto tem como objetivo automatizar e validar cenários de teste do Juice Shop de forma **determinística, rastreável e baseada no comportamento real da aplicação**.

A automação:

- executa cenários definidos em `scenarios/scenarios.json`;
- interage com a aplicação por meio da interface real;
- utiliza localizadores semânticos e comportamento observado no DOM;
- valida o estado final esperado de cada cenário;
- registra URLs, ações, resultados observados, mensagens, controles e evidências;
- captura screenshots durante a execução;
- gera relatórios em JSON e Markdown;
- gera relatórios DOCX consolidados por domínio e um relatório geral;
- pode usar uma LLM para transformar evidências técnicas em descrições funcionais humanizadas;
- permite execução de cenários individuais, domínios ou da suíte completa.

## Resultado atual

A suíte principal possui **72 cenários validados**, distribuídos em:

| Domínio | Cenários |
|---|---:|
| ADM | 3 |
| CAR | 7 |
| CAT | 17 |
| CHK | 28 |
| IDT | 17 |
| **Total** | **72** |

A versão atual está consolidada na branch `main`.

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| **Python 3.10+** | Linguagem principal da automação |
| **Playwright** | Automação e interação com a interface web |
| **Chromium** | Navegador utilizado pelos testes |
| **Docker / Docker Compose** | Execução isolada e reproduzível do Juice Shop |
| **OWASP Juice Shop** | Aplicação alvo dos testes |
| **pytest** | Estrutura e execução de testes automatizados |
| **python-dotenv** | Gerenciamento de variáveis de ambiente |
| **python-docx** | Geração dos relatórios em Word/DOCX |
| **JSON** | Catálogo de cenários e evidências estruturadas |
| **Markdown** | Relatórios e documentação |
| **Git / GitHub** | Versionamento e colaboração |

### Ambiente da aplicação

O projeto utiliza uma configuração Docker em `juice-shop/`, com a imagem versionada do Juice Shop:

```text
bkimminich/juice-shop:v20.3.0
```

A aplicação é executada localmente e a porta do container é vinculada ao endereço `127.0.0.1`.

## Estrutura do projeto

```text
juice-shop-execution/
├── automation/              # Motor de automação e execução
├── config/                  # Configurações da aplicação
├── reporting/               # Geração de relatórios
├── scenarios/               # Catálogo de cenários
├── tests/                   # Testes automatizados do próprio projeto
├── juice-shop/              # Docker Compose do ambiente alvo
├── reports/
│   ├── executions/          # Evidências JSON das execuções
│   ├── final/               # Relatórios finais em Markdown
│   └── docx/                # Relatórios DOCX gerados
├── screenshots/             # Evidências visuais
├── requirements.txt         # Dependências Python
├── run.py                   # Ponto de entrada da execução
└── README.md
```

## Requisitos

Antes de executar o projeto, instale:

- Python 3.10 ou superior;
- Docker Desktop no Windows/macOS ou Docker Engine + Docker Compose v2 no Linux;
- Git;
- Playwright/Chromium.

No Windows, o PowerShell é recomendado para os comandos abaixo.

## Instalação

Clone o repositório:

```powershell
git clone https://github.com/yhsww/juice-shop-execution.git
cd juice-shop-execution
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

Instale o navegador utilizado pelo Playwright:

```powershell
python -m playwright install chromium
```

Se o projeto utilizar variáveis de ambiente locais:

```powershell
Copy-Item .env.example .env
```

Configure o arquivo `.env` conforme o ambiente de execução.

## Executando o Juice Shop

O executor pode iniciar o ambiente Docker automaticamente.

Para executar um cenário específico:

```powershell
python run.py --start-app --scenario CEN-IDT-01
```

Para executar um domínio:

```powershell
python run.py --start-app --domain CHK
```

Também é possível executar mais de um domínio:

```powershell
python run.py --start-app --domain CHK --domain IDT
```

Para executar toda a suíte:

```powershell
python run.py --start-app --all
```

Para iniciar a aplicação, executar todos os cenários e desligar o container ao final:

```powershell
python run.py --start-app --all --stop-app
```

### Execução sem iniciar o Docker

Se o Juice Shop já estiver disponível em:

```text
http://127.0.0.1:3000
```

o executor pode reutilizar a instância existente.

## Docker manual

Também é possível controlar o ambiente diretamente:

```powershell
docker compose -f juice-shop/docker-compose.yml up -d
```

Verificar o container:

```powershell
docker compose -f juice-shop/docker-compose.yml ps
```

Visualizar logs:

```powershell
docker compose -f juice-shop/docker-compose.yml logs -f
```

Encerrar:

```powershell
docker compose -f juice-shop/docker-compose.yml down
```

## Execução e evidências

Durante uma execução, o runner registra evidências da atividade do cenário.

Entre os dados registrados estão:

- cenário executado;
- ação realizada;
- ação técnica e descrição da ação do usuário;
- dados utilizados;
- URL antes e depois;
- resultado observado;
- alteração detectada;
- sucesso ou falha da etapa;
- mensagens da aplicação;
- estado visível da interface;
- controles encontrados;
- informações de rede;
- screenshot da etapa;
- URL final;
- resultado da validação.

As evidências individuais são armazenadas em:

```text
reports/executions/
```

Screenshots são armazenados em:

```text
screenshots/
```

## Relatórios

Os relatórios Markdown finais ficam em:

```text
reports/final/
```

Incluem relatórios por domínio:

- `ADM.md`
- `CAR.md`
- `CAT.md`
- `CHK.md`
- `IDT.md`

e o relatório consolidado disponível no diretório de relatórios finais.

### Geração dos relatórios DOCX

Depois de executar os cenários, gere os documentos Word com:

```powershell
python -m reporting.docx_generator
```

Por padrão, o gerador usa a humanização por LLM quando OPENAI_API_KEY está configurada. Se a chave não estiver disponível, utiliza a humanização determinística já existente.

Para exigir LLM:

```powershell
python -m reporting.docx_generator --humanize llm
```

Para gerar sem LLM:

```powershell
python -m reporting.docx_generator --humanize deterministic
```

A documentação humanizada é armazenada em reports/humanized/ e reutilizada em execuções seguintes quando as evidências e o modelo não mudarem. O diretório é cache gerado e não é versionado.

A LLM recebe somente o cenário e as evidências funcionais normalizadas. URLs, rotas, seletores, waits, credenciais e detalhes de implementação são removidos antes do envio. O status do teste e as evidências de execução continuam sob autoridade do executor; a LLM atua somente na redação.

O gerador cria:

- um relatório DOCX para cada domínio;
- um relatório DOCX geral;
- evidências detalhadas por cenário;
- descrições funcionais humanizadas por cenário;
- informações das etapas executadas;
- resultados;
- validações;
- mensagens;
- screenshots disponíveis;
- conclusão baseada na execução real.

Os arquivos são gerados em:

```text
reports/docx/
```

Os DOCX são artefatos gerados e não precisam ser versionados no Git.

## Catálogo de cenários

Os cenários são definidos em:

```text
scenarios/scenarios.json
```

Cada cenário descreve, entre outras informações:

- identificador;
- domínio;
- nome;
- ações;
- dados utilizados;
- comportamento esperado;
- validação final.

O catálogo é separado do executor para permitir evolução dos cenários sem precisar alterar o motor de automação para cada novo caso.

## Princípios de engenharia

O projeto segue alguns princípios importantes:

1. **Evidência real:** um cenário não deve ser considerado aprovado apenas porque a ação foi enviada; o estado observado precisa corresponder ao resultado esperado.
2. **Localizadores genéricos:** correções devem atuar sobre padrões reais da aplicação, evitando soluções específicas para um único ID de cenário.
3. **Sem mascaramento de falhas:** exceções, timeouts excessivos ou ações forçadas não devem ser utilizados para transformar uma falha funcional em sucesso artificial.
4. **Rastreabilidade:** cada resultado deve poder ser relacionado ao cenário, às etapas executadas e às evidências produzidas.
5. **Reprodutibilidade:** o ambiente da aplicação é controlado por Docker e a suíte utiliza dependências declaradas em `requirements.txt`.
6. **Separação entre execução e relatório:** o executor produz evidências estruturadas e o gerador de relatórios transforma essas evidências em documentação.

## Segurança

O OWASP Juice Shop é uma aplicação propositalmente vulnerável e deve ser executado somente em ambiente controlado.

A configuração deste projeto vincula o serviço localmente em `127.0.0.1`. Não exponha o Juice Shop vulnerável diretamente à Internet ou a redes não autorizadas.

## Contribuição e manutenção

A branch oficial do projeto é:

```text
main
```

Antes de enviar alterações, execute a suíte relevante e confirme:

```powershell
git status
python run.py --start-app --all
```

Para mudanças no executor ou nos localizadores, priorize correções genéricas baseadas no DOM e no comportamento real da aplicação, evitando regras específicas para IDs individuais de cenários.

## Licença e aplicação alvo

Este projeto automatiza testes sobre o OWASP Juice Shop. Consulte a documentação e o repositório oficial do projeto para informações sobre a aplicação alvo e sua licença.

- OWASP Juice Shop: https://github.com/juice-shop/juice-shop
