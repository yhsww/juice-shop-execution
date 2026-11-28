# Ficha de Cenário

**ID do cenário:** CEN-ADM-07
**Domínio:** ADM
**Nome do cenário:** Remover feedback de cliente
**Ator:** Administrador
**Fluxo:** Na lista de feedbacks, remover o primeiro item e observar a lista.

## Pré-condição (estado inicial)

Administrador autenticado; ao menos 1 feedback.

## Descrição do cenário

Administrador executa o fluxo 'Na lista de feedbacks, remover o primeiro item e observar a lista.'. A descrição corresponde ao cenário 'Remover feedback de cliente' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 2 Great shop! | Awesome service! | (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! | (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (* Texto transitório capturado: Keep up the good work! (anonymous) | star_ratestar_ratestar_rate | Support Team: Sorry, only order confirmation PDFs can be attached to complaints! | the | 1 – 7 of 7 Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat | Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat | Registered Users Items per page: 10 0 of 0 | Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Keep up the good work! (anonymous) | star_ratestar_ratestar_rate | Support Team: Sorry, only order confirmation PDFs can be attached to complaints! | the | 1 – 6 of 6 Mensagem transitória: 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate | 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage bl

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

## Coerente com loja de sucos?

Sim.

## Justificativa

Moderar feedback é função administrativa.

## Descrição funcional do cenário

Administrador executa o fluxo 'Na lista de feedbacks, remover o primeiro item e observar a lista.'. A descrição corresponde ao cenário 'Remover feedback de cliente' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration | /#/administration | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 2 Great shop! \| Awesome service! \| (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (* Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Suppor |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op)  |
| 3 | Clicar no elemento |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Support Team: Sorry, only order confirmation PDFs can be attached to complaints! \| the \| 1 – 6 of 6 Mensagem transitória: 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate \| 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op) star_rate Incompetent customer support! Can't even upload photo of broken purchase! Support Team: Sorry, only order confirmation PDFs can be attached to complaints! (anonymous) star_ratestar_rate This is the store |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op) star_rate Incompetent customer support! Can't even upload photo of broken purchase! Su |
