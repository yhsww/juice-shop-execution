# Ficha de Cenário

**ID do cenário:** CEN-CHK-21
**Domínio:** CHK
**Nome do cenário:** Acessar PDF de pedido pelo histórico
**Ator:** Cliente
**Fluxo:** Abrir o histórico de pedidos e acionar a impressão da confirmação associada ao pedido de teste.

## Pré-condição (estado inicial)

Cliente autenticado; pedido concluído.

## Descrição do cenário

Cliente executa o fluxo 'Abrir o histórico de pedidos e acionar a impressão da confirmação associada ao pedido de teste.'. A descrição corresponde ao cenário 'Acessar PDF de pedido pelo histórico' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. Texto transitório capturado: Price | Quantity | Apple Juice (1000ml) | 1 | rate_review Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. | Order History No results found You have not placed any orders yet. | Order History | No results found You have not placed any orders yet.
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Placed Apple Juice (1000ml) into basket. X Print Order Confirmation | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. X Print Order Confirmation | Print Order Confirmation | Placed Apple Juice (1000ml) into basket. X | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Print Order Confirmation Mensagem transitória: note | Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note | Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet.
- Order History No results found You have not placed any orders yet.
- Order History
- No results found You have not placed any orders yet.
- No results found
- You have not placed any orders yet.
- Order History Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. X
- Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review
- Order ID
- Order ID #b3a8-3f56a97055242e35
- Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note
- #b3a8-3f56a97055242e35
- Total Price
- Total Price 1.99¤
- 1.99¤
- Bonus
- Bonus 0

## Dados manipulados

Dados declarados no cenário: Pedido concluído disponível no histórico.
Passo 1: /#/order-history

## Coerente com loja de sucos?

Sim.

## Justificativa

O PDF permite obter uma confirmação documental.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir o histórico de pedidos e acionar a impressão da confirmação associada ao pedido de teste.'. A descrição corresponde ao cenário 'Acessar PDF de pedido pelo histórico' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/order-history | /#/order-history | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. Texto transitório capturado: Price \| Quantity \| Apple Juice (1000ml) \| 1 \| rate_review Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History No results found You have not placed any orders yet. Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close ac |
| 2 | Clicar em "Print order confirmation" |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Placed Apple Juice (1000ml) into basket. X Print Order Confirmation \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Order History Order ID #b3a8-3f56a97055242e35 Total Price 1.99¤ Bonus 0 In Transit local_shipping note Product Price Quantity Total Price Apple Juice (1000ml) 1.99¤ 1 1.99¤ rate_review Placed Apple Juice (1000ml) into basket. X Print Order Confirmation \| Print Order Confirmation \| Placed Apple Juice (1000ml) into basket. X \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 lan |
