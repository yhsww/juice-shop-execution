# Ficha de Cenário

**ID do cenário:** CEN-CHK-09
**Domínio:** CHK
**Nome do cenário:** Avançar da etapa de pagamento
**Ator:** Cliente
**Fluxo:** Selecionar a linha do cartão terminado em 0002 e prosseguir para o resumo do pedido.

## Pré-condição (estado inicial)

Cliente autenticado; método de entrega selecionado; cartão de teste cadastrado.

## Descrição do cenário

Cliente executa o fluxo 'Selecionar a linha do cartão terminado em 0002 e prosseguir para o resumo do pedido.'. A descrição corresponde ao cenário 'Avançar da etapa de pagamento' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/payment/shop → http://127.0.0.1:3000/#/order-summary Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-09-7729bcd1f5@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Payment Method | Card ending in | Card ending in 0002 | Card Holder" | Card Holder" Cliente Teste Mensagem transitória: ************0002 Cliente Teste 12/2090 | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | navigate_next Continue | navigate_before Back You can review this order before it is finalized. navigate_next Continue | My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to rece

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- ************0002 Cliente Teste 12/2090
- navigate_next Continue
- navigate_before Back You can review this order before it is finalized. navigate_next Continue
- My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
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

## Dados manipulados

Dados declarados no cenário: Cartão de teste cadastrado terminado em 0002.
Passo 1: /#/payment/shop

## Coerente com loja de sucos?

Sim.

## Justificativa

A etapa de pagamento deve levar ao resumo do pedido.

## Descrição funcional do cenário

Cliente executa o fluxo 'Selecionar a linha do cartão terminado em 0002 e prosseguir para o resumo do pedido.'. A descrição corresponde ao cenário 'Avançar da etapa de pagamento' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 2 | Clicar em "0002" |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| ************0002 Cliente Teste 12/2090 \| navigate_next Continue \| navigate_before Back You can review this order before it is finalized. navigate_next Continue \| My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.0 |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 4 | Clicar em "Continue" |  | URL: http://127.0.0.1:3000/#/payment/shop → http://127.0.0.1:3000/#/order-summary Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-09-7729bcd1f5@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Payment Method \| Card ending in \| Card ending in 0002 \| Card Holder" \| Card Holder" Cliente Teste Mensagem transitória: ************0002 Cliente Teste 12/2090 \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice  |
| 5 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-09-7729bcd1f5@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! |
