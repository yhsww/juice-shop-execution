# Ficha de Cenário

**ID do cenário:** CEN-CAR-05
**Domínio:** CAR
**Nome do cenário:** Remover produto do carrinho
**Ator:** Cliente
**Fluxo:** Remover um produto do carrinho.

## Pré-condição (estado inicial)

Há pelo menos um produto no carrinho.

## Descrição do cenário

Cliente executa o fluxo 'Remover um produto do carrinho.'. A descrição corresponde ao cenário 'Remover produto do carrinho' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ | Apple Juice (1000ml) 1 1.99¤ | Apple Juice (1000ml) | 1 | 1.99¤ Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Checkout | You will gain 0 Bonus Points from this order!
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Total Price: 0¤ | Your Basket (anonymous) Total Price: 0¤ | 0 Mensagem transitória: Placed Apple Juice (1000ml) into basket. X | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 la

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Checkout
- You will gain 0 Bonus Points from this order!
- Your Basket (anonymous)
- Your Basket (anonymous) Total Price: 0¤
- (anonymous)
- Total Price: 0¤
- Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- Total Price: 1.99¤
- Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤
- Apple Juice (1000ml) 1 1.99¤
- Apple Juice (1000ml)
- 1
- 1.99¤
- Placed Apple Juice (1000ml) into basket. X
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!

## Dados manipulados

Dados declarados no cenário: Produto selecionado para remoção.
Passo 1: /#/basket

## Coerente com loja de sucos?

Sim.

## Justificativa

A remoção permite corrigir a seleção antes da compra.

## Descrição funcional do cenário

Cliente executa o fluxo 'Remover um produto do carrinho.'. A descrição corresponde ao cenário 'Remover produto do carrinho' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket | /#/basket | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ \| Apple Juice (1000ml) 1 1.99¤ \| Apple Juice (1000ml) \| 1 \| 1.99¤ Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close  |
| 2 | Clicar em "Remove" |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! \| Total Price: 0¤ \| Your Basket (anonymous) Total Price: 0¤ \| 0 Mensagem transitória: Placed Apple Juice (1000ml) into basket. X \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! |
