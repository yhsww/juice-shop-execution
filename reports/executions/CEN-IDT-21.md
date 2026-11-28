# Ficha de Cenário

**ID do cenário:** CEN-IDT-21
**Domínio:** IDT
**Nome do cenário:** Login com campos vazios
**Ator:** Visitante não autenticado
**Fluxo:** Abrir a tela de login e verificar o botão sem preencher nada; depois preencher só o e-mail.

## Pré-condição (estado inicial)

Sem sessão ativa.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Abrir a tela de login e verificar o botão sem preencher nada; depois preencher só o e-mail.'. A descrição corresponde ao cenário 'Login com campos vazios' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? | exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | or | Log in with Google Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? | Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? | Login | Forgot your password? | Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer?

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer?
- Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer?
- Login
- Forgot your password?
- Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer?
- exit_to_app
- exit_to_app Log in
- Log in
- Remember me
- Not yet a customer?
- Email
- Password visibility
- Password
- visibility
- Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer?
- Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer?
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer?
- or
- Log in with Google

## Dados manipulados

Dados declarados no cenário: Nenhum dado; depois apenas e-mail.
Passo 1: /#/login
Passo 4: cen-cen-idt-21-910ee4993a@example.com

## Coerente com loja de sucos?

Sim.

## Justificativa

Evita envio de tentativa de login sem dados.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Abrir a tela de login e verificar o botão sem preencher nada; depois preencher só o e-mail.'. A descrição corresponde ao cenário 'Login com campos vazios' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/login | /#/login | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? \| exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| or \| Log in with Google Mensagem transitória: menu OWASP Juice Shop s |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? |
| 3 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? |
| 4 | Preencher "Email" | cen-cen-idt-21-910ee4993a@example.com | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Email \| Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? Mensagem transitória: Email \| Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close accou |
| 5 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? |
| 6 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? |
