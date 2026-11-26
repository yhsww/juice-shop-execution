# Ficha de Cenário

**ID do cenário:** CEN-IDT-10
**Domínio:** IDT
**Nome do cenário:** Pergunta de segurança na recuperação
**Ator:** Cliente
**Fluxo:** Informar e-mail e verificar a solicitação da pergunta de segurança.

## Pré-condição (estado inicial)

Conta de teste do cenário cadastrada com pergunta e resposta de segurança.

## Descrição do cenário

Cliente executa o fluxo 'Informar e-mail e verificar a solicitação da pergunta de segurança.'. A descrição corresponde ao cenário 'Pergunta de segurança na recuperação' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/forgot-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. | 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload Texto transitório capturado: help_outline | Security Question | Password must be 5-40 characters long. 0/20 | 0/20 | Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload | Language has been changed to English Force page reload | Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change | Forgot Password
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload | Email | Language has been changed to English Force page reload | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle A

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
Passo 2: cen-cen-idt-10-2d58afe976@example.com

## Coerente com loja de sucos?

Sim.

## Justificativa

A pergunta integra o mecanismo de recuperação configurado no aplicativo.

## Descrição funcional do cenário

Cliente executa o fluxo 'Informar e-mail e verificar a solicitação da pergunta de segurança.'. A descrição corresponde ao cenário 'Pergunta de segurança na recuperação' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/forgot-password | /#/forgot-password | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/forgot-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. \| 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload Texto transitório capturado: help_outline \| Security Question \| Password must be 5-40 characters long. 0/20 \| 0/20 \| Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| This web |
| 2 | Preencher "Email" | cen-cen-idt-10-2d58afe976@example.com | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload \| Email \| Language has been changed to English Force page reload \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice  |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change |
