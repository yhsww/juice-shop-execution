# Ficha de Cenário

**ID do cenário:** CEN-CHK-26
**Domínio:** CHK
**Nome do cenário:** Conferir total no resumo
**Ator:** Cliente
**Fluxo:** Comparar o total exibido no carrinho com o total do resumo.

## Pré-condição (estado inicial)

Carrinho e checkout preparados.

## Descrição do cenário

Cliente executa o fluxo 'Comparar o total exibido no carrinho com o total do resumo.'. A descrição corresponde ao cenário 'Conferir total no resumo' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Payment Method | Card ending in | Card ending in 0002 | Card Holder" | Card Holder" Cliente Teste Mensagem transitória: 1.99¤ | Items 1.99¤ | Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ | Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!

## Mensagens exibidas ao usuário

- 1.99¤
- Items 1.99¤
- Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤
- Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- Total Price 1.99¤
- Apple Juice (1000ml) 1 1.99¤
- Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤
- Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- Apple Juice (1000ml)
- 1
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order!
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste
- Delivery Address
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999
- Cliente Teste
- Rua Teste, 100, Fortaleza, CE, 60000000

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/order-summary

## Coerente com loja de sucos?

Sim.

## Justificativa

A consistência do valor é essencial para confirmar a compra.

## Descrição funcional do cenário

Cliente executa o fluxo 'Comparar o total exibido no carrinho com o total do resumo.'. A descrição corresponde ao cenário 'Conferir total no resumo' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/order-summary | /#/order-summary | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! Texto transitório capturado: Payment Method \| Card ending in \| Card ending in 0002 \| Card Holder" \| Card Holder" Cliente Teste Mensagem transitória: 1.99¤ \| Items 1.99¤ \| Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ \| Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bo |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Payment Method Card ending in 0002 Card Holder" Cliente Teste Your Basket (cen-cen-chk-26-b71da88ccc@example.com) Apple Juice (1000ml) 1 1.99¤ Order Summary Items 1.99¤ Delivery 0.00¤ Promotion 0.00¤ Total Price 1.99¤ monetization_onPlace your order and pay You will gain 0 Bonus Points from this order! |
