# Ficha de Cenário

**ID do cenário:** CEN-CHK-11
**Domínio:** CHK
**Nome do cenário:** Confirmar pedido
**Ator:** Cliente
**Fluxo:** Confirmar a compra a partir do resumo.

## Pré-condição (estado inicial)

Cliente autenticado; resumo do pedido acessível.

## Descrição do cenário

Cliente executa o fluxo 'Confirmar a compra a partir do resumo.'. A descrição corresponde ao cenário 'Confirmar pedido' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Payment Method | Card ending in | Card ending in 0002 | Card Holder" | Card Holder" Cliente Teste Mensagem transitória: (cen-cen-chk-11-2f329af570@example.com) | Your Basket (cen-cen-chk-11-2f329af570@example.com) | Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! | Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-11-2f329af570@example.com)
2. URL: http://127.0.0.1:3000/#/order-summary → http://127.0.0.1:3000/#/order-completion/3983-d6ade1f6f90d5fca Texto visível: Your order has been placed and is being processed. | You can check for status updates on our Track Orders page. | Your order will be delivered in 5 days. | Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Order Summary note Product Price Quantity Total Price Items Delivery Promotion Total Price 0.00¤ 0.00¤ 0.00¤ 0.00¤ You have gained 0 Bonus Points from this order! Texto transitório capturado: Rua Teste, 100, Fortaleza, CE, 60000000 | Brazil | Phone Number 8599999999 | Delivery Address | Phone Number Mensagem transitória: monetization_onPlace your order and pay | Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! | Delivery A

## Mensagens exibidas ao usuário

- (cen-cen-chk-11-2f329af570@example.com)
- Your Basket (cen-cen-chk-11-2f329af570@example.com)
- Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-11-2f329af570@example.com)
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste
- Delivery Address
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999
- Cliente Teste
- Rua Teste, 100, Fortaleza, CE, 60000000
- Brazil
- Phone Number
- Phone Number 8599999999
- Payment Method Card ending in 0002 Card Holder" Cliente Teste
- Payment Method
- Card ending in
- Card ending in 0002

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/order-summary

## Coerente com loja de sucos?

Sim.

## Justificativa

A confirmação conclui o fluxo de compra.

## Descrição funcional do cenário

Cliente executa o fluxo 'Confirmar a compra a partir do resumo.'. A descrição corresponde ao cenário 'Confirmar pedido' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/order-summary | /#/order-summary | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Payment Method \| Card ending in \| Card ending in 0002 \| Card Holder" \| Card Holder" Cliente Teste Mensagem transitória: (cen-cen-chk-11-2f329af570@example.com) \| Your Basket (cen-cen-chk-11-2f329af570@example.com) \| Your Basket (cen-cen-chk-11-2f329af570@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your |
| 2 | Clicar em "Place your order and pay" |  | URL: http://127.0.0.1:3000/#/order-summary → http://127.0.0.1:3000/#/order-completion/3983-d6ade1f6f90d5fca Texto visível: Your order has been placed and is being processed. \| You can check for status updates on our Track Orders page. \| Your order will be delivered in 5 days. \| Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Order Summary note Product Price Quantity Total Price Items Delivery Promotion Total Price 0.00¤ 0.00¤ 0.00¤ 0.00¤ You have gained 0 Bonus Points from this order! Texto transitório capturado: Rua Teste, 100, Fortaleza, CE, 60000000 \| Brazil \| Phone Number 8599999999 \| Delivery Address \| Phone Number Mensagem transitória: monetization_onPlace your order and pay \| Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points fr |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Thank you for your purchase! Your order has been placed and is being processed. You can check for status updates on our Track Orders page. Your order will be delivered in 5 days. Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Order Summary note Product Price Quantity Total Price Items Delivery Promotion Total Price 0.00¤ 0.00¤ 0.00¤ 0.00¤ You have gained 0 Bonus Points from this order! |
