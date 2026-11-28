# Ficha de Cenário

**ID do cenário:** CEN-CHK-35
**Domínio:** CHK
**Nome do cenário:** Cartão sem validade
**Ator:** Cliente autenticado
**Fluxo:** Cadastrar cartão sem escolher mês e ano.

## Pré-condição (estado inicial)

Cliente autenticado; método de entrega selecionado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Cadastrar cartão sem escolher mês e ano.'. A descrição corresponde ao cenário 'Cartão sem validade' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Add new card Add a credit or debit card | My Payment Options Add new card Add a credit or debit card | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue Mensagem transitória: Add new card Add a credit or debit card | My Payment Options Add new card Add a credit or debit card | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue | My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 16/16 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 

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
- 16/16
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue
- Card Number 16/16
- Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099
- Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit

## Dados manipulados

Dados declarados no cenário: Nome e número válidos.
Passo 1: /#/payment/shop
Passo 4: Cliente Teste
Passo 5: 4000000000000002

## Coerente com loja de sucos?

Sim.

## Justificativa

Validade é obrigatória para pagamento.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Cadastrar cartão sem escolher mês e ano.'. A descrição corresponde ao cenário 'Cartão sem validade' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/payment/shop | /#/payment/shop | Nenhuma mudança visual relevante detectada. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Other payment options \| Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card Mensagem transitória: Add a coupon Add a co |
| 2 | Clicar em "Add new card" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. Texto transitório capturado: Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Pay using wallet Wallet Balance 0.00 Pay NaN¤  |
| 3 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 4 | Preencher "Name" | Cliente Teste | Nenhuma mudança visual relevante detectada. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Name \| Name |
| 5 | Preencher "Card Number" | 4000000000000002 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 16/16 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue \| Card Number 16/16 \| Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 \| Name Card Number 16/16 Expiry Month 1 2 3 4  |
| 6 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
| 7 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Pay using wallet Wallet Balance 0.00 Pay NaN¤ Add a coupon Add a coupon code to receive discounts Other payment options navigate_before Back You can review this order before it is finalized. navigate_next Continue |
