# Ficha de Cenário

**ID do cenário:** CEN-IDT-09
**Domínio:** IDT
**Nome do cenário:** Recuperação de senha
**Ator:** Cliente
**Fluxo:** Abrir o fluxo de recuperação de senha.

## Pré-condição (estado inicial)

Usuário possui e-mail cadastrado.

## Descrição do cenário

Cliente executa o fluxo 'Abrir o fluxo de recuperação de senha.'. A descrição corresponde ao cenário 'Recuperação de senha' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/forgot-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. | 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload Texto transitório capturado: help_outline | Security Question | Password must be 5-40 characters long. 0/20 | 0/20 | Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload | Language has been changed to English Force page reload | Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change | Forgot Password

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload
- Language has been changed to English Force page reload
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

## Dados manipulados

Dados declarados no cenário: E-mail: teste@example.com.
Passo 1: /#/forgot-password

## Coerente com loja de sucos?

Sim.

## Justificativa

A recuperação permite recuperar uma conta inacessível.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir o fluxo de recuperação de senha.'. A descrição corresponde ao cenário 'Recuperação de senha' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/forgot-password | /#/forgot-password | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/forgot-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. \| 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload Texto transitório capturado: help_outline \| Security Question \| Password must be 5-40 characters long. 0/20 \| 0/20 \| Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| This web |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload |
