# Ficha de Cenário

**ID do cenário:** CEN-ADM-01
**Domínio:** ADM
**Nome do cenário:** Acesso à área administrativa
**Ator:** Administrador
**Fluxo:** Acessar a área de administração com uma conta administrativa válida.

## Pré-condição (estado inicial)

Juice Shop em execução; usuário administrador disponível.

## Descrição do cenário

Administrador executa o fluxo 'Acessar a área de administração com uma conta administrativa válida.'. A descrição corresponde ao cenário 'Acesso à área administrativa' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? | exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? Language has been changed to English Force page reload | or | Log in with Google Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? Language has been changed to English Force page reload | Language has been changed to English Force page reload | Login Email Password visibility Forgot your password? exit_to_app Log in Remember me Not yet a customer? | Login
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log 

## Mensagens exibidas ao usuário

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

## Dados manipulados

Dados declarados no cenário: E-mail: admin@juice-sh.op; senha: admin123.
Passo 1: /#/login
Passo 2: admin@juice-sh.op
Passo 3: admin123
Passo 6: /#/administration

## Coerente com loja de sucos?

Sim.

## Justificativa

A administração reúne funções restritas de gestão da loja.

## Descrição funcional do cenário

Administrador executa o fluxo 'Acessar a área de administração com uma conta administrativa válida.'. A descrição corresponde ao cenário 'Acesso à área administrativa' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/login | /#/login | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/login Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? \| exit_to_app Log in Remember me or Log in with Google Not yet a customer? Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your B |
| 2 | Preencher "Email" | admin@juice-sh.op | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? Language has been changed to English Force page reload \| Language has been changed to English Force page reload \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it!  |
| 3 | Preencher "Password" | admin123 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Password visibility \| Password \| exit_to_app Log in Mensagem transitória: Email \| Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| Login Email Password visibility Forgot your password? exit_to_app Log in Remember me or Log in with Google Not yet a customer? \| This website u |
| 4 | Clicar em "Login" |  | URL: http://127.0.0.1:3000/#/login → http://127.0.0.1:3000/#/search Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping Texto transitório capturado: Lemon Juice (500ml) 2.99¤ add_shopping_cart Add to Basket \| Lemon Juice (500ml) \| 1 – |
| 5 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Ba |
| 6 | Abrir a rota /#/administration | /#/administration | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 85 Customer Feedback 1 I love this shop! \| Best products in town! \| Highly recommended! \| (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! \| Awesome service! \| (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! \| (***der@juice-sh.op) star_rate 21 Please send me th Texto transitório capturado: Keep up the good work! (anonymous) \| star_ratestar_ratestar_rate \| Sup |
| 7 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 6 language EN Administration Registered Users admin@juice-sh.op jim@juice-sh.op bender@juice-sh.op bjoern.kimminich@gmail.com ciso@juice-sh.op support@juice-sh.op morty@juice-sh.op mc.safesearch@juice-sh.op J12934@juice-sh.op wurstbrot@juice-sh.op Items per page: 10 1 – 10 of 85 Customer Feedback 1 I love this shop! Best products in town! Highly recommended! (***in@juice-sh.op) star_ratestar_ratestar_ratestar_ratestar_rate 2 Great shop! Awesome service! (***@juice-sh.op) star_ratestar_ratestar_ratestar_rate 3 Nothing useful available here! (***der@juice-sh.op) star_rate 21 Please send me the juicy chatbot NFT in my w |
