# Relatório do domínio ADM

**Cenários executados:** 8
**Cenários aprovados:** 8
**Status do conjunto:** PASSED

## Cenários

| ID | Cenário | Status | Comportamento observado |
|---|---|---|---|
| CEN-ADM-01 | Acesso à área administrativa | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? \| exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Logi |
| CEN-ADM-02 | Visualização de usuários cadastrados | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 155 Customer Feedback 2 Great shop! \| Awesome service! \| (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (* Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Support Team: Sorry, only order confirmation PDFs can be attached to complaints! \| the \| 1 – 7 of 7 Mens |
| CEN-ADM-03 | Visualização e gestão de feedbacks | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 155 Customer Feedback 2 Great shop! \| Awesome service! \| (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (* Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Support Team: Sorry, only order confirmation PDFs can be attached to complaints! \| the \| 1 – 7 of 7 Mens |
| CEN-ADM-04 | Cliente comum tenta abrir a administração | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Registration completed successfully. You can now log in. X \| 403 You are not allowed to access this page! \| You are not allowed to access this page! \| 403 \| Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Registration completed successfull |
| CEN-ADM-05 | Visitante tenta abrir a administração | PASSED | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! \| EN \| language EN \| account_circle Account shopping_cart Your Basket 0 language EN \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 You are not allowed to access this page! \| 403 You are not allowed to access this page! \| You are not allowed to access this page! \| 403 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 40 |
| CEN-ADM-06 | Ver detalhes de um usuário cadastrado | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 2 Great shop! \| Awesome service! \| (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (* Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Support Team: Sorry, only orde |
| CEN-ADM-07 | Remover feedback de cliente | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 2 Great shop! \| Awesome service! \| (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (* Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Support Team: Sorry, only orde |
| CEN-ADM-08 | Gerenciar produtos e pedidos como administrador | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my wallet at /juicy-nft : "purpose betray marriage blame crunch monitor spin slide donate sport lift clutch" (***ereum@juice-sh.op) star_rate Incompetent customer support! \| Can't even upload photo of Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Support Team: Sorry, only order  |

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
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat Language has been changed to English Force page reload
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
- Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 155
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users Items per page: 10 0 of 0 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 155 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Registration completed successfully. You can now log in. X
- 403 You are not allowed to access this page!
- You are not allowed to access this page!
- 403
- Registration completed successfully. You can now log in. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 You are not allowed to access this page!
- EN
- language EN
- account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
- Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234
- Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 234 Customer Feedback Items per page: 10 0 of 0 Settings Show tool calls in AI chat

## Rastreabilidade

Cada descrição acima é derivada dos passos e evidências da execução do respectivo cenário; nenhum comportamento é inferido a partir de END, COMP ou REQ.
