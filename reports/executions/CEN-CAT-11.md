# Ficha de Cenário

**ID do cenário:** CEN-CAT-11
**Domínio:** CAT
**Nome do cenário:** Visualização de preço do produto
**Ator:** Cliente
**Fluxo:** Conferir o preço exibido para um produto.

## Pré-condição (estado inicial)

Catálogo disponível.

## Descrição do cenário

Cliente executa o fluxo 'Conferir o preço exibido para um produto.'. A descrição corresponde ao cenário 'Visualização de preço do produto' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (50

## Mensagens exibidas ao usuário

Nenhuma mensagem transitória relevante capturada.

## Dados manipulados

Dados declarados no cenário: Produto: Apple Juice.
Passo 1: /#/

## Coerente com loja de sucos?

Sim.

## Justificativa

O preço é informação essencial para a decisão de compra.

## Descrição funcional do cenário

Cliente executa o fluxo 'Conferir o preço exibido para um produto.'. A descrição corresponde ao cenário 'Visualização de preço do produto' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/ | /#/ | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close a |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Ba |
