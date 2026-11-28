# Ficha de Cenário

**ID do cenário:** CEN-IDT-04
**Domínio:** IDT
**Nome do cenário:** Login com senha inválida
**Ator:** Cliente
**Fluxo:** Informar e-mail válido com senha incorreta.

## Pré-condição (estado inicial)

Conta de teste disponível para autenticação.

## Descrição do cenário

Cliente executa o fluxo 'Informar e-mail válido com senha incorreta.'. A descrição corresponde ao cenário 'Login com senha inválida' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? | exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? Language has been changed to English Force page reload | or | Log in with Google Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? Language has been changed to English Force page reload | Language has been changed to English Force page reload | Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? | Login
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log 

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer?
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? Language has been changed to English Force page reload
- Language has been changed to English Force page reload
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
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? Language has been changed to English Force page reload

## Dados manipulados

Dados declarados no cenário: Senha incorreta: SenhaErrada@123.
Passo 1: /#/login
Passo 2: cen-cen-idt-04-b4702e66ef@example.com
Passo 3: SenhaErrada@123

## Coerente com loja de sucos?

Sim.

## Justificativa

O sistema deve rejeitar credenciais inválidas.

## Descrição funcional do cenário

Cliente executa o fluxo 'Informar e-mail válido com senha incorreta.'. A descrição corresponde ao cenário 'Login com senha inválida' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/login | /#/login | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? \| exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your B |
| 2 | Preencher "Email" | cen-cen-idt-04-b4702e66ef@example.com | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? Language has been changed to English Force page reload \| Language has been changed to English Force page reload \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it!  |
| 3 | Preencher "Password" | SenhaErrada@123 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Password visibility \| Password \| exit_to_app Log in Mensagem transitória: Email \| Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website u |
| 4 | Clicar em "Login" |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Login Invalid email or password. Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Invalid email or password. Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Invalid email or password. Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Invalid email or password. \|  |
| 5 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Invalid email or password. Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? |
