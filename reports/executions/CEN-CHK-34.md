# Ficha de Cenário

**ID do cenário:** CEN-CHK-34
**Domínio:** CHK
**Nome do cenário:** Cartão com número incompleto
**Ator:** Cliente autenticado
**Fluxo:** Cadastrar cartão com 12 dígitos.

## Pré-condição (estado inicial)

Cliente autenticado; método de entrega selecionado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Cadastrar cartão com 12 dígitos.'. A descrição corresponde ao cenário 'Cartão com número incompleto' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Add new card Add a credit or debit card | My Payment Options Add new card Add a credit or debit card | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue Mensagem transitória: Add new card Add a credit or debit card | My Payment Options Add new card Add a credit or debit card | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 12/16 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 

## Mensagens exibidas ao usuário

- Add a coupon Add a coupon code to receive discounts
- My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Other payment options
- Add new card Add a credit or debit card
- My Payment Options Add new card Add a credit or debit card
- Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Name
- Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099
- Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- Card Number 0/16
- Card Number
- 12/16
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Card Number 12/16
- Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099
- Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12

## Dados manipulados

Dados declarados no cenário: Número '400000000000'.
Passo 1: /#/payment/shop
Passo 4: Cliente Teste
Passo 5: 400000000000
Passo 6: 12
Passo 7: 2090

## Coerente com loja de sucos?

Sim.

## Justificativa

Cartão inválido não pode ser salvo.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Cadastrar cartão com 12 dígitos.'. A descrição corresponde ao cenário 'Cartão com número incompleto' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | Nenhuma mudança visual relevante detectada. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Other payment options \| Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card Mensagem transitória: Add a coupon Add a co |
| 2 | Clicar em "Add new card" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤  |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 4 | Preencher "Name" | Cliente Teste | Nenhuma mudança visual relevante detectada. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Name \| Name |
| 5 | Preencher "Card Number" | 400000000000 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 12/16 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Card Number 12/16 \| Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 \| Name Card Number 12/16 Expiry Month 1 2 3 4  |
| 6 | Selecionar "Expiry Month" | 12 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 \| Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 \| Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a  |
| 7 | Selecionar "Expiry Year" | 2090 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 \| Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 \| Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send  |
| 8 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 9 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 12/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
