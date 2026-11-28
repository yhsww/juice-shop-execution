# Ficha de Cenário

**ID do cenário:** CEN-CAR-09
**Domínio:** CAR
**Nome do cenário:** Diminuir quantidade abaixo de 1
**Ator:** Cliente autenticado
**Fluxo:** Com 1 unidade no carrinho, clicar em diminuir.

## Pré-condição (estado inicial)

Cliente autenticado; há pelo menos um produto no carrinho (1 unidade).

## Descrição do cenário

Cliente autenticado executa o fluxo 'Com 1 unidade no carrinho, clicar em diminuir.'. A descrição corresponde ao cenário 'Diminuir quantidade abaixo de 1' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ | Apple Juice (1000ml) 1 1.99¤ | Apple Juice (1000ml) | 1 | 1.99¤ Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Checkout | You will gain 0 Bonus Points from this order!
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! | Apple Juice (1000ml) | 1.99¤ | Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Mensagem transitória: 1 | Apple Juice (1000ml) 1 1.99¤ | Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Checkout
- You will gain 0 Bonus Points from this order!
- Your Basket
- Your Basket Total Price: 0¤
- Total Price: 0¤
- (cen-cen-car-09-96ab6ae885@example.com)
- Your Basket (cen-cen-car-09-96ab6ae885@example.com)
- Your Basket (cen-cen-car-09-96ab6ae885@example.com) Total Price: 0¤
- Your Basket (cen-cen-car-09-96ab6ae885@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- Total Price: 1.99¤
- Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤
- Apple Juice (1000ml) 1 1.99¤
- Apple Juice (1000ml)

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/basket

## Coerente com loja de sucos?

Sim.

## Justificativa

Quantidade zero ou negativa não faz sentido num pedido.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Com 1 unidade no carrinho, clicar em diminuir.'. A descrição corresponde ao cenário 'Diminuir quantidade abaixo de 1' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket | /#/basket | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ \| Apple Juice (1000ml) 1 1.99¤ \| Apple Juice (1000ml) \| 1 \| 1.99¤ Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Yo |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X |
| 3 | Clicar no elemento |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! \| Apple Juice (1000ml) \| 1.99¤ \| Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Mensagem transitória: 1 \| Apple Juice (1000ml) 1 1.99¤ \| Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Appl |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-09-96ab6ae885@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! |
