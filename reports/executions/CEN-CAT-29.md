# Ficha de Cenário

**ID do cenário:** CEN-CAT-29
**Domínio:** CAT
**Nome do cenário:** Página 'About Us'
**Ator:** Visitante não autenticado
**Fluxo:** Abrir 'About Us' pelo menu lateral.

## Pré-condição (estado inicial)

Catálogo disponível.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Abrir 'About Us' pelo menu lateral.'. A descrição corresponde ao cenário 'Página 'About Us'' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/about Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN About Us Corporate History & Policy Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. | At vero eos et accusam et justo duo dolores et ea rebum. | Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. | Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. | At vero eos et accusam et justo duo dolores et ea rebum. | Stet clita kasd gubergren, no sea takima Texto transitório capturado: Press Kit | NFT | Great shop! Awesome service! (***@juice-sh.op) () | Customer Feedback Great shop! Awesome service! (***@juice-sh.op) () | () Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0 | EN | language EN | account_circle Account shopping_cart Your Basket 0 language EN | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
2. Texto visível: Customer Feedback Nothing useful available here! Texto transitório capturado: Nothing useful available here! (***der@juice-sh.op) () | () Mensagem transitória: Nothing useful available here! (***der@juice-sh.op) () | ()

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0
- EN
- language EN
- account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
- About Us
- Corporate History & Policy
- Customer Feedback
- Check out our boring terms of use if you are interested in such lame stuff.
- Follow us on Social Media BlueSky Mastodon Twitter Facebook Slack Reddit Press Kit NFT
- Follow us on Social Media
- BlueSky Mastodon Twitter Facebook Slack Reddit Press Kit NFT
- BlueSky
- Mastodon
- Twitter
- Facebook
- Slack
- Reddit
- Press Kit
- NFT

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/about

## Coerente com loja de sucos?

Sim.

## Justificativa

Informação institucional da loja.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Abrir 'About Us' pelo menu lateral.'. A descrição corresponde ao cenário 'Página 'About Us'' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/about | /#/about | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/about Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN About Us Corporate History & Policy Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. \| At vero eos et accusam et justo duo dolores et ea rebum. \| Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. \| Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. \| At vero eos et accusam et justo duo dolores et ea rebum. \| Stet clita kasd gubergren, no sea takima Texto transitório capturado: Press Kit \| NFT \| Great shop! Awesome service! (***@juice-sh.op) () \| Customer Feedba |
| 2 | Aguardar a atualização da interface |  | Texto visível: Customer Feedback Nothing useful available here! Texto transitório capturado: Nothing useful available here! (***der@juice-sh.op) () \| () Mensagem transitória: Nothing useful available here! (***der@juice-sh.op) () \| () |
