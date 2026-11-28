# Ficha de Cenário

**ID do cenário:** CEN-IDT-15
**Domínio:** IDT
**Nome do cenário:** Validação de campos obrigatórios
**Ator:** Cliente
**Fluxo:** Tentar concluir o cadastro sem preencher todos os campos obrigatórios.

## Pré-condição (estado inicial)

Tela de cadastro aberta.

## Descrição do cenário

Cliente executa o fluxo 'Tentar concluir o cadastro sem preencher todos os campos obrigatórios.'. A descrição corresponde ao cenário 'Validação de campos obrigatórios' e deve ser interpretada em conjunto com as evidências registradas nos passos.

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

Dados declarados no cenário: Campos obrigatórios deixados vazios.
Passo 1: /#/register

## Coerente com loja de sucos?

Sim.

## Justificativa

A validação impede registros incompletos.

## Descrição funcional do cenário

Cliente executa o fluxo 'Tentar concluir o cadastro sem preencher todos os campos obrigatórios.'. A descrição corresponde ao cenário 'Validação de campos obrigatórios' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/register | /#/register | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/register Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. \| 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! \| Answer person_add Register Already a customer? Texto transitório capturado: Security Question \| Password must be 5-40 characters long. 0/20 \| 0/40 \| This cannot be changed later! \| Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Regist |
| 2 | Clicar em "Email address" |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? Language has been changed to English Force page reload \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice S |
| 3 | Pressionar Tab |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Please provide an email address. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Please provide an email address. Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? \| Email \| Please provide an email address. \| Password Password must be 5-40 characters long. 0/20 \| Password Mensagem transitória: Email Please provide an email address. \| Email Please provide an email address. Password Password |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN User Registration Email Please provide an email address. Password Password must be 5-40 characters long. 0/20 Repeat Password 0/40 Show password advice Security Question This cannot be changed later! Answer person_add Register Already a customer? |
