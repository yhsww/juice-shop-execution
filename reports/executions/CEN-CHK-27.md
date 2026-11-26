# Ficha de Cenário

**ID do cenário:** CEN-CHK-27
**Domínio:** CHK
**Nome do cenário:** Retornar de uma etapa do checkout
**Ator:** Cliente
**Fluxo:** Selecionar 'Standard Delivery', avançar para pagamento, retornar à etapa de entrega e verificar que a opção pode ser selecionada novamente.

## Pré-condição (estado inicial)

Cliente autenticado; endereço de entrega selecionado.

## Descrição do cenário

Cliente executa o fluxo 'Selecionar 'Standard Delivery', avançar para pagamento, retornar à etapa de entrega e verificar que a opção pode ser selecionada novamente.'. A descrição corresponde ao cenário 'Retornar de uma etapa do checkout' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue Texto transitório capturado: 3 Days | Standard Delivery 0.00¤ 5 Days | Standard Delivery | 0.00¤ | 5 Days Mensagem transitória: Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue | Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 | Cliente Teste
2. URL: http://127.0.0.1:3000/#/delivery-method → http://127.0.0.1:3000/#/payment/shop Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. | navigate_next Continue Texto transitório capturado: 0.00 | Wallet Balance 0.00 | Pay using wallet Wallet Balance 0.00 Pay NaN¤ | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment 

## Mensagens exibidas ao usuário

- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999
- Cliente Teste
- Rua Teste, 100, Fortaleza, CE, 60000000
- Brazil
- Phone Number 8599999999
- Delivery Address
- Phone Number
- Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days
- Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue
- One Day Delivery 0.99¤ 1 Days
- One Day Delivery
- 0.99¤
- 1 Days
- Fast Delivery 0.50¤ 3 Days
- Fast Delivery

## Dados manipulados

Dados declarados no cenário: Método selecionado: Standard Delivery.
Passo 1: /#/delivery-method

## Coerente com loja de sucos?

Sim.

## Justificativa

O usuário precisa corrigir dados antes de concluir a compra.

## Descrição funcional do cenário

Cliente executa o fluxo 'Selecionar 'Standard Delivery', avançar para pagamento, retornar à etapa de entrega e verificar que a opção pode ser selecionada novamente.'. A descrição corresponde ao cenário 'Retornar de uma etapa do checkout' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/delivery-method | /#/delivery-method | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue Texto transitório capturado: 3 Days \| Standard Delivery 0.00¤ 5 Days \| Standard Delivery \| 0.00¤ \| 5 Days Mensagem transitória: Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 6000 |
| 2 | Clicar em "Standard Delivery" |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days \| Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days \| navigate_nextContinue \| navigate_before Back navigate_nextContinue \| Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket |
| 3 | Clicar em "Proceed to delivery method selection" |  | URL: http://127.0.0.1:3000/#/delivery-method → http://127.0.0.1:3000/#/payment/shop Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. \| navigate_next Continue Texto transitório capturado: 0.00 \| Wallet Balance 0.00 \| Pay using wallet Wallet Balance 0.00 Pay NaN¤ \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 P |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 5 | Clicar em "Back" |  | URL: http://127.0.0.1:3000/#/payment/shop → http://127.0.0.1:3000/#/delivery-method Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue Texto transitório capturado: 3 Days \| Standard Delivery 0.00¤ 5 Days \| Standard Delivery \| 0.00¤ \| 5 Days Mensagem transitória: navigate_before Back \| navigate_before Back You can review this order before it is finalized. navigate_next Continue \| My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other |
| 6 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue |
| 7 | Clicar em "Standard Delivery" |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days \| Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days \| navigate_nextContinue \| navigate_before Back navigate_nextContinue \| Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket |
| 8 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue |
| 9 | ASSERT_SELECTED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue |
