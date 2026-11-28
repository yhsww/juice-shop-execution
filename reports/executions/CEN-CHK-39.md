# Ficha de Cenário

**ID do cenário:** CEN-CHK-39
**Domínio:** CHK
**Nome do cenário:** Pagar com carteira digital sem saldo
**Ator:** Cliente autenticado
**Fluxo:** Na etapa de pagamento, escolher a carteira (Wallet) com saldo 0 e tentar avançar.

## Pré-condição (estado inicial)

Cliente autenticado (conta nova, saldo 0); método de entrega selecionado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Na etapa de pagamento, escolher a carteira (Wallet) com saldo 0 e tentar avançar.'. A descrição corresponde ao cenário 'Pagar com carteira digital sem saldo' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

A execução foi concluída na URL observada: http://127.0.0.1:3000/#/payment/shop.

## Mensagens exibidas ao usuário

- Add a coupon Add a coupon code to receive discounts
- My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Other payment options
- Add new card Add a credit or debit card
- My Payment Options Add new card Add a credit or debit card

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/payment/shop

## Coerente com loja de sucos?

Sim.

## Justificativa

Não se paga com saldo inexistente.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Na etapa de pagamento, escolher a carteira (Wallet) com saldo 0 e tentar avançar.'. A descrição corresponde ao cenário 'Pagar com carteira digital sem saldo' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | Nenhuma mudança visual relevante detectada. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Other payment options \| Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card Mensagem transitória: Add a coupon Add a co |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
