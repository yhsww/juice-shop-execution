# Ficha de Cenário

**ID do cenário:** CEN-CAR-15
**Domínio:** CAR
**Nome do cenário:** Checkout com carrinho vazio
**Ator:** Cliente autenticado
**Fluxo:** Com o carrinho vazio (conta nova), tentar iniciar o checkout.

## Pré-condição (estado inicial)

Cliente autenticado; carrinho vazio.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Com o carrinho vazio (conta nova), tentar iniciar o checkout.'. A descrição corresponde ao cenário 'Checkout com carrinho vazio' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: (cen-cen-car-15-0aefd8cd25@example.com) | Your Basket (cen-cen-car-15-0aefd8cd25@example.com) | Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ | Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Checkout | You will gain 0 Bonus Points from this order! | Your Basket

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Checkout
- You will gain 0 Bonus Points from this order!
- Your Basket
- Your Basket Total Price: 0¤
- Total Price: 0¤
- (cen-cen-car-15-0aefd8cd25@example.com)
- Your Basket (cen-cen-car-15-0aefd8cd25@example.com)
- Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤
- Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/basket

## Coerente com loja de sucos?

Sim.

## Justificativa

Não há pedido sem itens.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Com o carrinho vazio (conta nova), tentar iniciar o checkout.'. A descrição corresponde ao cenário 'Checkout com carrinho vazio' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket | /#/basket | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: (cen-cen-car-15-0aefd8cd25@example.com) \| Your Basket (cen-cen-car-15-0aefd8cd25@example.com) \| Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ \| Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Mensagem transitória: menu OWASP Jui |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! |
| 3 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (cen-cen-car-15-0aefd8cd25@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! |
