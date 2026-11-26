# Ficha de Cenário

**ID do cenário:** CEN-PER-06
**Domínio:** PER
**Nome do cenário:** Visualização do histórico de pedidos
**Ator:** Cliente autenticado; pode não haver pedidos anteriores.
**Fluxo:** Abrir a área de pedidos e consultar pedidos realizados.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado; pode não haver pedidos anteriores. executa o fluxo 'Abrir a área de pedidos e consultar pedidos realizados.'. A descrição corresponde ao cenário 'Visualização do histórico de pedidos' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. Texto transitório capturado: Order History No results found You have not placed any orders yet. | Order History | No results found You have not placed any orders yet. | No results found | You have not placed any orders yet. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. | Order History No results found You have not placed any orders yet. | Order History | No results found You have not placed any orders yet.

## Mensagens exibidas ao usuário

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

Cliente autenticado; pode não haver pedidos anteriores. executa o fluxo 'Abrir a área de pedidos e consultar pedidos realizados.'. A descrição corresponde ao cenário 'Visualização do histórico de pedidos' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/order-history | /#/order-history | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. Texto transitório capturado: Order History No results found You have not placed any orders yet. \| Order History \| No results found You have not placed any orders yet. \| No results found \| You have not placed any orders yet. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language E |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. |
