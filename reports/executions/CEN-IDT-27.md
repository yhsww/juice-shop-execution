# Ficha de Cenário

**ID do cenário:** CEN-IDT-27
**Domínio:** IDT
**Nome do cenário:** Recuperação de senha com e-mail não cadastrado
**Ator:** Visitante não autenticado
**Fluxo:** Informar e-mail inexistente na recuperação e observar se a pergunta de segurança é liberada.

## Pré-condição (estado inicial)

Sem sessão ativa.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Informar e-mail inexistente na recuperação e observar se a pergunta de segurança é liberada.'. A descrição corresponde ao cenário 'Recuperação de senha com e-mail não cadastrado' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/forgot-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. | 0/20 Repeat New Password 0/20 Show password advice Change Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change | EN | language EN | account_circle Account shopping_cart Your Basket 0 language EN | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change | Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change | Forgot Password | Show password advice | Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change
- Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change
- Forgot Password
- Show password advice
- Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice
- Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change
- Change
- Email help_outline
- Security Question help_outline
- New Password Password must be 5-40 characters long. 0/20
- Repeat New Password 0/20
- New Password
- Repeat New Password
- Email
- help_outline
- Security Question
- Password must be 5-40 characters long. 0/20
- 0/20
- Password must be 5-40 characters long.
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change

## Dados manipulados

Dados declarados no cenário: E-mail inexistente.
Passo 1: /#/forgot-password
Passo 2: nao-existe-cen-cen-idt-27-1c57622267@example.com

## Coerente com loja de sucos?

Sim.

## Justificativa

Sem conta, não há pergunta de segurança a responder.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Informar e-mail inexistente na recuperação e observar se a pergunta de segurança é liberada.'. A descrição corresponde ao cenário 'Recuperação de senha com e-mail não cadastrado' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/forgot-password | /#/forgot-password | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/forgot-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. \| 0/20 Repeat New Password 0/20 Show password advice Change Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| EN \| language EN \| account_circle Account shopping_cart Your Basket 0 language EN \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: me |
| 2 | Preencher "Email" | nao-existe-cen-cen-idt-27-1c57622267@example.com | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Email help_outline \| Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| Email Mensagem transitória: Email help_outline \| Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/ |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change |
| 4 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change |
