# Ficha de Cenário

**ID do cenário:** CEN-CHK-14
**Domínio:** CHK
**Nome do cenário:** Acessar merchandise pelas outras opções
**Ator:** Cliente
**Fluxo:** Abrir a opção de merchandise disponibilizada.

## Pré-condição (estado inicial)

Cliente autenticado; etapa de pagamento acessível; seção 'Other payment options' disponível.

## Descrição do cenário

Cliente executa o fluxo 'Abrir a opção de merchandise disponibilizada.'. A descrição corresponde ao cenário 'Acessar merchandise pelas outras opções' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card | 0.00 | Wallet Balance 0.00 | Pay using wallet Wallet Balance 0.00 Pay NaN¤ | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | Pay NaN¤ | Pay using wallet Wallet Balance Pay NaN¤ | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | Add a coupon Add a coupon code to receive discounts
2. Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options Donations (Thank you for supporting OWASP Juice Shop!) Credit Card Merchandise (Official stores for OWASP Juice Shop apparel, mugs and stickers!) Spreadshirt (US) Spreadshirt (DE) StickerYou Leanpub OpenSea navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Other payment options | My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balanc

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay 0.00¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Pay NaN¤
- Pay using wallet Wallet Balance Pay NaN¤
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Add a coupon Add a coupon code to receive discounts
- My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Other payment options
- Add new card Add a credit or debit card
- My Payment Options Add new card Add a credit or debit card
- 0.00
- Wallet Balance 0.00
- Pay using wallet Wallet Balance 0.00 Pay NaN¤
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue

## Dados manipulados

Dados declarados no cenário: Nenhum pagamento real.
Passo 1: /#/payment/shop

## Coerente com loja de sucos?

Sim.

## Justificativa

A opção integra as alternativas apresentadas pela aplicação.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir a opção de merchandise disponibilizada.'. A descrição corresponde ao cenário 'Acessar merchandise pelas outras opções' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card \| 0.00 \| Wallet Balance 0.00 \| Pay using wallet Wallet Balance 0.00 Pay NaN¤ \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Acc |
| 2 | Clicar em "Other payment options" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options Donations (Thank you for supporting OWASP Juice Shop!) Credit Card Merchandise (Official stores for OWASP Juice Shop apparel, mugs and stickers!) Spreadshirt (US) Spreadshirt (DE) StickerYou Leanpub OpenSea navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Other payment options \| My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Conti |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options Donations (Thank you for supporting OWASP Juice Shop!) Credit Card Merchandise (Official stores for OWASP Juice Shop apparel, mugs and stickers!) Spreadshirt (US) Spreadshirt (DE) StickerYou Leanpub OpenSea navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 4 | Clicar em "Spreadshirt (US)" |  | URL: http://127.0.0.1:3000/#/payment/shop → http://shop.spreadshirt.com/juiceshop Texto visível: spreadshop Service unavailable in your region We do not serve your country for e-commerce purposes. \| If you are a partner operating from this country, please connect via a VPN in the EU or US. Texto observado durante a ação: spreadshop Service unavailable in your region We do not serve your country for e-commerce purposes. If you are a partner operating from this country, please connect via a VPN in the EU or US. |
| 5 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: spreadshop Service unavailable in your region We do not serve your country for e-commerce purposes. If you are a partner operating from this country, please connect via a VPN in the EU or US. |
