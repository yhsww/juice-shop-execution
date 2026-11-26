# Ficha de Cenário

**ID do cenário:** CEN-CAT-05
**Domínio:** CAT
**Nome do cenário:** Pesquisa sem resultado
**Ator:** Cliente
**Fluxo:** Pesquisar por termo sem correspondência.

## Pré-condição (estado inicial)

Catálogo disponível.

## Descrição do cenário

Cliente executa o fluxo 'Pesquisar por termo sem correspondência.'. A descrição corresponde ao cenário 'Pesquisa sem resultado' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/search Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Lemon Juice (500ml) 2.99¤ add_shopping_cart Add to B Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0 | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0 Language has been changed to English Force page reload | All Products Items per page: 15 0 of 0 | All Products | Items per page: 15 0 of 0
2. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/search?q=ProdutoInexistenteXYZ Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - ProdutoInexistenteXYZ No results found Try adjusting your search to find what you're looking for. Texto transitório capturado: Try adjusting your search to find what you're looking for. | 0 of 0 | Items per page: 16 0 of 0 | 15 | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 langua

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0 Language has been changed to English Force page reload
- All Products Items per page: 15 0 of 0
- All Products
- Items per page: 15 0 of 0
- Items per page: 15
- 0 of 0
- Items per page:
- 15
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Items per page: 15 1 – 15 of 46 Language has been changed to English Force page reload
- Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket
- All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Items per page: 15 1 – 15 of 46
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Items per page: 15 1 – 15 of 46
- Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket
- Apple Pomace 0.89¤ add_shopping_cart Add to Basket
- Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket
- Basil Smoothie 2.99¤ add_shopping_cart Add to Basket
- Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket
- Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket
- Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket

## Dados manipulados

Dados declarados no cenário: Termo: ProdutoInexistenteXYZ.
Passo 1: /#/search
Passo 2: ProdutoInexistenteXYZ

## Coerente com loja de sucos?

Sim.

## Justificativa

O usuário precisa receber um estado claro quando não houver resultado.

## Descrição funcional do cenário

Cliente executa o fluxo 'Pesquisar por termo sem correspondência.'. A descrição corresponde ao cenário 'Pesquisa sem resultado' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/search | /#/search | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/search Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shoppin |
| 2 | Preencher "Search" | ProdutoInexistenteXYZ | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Click for more information Click for more information \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eg |
| 3 | Pressionar Enter |  | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/search?q=ProdutoInexistenteXYZ Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - ProdutoInexistenteXYZ No results found Try adjusting your search to find what you're looking for. Texto transitório capturado: Try adjusting your search to find what you're looking for. \| 0 of 0 \| Items per page: 16 0 of 0 \| 15 \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - ProdutoInexistenteXYZ No results found Try adjusting your search to find what you're looking for. Items per page: 15 0 of 0 Mensagem transitória: Search Results - ProdutoInexistenteXYZ \| Search Results -  |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - ProdutoInexistenteXYZ No results found Try adjusting your search to find what you're looking for. Items per page: 15 0 of 0 |
