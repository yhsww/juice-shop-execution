# Ficha de Cenário

**ID do cenário:** CEN-CHK-04
**Domínio:** CHK
**Nome do cenário:** Confirmar seleção de endereço
**Ator:** Cliente
**Fluxo:** Selecionar um endereço cadastrado e verificar a habilitação do avanço.

## Pré-condição (estado inicial)

Carrinho contém produto; há endereço cadastrado.

## Descrição do cenário

Cliente executa o fluxo 'Selecionar um endereço cadastrado e verificar a habilitação do avanço.'. A descrição corresponde ao cenário 'Confirmar seleção de endereço' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/address/select → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ | Apple Juice (1000ml) 1 1.99¤ | Apple Juice (1000ml) | 1 | 1.99¤ Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Checkout | You will gain 0 Bonus Points from this order!
2. URL: http://127.0.0.1:3000/#/basket → http://127.0.0.1:3000/#/address/select Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue Texto transitório capturado: Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue | Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil | Cliente Teste | Rua Teste, 100, Fortaleza, CE, 60000000 | Brazil Mensagem transitória: Checkout | Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple J

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Checkout
- You will gain 0 Bonus Points from this order!
- Your Basket
- Your Basket Total Price: 0¤
- Total Price: 0¤
- (cen-cen-chk-04-c12a7c055b@example.com)
- Your Basket (cen-cen-chk-04-c12a7c055b@example.com)
- Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Total Price: 0¤
- Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- Total Price: 1.99¤
- Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤
- Apple Juice (1000ml) 1 1.99¤
- Apple Juice (1000ml)

## Dados manipulados

Dados declarados no cenário: Endereço: Rua Teste, 100.
Passo 1: /#/basket

## Coerente com loja de sucos?

Sim.

## Justificativa

A etapa seguinte depende da seleção de um endereço.

## Descrição funcional do cenário

Cliente executa o fluxo 'Selecionar um endereço cadastrado e verificar a habilitação do avanço.'. A descrição corresponde ao cenário 'Confirmar seleção de endereço' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket | /#/basket | URL: http://127.0.0.1:3000/#/address/select → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ \| Apple Juice (1000ml) 1 1.99¤ \| Apple Juice (1000ml) \| 1 \| 1.99¤ Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop searc |
| 2 | Clicar em "Checkout" |  | URL: http://127.0.0.1:3000/#/basket → http://127.0.0.1:3000/#/address/select Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue Texto transitório capturado: Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue \| Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil \| Cliente Teste \| Rua Teste, 100, Fortaleza, CE, 60000000 \| Brazil Mensagem transitória: Checkout \| Your Basket (cen-cen-chk-04-c12a7c055b@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN You |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue |
| 4 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue |
| 5 | Clicar em "Rua Teste, 100" |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue \| Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil \| Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue \| navigate_nextContinue Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 10 |
| 6 | ASSERT_ENABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue |
