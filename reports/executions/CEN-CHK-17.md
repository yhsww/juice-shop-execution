# Ficha de Cenário

**ID do cenário:** CEN-CHK-17
**Domínio:** CHK
**Nome do cenário:** Acessar histórico de pedidos
**Ator:** Cliente
**Fluxo:** Abrir o histórico de pedidos após uma compra.

## Pré-condição (estado inicial)

Cliente autenticado; pedido concluído.

## Descrição do cenário

Cliente executa o fluxo 'Abrir o histórico de pedidos após uma compra.'. A descrição corresponde ao cenário 'Acessar histórico de pedidos' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #1c08-9515e65bc503f871 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. Texto transitório capturado: Price | Quantity | Apple Juice (1000ml) | 1 | rate_review Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. | Order History No results found You have not placed any orders yet. | Order History | No results found You have not placed any orders yet.

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet.
- Order History No results found You have not placed any orders yet.
- Order History
- No results found You have not placed any orders yet.
- No results found
- You have not placed any orders yet.
- Order History Order ID #1c08-9515e65bc503f871 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #1c08-9515e65bc503f871 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #1c08-9515e65bc503f871 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. X
- Order ID #1c08-9515e65bc503f871 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review
- Order ID
- Order ID #1c08-9515e65bc503f871
- Order ID #1c08-9515e65bc503f871 Total Price 1.99¤ Bonus 0 In Transit local_shipping note
- #1c08-9515e65bc503f871
- Total Price
- Total Price 1.99¤
- 1.99¤
- Bonus
- Bonus 0

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/order-history

## Coerente com loja de sucos?

Sim.

## Justificativa

O histórico permite acompanhar compras anteriores.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir o histórico de pedidos após uma compra.'. A descrição corresponde ao cenário 'Acessar histórico de pedidos' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/order-history | /#/order-history | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #1c08-9515e65bc503f871 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. Texto transitório capturado: Price \| Quantity \| Apple Juice (1000ml) \| 1 \| rate_review Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close ac |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #1c08-9515e65bc503f871 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. X |
