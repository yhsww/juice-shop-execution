# Ficha de Cenário

**ID do cenário:** CEN-CHK-20
**Domínio:** CHK
**Nome do cenário:** Visualizar status de trânsito
**Ator:** Cliente
**Fluxo:** Conferir o status de trânsito de um pedido.

## Pré-condição (estado inicial)

Cliente autenticado; pedido concluído.

## Descrição do cenário

Cliente executa o fluxo 'Conferir o status de trânsito de um pedido.'. A descrição corresponde ao cenário 'Visualizar status de trânsito' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #d9e0-077edcda7015af96 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. Texto transitório capturado: Price | Quantity | Apple Juice (1000ml) | 1 | rate_review Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. | Order History No results found You have not placed any orders yet. | Order History | No results found You have not placed any orders yet.
2. URL: http://127.0.0.1:3000/#/order-history → http://127.0.0.1:3000/#/track-result?id=d9e0-077edcda7015af96 Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Search Results - d9e0-077edcda7015af96 Expected Delivery 5 Days Ordered products Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ Bonus Points Earned: 0 (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) Texto transitório capturado: Search Results - d9e0-077edcda7015af96 | 5 Days | Expected Delivery 5 Days | Bonus Points Earned: 0 | Bonus Points Earned: 0 (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) Mensagem transitória: Placed Apple Juice (1000ml) into basket. X | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #d9e0-077edcda7015af96 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. X | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! M

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet.
- Order History No results found You have not placed any orders yet.
- Order History
- No results found You have not placed any orders yet.
- No results found
- You have not placed any orders yet.
- Order History Order ID #d9e0-077edcda7015af96 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #d9e0-077edcda7015af96 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #d9e0-077edcda7015af96 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. X
- Order ID #d9e0-077edcda7015af96 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review
- Order ID
- Order ID #d9e0-077edcda7015af96
- Order ID #d9e0-077edcda7015af96 Total Price 1.99¤ Bonus 0 In Transit local_shipping note
- #d9e0-077edcda7015af96
- Total Price
- Total Price 1.99¤
- 1.99¤
- Bonus
- Bonus 0

## Dados manipulados

Dados declarados no cenário: Pedido de teste.
Passo 1: /#/order-history

## Coerente com loja de sucos?

Sim.

## Justificativa

O status informa a situação logística do pedido.

## Descrição funcional do cenário

Cliente executa o fluxo 'Conferir o status de trânsito de um pedido.'. A descrição corresponde ao cenário 'Visualizar status de trânsito' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/order-history | /#/order-history | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #d9e0-077edcda7015af96 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. Texto transitório capturado: Price \| Quantity \| Apple Juice (1000ml) \| 1 \| rate_review Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close ac |
| 2 | Clicar em "Track Your Order" |  | URL: http://127.0.0.1:3000/#/order-history → http://127.0.0.1:3000/#/track-result?id=d9e0-077edcda7015af96 Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Search Results - d9e0-077edcda7015af96 Expected Delivery 5 Days Ordered products Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ Bonus Points Earned: 0 (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) Texto transitório capturado: Search Results - d9e0-077edcda7015af96 \| 5 Days \| Expected Delivery 5 Days \| Bonus Points Earned: 0 \| Bonus Points Earned: 0 (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) Mensagem transitória: Placed Apple Juice (1000ml) into basket. X \| This website uses fruit cookies to ensure you get the juiciest tracking experie |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Search Results - d9e0-077edcda7015af96 Expected Delivery 5 Days Ordered products Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ Bonus Points Earned: 0 (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) |
