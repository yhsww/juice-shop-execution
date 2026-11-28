# Ficha de Cenário

**ID do cenário:** CEN-IDT-14
**Domínio:** IDT
**Nome do cenário:** Cadastro com e-mail já utilizado
**Ator:** Cliente
**Fluxo:** Tentar cadastrar uma conta utilizando e-mail existente.

## Pré-condição (estado inicial)

Existe usuário com o e-mail informado.

## Descrição do cenário

Cliente executa o fluxo 'Tentar cadastrar uma conta utilizando e-mail existente.'. A descrição corresponde ao cenário 'Cadastro com e-mail já utilizado' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/register Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. | 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! | Answer person_add Register Already a customer? Texto transitório capturado: Security Question | Password must be 5-40 characters long. 0/20 | 0/40 | This cannot be changed later! | Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? | User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? | User Registration | Show password advice
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password must be 5-40 characters long. 11/20 | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? | Password Password must be 5-40 characters long. 11/20 | Email Password Password must be 5-40 characters long. 11/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? | User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 0/

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer?
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer?
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
- Password must be 5-40 characters long. 0/20

## Dados manipulados

Dados declarados no cenário: E-mail: teste@example.com.
Passo 1: /#/register
Passo 2: teste@example.com
Passo 3: Teste@12345
Passo 4: Teste@12345
Passo 5: Your favorite book?
Passo 6: a

## Coerente com loja de sucos?

Sim.

## Justificativa

A aplicação deve evitar duplicidade de contas.

## Descrição funcional do cenário

Cliente executa o fluxo 'Tentar cadastrar uma conta utilizando e-mail existente.'. A descrição corresponde ao cenário 'Cadastro com e-mail já utilizado' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/register | /#/register | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/register Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. \| 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! \| Answer person_add Register Already a customer? Texto transitório capturado: Security Question \| Password must be 5-40 characters long. 0/20 \| 0/40 \| This cannot be changed later! \| Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add  |
| 2 | Preencher "Email address" | teste@example.com | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Email \| Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Reg |
| 3 | Preencher "Password" | Teste@12345 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password must be 5-40 characters long. 11/20 \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| Password Password must be 5-40 characters long. 11/20 \| Email Password Password must be 5-40 characters long. 11/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| User Registration Email Password Password must be 5-40 characters long. 11/20 Repea |
| 4 | Preencher "Repeat Password" | Teste@12345 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 11/40 \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| Repeat Password 11/40 \| Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question This cannot b |
| 5 | Selecionar "Security Question" | Your favorite book? | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question Your favorite book? Your eldest siblings middle name? Mother's maiden name? Mother's birth date? (MM/DD/YY) Father's birth date? (MM/DD/YY) Maternal grandmother's first name? Paternal grandmother's first name? Name of your favorite pet? Last name of dentist when you were a teenager? (Do not include 'Dr.') Your ZIP/postal code when you were a teenager? Company you first work for as an adult? Your favorite book? Your favorite movie? Number of one of your customer or ID cards? What's your favorite place to go hiking? This cannot be changed later! Answer person_add Register Already a customer? \| Security Question Your favorite book? Your eldest siblings middle name? Mother's  |
| 6 | Preencher "Answer" | a | Nenhuma mudança visual relevante detectada. Texto transitório capturado: User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question Your favorite book? This cannot be changed later! Answer person_add Register Already a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question Your favorite book? This cannot be changed later! Answer person_add Register Already a customer? \| Security Question Your favorite book? \| Answer \| person_add Register Mensagem transitória: Security Question Your favorite book? This |
| 7 | Clicar em "Register" |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: person_add Register \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question Your favorite book? This cannot be changed later! Answer person_add Register Already a customer? \| Email must be unique \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email must be unique Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question Your favorite book? This cannot be changed later! Answe |
| 8 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email must be unique Email Password Password must be 5-40 characters long. 11/20 Repeat Password 11/40 Show password advice Security Question Your favorite book? This cannot be changed later! Answer person_add Register Already a customer? |
