# Fichas dos cenários complementares (Etapa 1 — AMBOLS)

Gerado por `tools/gerar_cenarios_alternativos.py`. Os campos de resultado observado são preenchidos a partir das evidências em `reports/executions/`.

## IDT (Gestão de Identidade e Usuários)

### CEN-IDT-18 — Cadastro com senha abaixo do tamanho mínimo

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-18 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Cadastro com senha abaixo do tamanho mínimo |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — formulário inválido |
| Cenário de origem | CEN-IDT-01 |
| Pré-condição (estado inicial) | Sem sessão ativa; tela de cadastro aberta. |
| Resultado esperado (critério verificável) | URL contém `/#/register`; texto contém `5-40 characters` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | E-mail único; senha '123'; pergunta e resposta preenchidas. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Regra de tamanho de senha protege a conta do cliente. |
| Requisito candidato (opcional) | O sistema deve rejeitar senhas fora do intervalo de tamanho permitido e informar o limite ao usuário. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/register |  | _preencher_ |
| 2 | Preencher 'Email address' | ${UNIQUE_EMAIL} | _preencher_ |
| 3 | Preencher 'Password' | 123 | _preencher_ |
| 4 | Preencher 'Repeat Password' | 123 | _preencher_ |
| 5 | Selecionar em 'Security Question' | Your favorite book? | _preencher_ |
| 6 | Preencher 'Answer' | a | _preencher_ |
| 7 | Pressionar Tab em 'Answer' |  | _preencher_ |
| 8 | Verificar que 'Button to complete the registration' está desabilitado |  | _preencher_ |

### CEN-IDT-19 — Cadastro sem pergunta de segurança

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-19 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Cadastro sem pergunta de segurança |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — formulário incompleto |
| Cenário de origem | CEN-IDT-01 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | URL contém `/#/register` — confiança: **alta** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | E-mail único; senha válida repetida; pergunta e resposta vazias. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | A pergunta de segurança é usada depois na recuperação de senha. |
| Requisito candidato (opcional) | O sistema deve exigir pergunta e resposta de segurança para concluir o cadastro. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/register |  | _preencher_ |
| 2 | Preencher 'Email address' | ${UNIQUE_EMAIL} | _preencher_ |
| 3 | Preencher 'Password' | Teste@12345 | _preencher_ |
| 4 | Preencher 'Repeat Password' | Teste@12345 | _preencher_ |
| 5 | Verificar que 'Button to complete the registration' está desabilitado |  | _preencher_ |

### CEN-IDT-20 — Login com e-mail não cadastrado

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-20 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Login com e-mail não cadastrado |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — dados inválidos |
| Cenário de origem | CEN-IDT-03 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | URL contém `/#/login`; texto contém `Invalid email or password` — confiança: **alta** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | E-mail inexistente; senha 'Teste@12345'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O cliente precisa saber que não conseguiu entrar, sem que a loja revele quais e-mails existem. |
| Requisito candidato (opcional) | O sistema deve recusar credenciais de conta inexistente com mensagem genérica. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/login |  | _preencher_ |
| 2 | Preencher 'Email' | nao-existe-${UNIQUE_EMAIL} | _preencher_ |
| 3 | Preencher 'Password' | Teste@12345 | _preencher_ |
| 4 | Clicar em 'Login' |  | _preencher_ |

### CEN-IDT-21 — Login com campos vazios

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-21 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Login com campos vazios |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — formulário incompleto |
| Cenário de origem | CEN-IDT-03 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | URL contém `/#/login` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Nenhum dado; depois apenas e-mail. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Evita envio de tentativa de login sem dados. |
| Requisito candidato (opcional) | O sistema deve impedir o envio do login enquanto e-mail e senha não forem informados. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/login |  | _preencher_ |
| 2 | Verificar que 'Login' está desabilitado |  | _preencher_ |
| 3 | Preencher 'Email' | ${SCENARIO_EMAIL} | _preencher_ |
| 4 | Verificar que 'Login' está desabilitado |  | _preencher_ |

### CEN-IDT-22 — Acesso a área restrita após logout

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-22 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Acesso a área restrita após logout |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — ação sem login |
| Cenário de origem | CEN-IDT-05 |
| Pré-condição (estado inicial) | Cliente autenticado com sessão ativa. |
| Resultado esperado (critério verificável) | URL contém `/#/order-history`; texto contém `You have not placed any orders yet` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Rota /#/order-history digitada após logout. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Após sair, dados do cliente não devem continuar acessíveis no navegador. |
| Requisito candidato (opcional) | O sistema deve encerrar a sessão no logout e não exibir dados pessoais em rotas restritas sem nova autenticação. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Observado na v20.3.0: a rota não redireciona ao login; mostra o histórico vazio. Registrar como comportamento (dados do cliente não aparecem).

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'Account' |  | _preencher_ |
| 3 | Clicar em 'Logout' |  | _preencher_ |
| 4 | Abrir a rota /#/order-history |  | _preencher_ |

### CEN-IDT-23 — Troca de senha com senha atual incorreta

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-23 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Troca de senha com senha atual incorreta |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — dados inválidos |
| Cenário de origem | CEN-IDT-08 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | texto contém `Current password is not correct` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Senha atual 'Errada@999'; nova 'Nova@12345' duas vezes. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Somente o dono da conta deve conseguir trocar a senha. |
| Requisito candidato (opcional) | O sistema deve exigir a senha atual correta para alterar a senha. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/privacy-security/change-password |  | _preencher_ |
| 2 | Preencher 'Current Password' | Errada@999 | _preencher_ |
| 3 | Preencher 'New Password' | Nova@12345 | _preencher_ |
| 4 | Preencher 'Repeat New Password' | Nova@12345 | _preencher_ |
| 5 | Clicar em 'Change' |  | _preencher_ |

### CEN-IDT-24 — Troca de senha com confirmação divergente

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-24 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Troca de senha com confirmação divergente |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — formulário inválido |
| Cenário de origem | CEN-IDT-08 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | texto contém `do not match` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Atual 'Teste@12345'; nova 'Nova@12345'; repetição 'Nova@54321'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Evita que o cliente fixe uma senha digitada errado. |
| Requisito candidato (opcional) | O sistema deve bloquear a troca quando a nova senha e a repetição forem diferentes. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/privacy-security/change-password |  | _preencher_ |
| 2 | Preencher 'Current Password' | Teste@12345 | _preencher_ |
| 3 | Preencher 'New Password' | Nova@12345 | _preencher_ |
| 4 | Preencher 'Repeat New Password' | Nova@54321 | _preencher_ |
| 5 | Pressionar Tab em 'Repeat New Password' |  | _preencher_ |
| 6 | Verificar que 'Button to confirm the change' está desabilitado |  | _preencher_ |

### CEN-IDT-25 — Recuperação de senha com resposta errada

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-25 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Recuperação de senha com resposta errada |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — dados inválidos |
| Cenário de origem | CEN-IDT-10 |
| Pré-condição (estado inicial) | Conta criada no próprio cenário com resposta 'resposta-teste'. |
| Resultado esperado (critério verificável) | texto contém `Wrong answer` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Resposta 'errada'; nova senha 'Nova@12345'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | A recuperação só deve funcionar para quem conhece a resposta cadastrada. |
| Requisito candidato (opcional) | O sistema deve recusar a redefinição de senha quando a resposta de segurança estiver incorreta. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/register |  | _preencher_ |
| 2 | Preencher 'Email address' | ${UNIQUE_EMAIL} | _preencher_ |
| 3 | Preencher 'Password' | Teste@12345 | _preencher_ |
| 4 | Preencher 'Repeat Password' | Teste@12345 | _preencher_ |
| 5 | Selecionar em 'Security Question' | Your favorite book? | _preencher_ |
| 6 | Preencher 'Answer' | resposta-teste | _preencher_ |
| 7 | Clicar em 'Register' |  | _preencher_ |
| 8 | Abrir a rota /#/forgot-password |  | _preencher_ |
| 9 | Preencher 'Email' | ${UNIQUE_EMAIL} | _preencher_ |
| 10 | Preencher 'Security Question' | errada | _preencher_ |
| 11 | Preencher 'New Password' | Nova@12345 | _preencher_ |
| 12 | Preencher 'Repeat New Password' | Nova@12345 | _preencher_ |
| 13 | Clicar em 'Change' |  | _preencher_ |

### CEN-IDT-26 — Recuperação de senha concluída e login com a nova senha

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-26 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Recuperação de senha concluída e login com a nova senha |
| Ator | Visitante não autenticado |
| Fluxo | Principal (ausente no catálogo atual) |
| Cenário de origem | CEN-IDT-09 |
| Pré-condição (estado inicial) | Conta criada no próprio cenário com resposta 'resposta-teste'. |
| Resultado esperado (critério verificável) | texto NÃO contém `Invalid email or password` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Resposta correta; nova senha 'Nova@12345'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O catálogo atual só abre a tela de recuperação; não verifica a mudança de estado (senha trocada). |
| Requisito candidato (opcional) | O sistema deve permitir redefinir a senha com a resposta de segurança correta e aceitar a nova senha no login. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/register |  | _preencher_ |
| 2 | Preencher 'Email address' | ${UNIQUE_EMAIL} | _preencher_ |
| 3 | Preencher 'Password' | Teste@12345 | _preencher_ |
| 4 | Preencher 'Repeat Password' | Teste@12345 | _preencher_ |
| 5 | Selecionar em 'Security Question' | Your favorite book? | _preencher_ |
| 6 | Preencher 'Answer' | resposta-teste | _preencher_ |
| 7 | Clicar em 'Register' |  | _preencher_ |
| 8 | Abrir a rota /#/forgot-password |  | _preencher_ |
| 9 | Preencher 'Email' | ${UNIQUE_EMAIL} | _preencher_ |
| 10 | Preencher 'Security Question' | resposta-teste | _preencher_ |
| 11 | Preencher 'New Password' | Nova@12345 | _preencher_ |
| 12 | Preencher 'Repeat New Password' | Nova@12345 | _preencher_ |
| 13 | Clicar em 'Change' |  | _preencher_ |
| 14 | Abrir a rota /#/login |  | _preencher_ |
| 15 | Preencher 'Email' | ${UNIQUE_EMAIL} | _preencher_ |
| 16 | Preencher 'Password' | Nova@12345 | _preencher_ |
| 17 | Clicar em 'Login' |  | _preencher_ |

### CEN-IDT-27 — Recuperação de senha com e-mail não cadastrado

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-27 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Recuperação de senha com e-mail não cadastrado |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — dados inválidos |
| Cenário de origem | CEN-IDT-10 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | URL contém `/#/forgot-password` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | E-mail inexistente. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Sem conta, não há pergunta de segurança a responder. |
| Requisito candidato (opcional) | O sistema não deve permitir redefinição de senha para e-mail sem conta. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/forgot-password |  | _preencher_ |
| 2 | Preencher 'Email' | nao-existe-${UNIQUE_EMAIL} | _preencher_ |
| 3 | Verificar que 'Button to confirm the changes' está desabilitado |  | _preencher_ |

### CEN-IDT-28 — Cadastro com Enter em vez do botão

| Campo | Valor |
|---|---|
| ID do cenário | CEN-IDT-28 |
| Domínio | IDT (Gestão de Identidade e Usuários) |
| Nome do cenário | Cadastro com Enter em vez do botão |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — interação diferente |
| Cenário de origem | CEN-IDT-01 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | URL contém `/#/login` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Mesmos dados válidos do CEN-IDT-01. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Usuários de teclado esperam enviar formulários com Enter. |
| Requisito candidato (opcional) | O sistema deve aceitar a submissão do cadastro pelo teclado. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Se permanecer em /#/register, registrar como comportamento observado (não é falha da aplicação por si só).

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/register |  | _preencher_ |
| 2 | Preencher 'Email address' | ${UNIQUE_EMAIL} | _preencher_ |
| 3 | Preencher 'Password' | Teste@12345 | _preencher_ |
| 4 | Preencher 'Repeat Password' | Teste@12345 | _preencher_ |
| 5 | Selecionar em 'Security Question' | Your favorite book? | _preencher_ |
| 6 | Preencher 'Answer' | a | _preencher_ |
| 7 | Pressionar Enter em 'Answer' |  | _preencher_ |


## CAT (Catálogo de Produtos)

### CEN-CAT-18 — Busca sem diferenciar maiúsculas

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-18 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Busca sem diferenciar maiúsculas |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — entrada variante |
| Cenário de origem | CEN-CAT-03 |
| Pré-condição (estado inicial) | Catálogo disponível. |
| Resultado esperado (critério verificável) | texto contém `Apple Juice` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Termo 'APPLE'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O cliente não deve precisar acertar a caixa das letras. |
| Requisito candidato (opcional) | A busca deve ignorar diferença entre maiúsculas e minúsculas. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/search |  | _preencher_ |
| 2 | Preencher 'Search' | APPLE | _preencher_ |
| 3 | Pressionar Enter em 'Search' |  | _preencher_ |

### CEN-CAT-19 — Busca com termo muito longo

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-19 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Busca com termo muito longo |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — entrada limite |
| Cenário de origem | CEN-CAT-05 |
| Pré-condição (estado inicial) | Catálogo disponível. |
| Resultado esperado (critério verificável) | texto contém `No results found` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | 'suco' repetido até 300 caracteres. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | A interface não pode travar com entradas grandes. |
| Requisito candidato (opcional) | A busca deve responder sem erro a termos longos, informando ausência de resultados. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/search |  | _preencher_ |
| 2 | Preencher 'Search' | sucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosucosuco | _preencher_ |
| 3 | Pressionar Enter em 'Search' |  | _preencher_ |

### CEN-CAT-20 — Busca só com espaços

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-20 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Busca só com espaços |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — formulário vazio |
| Cenário de origem | CEN-CAT-08 |
| Pré-condição (estado inicial) | Catálogo disponível. |
| Resultado esperado (critério verificável) | URL contém `/#/search` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | '   '. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Busca vazia deve ter comportamento previsível (todos os produtos ou nenhum). |
| Requisito candidato (opcional) | A busca deve tratar termo em branco de forma definida. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Registrar se lista todos os produtos ou mostra 'No results found'.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/search |  | _preencher_ |
| 2 | Preencher 'Search' |     | _preencher_ |
| 3 | Pressionar Enter em 'Search' |  | _preencher_ |

### CEN-CAT-21 — Tentar avaliar produto sem login

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-21 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Tentar avaliar produto sem login |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — ação sem login |
| Cenário de origem | CEN-CAT-12 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | texto contém `Reviews`; texto NÃO contém `Write a review` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Texto 'Ótimo suco'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Avaliação deve ter autor identificado. |
| Requisito candidato (opcional) | O sistema deve exigir autenticação para publicar avaliações de produto. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Observado na v20.3.0: para visitante, o detalhe mostra as avaliações mas não exibe o formulário 'Write a review'.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'Apple Juice (1000ml)' |  | _preencher_ |

### CEN-CAT-22 — Publicar avaliação de produto

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-22 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Publicar avaliação de produto |
| Ator | Cliente autenticado |
| Fluxo | Principal (ausente no catálogo atual) |
| Cenário de origem | CEN-CAT-12 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | texto contém `review has been saved` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Texto 'Suco muito bom - teste AMBOLS'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Avaliações ajudam outros clientes a escolher sucos. |
| Requisito candidato (opcional) | O sistema deve permitir que cliente autenticado publique avaliação de produto. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: O rótulo do campo de avaliação deve ser confirmado na primeira execução.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'Apple Juice (1000ml)' |  | _preencher_ |
| 3 | Preencher 'Text field to review a product' | Suco muito bom - teste AMBOLS | _preencher_ |
| 4 | Clicar em 'Send the review' |  | _preencher_ |

### CEN-CAT-23 — Avaliação vazia

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-23 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Avaliação vazia |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — formulário incompleto |
| Cenário de origem | CEN-CAT-22 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | texto contém `Write a review` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Nenhum texto. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Avaliação sem conteúdo não tem valor. |
| Requisito candidato (opcional) | O sistema deve impedir o envio de avaliação vazia. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'Apple Juice (1000ml)' |  | _preencher_ |
| 3 | Verificar que 'Send the review' está desabilitado |  | _preencher_ |

### CEN-CAT-24 — Produto que não é suco à venda (obra de arte)

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-24 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Produto que não é suco à venda (obra de arte) |
| Ator | Visitante não autenticado |
| Fluxo | Incoerente com loja de sucos |
| Cenário de origem | CEN-CAT-02 |
| Pré-condição (estado inicial) | Catálogo disponível. |
| Resultado esperado (critério verificável) | texto contém `Artwork` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Produto 'Best Juice Shop Salesman Artwork' (5000¤). |
| Coerente com loja de sucos? | Não. |
| Justificativa | Uma obra de arte de 5000¤ não pertence ao domínio de uma loja de sucos; é comportamento a registrar. |
| Requisito candidato (opcional) | (Nenhum — registrar como item fora do domínio de negócio.) |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/search |  | _preencher_ |
| 2 | Preencher 'Search' | Artwork | _preencher_ |
| 3 | Pressionar Enter em 'Search' |  | _preencher_ |
| 4 | Clicar em 'Best Juice Shop Salesman Artwork' |  | _preencher_ |

### CEN-CAT-25 — Produto 'Permafrost 2020 Edition' com preço desproporcional

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-25 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Produto 'Permafrost 2020 Edition' com preço desproporcional |
| Ator | Visitante não autenticado |
| Fluxo | Incoerente com loja de sucos |
| Cenário de origem | CEN-CAT-11 |
| Pré-condição (estado inicial) | Catálogo disponível. |
| Resultado esperado (critério verificável) | texto contém `Permafrost`; texto contém `9999.99` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Termo 'Permafrost'. |
| Coerente com loja de sucos? | Não. |
| Justificativa | Preço e natureza do item não condizem com sucos; registrar sem investigar. |
| Requisito candidato (opcional) | (Nenhum — registrar como item fora do domínio de negócio.) |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/search |  | _preencher_ |
| 2 | Preencher 'Search' | Permafrost | _preencher_ |
| 3 | Pressionar Enter em 'Search' |  | _preencher_ |

### CEN-CAT-26 — Troca de idioma da loja

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-26 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Troca de idioma da loja |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — estado da interface |
| Cenário de origem | CEN-CAT-01 |
| Pré-condição (estado inicial) | Catálogo em inglês. |
| Resultado esperado (critério verificável) | texto contém `Seu Carrinho`; texto contém `Adicionar ao carrinho` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Idioma 'Português (Brasil)'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Cliente brasileiro deve conseguir ler a loja em português. |
| Requisito candidato (opcional) | O sistema deve permitir trocar o idioma da interface mantendo o catálogo. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: O cenário volta para English no fim: o navegador da suíte é compartilhado e o idioma fica salvo em cookie.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'button[aria-label='Language selection menu']' |  | _preencher_ |
| 3 | Clicar em 'mat-radio-button:has-text('Português (Brasil)') label' |  | _preencher_ |
| 4 | Clicar em 'button[aria-label='Language selection menu']' |  | _preencher_ |
| 5 | Clicar em 'mat-radio-button:has-text('English') label' |  | _preencher_ |

### CEN-CAT-27 — Mural de fotos (Photo Wall)

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-27 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Mural de fotos (Photo Wall) |
| Ator | Visitante não autenticado |
| Fluxo | Incoerente com loja de sucos |
| Cenário de origem | CEN-CAT-01 |
| Pré-condição (estado inicial) | Catálogo disponível. |
| Resultado esperado (critério verificável) | URL contém `/#/photo-wall`; texto contém `Photo Wall`; texto contém `bkimminich`; texto NÃO contém `Share a memory` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Parcial. |
| Justificativa | Rede social de fotos não é função de venda de sucos; pode ser marketing. |
| Requisito candidato (opcional) | (Registrar como funcionalidade periférica.) |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Observado na v20.3.0: visitante vê o mural, mas o formulário 'Share a memory' só aparece com login.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/photo-wall |  | _preencher_ |

### CEN-CAT-28 — Chat com IA na loja

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-28 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Chat com IA na loja |
| Ator | Visitante não autenticado |
| Fluxo | Incoerente com loja de sucos |
| Cenário de origem | CEN-CAT-01 |
| Pré-condição (estado inicial) | Catálogo disponível. |
| Resultado esperado (critério verificável) | texto contém `Chat` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Parcial. |
| Justificativa | Atendimento por chat pode ser coerente; registrar apenas o comportamento visível, sem testar o bot. |
| Requisito candidato (opcional) | (Registrar como funcionalidade periférica.) |
| Escopo | Em escopo só para observação da tela; interações de manipulação do bot são fora de escopo. |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'Open side menu' |  | _preencher_ |
| 3 | Clicar em 'AI Chat' |  | _preencher_ |

### CEN-CAT-29 — Página 'About Us'

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAT-29 |
| Domínio | CAT (Catálogo de Produtos) |
| Nome do cenário | Página 'About Us' |
| Ator | Visitante não autenticado |
| Fluxo | Principal (ausente no catálogo atual) |
| Cenário de origem | CEN-CAT-01 |
| Pré-condição (estado inicial) | Catálogo disponível. |
| Resultado esperado (critério verificável) | texto contém `About Us`; texto contém `Corporate History` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Informação institucional da loja. |
| Requisito candidato (opcional) | O sistema deve apresentar informações institucionais da loja. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/about |  | _preencher_ |


## CAR (Carrinho de Compras)

### CEN-CAR-08 — Aumentar quantidade com verificação do total

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAR-08 |
| Domínio | CAR (Carrinho de Compras) |
| Nome do cenário | Aumentar quantidade com verificação do total |
| Ator | Cliente autenticado |
| Fluxo | Principal (corrige CEN-CAR-03) |
| Cenário de origem | CEN-CAR-03 |
| Pré-condição (estado inicial) | Cliente autenticado; há pelo menos um produto no carrinho (conta nova: 1 unidade de Apple Juice). |
| Resultado esperado (critério verificável) | texto contém `3.98` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Apple Juice 1.99¤. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O CEN-CAR-03 atual passa por coincidência (o '2' de 'v20.3.0'); este cenário verifica o total. |
| Requisito candidato (opcional) | O sistema deve recalcular o total quando a quantidade de um item muda. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: O seletor do botão '+' deve ser confirmado: a evidência atual mostra que 'Increase quantity' abriu o menu lateral.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket |  | _preencher_ |
| 2 | Clicar em 'button:has(svg.fa-plus-square)' |  | _preencher_ |

### CEN-CAR-09 — Diminuir quantidade abaixo de 1

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAR-09 |
| Domínio | CAR (Carrinho de Compras) |
| Nome do cenário | Diminuir quantidade abaixo de 1 |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — limite inferior |
| Cenário de origem | CEN-CAR-03 |
| Pré-condição (estado inicial) | Cliente autenticado; há pelo menos um produto no carrinho (1 unidade). |
| Resultado esperado (critério verificável) | texto NÃO contém `-1` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Quantidade zero ou negativa não faz sentido num pedido. |
| Requisito candidato (opcional) | O sistema não deve permitir quantidade menor que 1 (ou deve remover o item). |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Registrar se o item continua com 1 ou é removido.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket |  | _preencher_ |
| 2 | Clicar em 'button:has(svg.fa-minus-square)' |  | _preencher_ |

### CEN-CAR-10 — Exceder limite de unidades por produto

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAR-10 |
| Domínio | CAR (Carrinho de Compras) |
| Nome do cenário | Exceder limite de unidades por produto |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — regra de negócio |
| Cenário de origem | CEN-CAR-03 |
| Pré-condição (estado inicial) | Cliente autenticado; carrinho vazio. |
| Resultado esperado (critério verificável) | texto contém `only up to` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Apple Juice, 6 cliques em 'Add to Basket'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Limite por pedido é regra comum em lojas. |
| Requisito candidato (opcional) | O sistema deve limitar a quantidade de unidades de um mesmo produto por pedido e avisar o cliente. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Hipótese: limite de 5 unidades. O primeiro botão 'Add to Basket' deve ser o do Apple Juice.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'Add to Basket' |  | _preencher_ |
| 3 | Clicar em 'Add to Basket' |  | _preencher_ |
| 4 | Clicar em 'Add to Basket' |  | _preencher_ |
| 5 | Clicar em 'Add to Basket' |  | _preencher_ |
| 6 | Clicar em 'Add to Basket' |  | _preencher_ |
| 7 | Clicar em 'Add to Basket' |  | _preencher_ |

### CEN-CAR-11 — Exceder o limite de 1 unidade de um produto restrito

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAR-11 |
| Domínio | CAR (Carrinho de Compras) |
| Nome do cenário | Exceder o limite de 1 unidade de um produto restrito |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — regra de negócio |
| Cenário de origem | CEN-CAR-01 |
| Pré-condição (estado inicial) | Cliente autenticado; carrinho vazio (conta nova). |
| Resultado esperado (critério verificável) | texto contém `You can order only up to 1 items of this product` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Produto Permafrost (9999.99¤). |
| Coerente com loja de sucos? | Sim. |
| Justificativa | A loja não pode vender mais do que o limite definido para o produto. |
| Requisito candidato (opcional) | O sistema deve impedir a inclusão acima do limite por cliente e avisar o cliente. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Observado na v20.3.0: o aviso 'Only N left' do Berry Juice não bloqueia a inclusão (5 unidades entraram com 'Only 3 left'); o limite só aparece em produtos com restrição por cliente, como o Permafrost.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/search |  | _preencher_ |
| 2 | Preencher 'Search' | Permafrost | _preencher_ |
| 3 | Pressionar Enter em 'Search' |  | _preencher_ |
| 4 | Clicar em 'Add to Basket' |  | _preencher_ |
| 5 | Clicar em 'Add to Basket' |  | _preencher_ |

### CEN-CAR-12 — Adicionar o mesmo produto duas vezes

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAR-12 |
| Domínio | CAR (Carrinho de Compras) |
| Nome do cenário | Adicionar o mesmo produto duas vezes |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — repetição |
| Cenário de origem | CEN-CAR-01 |
| Pré-condição (estado inicial) | Cliente autenticado; carrinho vazio. |
| Resultado esperado (critério verificável) | texto contém `3.98` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Apple Juice. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O carrinho deve somar a quantidade, não duplicar a linha. |
| Requisito candidato (opcional) | O sistema deve acumular a quantidade quando o mesmo produto é adicionado de novo. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'Add to Basket' |  | _preencher_ |
| 3 | Clicar em 'Add to Basket' |  | _preencher_ |
| 4 | Abrir a rota /#/basket |  | _preencher_ |

### CEN-CAR-13 — Carrinho anônimo e login em seguida

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAR-13 |
| Domínio | CAR (Carrinho de Compras) |
| Nome do cenário | Carrinho anônimo e login em seguida |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — mudança de estado de acesso |
| Cenário de origem | CEN-CAR-07 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | texto contém `Your Basket` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Apple Juice; conta do cenário. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O cliente espera não perder o que escolheu antes de entrar. |
| Requisito candidato (opcional) | O sistema deve definir o que acontece com o carrinho anônimo após a autenticação. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Registrar se o Apple Juice anônimo aparece no carrinho do cliente após o login.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'Add to Basket' |  | _preencher_ |
| 3 | Abrir a rota /#/basket |  | _preencher_ |
| 4 | Abrir a rota /#/register |  | _preencher_ |
| 5 | Preencher 'Email address' | ${UNIQUE_EMAIL} | _preencher_ |
| 6 | Preencher 'Password' | Teste@12345 | _preencher_ |
| 7 | Preencher 'Repeat Password' | Teste@12345 | _preencher_ |
| 8 | Selecionar em 'Security Question' | Your favorite book? | _preencher_ |
| 9 | Preencher 'Answer' | resposta-teste | _preencher_ |
| 10 | Clicar em 'Register' |  | _preencher_ |
| 11 | Abrir a rota /#/login |  | _preencher_ |
| 12 | Preencher 'Email' | ${UNIQUE_EMAIL} | _preencher_ |
| 13 | Preencher 'Password' | Teste@12345 | _preencher_ |
| 14 | Clicar em 'Login' |  | _preencher_ |
| 15 | Abrir a rota /#/basket |  | _preencher_ |

### CEN-CAR-14 — Checkout com carrinho anônimo

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAR-14 |
| Domínio | CAR (Carrinho de Compras) |
| Nome do cenário | Checkout com carrinho anônimo |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — ação sem login |
| Cenário de origem | CEN-CHK-01 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | texto NÃO contém `Select an address` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Apple Juice. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Compra precisa de cliente identificado (endereço, pagamento). |
| Requisito candidato (opcional) | O sistema deve exigir autenticação antes de prosseguir para o checkout. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Registrar se a interface leva ao login, mostra erro ou bloqueia o botão.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ |  | _preencher_ |
| 2 | Clicar em 'Add to Basket' |  | _preencher_ |
| 3 | Abrir a rota /#/basket |  | _preencher_ |
| 4 | Clicar em 'Checkout' |  | _preencher_ |

### CEN-CAR-15 — Checkout com carrinho vazio

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CAR-15 |
| Domínio | CAR (Carrinho de Compras) |
| Nome do cenário | Checkout com carrinho vazio |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — estado vazio |
| Cenário de origem | CEN-CHK-01 |
| Pré-condição (estado inicial) | Cliente autenticado; carrinho vazio. |
| Resultado esperado (critério verificável) | texto contém `Total Price: 0` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Não há pedido sem itens. |
| Requisito candidato (opcional) | O sistema não deve permitir iniciar checkout com carrinho vazio. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket |  | _preencher_ |
| 2 | Verificar que 'Checkout' está desabilitado |  | _preencher_ |


## CHK (Checkout e Pedidos)

### CEN-CHK-29 — Endereço sem cidade

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-29 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Endereço sem cidade |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — formulário incompleto |
| Cenário de origem | CEN-CHK-02 |
| Pré-condição (estado inicial) | Cliente autenticado; formulário de novo endereço aberto (sem carrinho exigido). |
| Resultado esperado (critério verificável) | URL contém `/#/address/create` — confiança: **alta** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Endereço completo exceto City. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Entrega exige endereço completo. |
| Requisito candidato (opcional) | O sistema deve exigir o campo City no cadastro de endereço. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create |  | _preencher_ |
| 2 | Preencher 'Country' | Brazil | _preencher_ |
| 3 | Preencher 'Name' | Cliente Alternativo | _preencher_ |
| 4 | Preencher 'Mobile Number' | 8599999999 | _preencher_ |
| 5 | Preencher 'ZIP Code' | 60000000 | _preencher_ |
| 6 | Preencher 'Address' | Rua Alternativa, 200 | _preencher_ |
| 7 | Preencher 'State' | CE | _preencher_ |
| 8 | Verificar que 'Submit' está desabilitado |  | _preencher_ |

### CEN-CHK-30 — Endereço sem celular

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-30 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Endereço sem celular |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — formulário incompleto |
| Cenário de origem | CEN-CHK-02 |
| Pré-condição (estado inicial) | Cliente autenticado; formulário de novo endereço aberto (sem carrinho exigido). |
| Resultado esperado (critério verificável) | URL contém `/#/address/create` — confiança: **alta** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Endereço completo exceto Mobile Number. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Entrega exige endereço completo. |
| Requisito candidato (opcional) | O sistema deve exigir o campo Mobile Number no cadastro de endereço. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create |  | _preencher_ |
| 2 | Preencher 'Country' | Brazil | _preencher_ |
| 3 | Preencher 'Name' | Cliente Alternativo | _preencher_ |
| 4 | Preencher 'ZIP Code' | 60000000 | _preencher_ |
| 5 | Preencher 'Address' | Rua Alternativa, 200 | _preencher_ |
| 6 | Preencher 'City' | Fortaleza | _preencher_ |
| 7 | Preencher 'State' | CE | _preencher_ |
| 8 | Verificar que 'Submit' está desabilitado |  | _preencher_ |

### CEN-CHK-31 — Endereço sem país

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-31 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Endereço sem país |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — formulário incompleto |
| Cenário de origem | CEN-CHK-02 |
| Pré-condição (estado inicial) | Cliente autenticado; formulário de novo endereço aberto (sem carrinho exigido). |
| Resultado esperado (critério verificável) | URL contém `/#/address/create` — confiança: **alta** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Endereço completo exceto Country. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Entrega exige endereço completo. |
| Requisito candidato (opcional) | O sistema deve exigir o campo Country no cadastro de endereço. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create |  | _preencher_ |
| 2 | Preencher 'Name' | Cliente Alternativo | _preencher_ |
| 3 | Preencher 'Mobile Number' | 8599999999 | _preencher_ |
| 4 | Preencher 'ZIP Code' | 60000000 | _preencher_ |
| 5 | Preencher 'Address' | Rua Alternativa, 200 | _preencher_ |
| 6 | Preencher 'City' | Fortaleza | _preencher_ |
| 7 | Preencher 'State' | CE | _preencher_ |
| 8 | Verificar que 'Submit' está desabilitado |  | _preencher_ |

### CEN-CHK-32 — Endereço com celular em formato inválido

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-32 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Endereço com celular em formato inválido |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — dados inválidos |
| Cenário de origem | CEN-CHK-02 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | URL contém `/#/address/create` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Mobile Number '123'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Telefone de contato é usado na entrega. |
| Requisito candidato (opcional) | O sistema deve validar o formato do telefone do endereço. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create |  | _preencher_ |
| 2 | Preencher 'Country' | Brazil | _preencher_ |
| 3 | Preencher 'Name' | Cliente Alternativo | _preencher_ |
| 4 | Preencher 'Mobile Number' | 123 | _preencher_ |
| 5 | Preencher 'ZIP Code' | 60000000 | _preencher_ |
| 6 | Preencher 'Address' | Rua Alternativa, 200 | _preencher_ |
| 7 | Preencher 'City' | Fortaleza | _preencher_ |
| 8 | Preencher 'State' | CE | _preencher_ |
| 9 | Pressionar Tab em 'Mobile Number' |  | _preencher_ |
| 10 | Verificar que 'Submit' está desabilitado |  | _preencher_ |

### CEN-CHK-33 — Endereço com CEP acima do tamanho

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-33 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Endereço com CEP acima do tamanho |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — dados inválidos |
| Cenário de origem | CEN-CHK-02 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | URL contém `/#/address/create` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | ZIP '123456789012'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | CEP deve ter tamanho válido. |
| Requisito candidato (opcional) | O sistema deve limitar o tamanho do CEP. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create |  | _preencher_ |
| 2 | Preencher 'Country' | Brazil | _preencher_ |
| 3 | Preencher 'Name' | Cliente Alternativo | _preencher_ |
| 4 | Preencher 'Mobile Number' | 8599999999 | _preencher_ |
| 5 | Preencher 'ZIP Code' | 123456789012 | _preencher_ |
| 6 | Preencher 'Address' | Rua Alternativa, 200 | _preencher_ |
| 7 | Preencher 'City' | Fortaleza | _preencher_ |
| 8 | Preencher 'State' | CE | _preencher_ |
| 9 | Pressionar Tab em 'ZIP Code' |  | _preencher_ |
| 10 | Verificar que 'Submit' está desabilitado |  | _preencher_ |

### CEN-CHK-34 — Cartão com número incompleto

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-34 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Cartão com número incompleto |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — dados inválidos |
| Cenário de origem | CEN-CHK-07 |
| Pré-condição (estado inicial) | Cliente autenticado; método de entrega selecionado. |
| Resultado esperado (critério verificável) | URL contém `/#/payment/shop` — confiança: **alta** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Número '400000000000'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Cartão inválido não pode ser salvo. |
| Requisito candidato (opcional) | O sistema deve exigir número de cartão com 16 dígitos. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop |  | _preencher_ |
| 2 | Clicar em 'Add new card' |  | _preencher_ |
| 3 | Preencher 'Name' | Cliente Teste | _preencher_ |
| 4 | Preencher 'Card Number' | 400000000000 | _preencher_ |
| 5 | Selecionar em 'Expiry Month' | 12 | _preencher_ |
| 6 | Selecionar em 'Expiry Year' | 2090 | _preencher_ |
| 7 | Verificar que 'Submit' está desabilitado |  | _preencher_ |

### CEN-CHK-35 — Cartão sem validade

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-35 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Cartão sem validade |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — formulário incompleto |
| Cenário de origem | CEN-CHK-07 |
| Pré-condição (estado inicial) | Cliente autenticado; método de entrega selecionado. |
| Resultado esperado (critério verificável) | URL contém `/#/payment/shop` — confiança: **alta** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Nome e número válidos. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Validade é obrigatória para pagamento. |
| Requisito candidato (opcional) | O sistema deve exigir mês e ano de validade do cartão. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop |  | _preencher_ |
| 2 | Clicar em 'Add new card' |  | _preencher_ |
| 3 | Preencher 'Name' | Cliente Teste | _preencher_ |
| 4 | Preencher 'Card Number' | 4000000000000002 | _preencher_ |
| 5 | Verificar que 'Submit' está desabilitado |  | _preencher_ |

### CEN-CHK-36 — Resgatar cupom vazio

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-36 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Resgatar cupom vazio |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — formulário incompleto |
| Cenário de origem | CEN-CHK-15 |
| Pré-condição (estado inicial) | Cliente autenticado; etapa de pagamento acessível; campo de cupom disponível. |
| Resultado esperado (critério verificável) | URL contém `/#/payment/shop` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Evita requisição sem dado. |
| Requisito candidato (opcional) | O sistema deve impedir o resgate de cupom sem código. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop |  | _preencher_ |
| 2 | Clicar em 'Add a coupon' |  | _preencher_ |
| 3 | Verificar que 'Redeem' está desabilitado |  | _preencher_ |

### CEN-CHK-37 — Entrega rápida altera o total do resumo

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-37 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Entrega rápida altera o total do resumo |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — escolha diferente |
| Cenário de origem | CEN-CHK-05 |
| Pré-condição (estado inicial) | Cliente autenticado; carrinho contém produto; endereço Rua Teste, 100 cadastrado; método de entrega disponível; cartão de teste terminado em 0002 cadastrado. |
| Resultado esperado (critério verificável) | URL contém `/#/order-summary`; texto contém `Delivery`; texto contém `0.99` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Método 'One Day Delivery'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Cliente paga mais para receber antes. |
| Requisito candidato (opcional) | O sistema deve somar o custo do método de entrega escolhido ao total do pedido. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket |  | _preencher_ |
| 2 | Clicar em 'Checkout' |  | _preencher_ |
| 3 | Clicar em 'Rua Teste, 100' |  | _preencher_ |
| 4 | Clicar em 'Continue' |  | _preencher_ |
| 5 | Clicar em 'One Day Delivery' |  | _preencher_ |
| 6 | Clicar em 'Continue' |  | _preencher_ |
| 7 | Clicar em '0002' |  | _preencher_ |
| 8 | Clicar em 'Continue' |  | _preencher_ |

### CEN-CHK-38 — Pular etapas: abrir resumo do pedido direto

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-38 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Pular etapas: abrir resumo do pedido direto |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — contra o fluxo |
| Cenário de origem | CEN-CHK-10 |
| Pré-condição (estado inicial) | Cliente autenticado; carrinho contém produto; nenhuma etapa do checkout concluída nesta sessão. |
| Resultado esperado (critério verificável) | texto NÃO contém `Thank you for your purchase` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | A loja não deve aceitar pedido sem endereço, entrega e pagamento. |
| Requisito candidato (opcional) | O sistema deve impedir a confirmação do pedido sem as etapas obrigatórias concluídas. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Não clicar em concluir se o botão parecer liberado; registrar o estado da tela (fora de escopo investigar desvio).

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/order-summary |  | _preencher_ |

### CEN-CHK-39 — Pagar com carteira digital sem saldo

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-39 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Pagar com carteira digital sem saldo |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — saldo insuficiente |
| Cenário de origem | CEN-CHK-09 |
| Pré-condição (estado inicial) | Cliente autenticado (conta nova, saldo 0); método de entrega selecionado. |
| Resultado esperado (critério verificável) | texto contém `Pay using wallet`; texto contém `Wallet Balance` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Não se paga com saldo inexistente. |
| Requisito candidato (opcional) | O sistema deve impedir pagamento pela carteira sem saldo suficiente. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Registrar se a opção de carteira aparece desabilitada ou se o avanço falha com mensagem.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop |  | _preencher_ |

### CEN-CHK-40 — Acessar pagamento sem login

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-40 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Acessar pagamento sem login |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — ação sem login |
| Cenário de origem | CEN-CHK-07 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | texto contém `My Payment Options`; texto NÃO contém `0002` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Cartões salvos são dados pessoais. |
| Requisito candidato (opcional) | O sistema deve exigir autenticação para exibir a etapa de pagamento. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Observado na v20.3.0: a etapa de pagamento abre sem login (sem cartões e com avanço bloqueado). Registrar como achado de coerência.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop |  | _preencher_ |
| 2 | Verificar que 'Proceed to review' está desabilitado |  | _preencher_ |

### CEN-CHK-41 — Rastrear pedido inexistente

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-41 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Rastrear pedido inexistente |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — dados inválidos |
| Cenário de origem | CEN-CHK-19 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | URL contém `/#/track-result`; texto contém `pedido-inexistente-000`; texto contém `? Days` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | id 'pedido-inexistente-000'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O cliente precisa saber que o código está errado. |
| Requisito candidato (opcional) | O sistema deve informar quando o código de rastreamento não corresponde a pedido algum. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Observado na v20.3.0: não há mensagem de pedido inexistente; a tela mostra '? Days' e o marcador não renderizado {{bonus}}. Não variar o id para descobrir pedidos de terceiros (fora de escopo).

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/track-result?id=pedido-inexistente-000 |  | _preencher_ |

### CEN-CHK-42 — Histórico de pedidos de cliente sem compras

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-42 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Histórico de pedidos de cliente sem compras |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — estado vazio |
| Cenário de origem | CEN-CHK-17 |
| Pré-condição (estado inicial) | Conta criada no cenário, sem pedidos. |
| Resultado esperado (critério verificável) | texto contém `You have not placed any orders yet` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Tela vazia precisa ser compreensível. |
| Requisito candidato (opcional) | O sistema deve informar que o cliente ainda não possui pedidos. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/register |  | _preencher_ |
| 2 | Preencher 'Email address' | ${UNIQUE_EMAIL} | _preencher_ |
| 3 | Preencher 'Password' | Teste@12345 | _preencher_ |
| 4 | Preencher 'Repeat Password' | Teste@12345 | _preencher_ |
| 5 | Selecionar em 'Security Question' | Your favorite book? | _preencher_ |
| 6 | Preencher 'Answer' | resposta-teste | _preencher_ |
| 7 | Clicar em 'Register' |  | _preencher_ |
| 8 | Abrir a rota /#/login |  | _preencher_ |
| 9 | Preencher 'Email' | ${UNIQUE_EMAIL} | _preencher_ |
| 10 | Preencher 'Password' | Teste@12345 | _preencher_ |
| 11 | Clicar em 'Login' |  | _preencher_ |
| 12 | Abrir a rota /#/order-history |  | _preencher_ |

### CEN-CHK-43 — Opções de pagamento em criptomoeda

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-43 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Opções de pagamento em criptomoeda |
| Ator | Cliente autenticado |
| Fluxo | Incoerente com loja de sucos |
| Cenário de origem | CEN-CHK-12 |
| Pré-condição (estado inicial) | Cliente autenticado; etapa de pagamento acessível; seção 'Other payment options' disponível. |
| Resultado esperado (critério verificável) | texto contém `Other payment options` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Não. |
| Justificativa | Doações e loja de camisetas não fazem parte da compra de sucos; registrar sem clicar. |
| Requisito candidato (opcional) | (Registrar como elementos fora do domínio.) |
| Escopo | Em escopo só para registro; seguir links externos já está coberto em CEN-CHK-13/14. |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop |  | _preencher_ |
| 2 | Clicar em 'Other payment options' |  | _preencher_ |

### CEN-CHK-44 — Assinatura 'Deluxe Membership'

| Campo | Valor |
|---|---|
| ID do cenário | CEN-CHK-44 |
| Domínio | CHK (Checkout e Pedidos) |
| Nome do cenário | Assinatura 'Deluxe Membership' |
| Ator | Cliente autenticado |
| Fluxo | Incoerente com loja de sucos |
| Cenário de origem | CEN-CHK-12 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | texto contém `Deluxe Membership`; texto contém `49` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Parcial. |
| Justificativa | Clube de vantagens é plausível, mas não aparece no fluxo principal de compra. |
| Requisito candidato (opcional) | (Registrar benefícios observados como candidatos a requisito.) |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/deluxe-membership |  | _preencher_ |


## PER (Gestão de Perfil)

### CEN-PER-07 — Alterar nome de usuário

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-07 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Alterar nome de usuário |
| Ator | Cliente autenticado |
| Fluxo | Principal (ausente no catálogo atual) |
| Cenário de origem | CEN-IDT-07 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | texto contém `clienteambols` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Username 'clienteambols'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O CEN-IDT-07 atual só abre a tela de privacidade; não altera dado algum. |
| Requisito candidato (opcional) | O sistema deve permitir que o cliente altere seu nome de usuário. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: O perfil é servido em /profile (fora do roteador /#/).

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /profile |  | _preencher_ |
| 2 | Preencher 'Text field for the username' | clienteambols | _preencher_ |
| 3 | Clicar em 'Button to save/set the username' |  | _preencher_ |

### CEN-PER-08 — Adicionar endereço pela área de perfil

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-08 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Adicionar endereço pela área de perfil |
| Ator | Cliente autenticado |
| Fluxo | Principal (ausente no catálogo atual) |
| Cenário de origem | CEN-PER-02 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | texto contém `Rua Alternativa, 200` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Endereço 'Rua Alternativa, 200'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Gerenciar endereços fora do checkout é previsto no guia (PER). |
| Requisito candidato (opcional) | O sistema deve permitir cadastrar endereço pela área do cliente. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create |  | _preencher_ |
| 2 | Preencher 'Country' | Brazil | _preencher_ |
| 3 | Preencher 'Name' | Cliente Alternativo | _preencher_ |
| 4 | Preencher 'Mobile Number' | 8599999999 | _preencher_ |
| 5 | Preencher 'ZIP Code' | 60000000 | _preencher_ |
| 6 | Preencher 'Address' | Rua Alternativa, 200 | _preencher_ |
| 7 | Preencher 'City' | Fortaleza | _preencher_ |
| 8 | Preencher 'State' | CE | _preencher_ |
| 9 | Clicar em 'Submit' |  | _preencher_ |
| 10 | Abrir a rota /#/address/saved |  | _preencher_ |

### CEN-PER-09 — Editar endereço salvo

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-09 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Editar endereço salvo |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — atualização de dados |
| Cenário de origem | CEN-PER-08 |
| Pré-condição (estado inicial) | Cliente autenticado; o próprio cenário cadastra o endereço antes de editar. |
| Resultado esperado (critério verificável) | texto contém `Cliente Editado` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Nome 'Cliente Editado'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Atualização de dados cadastrais é fluxo alternativo exigido na Etapa 1. |
| Requisito candidato (opcional) | O sistema deve permitir editar um endereço salvo. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Nome acessível do ícone de edição a confirmar.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create |  | _preencher_ |
| 2 | Preencher 'Country' | Brazil | _preencher_ |
| 3 | Preencher 'Name' | Cliente Alternativo | _preencher_ |
| 4 | Preencher 'Mobile Number' | 8599999999 | _preencher_ |
| 5 | Preencher 'ZIP Code' | 60000000 | _preencher_ |
| 6 | Preencher 'Address' | Rua Alternativa, 200 | _preencher_ |
| 7 | Preencher 'City' | Fortaleza | _preencher_ |
| 8 | Preencher 'State' | CE | _preencher_ |
| 9 | Clicar em 'Submit' |  | _preencher_ |
| 10 | Abrir a rota /#/address/saved |  | _preencher_ |
| 11 | Clicar em 'button:has(svg.fa-edit)' |  | _preencher_ |
| 12 | Preencher 'Name' | Cliente Editado | _preencher_ |
| 13 | Clicar em 'Submit' |  | _preencher_ |

### CEN-PER-10 — Remover endereço salvo

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-10 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Remover endereço salvo |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — exclusão |
| Cenário de origem | CEN-PER-08 |
| Pré-condição (estado inicial) | Cliente autenticado; o próprio cenário cadastra o endereço antes de remover. |
| Resultado esperado (critério verificável) | texto NÃO contém `Rua Alternativa, 200` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Cliente deve poder descartar endereço antigo. |
| Requisito candidato (opcional) | O sistema deve permitir remover um endereço salvo. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Registrar o que acontece se o endereço removido era o selecionado num checkout em andamento.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create |  | _preencher_ |
| 2 | Preencher 'Country' | Brazil | _preencher_ |
| 3 | Preencher 'Name' | Cliente Alternativo | _preencher_ |
| 4 | Preencher 'Mobile Number' | 8599999999 | _preencher_ |
| 5 | Preencher 'ZIP Code' | 60000000 | _preencher_ |
| 6 | Preencher 'Address' | Rua Alternativa, 200 | _preencher_ |
| 7 | Preencher 'City' | Fortaleza | _preencher_ |
| 8 | Preencher 'State' | CE | _preencher_ |
| 9 | Clicar em 'Submit' |  | _preencher_ |
| 10 | Abrir a rota /#/address/saved |  | _preencher_ |
| 11 | Clicar em 'button:has(svg.fa-trash-alt)' |  | _preencher_ |

### CEN-PER-11 — Remover cartão salvo

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-11 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Remover cartão salvo |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — exclusão |
| Cenário de origem | CEN-PER-03 |
| Pré-condição (estado inicial) | Cliente autenticado; o próprio cenário cadastra o cartão 0002 antes de remover. |
| Resultado esperado (critério verificável) | texto NÃO contém `0002` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Cliente deve poder apagar meios de pagamento. |
| Requisito candidato (opcional) | O sistema deve permitir remover um cartão salvo. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/saved-payment-methods |  | _preencher_ |
| 2 | Clicar em 'Add new card' |  | _preencher_ |
| 3 | Preencher 'Name' | Cliente Teste | _preencher_ |
| 4 | Preencher 'Card Number' | 4000000000000002 | _preencher_ |
| 5 | Selecionar em 'Expiry Month' | 12 | _preencher_ |
| 6 | Selecionar em 'Expiry Year' | 2090 | _preencher_ |
| 7 | Clicar em 'Submit' |  | _preencher_ |
| 8 | Clicar em 'button:has(svg.fa-trash-alt)' |  | _preencher_ |

### CEN-PER-12 — Perfil sem login

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-12 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Perfil sem login |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — ação sem login |
| Cenário de origem | CEN-PER-01 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | texto contém `Blocked illegal activity`; texto NÃO contém `Set Username` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Dados de perfil são pessoais. |
| Requisito candidato (opcional) | O sistema deve exigir autenticação para exibir o perfil. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Observado na v20.3.0: sem sessão, /profile devolve uma página de erro 500 do servidor ('Blocked illegal activity') em vez de levar ao login. Registrar como achado de usabilidade; não investigar.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /profile |  | _preencher_ |

### CEN-PER-13 — Endereços salvos sem login

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-13 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Endereços salvos sem login |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — ação sem login |
| Cenário de origem | CEN-PER-02 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | texto contém `Please login to view this page` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Endereços são dados pessoais. |
| Requisito candidato (opcional) | O sistema deve exigir autenticação para listar endereços. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/saved |  | _preencher_ |

### CEN-PER-14 — Consultar carteira digital

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-14 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Consultar carteira digital |
| Ator | Cliente autenticado |
| Fluxo | Principal (ausente no catálogo atual) |
| Cenário de origem | CEN-PER-03 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | texto contém `Digital Wallet`; texto contém `Wallet Balance` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Parcial. |
| Justificativa | Carteira com saldo é recurso comum em e-commerce, mas não essencial a uma loja de sucos. |
| Requisito candidato (opcional) | O sistema deve exibir o saldo da carteira do cliente. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/wallet |  | _preencher_ |

### CEN-PER-15 — Enviar feedback ao cliente sem nota

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-15 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Enviar feedback ao cliente sem nota |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — formulário incompleto |
| Cenário de origem | CEN-ADM-03 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | URL contém `/#/contact` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Comentário 'Teste AMBOLS'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Feedback sem nota fica incompleto. |
| Requisito candidato (opcional) | O sistema deve exigir comentário e nota para enviar feedback. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: O formulário tem um CAPTCHA aritmético da própria aplicação; no fluxo completo ele deve ser preenchido manualmente pelo avaliador.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/contact |  | _preencher_ |
| 2 | Preencher 'Comment' | Teste AMBOLS | _preencher_ |
| 3 | Verificar que 'Button to send the review' está desabilitado |  | _preencher_ |

### CEN-PER-16 — Registrar reclamação (Complaint)

| Campo | Valor |
|---|---|
| ID do cenário | CEN-PER-16 |
| Domínio | PER (Gestão de Perfil) |
| Nome do cenário | Registrar reclamação (Complaint) |
| Ator | Cliente autenticado |
| Fluxo | Principal (ausente no catálogo atual) |
| Cenário de origem | CEN-PER-15 |
| Pré-condição (estado inicial) | Cliente autenticado. |
| Resultado esperado (critério verificável) | texto contém `Customer support will get in touch` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | Mensagem 'Pedido chegou incompleto - teste'. |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Canal de reclamação é esperado em loja virtual. |
| Requisito candidato (opcional) | O sistema deve permitir que o cliente registre uma reclamação e receba um número de protocolo. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Não anexar arquivos (upload fica fora de escopo).

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/complain |  | _preencher_ |
| 2 | Preencher 'Message' | Pedido chegou incompleto - teste | _preencher_ |
| 3 | Clicar em 'Button to send the complaint' |  | _preencher_ |


## ADM (Administração)

### CEN-ADM-04 — Cliente comum tenta abrir a administração

| Campo | Valor |
|---|---|
| ID do cenário | CEN-ADM-04 |
| Domínio | ADM (Administração) |
| Nome do cenário | Cliente comum tenta abrir a administração |
| Ator | Cliente autenticado |
| Fluxo | Alternativo — perfil sem permissão |
| Cenário de origem | CEN-ADM-01 |
| Pré-condição (estado inicial) | Cliente autenticado sem perfil administrador. |
| Resultado esperado (critério verificável) | texto contém `You are not allowed to access this page`; texto NÃO contém `Registered Users` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Funções de gestão são restritas. |
| Requisito candidato (opcional) | O sistema deve negar a área administrativa a usuários sem perfil de administrador. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration |  | _preencher_ |

### CEN-ADM-05 — Visitante tenta abrir a administração

| Campo | Valor |
|---|---|
| ID do cenário | CEN-ADM-05 |
| Domínio | ADM (Administração) |
| Nome do cenário | Visitante tenta abrir a administração |
| Ator | Visitante não autenticado |
| Fluxo | Alternativo — ação sem login |
| Cenário de origem | CEN-ADM-01 |
| Pré-condição (estado inicial) | Sem sessão ativa. |
| Resultado esperado (critério verificável) | texto contém `You are not allowed to access this page`; texto NÃO contém `Registered Users` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Funções de gestão são restritas. |
| Requisito candidato (opcional) | O sistema deve negar a área administrativa a visitantes não autenticados. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration |  | _preencher_ |

### CEN-ADM-06 — Ver detalhes de um usuário cadastrado

| Campo | Valor |
|---|---|
| ID do cenário | CEN-ADM-06 |
| Domínio | ADM (Administração) |
| Nome do cenário | Ver detalhes de um usuário cadastrado |
| Ator | Administrador |
| Fluxo | Principal (ausente no catálogo atual) |
| Cenário de origem | CEN-ADM-02 |
| Pré-condição (estado inicial) | Administrador autenticado. |
| Resultado esperado (critério verificável) | texto contém `Email` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O CEN-ADM-02 atual só confirma o título da seção. |
| Requisito candidato (opcional) | O sistema deve permitir ao administrador consultar dados de um usuário. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: O botão de detalhes é um ícone de olho sem rótulo acessível (achado de acessibilidade).

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration |  | _preencher_ |
| 2 | Clicar em 'button:has(svg.fa-eye)' |  | _preencher_ |

### CEN-ADM-07 — Remover feedback de cliente

| Campo | Valor |
|---|---|
| ID do cenário | CEN-ADM-07 |
| Domínio | ADM (Administração) |
| Nome do cenário | Remover feedback de cliente |
| Ator | Administrador |
| Fluxo | Alternativo — gestão de dados |
| Cenário de origem | CEN-ADM-03 |
| Pré-condição (estado inicial) | Administrador autenticado; ao menos 1 feedback. |
| Resultado esperado (critério verificável) | texto contém `Customer Feedback` — confiança: **confirmado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | Moderar feedback é função administrativa. |
| Requisito candidato (opcional) | O sistema deve permitir ao administrador remover feedbacks. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Anotar a contagem de feedbacks antes e depois (mudança de estado).

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration |  | _preencher_ |
| 2 | Clicar em 'button:has(svg.fa-trash-alt)' |  | _preencher_ |

### CEN-ADM-08 — Gerenciar produtos e pedidos como administrador

| Campo | Valor |
|---|---|
| ID do cenário | CEN-ADM-08 |
| Domínio | ADM (Administração) |
| Nome do cenário | Gerenciar produtos e pedidos como administrador |
| Ator | Administrador |
| Fluxo | Lacuna — previsto no guia |
| Cenário de origem | CEN-ADM-01 |
| Pré-condição (estado inicial) | Administrador autenticado. |
| Resultado esperado (critério verificável) | texto contém `You are not allowed to access this page` — confiança: **observado** |
| Resultado observado (mudança de estado) | _preencher na execução_ |
| Mensagens exibidas ao usuário | _preencher na execução_ |
| Dados manipulados | — |
| Coerente com loja de sucos? | Sim. |
| Justificativa | O guia exige 'consultar e gerenciar produtos e pedidos', mas a tela de administração mostra só usuários e feedbacks. |
| Requisito candidato (opcional) | O sistema deve oferecer gestão de produtos e pedidos a um perfil autorizado. |
| Escopo | Em escopo |
| Status de execução | PASSED — 2026-11-28, Juice Shop v20.3.0 |

> Observação: Hipótese: a gestão de estoque/preço e de pedidos fica em /#/accounting, para outro perfil (contabilidade). Registrar a resposta; não tentar obter outra conta.

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration |  | _preencher_ |
| 2 | Abrir a rota /#/accounting |  | _preencher_ |
