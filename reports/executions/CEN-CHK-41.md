# Ficha de Cenário

**ID do cenário:** CEN-CHK-41
**Domínio:** CHK
**Nome do cenário:** Rastrear pedido inexistente
**Ator:** Visitante não autenticado
**Fluxo:** Abrir o rastreamento com um código de pedido que não existe.

## Pré-condição (estado inicial)

Sem sessão ativa.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Abrir o rastreamento com um código de pedido que não existe.'. A descrição corresponde ao cenário 'Rastrear pedido inexistente' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/track-result?id=pedido-inexistente-000 Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - pedido-inexistente-000 Expected Delivery ? | Days Ordered products Product Price Quantity Total Price Bonus Points Earned: {{bonus}} (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) Texto transitório capturado: Search Results - pedido-inexistente-000 | Search Results - pedido-inexistente-000 Expected Delivery ? Days Ordered products Product Price Quantity Total Price Bonus Points Earned: {{bonus}} (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - pedido-inexistente-000 Expected Delivery ? Days Ordered products Product Price Quantity Total Price Bonus Points Earned: {{bonus}} (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) | ? Days | Expected Delivery ? Days Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0 | EN | language EN | account_circle Account shopping_cart Your Basket 0 language EN | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0
- EN
- language EN
- account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - Expected Delivery Days Ordered products Product Price Quantity Total Price Bonus Points Earned: {{bonus}} (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!)
- Search Results - Expected Delivery Days Ordered products Product Price Quantity Total Price Bonus Points Earned: {{bonus}} (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!)
- Days
- Expected Delivery Days
- Bonus Points Earned: {{bonus}}
- Bonus Points Earned: {{bonus}} (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!)
- The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!
- (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!)
- added 1:1 to your wallet ¤-fund
- Product Price Quantity Total Price
- Product
- Price
- Quantity
- Total Price
- Search Results

## Dados manipulados

Dados declarados no cenário: id 'pedido-inexistente-000'.
Passo 1: /#/track-result?id=pedido-inexistente-000

## Coerente com loja de sucos?

Sim.

## Justificativa

O cliente precisa saber que o código está errado.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Abrir o rastreamento com um código de pedido que não existe.'. A descrição corresponde ao cenário 'Rastrear pedido inexistente' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/track-result?id=pedido-inexistente-000 | /#/track-result?id=pedido-inexistente-000 | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/track-result?id=pedido-inexistente-000 Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - pedido-inexistente-000 Expected Delivery ? \| Days Ordered products Product Price Quantity Total Price Bonus Points Earned: {{bonus}} (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) Texto transitório capturado: Search Results - pedido-inexistente-000 \| Search Results - pedido-inexistente-000 Expected Delivery ? Days Ordered products Product Price Quantity Total Price Bonus Points Earned: {{bonus}} (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Resul |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Search Results - pedido-inexistente-000 Expected Delivery ? Days Ordered products Product Price Quantity Total Price Bonus Points Earned: {{bonus}} (The bonus points from this order will be added 1:1 to your wallet ¤-fund for future purchases!) |
