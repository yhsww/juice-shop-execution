# Ficha de Cenário

**ID do cenário:** CEN-CHK-22
**Domínio:** CHK
**Nome do cenário:** Verificar carrinho após conclusão
**Ator:** Cliente
**Fluxo:** Abrir o carrinho após a conclusão do pedido e verificar que o produto comprado não permanece como item pendente.

## Pré-condição (estado inicial)

Cliente autenticado; pedido concluído com sucesso.

## Descrição do cenário

Cliente executa o fluxo 'Abrir o carrinho após a conclusão do pedido e verificar que o produto comprado não permanece como item pendente.'. A descrição corresponde ao cenário 'Verificar carrinho após conclusão' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: (cen-cen-chk-22-a3a45b746f@example.com) | Your Basket (cen-cen-chk-22-a3a45b746f@example.com) | Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ | Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Your Basket Total Price: 0¤ Checkout You

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Checkout
- You will gain 0 Bonus Points from this order!
- Your Basket
- Your Basket Total Price: 0¤
- Total Price: 0¤
- (cen-cen-chk-22-a3a45b746f@example.com)
- Your Basket (cen-cen-chk-22-a3a45b746f@example.com)
- Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤
- Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X

## Dados manipulados

Dados declarados no cenário: Pedido de teste concluído; o produto utilizado no pedido foi Apple Juice.
Passo 1: /#/basket

## Coerente com loja de sucos?

Sim.

## Justificativa

Após a conclusão, os produtos comprados não devem permanecer como itens pendentes no carrinho.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir o carrinho após a conclusão do pedido e verificar que o produto comprado não permanece como item pendente.'. A descrição corresponde ao cenário 'Verificar carrinho após conclusão' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket | /#/basket | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: (cen-cen-chk-22-a3a45b746f@example.com) \| Your Basket (cen-cen-chk-22-a3a45b746f@example.com) \| Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ \| Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Tota |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-chk-22-a3a45b746f@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X |
