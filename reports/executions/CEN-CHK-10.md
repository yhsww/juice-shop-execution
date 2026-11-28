# Ficha de Cenário

**ID do cenário:** CEN-CHK-10
**Domínio:** CHK
**Nome do cenário:** Conferir resumo do pedido
**Ator:** Cliente
**Fluxo:** Visualizar os dados consolidados antes da confirmação.

## Pré-condição (estado inicial)

Cliente autenticado; pedido com endereço, entrega e pagamento definidos.

## Descrição do cenário

Cliente executa o fluxo 'Visualizar os dados consolidados antes da confirmação.'. A descrição corresponde ao cenário 'Conferir resumo do pedido' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Payment Method | Card ending in | Card ending in 0002 | Card Holder" | Card Holder" Cliente Teste Mensagem transitória: Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) | Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) Order Summary Items 0.00¤ Delivery 0

## Mensagens exibidas ao usuário

- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com)
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
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
- Card Holder"
- Card Holder" Cliente Teste

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/order-summary

## Coerente com loja de sucos?

Sim.

## Justificativa

O resumo permite validar a compra antes da confirmação.

## Descrição funcional do cenário

Cliente executa o fluxo 'Visualizar os dados consolidados antes da confirmação.'. A descrição corresponde ao cenário 'Conferir resumo do pedido' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/order-summary | /#/order-summary | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Payment Method \| Card ending in \| Card ending in 0002 \| Card Holder" \| Card Holder" Cliente Teste Mensagem transitória: Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) \| Delivery Address Cliente Teste  |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-10-1fb1029e94@example.com) Order Summary Items 0.00¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 0.00¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! |
