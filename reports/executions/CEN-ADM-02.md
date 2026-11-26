# Ficha de Cenário

**ID do cenário:** CEN-ADM-02
**Domínio:** ADM
**Nome do cenário:** Visualização de usuários cadastrados
**Ator:** Administrador
**Fluxo:** Abrir a administração e verificar a área de usuários.

## Pré-condição (estado inicial)

Administrador autenticado.

## Descrição do cenário

Administrador executa o fluxo 'Abrir a administração e verificar a área de usuários.'. A descrição corresponde ao cenário 'Visualização de usuários cadastrados' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 101 Customer Feedback 1 I love this shop! | Best products in town! | Highly recommended! | (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! | Awesome service! | (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! | (***der@juice-sh.op) star_rate 21 Please send me t Texto transitório capturado: Keep up the good work! (anonymous) | star_ratestar_ratestar_rate | Support Team: Sorry, only order confirmation PDFs can be attached to complaints! | the | 1 – 8 of 8 Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in 

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
- Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 101
- Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 101 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/administration

## Coerente com loja de sucos?

Sim.

## Justificativa

A gestão de usuários é uma função administrativa da loja.

## Descrição funcional do cenário

Administrador executa o fluxo 'Abrir a administração e verificar a área de usuários.'. A descrição corresponde ao cenário 'Visualização de usuários cadastrados' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration | /#/administration | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 101 Customer Feedback 1 I love this shop! \| Best products in town! \| Highly recommended! \| (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! \| Awesome service! \| (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me t Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Sup |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 101 Customer Feedback 1 I love this shop! Best products in town! Highly recommended! (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my  |
