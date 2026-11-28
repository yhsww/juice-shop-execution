# Ficha de Cenário

**ID do cenário:** CEN-CAR-08
**Domínio:** CAR
**Nome do cenário:** Aumentar quantidade com verificação do total
**Ator:** Cliente autenticado
**Fluxo:** Com 1 Apple Juice no carrinho, clicar em aumentar e conferir quantidade 2 e total 3.98¤.

## Pré-condição (estado inicial)

Cliente autenticado; há pelo menos um produto no carrinho (conta nova: 1 unidade de Apple Juice).

## Descrição do cenário

Cliente autenticado executa o fluxo 'Com 1 Apple Juice no carrinho, clicar em aumentar e conferir quantidade 2 e total 3.98¤.'. A descrição corresponde ao cenário 'Aumentar quantidade com verificação do total' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ | Apple Juice (1000ml) 1 1.99¤ | Apple Juice (1000ml) | 1 | 1.99¤ Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Checkout | You will gain 0 Bonus Points from this order!
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 2 | 1.99¤ | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 2 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 2 1.99¤ Total Price: 3.98¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 2 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 2 1.99¤ Total Price: 3.98¤ Checkout You will gain 0 Bonus Points from this order! Mensagem transitória: 1 | Apple Juice (1000ml) 1 1.99¤ | Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | Total Price: 3.98¤

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- Checkout
- You will gain 0 Bonus Points from this order!
- Your Basket
- Your Basket Total Price: 0¤
- Total Price: 0¤
- (cen-cen-car-08-8e3a01b9c3@example.com)
- Your Basket (cen-cen-car-08-8e3a01b9c3@example.com)
- Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Total Price: 0¤
- Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X
- Total Price: 1.99¤
- Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤
- Apple Juice (1000ml) 1 1.99¤
- Apple Juice (1000ml)

## Dados manipulados

Dados declarados no cenário: Apple Juice 1.99¤.
Passo 1: /#/basket

## Coerente com loja de sucos?

Sim.

## Justificativa

O CEN-CAR-03 atual passa por coincidência (o '2' de 'v20.3.0'); este cenário verifica o total.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Com 1 Apple Juice no carrinho, clicar em aumentar e conferir quantidade 2 e total 3.98¤.'. A descrição corresponde ao cenário 'Aumentar quantidade com verificação do total' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket | /#/basket | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ \| Apple Juice (1000ml) 1 1.99¤ \| Apple Juice (1000ml) \| 1 \| 1.99¤ Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Yo |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X |
| 3 | Clicar no elemento |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 2 \| 1.99¤ \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 2 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 2 1.99¤ Total Price: 3.98¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X \| Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 2 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 2 1.99¤ Total Price: 3.98¤ Checkout You will gain 0 Bonus Points from this order! Mensagem transitória: 1 \| Apple Juice (1000ml) 1 1.99¤ \| Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ \| menu OWASP Juice Shop search sea |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 2 language EN Your Basket (cen-cen-car-08-8e3a01b9c3@example.com) Apple Juice (1000ml) 2 1.99¤ Total Price: 3.98¤ Checkout You will gain 0 Bonus Points from this order! |
