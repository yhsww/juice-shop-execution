# Ficha de Cenário

**ID do cenário:** CEN-CHK-08
**Domínio:** CHK
**Nome do cenário:** Selecionar cartão de crédito
**Ator:** Cliente
**Fluxo:** Selecionar a linha do cartão de teste cadastrado, identificada pelos quatro últimos dígitos 0002.

## Pré-condição (estado inicial)

Cliente autenticado; método de entrega selecionado; cartão de teste cadastrado.

## Descrição do cenário

Cliente executa o fluxo 'Selecionar a linha do cartão de teste cadastrado, identificada pelos quatro últimos dígitos 0002.'. A descrição corresponde ao cenário 'Selecionar cartão de crédito' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

A execução foi concluída na URL observada: http://127.0.0.1:3000/#/payment/shop.

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- ************0002 Cliente Teste 12/2090
- navigate_next Continue
- navigate_before Back You can review this order before it is finalized. navigate_next Continue
- My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue

## Dados manipulados

Dados declarados no cenário: Cartão de teste cadastrado terminado em 0002.
Passo 1: /#/payment/shop

## Coerente com loja de sucos?

Sim.

## Justificativa

A seleção define a forma de pagamento do pedido.

## Descrição funcional do cenário

Cliente executa o fluxo 'Selecionar a linha do cartão de teste cadastrado, identificada pelos quatro últimos dígitos 0002.'. A descrição corresponde ao cenário 'Selecionar cartão de crédito' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 3 | Clicar em "0002" |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| ************0002 Cliente Teste 12/2090 \| navigate_next Continue \| navigate_before Back You can review this order before it is finalized. navigate_next Continue \| My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.0 |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
