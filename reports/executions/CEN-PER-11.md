# Ficha de Cenário

**ID do cenário:** CEN-PER-11
**Domínio:** PER
**Nome do cenário:** Remover cartão salvo
**Ator:** Cliente autenticado
**Fluxo:** Em 'My Payment Options', remover o cartão terminado em 0002.

## Pré-condição (estado inicial)

Cliente autenticado; o próprio cenário cadastra o cartão 0002 antes de remover.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Em 'My Payment Options', remover o cartão terminado em 0002.'. A descrição corresponde ao cenário 'Remover cartão salvo' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/saved-payment-methods Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Texto transitório capturado: My Payment Options | Add new card | Add new card Add a credit or debit card | Add a credit or debit card | Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Registration completed successfully. You can now log in. X | My Payment Options Add new card Add a credit or debit card | My Payment Options | Add new card
2. Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Texto transitório capturado: Add new card Add a credit or debit card | My Payment Options Add new card Add a credit or debit card | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Mensagem transitória: Add new card Add a credit or debit card | My Payment Options Add new card Add a credit or debit card | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card
3. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 16/16 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit | Card Number 16/16 | Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Registration completed successfully. You can now log in. X
- My Payment Options Add new card Add a credit or debit card
- My Payment Options
- Add new card
- Add new card Add a credit or debit card
- Add a credit or debit card
- Registration completed successfully. You can now log in. X
- Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- Name
- Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099
- Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- Card Number 0/16
- Card Number
- 16/16
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- Card Number 16/16
- Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/saved-payment-methods
Passo 5: Cliente Teste
Passo 6: 4000000000000002
Passo 7: 12
Passo 8: 2090

## Coerente com loja de sucos?

Sim.

## Justificativa

Cliente deve poder apagar meios de pagamento.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Em 'My Payment Options', remover o cartão terminado em 0002.'. A descrição corresponde ao cenário 'Remover cartão salvo' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/saved-payment-methods | /#/saved-payment-methods | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/saved-payment-methods Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Texto transitório capturado: My Payment Options \| Add new card \| Add new card Add a credit or debit card \| Add a credit or debit card \| Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Registration completed successfully. You can now log in. X \| My Payment Options Add  |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card |
| 3 | Clicar em "Add new card" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Texto transitório capturado: Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Mensagem transitória: Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Pa |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit |
| 5 | Preencher "Name" | Cliente Teste | Nenhuma mudança visual relevante detectada. Texto transitório capturado: My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| Name \| Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 \| Name Card Number 0/16 Expiry Month 1 2 3  |
| 6 | Preencher "Card Number" | 4000000000000002 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 16/16 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| Card Number 16/16 \| Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 \| Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Mensagem transitória: Name \| Name Card Number 0/16 Expiry Month 1 2 3  |
| 7 | Selecionar "Expiry Month" | 12 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 \| Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 \| Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| 1 2 3 4 5 6 7 8 9 10 11 12 Mensagem transitória: Expiry Month  |
| 8 | Selecionar "Expiry Year" | 2090 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 \| send Submit \| Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089  |
| 9 | Clicar em "Submit" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Your card ending with 0002 has been saved for your convenience. \| X Texto transitório capturado: My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit \| ************0002 Cliente Teste 12/2090 \| ************0002 \| Cliente Teste \| 12/2090 Mensagem transitória: se |
| 10 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Your card ending with 0002 has been saved for your convenience. X |
| 11 | Clicar no elemento |  | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options ************0002 Cliente Teste 12/2090 Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Your card ending with 0002 has been saved for your convenience. X \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit Your card en |
| 12 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit |
