# Ficha de Cenário

**ID do cenário:** CEN-ADM-08
**Domínio:** ADM
**Nome do cenário:** Gerenciar produtos e pedidos como administrador
**Ator:** Administrador
**Fluxo:** Procurar na administração alguma tela de produtos ou pedidos; abrir /#/accounting.

## Pré-condição (estado inicial)

Administrador autenticado.

## Descrição do cenário

Administrador executa o fluxo 'Procurar na administração alguma tela de produtos ou pedidos; abrir /#/accounting.'. A descrição corresponde ao cenário 'Gerenciar produtos e pedidos como administrador' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 3 Nothing useful available here! | (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op) star_rate Incompetent customer support! | Can't even upload photo of Texto transitório capturado: Keep up the good work! (anonymous) | star_ratestar_ratestar_rate | Support Team: Sorry, only order confirmation PDFs can be attached to complaints! | the | 1 – 6 of 6 Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat | Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat | Registered Users Items per page: 10 0 of 0 | Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
2. URL: http://127.0.0.1:3000/#/administration → http://127.0.0.1:3000/#/accounting Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN 403 You are not allowed to access this page! Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN 403 You are not allowed to access this page! | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account sho

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- Registered Users Items per page: 10 0 of 0
- Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- Customer Feedback Items per page: 10 0 of 0
- Show tool calls in AI chat
- Settings Show tool calls in AI chat
- Items per page: 10 0 of 0
- Items per page: 10
- 0 of 0
- Items per page:
- 10
- Administration
- Registered Users
- Customer Feedback
- Settings
- admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op
- Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234
- Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/administration
Passo 3: /#/accounting

## Coerente com loja de sucos?

Sim.

## Justificativa

O guia exige 'consultar e gerenciar produtos e pedidos', mas a tela de administração mostra só usuários e feedbacks.

## Descrição funcional do cenário

Administrador executa o fluxo 'Procurar na administração alguma tela de produtos ou pedidos; abrir /#/accounting.'. A descrição corresponde ao cenário 'Gerenciar produtos e pedidos como administrador' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration | /#/administration | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op) star_rate Incompetent customer support! \| Can't even upload photo of  Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Support |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op) star_rate Incompetent customer support! Can't even upload photo of broken purchase! Su |
| 3 | Abrir a rota /#/accounting | /#/accounting | URL: http://127.0.0.1:3000/#/administration → http://127.0.0.1:3000/#/accounting Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN 403 You are not allowed to access this page! Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN 403 You are not allowed to access this page! \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN 403 You are not allowed to access this page! \| 403 You are not allowed to access this page! \| You are not allowed to access this page! \| 403 Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN 403 You are not allowed to access this page! |
