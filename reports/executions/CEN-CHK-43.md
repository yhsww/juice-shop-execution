# Ficha de Cenário

**ID do cenário:** CEN-CHK-43
**Domínio:** CHK
**Nome do cenário:** Opções de pagamento em criptomoeda
**Ator:** Cliente autenticado
**Fluxo:** Expandir 'Other payment options' e registrar as opções exibidas (cripto, doação, merchandising).

## Pré-condição (estado inicial)

Cliente autenticado; etapa de pagamento acessível; seção 'Other payment options' disponível.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Expandir 'Other payment options' e registrar as opções exibidas (cripto, doação, merchandising).'. A descrição corresponde ao cenário 'Opções de pagamento em criptomoeda' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options Donations (Thank you for supporting OWASP Juice Shop!) Credit Card Merchandise (Official stores for OWASP Juice Shop apparel, mugs and stickers!) Spreadshirt (US) Spreadshirt (DE) StickerYou Leanpub OpenSea navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Other payment options | My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue Mensagem transitória: Other payment options | My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continu

## Mensagens exibidas ao usuário

- Other payment options
- My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Add new card Add a credit or debit card
- My Payment Options Add new card Add a credit or debit card
- Add a coupon Add a coupon code to receive discounts

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/payment/shop

## Coerente com loja de sucos?

Não.

## Justificativa

Doações e loja de camisetas não fazem parte da compra de sucos; registrar sem clicar.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Expandir 'Other payment options' e registrar as opções exibidas (cripto, doação, merchandising).'. A descrição corresponde ao cenário 'Opções de pagamento em criptomoeda' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | Nenhuma mudança visual relevante detectada. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card \| Add a coupon Add a coupon code to receive discounts Mensagem tran |
| 2 | Clicar em "Other payment options" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options Donations (Thank you for supporting OWASP Juice Shop!) Credit Card Merchandise (Official stores for OWASP Juice Shop apparel, mugs and stickers!) Spreadshirt (US) Spreadshirt (DE) StickerYou Leanpub OpenSea navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Other payment options \| My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Conti |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options Donations (Thank you for supporting OWASP Juice Shop!) Credit Card Merchandise (Official stores for OWASP Juice Shop apparel, mugs and stickers!) Spreadshirt (US) Spreadshirt (DE) StickerYou Leanpub OpenSea navigate_before Back You can review this order before it is finalized. navigate_next Continue |
