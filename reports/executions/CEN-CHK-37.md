# Ficha de Cenário

**ID do cenário:** CEN-CHK-37
**Domínio:** CHK
**Nome do cenário:** Entrega rápida altera o total do resumo
**Ator:** Cliente autenticado
**Fluxo:** Escolher 'One Day Delivery' em vez de Standard e conferir o custo de entrega no resumo.

## Pré-condição (estado inicial)

Cliente autenticado; carrinho contém produto; endereço Rua Teste, 100 cadastrado; método de entrega disponível; cartão de teste terminado em 0002 cadastrado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Escolher 'One Day Delivery' em vez de Standard e conferir o custo de entrega no resumo.'. A descrição corresponde ao cenário 'Entrega rápida altera o total do resumo' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/payment/shop → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ | Apple Juice (1000ml) 1 1.99¤ | Apple Juice (1000ml) | 1 | 1.99¤ Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Checkout | You will gain 0 Bonus Points from this order! | Your Basket
2. URL: http://127.0.0.1:3000/#/basket → http://127.0.0.1:3000/#/address/select Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue Texto transitório capturado: Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue | Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil | Cliente Teste | Rua Teste, 100, Fortaleza, CE, 60000000 | Brazil Mensagem transitória: Checkout | Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue | Select an address addAdd New Address navigate_nextContinue
3. URL: http://127.0.0.1:3000/#/address/select → http://127.0.0.1:3000/#/delivery-method Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed 

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Checkout
- You will gain 0 Bonus Points from this order!
- Your Basket
- Your Basket Total Price: 0¤
- Total Price: 0¤
- (cen-cen-chk-37-350b6055de@example.com)
- Your Basket (cen-cen-chk-37-350b6055de@example.com)
- Your Basket (cen-cen-chk-37-350b6055de@example.com) Total Price: 0¤
- Your Basket (cen-cen-chk-37-350b6055de@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-37-350b6055de@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- Total Price: 1.99¤
- Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤
- Apple Juice (1000ml) 1 1.99¤
- Apple Juice (1000ml)
- 1
- 1.99¤

## Dados manipulados

Dados declarados no cenário: Método 'One Day Delivery'.
Passo 1: /#/basket

## Coerente com loja de sucos?

Sim.

## Justificativa

Cliente paga mais para receber antes.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Escolher 'One Day Delivery' em vez de Standard e conferir o custo de entrega no resumo.'. A descrição corresponde ao cenário 'Entrega rápida altera o total do resumo' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket | /#/basket | URL: http://127.0.0.1:3000/#/payment/shop → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ \| Apple Juice (1000ml) 1 1.99¤ \| Apple Juice (1000ml) \| 1 \| 1.99¤ Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! \| Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! \| Checkout \| You will gain 0 Bonus Points from this o |
| 2 | Clicar em "Checkout" |  | URL: http://127.0.0.1:3000/#/basket → http://127.0.0.1:3000/#/address/select Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue Texto transitório capturado: Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue \| Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil \| Cliente Teste \| Rua Teste, 100, Fortaleza, CE, 60000000 \| Brazil Mensagem transitória: Checkout \| Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN You |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue |
| 4 | Clicar em "Rua Teste, 100" |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue \| Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil \| Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue \| navigate_nextContinue Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue \| Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil \| Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Braz |
| 5 | Clicar em "Continue" |  | URL: http://127.0.0.1:3000/#/address/select → http://127.0.0.1:3000/#/delivery-method Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue Texto transitório capturado: 3 Days \| Standard Delivery 0.00¤ 5 Days \| Standard Delivery \| 0.00¤ \| 5 Days Mensagem transitória: navigate_nextContinue \| Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Te |
| 6 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue |
| 7 | Clicar em "One Day Delivery" |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days \| Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days \| navigate_nextContinue \| navigate_before Back navigate_nextContinue \| Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 859 |
| 8 | Clicar em "Continue" |  | URL: http://127.0.0.1:3000/#/delivery-method → http://127.0.0.1:3000/#/payment/shop Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay 2.98¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. \| navigate_next Continue Texto transitório capturado: My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay 2.98¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| ************0002 Cliente Teste 12/2 |
| 9 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay 2.98¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 10 | Clicar em "0002" |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay 2.98¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| ************0002 Cliente Teste 12/2090 \| navigate_next Continue \| navigate_before Back You can review this order before it is finalized. navigate_next Continue \| My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay 2.98¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back Y |
| 11 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay 2.98¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 12 | Clicar em "Continue" |  | URL: http://127.0.0.1:3000/#/payment/shop → http://127.0.0.1:3000/#/order-summary Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.99¤ Promotion 0.00¤ Total Price 2.98¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ \| Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (ce |
| 13 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-37-350b6055de@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.99¤ Promotion 0.00¤ Total Price 2.98¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! |
