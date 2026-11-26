# Ficha de Cenário

**ID do cenário:** CEN-PER-03
**Domínio:** PER
**Nome do cenário:** Acesso às opções de pagamento
**Ator:** Cliente autenticado
**Fluxo:** Abrir a área de opções de pagamento e consultar os cartões salvos.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir a área de opções de pagamento e consultar os cartões salvos.'. A descrição corresponde ao cenário 'Acesso às opções de pagamento' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/saved-payment-methods Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Texto transitório capturado: My Payment Options Add new card Add a credit or debit card | My Payment Options | Add new card | Add new card Add a credit or debit card | Add a credit or debit card Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card | My Payment Options Add new card Add a credit or debit card | My Payment Options | Add new card

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card
- My Payment Options Add new card Add a credit or debit card
- My Payment Options
- Add new card
- Add new card Add a credit or debit card
- Add a credit or debit card

## Dados manipulados

Dados declarados no cenário: Nenhum dado real de cartão.
Passo 1: /#/saved-payment-methods

## Coerente com loja de sucos?

Sim.

## Justificativa

A gestão dos meios de pagamento é necessária para compras recorrentes.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir a área de opções de pagamento e consultar os cartões salvos.'. A descrição corresponde ao cenário 'Acesso às opções de pagamento' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/saved-payment-methods | /#/saved-payment-methods | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/saved-payment-methods Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Texto transitório capturado: My Payment Options Add new card Add a credit or debit card \| My Payment Options \| Add new card \| Add new card Add a credit or debit card \| Add a credit or debit card Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card |
