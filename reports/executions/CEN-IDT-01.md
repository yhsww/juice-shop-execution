# Ficha de Cenário

**ID do cenário:** CEN-IDT-01
**Domínio:** IDT
**Nome do cenário:** Cadastro de novo cliente
**Ator:** Cliente
**Fluxo:** Abrir o cadastro, preencher os dados e concluir o registro.

## Pré-condição (estado inicial)

Não é necessária autenticação prévia; o e-mail usado para o cadastro deve estar disponível.

## Descrição do cenário

Cliente executa o fluxo 'Abrir o cadastro, preencher os dados e concluir o registro.'. A descrição corresponde ao cenário 'Cadastro de novo cliente' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/register Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. | 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! | Answer person_add Register Already a customer? Texto transitório capturado: Security Question | Password must be 5-40 characters long. 0/20 | 0/40 | This cannot be changed later! | Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? Language has been changed to English Force page reload | Language has been changed to English Force page reload | User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? | User Registration
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? Language has been changed to English Force page reload | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must 

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer?
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? Language has been changed to English Force page reload
- Language has been changed to English Force page reload
- User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer?
- User Registration
- Show password advice
- Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer?
- person_add
- person_add Register
- Register
- Already a customer?
- Email
- Password Password must be 5-40 characters long. 0/20
- Repeat Password 0/40
- Security Question This cannot be changed later!
- Security Question This cannot be changed later! Answer
- Answer
- Password
- Repeat Password
- Security Question

## Dados manipulados

Dados declarados no cenário: E-mail: teste@example.com; senha: Teste@12345; pergunta de segurança e resposta de teste.
Passo 1: /#/register
Passo 2: cen-cen-idt-01-e45a2ee205@example.com
Passo 3: Teste@12345
Passo 4: Teste@12345
Passo 5: Your favorite book?
Passo 6: a

## Coerente com loja de sucos?

Sim.

## Justificativa

O cadastro é essencial para identificação do cliente.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir o cadastro, preencher os dados e concluir o registro.'. A descrição corresponde ao cenário 'Cadastro de novo cliente' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/register | /#/register | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/register Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. \| 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! \| Answer person_add Register Already a customer? Texto transitório capturado: Security Question \| Password must be 5-40 characters long. 0/20 \| 0/40 \| This cannot be changed later! \| Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Regist |
| 2 | Preencher "Email address" | cen-cen-idt-01-e45a2ee205@example.com | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? Language has been changed to English Force page reload \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice S |
| 3 | Preencher "Password" | Teste@12345 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password must be 5-40 characters long. 11/20 \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| Password Password must be 5-40 characters long. 11/20 \| Email Password Password must be 5-40 characters long. 11/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| User Registration Email Password Password must be 5-40 characters long. 11/20 Repea |
| 4 | Preencher "Repeat Password" | Teste@12345 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 11/40 \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| Repeat Password 11/40 \| Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question This cannot b |
| 5 | Selecionar "Security Question" | Your favorite book? | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question Your favorite book? Your eldest siblings middle name? Mother's maiden name? Mother's birth date? (MM/DD/YY) Father's birth date? (MM/DD/YY) Maternal grandmother's first name? Paternal grandmother's first name? Name of your favorite pet? Last name of dentist when you were a teenager? (Do not include 'Dr.') Your ZIP/postal code when you were a teenager? Company you first work for as an adult? Your favorite book? Your favorite movie? Number of one of your customer or ID cards? What's your favorite place to go hiking? This cannot be changed later! Answer person_add Register Already a customer? \| Security Question Your favorite book? Your eldest siblings middle name? Mother's  |
| 6 | Preencher "Answer" | a | Nenhuma mudança visual relevante detectada. Texto transitório capturado: User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question Your favorite book? This cannot be changed later! Answer person_add Register Already a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question Your favorite book? This cannot be changed later! Answer person_add Register Already a customer? \| Security Question Your favorite book? \| Answer \| person_add Register Mensagem transitória: Security Question Your favorite book? This |
| 7 | Clicar em "Register" |  | URL: http://127.0.0.1:3000/#/register → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? \| exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Registration completed successfully. \| You can now log in. \| X Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWAS |
| 8 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? Registration completed successfully. You can now log in. X |
