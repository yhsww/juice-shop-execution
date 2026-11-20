# Juice Shop Execution

Automação determinística de cenários de teste no OWASP Juice Shop usando a interface real da aplicação.

## Escopo

O catálogo inicial contém **78 cenários definidos para execução**, distribuídos exatamente nos domínios definidos no trabalho:

| Domínio | Cenários |
|---|---:|
| ADM | 3 |
| CAR | 7 |
| CAT | 17 |
| CHK | 28 |
| IDT | 17 |
| **Total** | **72** |

A estrutura não limita o projeto a 72 casos. Novos cenários podem ser adicionados quando permanecerem dentro do mesmo escopo funcional e forem observáveis pela interface real.

O escopo cobre catálogo, busca, carrinho, identificação/autenticação, perfil, checkout, pedidos e administração da loja. O inventário também inclui fluxos de privacidade e segurança de conta que fazem parte da interface do Juice Shop.

## Execução

1. Instale as dependências:
   `pip install -r requirements.txt`
2. Instale o navegador:
   `playwright install chromium`
3. Suba uma instância local do Juice Shop em `http://localhost:3000`.
4. Copie `.env.example` para `.env` se quiser sobrescrever configurações.
5. Execute:
   `python run.py --scenario CEN-CAT-01`
   `python run.py --all`

## Conta administrativa de teste

O ambiente usa por padrão:

- E-mail: `admin@juice-sh.op`
- Senha: `admin123`

Essas credenciais são documentadas no Companion Guide oficial do OWASP Juice Shop para o desafio de login com as credenciais originais do administrador. citeturn610981search0

## Princípio da automação

O cenário descreve o objetivo e as ações planejadas. O executor:

1. abre a aplicação;
2. observa o estado atual;
3. localiza elementos compatíveis;
4. executa a ação;
5. observa novamente a interface;
6. valida a mudança observável;
7. captura evidências;
8. gera a Ficha de Cenário no padrão definido no trabalho.

O relatório não deve inventar resultados: campos de resultado e evidência devem ser preenchidos a partir do que foi observado durante a execução.

## Evidências

Cada execução registra ação, dados, URL antes/depois, resultado observado, mudança de estado, sucesso/erro, screenshot e timestamp.

## Sem IA

O projeto não usa LLM, RAG, embeddings, ChromaDB, API de IA ou chave de provedor. A tomada de decisão é baseada em regras e observação da interface.
