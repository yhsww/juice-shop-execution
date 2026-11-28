# Ficha de Cenário

**ID do cenário:** CEN-CHK-40
**Domínio:** CHK
**Nome do cenário:** Acessar pagamento sem login
**Ator:** Visitante não autenticado
**Fluxo:** Sem sessão, abrir diretamente /#/payment/shop.

## Pré-condição (estado inicial)

Sem sessão ativa.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Sem sessão, abrir diretamente /#/payment/shop.'. A descrição corresponde ao cenário 'Acessar pagamento sem login' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/payment/shop Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. | navigate_next Continue Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | EN | language EN | account_circle Account shopping_cart Your Basket 0 language EN | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to rece

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Pay using wallet Wallet Balance Pay 0.00¤
- Add a coupon Add a coupon code to receive discounts
- Other payment options
- navigate_before
- navigate_before Back
- navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Back
- You can review this order before it is finalized.
- navigate_next
- navigate_next Continue
- Wallet Balance
- Pay 0.00¤
- Pay using wallet
- Add a coupon
- Add a coupon code to receive discounts
- My Payment Options
- My Payment Options Add new card Add a credit or debit card
- Add new card

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/payment/shop

## Coerente com loja de sucos?

Sim.

## Justificativa

Cartões salvos são dados pessoais.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Sem sessão, abrir diretamente /#/payment/shop.'. A descrição corresponde ao cenário 'Acessar pagamento sem login' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/payment/shop Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. \| navigate_next Continue Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| EN \| language EN \| account_circ |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 3 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
