# Ficha de Cenário

**ID do cenário:** CEN-CHK-15
**Domínio:** CHK
**Nome do cenário:** Aplicar cupom no checkout
**Ator:** Cliente
**Fluxo:** Informar o código TESTE12345 no campo de cupom, solicitar o resgate e verificar a rejeição do cupom inválido.

## Pré-condição (estado inicial)

Cliente autenticado; etapa de pagamento acessível; campo de cupom disponível.

## Descrição do cenário

Cliente executa o fluxo 'Informar o código TESTE12345 no campo de cupom, solicitar o resgate e verificar a rejeição do cupom inválido.'. A descrição corresponde ao cenário 'Aplicar cupom no checkout' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | Other payment options | Add new card Add a credit or debit card | My Payment Options Add new card Add a credit or debit card Mensagem transitória: Pay NaN¤ | Pay using wallet Wallet Balance Pay NaN¤ | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | 0.00 | Wallet Balance 0.00
2. Texto visível: Follow us on BlueSky or Reddit for monthly coupons and other spam! Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 10/10 redeem Redeem Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 10/10 | Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 10/10 redeem Redeem | Add a coupon Add a coupon code to receive discounts Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other sp

## Mensagens exibidas ao usuário

- Pay NaN¤
- Pay using wallet Wallet Balance Pay NaN¤
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- 0.00
- Wallet Balance 0.00
- Pay using wallet Wallet Balance 0.00 Pay NaN¤
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Add a coupon Add a coupon code to receive discounts
- My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Other payment options
- Add new card Add a credit or debit card
- My Payment Options Add new card Add a credit or debit card
- Add a coupon Add a coupon code to receive discounts Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 0/10 redeem Redeem
- My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 0/10 redeem Redeem Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 0/10 redeem Redeem Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 0/10
- Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 0/10 redeem Redeem
- Coupon
- 10/10

## Dados manipulados

Dados declarados no cenário: Cupom inválido de teste: TESTE12345.
Passo 1: /#/payment/shop
Passo 2: TESTE12345

## Coerente com loja de sucos?

Sim.

## Justificativa

Cupons fazem parte da etapa de compra quando habilitados.

## Descrição funcional do cenário

Cliente executa o fluxo 'Informar o código TESTE12345 no campo de cupom, solicitar o resgate e verificar a rejeição do cupom inválido.'. A descrição corresponde ao cenário 'Aplicar cupom no checkout' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Other payment options \| Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card Mensagem transitória: Pay NaN¤ \| Pa |
| 2 | Preencher "Coupon" | TESTE12345 | Texto visível: Follow us on BlueSky or Reddit for monthly coupons and other spam! Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 10/10 redeem Redeem Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 10/10 \| Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and  |
| 3 | Clicar em "Redeem" |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Invalid coupon. Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 0/10 redeem Redeem Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Invalid coupon. \| 0/10 \| Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 0/10 \| Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons a |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Invalid coupon. Coupon Need a coupon code? Follow us on BlueSky or Reddit for monthly coupons and other spam! 0/10 redeem Redeem Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
