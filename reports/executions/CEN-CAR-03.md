# Ficha de Cenário

**ID do cenário:** CEN-CAR-03
**Domínio:** CAR
**Nome do cenário:** Alterar quantidade de produto
**Ator:** Cliente
**Fluxo:** Aumentar a quantidade de um produto no carrinho.

## Pré-condição (estado inicial)

Há pelo menos um produto no carrinho.

## Descrição do cenário

Cliente executa o fluxo 'Aumentar a quantidade de um produto no carrinho.'. A descrição corresponde ao cenário 'Alterar quantidade de produto' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ | Apple Juice (1000ml) 1 1.99¤ | Apple Juice (1000ml) | 1 | 1.99¤ Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! | Checkout | You will gain 0 Bonus Points from this order!
2. Texto visível: OWASP Juice Shop Contact feedback Customer Feedback auto_awesome AI Chat IMPROVED Company business_center About Us camera Photo Wall Score Board GitHub OWASP Juice Shop v20.3.0 menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! | Open side menu Texto transitório capturado: Open side menu | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Open side menu | OWASP Juice Shop Contact feedback Customer Feedback auto_awesome AI Chat IMPROVED Company business_center About Us camera Photo Wall Score Board GitHub OWASP Juice Shop v20.3.0 | OWASP Juice Shop Contact feedback Customer Feedback auto_awesome AI Chat IMPROVED Company business_center About Us camera Photo Wall Score Board GitHub OWASP Juice Shop v20.3.0 menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your B

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

Dados declarados no cenário: Quantidade desejada: 2 unidades.
Passo 1: /#/basket

## Coerente com loja de sucos?

Sim.

## Justificativa

A quantidade altera o valor da compra e precisa ser editável.

## Descrição funcional do cenário

Cliente executa o fluxo 'Aumentar a quantidade de um produto no carrinho.'. A descrição corresponde ao cenário 'Alterar quantidade de produto' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/basket | /#/basket | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/basket Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Texto transitório capturado: Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ \| Apple Juice (1000ml) 1 1.99¤ \| Apple Juice (1000ml) \| 1 \| 1.99¤ Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Total Price: 0¤ Checkout You will gain 0 Bonus Points from this order! Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close  |
| 2 | Clicar em "Increase quantity" |  | Texto visível: OWASP Juice Shop Contact feedback Customer Feedback auto_awesome AI Chat IMPROVED Company business_center About Us camera Photo Wall Score Board GitHub OWASP Juice Shop v20.3.0 menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! \| Open side menu Texto transitório capturado: Open side menu \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! Open side menu \| OWASP Juice Shop Contact feedback Customer Feedback  |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! OWASP Juice Shop Contact feedback Customer Feedback auto_awesome AI Chat IMPROVED Company business_center About Us camera Photo Wall Score Board GitHub OWASP Juice Shop v20.3.0 menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Your Basket (anonymous) Apple Juice (1000ml) 1 1.99¤ Total Price: 1.99¤ Checkout You will gain 0 Bonus Points from this order! |
