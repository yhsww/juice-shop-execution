# Ficha de Cenário

**ID do cenário:** CEN-CHK-38
**Domínio:** CHK
**Nome do cenário:** Pular etapas: abrir resumo do pedido direto
**Ator:** Cliente autenticado
**Fluxo:** Com carrinho cheio mas sem escolher endereço, entrega ou pagamento, abrir /#/order-summary e tentar concluir.

## Pré-condição (estado inicial)

Cliente autenticado; carrinho contém produto; nenhuma etapa do checkout concluída nesta sessão.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Com carrinho cheio mas sem escolher endereço, entrega ou pagamento, abrir /#/order-summary e tentar concluir.'. A descrição corresponde ao cenário 'Pular etapas: abrir resumo do pedido direto' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/order-summary Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-38-7747995d5d@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Apple Juice (1000ml) 1 1.99¤ | Your Basket (cen-cen-chk-38-7747995d5d@example.com) Apple Juice (1000ml) 1 1.99¤ | Your Basket (cen-cen-chk-38-7747995d5d@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! | Apple Juice (1000ml) | 1 Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! | Your Basket Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You 

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- Your Basket Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- Order Summary
- Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- Items
- Items 0.00¤
- Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤
- 0.00¤
- Delivery
- Delivery 0.00¤
- Promotion
- Promotion 0.00¤
- Total Price
- Total Price 0.00¤
- monetization_on
- monetization_onPlace your order and pay
- Place your order and pay
- You will gain 0 Bonus Points from this order!
- Your Basket

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/order-summary

## Coerente com loja de sucos?

Sim.

## Justificativa

A loja não deve aceitar pedido sem endereço, entrega e pagamento.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Com carrinho cheio mas sem escolher endereço, entrega ou pagamento, abrir /#/order-summary e tentar concluir.'. A descrição corresponde ao cenário 'Pular etapas: abrir resumo do pedido direto' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/order-summary | /#/order-summary | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/order-summary Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-38-7747995d5d@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Apple Juice (1000ml) 1 1.99¤ \| Your Basket (cen-cen-chk-38-7747995d5d@example.com) Apple Juice (1000ml) 1 1.99¤ \| Your Basket (cen-cen-chk-38-7747995d5d@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! \| Apple Juice (1000ml) \| 1 Mensagem transitória: menu OWASP Juice Shop search s |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-38-7747995d5d@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X |
