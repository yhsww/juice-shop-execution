# Ficha de Cenário

**ID do cenário:** CEN-CHK-01
**Domínio:** CHK
**Nome do cenário:** Iniciar checkout
**Ator:** Cliente
**Fluxo:** Abrir o carrinho e iniciar o checkout.

## Pré-condição (estado inicial)

Carrinho contém produto.

## Descrição do cenário

Cliente executa o fluxo 'Abrir o carrinho e iniciar o checkout.'. A descrição corresponde ao cenário 'Iniciar checkout' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ | Apple Juice (1000ml) 1 1.99¤ | Apple Juice (1000ml) | 1 | 1.99¤ Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Checkout | You will gain 0 Bonus Points from this order!
2. URL: http://127.0.0.1:3000/#/basket → http://127.0.0.1:3000/#/address/select Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue Texto transitório capturado: Add New Address | navigate_next | Continue | Placed Apple Juice (1000ml) into basket. X | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue Mensagem transitória: Checkout | Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Checkout
- You will gain 0 Bonus Points from this order!
- Your Basket
- Your Basket Total Price: 0¤
- Total Price: 0¤
- (cen-cen-chk-01-c9711f2c0b@example.com)
- Your Basket (cen-cen-chk-01-c9711f2c0b@example.com)
- Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Total Price: 0¤
- Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- Total Price: 1.99¤
- Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤
- Apple Juice (1000ml) 1 1.99¤
- Apple Juice (1000ml)

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/basket

## Coerente com loja de sucos?

Sim.

## Justificativa

O checkout inicia a etapa de conclusão da compra.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir o carrinho e iniciar o checkout.'. A descrição corresponde ao cenário 'Iniciar checkout' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket | /#/basket | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ \| Apple Juice (1000ml) 1 1.99¤ \| Apple Juice (1000ml) \| 1 \| 1.99¤ Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X \ |
| 2 | Clicar em "Checkout" |  | URL: http://127.0.0.1:3000/#/basket → http://127.0.0.1:3000/#/address/select Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue Texto transitório capturado: Add New Address \| navigate_next \| Continue \| Placed Apple Juice (1000ml) into basket. X \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue Mensagem transitória: Checkout \| Your Basket (cen-cen-chk-01-c9711f2c0b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! \| menu OWASP Juice Shop search search close account_circle |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue |
