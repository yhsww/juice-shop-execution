# Ficha de Cenário

**ID do cenário:** CEN-PER-06
**Domínio:** PER
**Nome do cenário:** Visualização do histórico de pedidos
**Ator:** Cliente autenticado
**Fluxo:** Abrir a área de pedidos e consultar pedidos realizados.

## Pré-condição (estado inicial)

Cliente autenticado; pode não haver pedidos anteriores.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir a área de pedidos e consultar pedidos realizados.'. A descrição corresponde ao cenário 'Visualização do histórico de pedidos' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. Texto transitório capturado: Order History No results found You have not placed any orders yet. | Order History | No results found You have not placed any orders yet. | No results found | You have not placed any orders yet. Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! | 0 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. | Order History No results found You have not placed any orders yet.

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it!
- 0
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet.
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet.
- Order History No results found You have not placed any orders yet.
- Order History
- No results found You have not placed any orders yet.
- No results found
- You have not placed any orders yet.

## Dados manipulados

Dados declarados no cenário: Nenhum dado pessoal adicional.
Passo 1: /#/order-history

## Coerente com loja de sucos?

Sim.

## Justificativa

O histórico permite acompanhar compras atuais e anteriores.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir a área de pedidos e consultar pedidos realizados.'. A descrição corresponde ao cenário 'Visualização do histórico de pedidos' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir o histórico de pedidos | /#/order-history | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. Texto transitório capturado: Order History No results found You have not placed any orders yet. \| Order History \| No results found You have not placed any orders yet. \| No results found \| You have not placed any orders yet. Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! \| 0 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! \| 0 |
