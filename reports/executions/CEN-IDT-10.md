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
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/forgot-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. | 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload Texto transitório capturado: help_outline | Security Question | Password must be 5-40 characters long. 0/20 | 0/20 | Password must be 5-40 characters long. Mensagem transitória: Click for more information | Language has been changed to English Force page reload Click for more information | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Lemon Juice (500ml) 2.99¤ add_shopping_cart Add to Basket Items per page: 16 1 – 16 of 46 Language has been changed to English Force page reload Click for more information | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 l

## Mensagens exibidas ao usuário

- Click for more information
- Language has been changed to English Force page reload Click for more information
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Lemon Juice (500ml) 2.99¤ add_shopping_cart Add to Basket Items per page: 16 1 – 16 of 46 Language has been changed to English Force page reload Click for more information
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

## Dados manipulados

Dados declarados no cenário: E-mail: teste@example.com.
Passo 1: /#/forgot-password
Passo 2: cen-cen-idt-10-883cb0c358@example.com

## Coerente com loja de sucos?

Sim.

## Justificativa

A pergunta integra o mecanismo de recuperação configurado no aplicativo.

## Descrição funcional do cenário

Cliente executa o fluxo 'Informar e-mail e verificar a solicitação da pergunta de segurança.'. A descrição corresponde ao cenário 'Pergunta de segurança na recuperação' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/forgot-password | /#/forgot-password | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/forgot-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. \| 0/20 Repeat New Password 0/20 Show password advice Change Language has been changed to English Force page reload Texto transitório capturado: help_outline \| Security Question \| Password must be 5-40 characters long. 0/20 \| 0/20 \| Password must be 5-40 characters long. Mensagem transitória: Click for more information \| Language has been changed to English Force page reload Click for more information \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account sho |
| 2 | Preencher "Email" | cen-cen-idt-10-883cb0c358@example.com | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| Email help_outline \| Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change \| Email Mensagem transitória: Language has been changed to Englis |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Forgot Password Email help_outline Security Question help_outline New Password Password must be 5-40 characters long. 0/20 Repeat New Password 0/20 Show password advice Change |
