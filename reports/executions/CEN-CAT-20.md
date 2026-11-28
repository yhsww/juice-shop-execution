# Ficha de Cenário

**ID do cenário:** CEN-CAT-20
**Domínio:** CAT
**Nome do cenário:** Busca só com espaços
**Ator:** Visitante não autenticado
**Fluxo:** Digitar apenas espaços no campo de busca e confirmar.

## Pré-condição (estado inicial)

Catálogo disponível.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Digitar apenas espaços no campo de busca e confirmar.'. A descrição corresponde ao cenário 'Busca só com espaços' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/search Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping Texto transitório capturado: 1 – 16 of 46 | 16 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Lemon Juice (500ml) 2.99¤ add_shopping_cart Add to Basket Items per page: 16 1 – 16 of 46 | Items per page: 16 | Items per page: 16 1 – 16 of Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder All Products Items per page: 15 0 of 0 | All Products Items per page: 15 0 of 0 | All Products | Items per page: 15 0 of 0 | Items per page: 15
2. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/search?q=%20%20%20 Texto transitório capturado: Search Results - | Search Results - Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shop

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder All Products Items per page: 15 0 of 0
- All Products Items per page: 15 0 of 0
- All Products
- Items per page: 15 0 of 0
- Items per page: 15
- 0 of 0
- Items per page:
- 15
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0
- EN
- language EN
- account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Items per page: 15 1 – 15 of 46
- Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket
- All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Items per page: 15 1 – 15 of 46
- Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket
- Apple Pomace 0.89¤ add_shopping_cart Add to Basket
- Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket
- Basil Smoothie 2.99¤ add_shopping_cart Add to Basket

## Dados manipulados

Dados declarados no cenário: ' '.
Passo 1: /#/search

## Coerente com loja de sucos?

Sim.

## Justificativa

Busca vazia deve ter comportamento previsível (todos os produtos ou nenhum).

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Digitar apenas espaços no campo de busca e confirmar.'. A descrição corresponde ao cenário 'Busca só com espaços' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/search | /#/search | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/search Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping Texto transitório capturado: 1 – 16 of 46 \| 16 \| menu OWASP Juice Shop search search close account_circle Account shopp |
| 2 | Preencher "Search" |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: search search close \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shop |
| 3 | Pressionar Enter |  | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/search?q=%20%20%20 Texto transitório capturado: Search Results - \| Search Results - Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_sho |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_ca |
