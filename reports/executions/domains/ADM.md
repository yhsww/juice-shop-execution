# Relatório do domínio ADM

**Cenários executados:** 3
**Cenários aprovados:** 3
**Status do conjunto:** PASSED

## Cenários

| ID | Cenário | Status | Comportamento observado |
|---|---|---|---|
| CEN-ADM-01 | Acesso à área administrativa | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? \| exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Logi |
| CEN-ADM-02 | Visualização de usuários cadastrados | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 29 Customer Feedback 1 I love this shop! \| Best products in town! \| Highly recommended! \| (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! \| Awesome service! \| (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me th Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Support Team: Sorry, only order confirmation PDFs can be attached to complaints! \| the \| 1 – 8 of 8 M |
| CEN-ADM-03 | Visualização e gestão de feedbacks | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 29 Customer Feedback 1 I love this shop! \| Best products in town! \| Highly recommended! \| (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! \| Awesome service! \| (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me th Texto transitório capturado: J12934@juice-sh.op \| wurstbrot@juice-sh.op \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Regis |

## Mensagens observadas

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
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
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
- 6
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- 1 I love this shop! Best products in town! Highly recommended! (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op) star_rate Incompetent customer support! Can't even upload photo of broken purchase! Support Team: Sorry, only order confirmation PDFs can be attached to complaints! (anonymous) star_ratestar_rate This is the store for awesome stuff of all kinds! (anonymous) star_ratestar_ratestar_ratestar_rate Never gonna buy anywhere else from now on! Thanks for the great service! (anonymous) star_ratestar_ratestar_ratestar_rate Keep up the good work! (anonymous) star_ratestar_ratestar_rate
- Customer Feedback 1 I love this shop! Best products in town! Highly recommended! (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op) star_rate Incompetent customer support! Can't even upload photo of broken purchase! Support Team: Sorry, only order confirmation PDFs can be attached to complaints! (anonymous) star_ratestar_rate This is the store for awesome stuff of all kinds! (anonymous) star_ratestar_ratestar_ratestar_rate Never gonna buy anywhere else from now on! Thanks for the great service! (anonymous) star_ratestar_ratestar_ratestar_rate Keep up the good work! (anonymous) star_ratestar_ratestar_rate Items per page: 10 1 – 8 of 8
- Registered Users Items per page: 10 0 of 0 Customer Feedback 1 I love this shop! Best products in town! Highly recommended! (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op) star_rate Incompetent customer support! Can't even upload photo of broken purchase! Support Team: Sorry, only order confirmation PDFs can be attached to complaints! (anonymous) star_ratestar_rate This is the store for awesome stuff of all kinds! (anonymous) star_ratestar_ratestar_ratestar_rate Never gonna buy anywhere else from now on! Thanks for the great service! (anonymous) star_ratestar_ratestar_ratestar_rate Keep up the good work! (anonymous) star_ratestar_ratestar_rate Items per page: 10 1 – 8 of 8 Settings Show tool calls in AI chat

## Rastreabilidade

Cada descrição acima é derivada dos passos e evidências da execução do respectivo cenário; nenhum comportamento é inferido a partir de END, COMP ou REQ.
