# Ficha de Cenário

**ID do cenário:** CEN-CHK-12
**Domínio:** CHK
**Nome do cenário:** Visualizar outras opções de pagamento
**Ator:** Cliente
**Fluxo:** Expandir a seção de outras opções de pagamento.

## Pré-condição (estado inicial)

Cliente autenticado; etapa de pagamento acessível; seção 'Other payment options' disponível.

## Descrição do cenário

Cliente executa o fluxo 'Expandir a seção de outras opções de pagamento.'. A descrição corresponde ao cenário 'Visualizar outras opções de pagamento' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | Other payment options | Add new card Add a credit or debit card | My Payment Options Add new card Add a credit or debit card Mensagem transitória: Pay NaN¤ | Pay using wallet Wallet Balance Pay NaN¤ | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | 0.00 | Wallet Balance 0.00
2. Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options Donations (Thank you for supporting OWASP Juice Shop!) Credit Card Merchandise (Official stores for OWASP Juice Shop apparel, mugs and stickers!) Spreadshirt (US) Spreadshirt (DE) StickerYou Leanpub OpenSea navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Other payment options | My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Acc

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

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/payment/shop

## Coerente com loja de sucos?

Sim.

## Justificativa

A loja oferece alternativas além do cartão no fluxo apresentado.

## Descrição funcional do cenário

Cliente executa o fluxo 'Expandir a seção de outras opções de pagamento.'. A descrição corresponde ao cenário 'Visualizar outras opções de pagamento' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Other payment options \| Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card Mensagem transitória: Pay NaN¤ \| Pa |
| 2 | Clicar em "Other payment options" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options Donations (Thank you for supporting OWASP Juice Shop!) Credit Card Merchandise (Official stores for OWASP Juice Shop apparel, mugs and stickers!) Spreadshirt (US) Spreadshirt (DE) StickerYou Leanpub OpenSea navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Other payment options \| My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Conti |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options Donations (Thank you for supporting OWASP Juice Shop!) Credit Card Merchandise (Official stores for OWASP Juice Shop apparel, mugs and stickers!) Spreadshirt (US) Spreadshirt (DE) StickerYou Leanpub OpenSea navigate_before Back You can review this order before it is finalized. navigate_next Continue |
