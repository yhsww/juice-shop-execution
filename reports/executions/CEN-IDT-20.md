# Ficha de Cenário

**ID do cenário:** CEN-IDT-20
**Domínio:** IDT
**Nome do cenário:** Login com e-mail não cadastrado
**Ator:** Visitante não autenticado
**Fluxo:** Informar um e-mail que nunca foi cadastrado e uma senha qualquer.

## Pré-condição (estado inicial)

Sem sessão ativa.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Informar um e-mail que nunca foi cadastrado e uma senha qualquer.'. A descrição corresponde ao cenário 'Login com e-mail não cadastrado' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? | exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | or | Log in with Google Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? | Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? | Login | Forgot your password? | Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer?
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password visibility | Login Invalid email or password. Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Invalid email or password. Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | Invalid email or password. | Email Mensagem transitória: exit_to_app Log in | Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | Password visibility

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer?
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
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer?
- EN
- language EN
- account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
- Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer?

## Dados manipulados

Dados declarados no cenário: E-mail inexistente; senha 'Teste@12345'.
Passo 1: /#/login
Passo 2: nao-existe-cen-cen-idt-20-eb5ce960ed@example.com
Passo 3: Teste@12345

## Coerente com loja de sucos?

Sim.

## Justificativa

O cliente precisa saber que não conseguiu entrar, sem que a loja revele quais e-mails existem.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Informar um e-mail que nunca foi cadastrado e uma senha qualquer.'. A descrição corresponde ao cenário 'Login com e-mail não cadastrado' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/login | /#/login | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? \| exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| or \| Log in with Google Mensagem transitória: menu OWASP Juice Shop s |
| 2 | Preencher "Email" | nao-existe-cen-cen-idt-20-eb5ce960ed@example.com | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Email \| Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? Mensagem transitória: Email \| Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close accou |
| 3 | Preencher "Password" | Teste@12345 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Password visibility \| Password \| exit_to_app Log in Mensagem transitória: Email \| Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Passwo |
| 4 | Clicar em "Login" |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password visibility \| Login Invalid email or password. Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Invalid email or password. Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Invalid email or password. \| Email Mensagem transitória: exit_to_app Log in \| Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close ac |
| 5 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Invalid email or password. Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? |
