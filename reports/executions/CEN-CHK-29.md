# Ficha de Cenário

**ID do cenário:** CEN-CHK-29
**Domínio:** CHK
**Nome do cenário:** Endereço sem cidade
**Ator:** Cliente autenticado
**Fluxo:** Preencher o formulário de novo endereço sem o campo City e tentar enviar.

## Pré-condição (estado inicial)

Cliente autenticado; formulário de novo endereço aberto (sem carrinho exigido).

## Descrição do cenário

Cliente autenticado executa o fluxo 'Preencher o formulário de novo endereço sem o campo City e tentar enviar.'. A descrição corresponde ao cenário 'Endereço sem cidade' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. | 160 characters 0/160 City State navigate_before Back send Submit Placed Apple Juice (1000ml) into basket. Texto transitório capturado: ZIP Code | Address | 0/8 | Max. 160 characters 0/160 | Max. 160 characters Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address | navigate_before
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Placed Apple Juice (1000ml) into basket. X | Country | Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Placed Apple Juice (1000ml) into basket. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Placed Apple Juice (1000ml) into basket. X | Country | Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before B

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Placed Apple Juice (1000ml) into basket. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit
- Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit
- Add New Address
- navigate_before
- navigate_before Back
- navigate_before Back send Submit
- Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit
- Back
- send
- send Submit
- Submit
- Country
- Name
- Mobile Number
- ZIP Code 0/8
- Address Max. 160 characters 0/160
- City
- State
- ZIP Code

## Dados manipulados

Dados declarados no cenário: Endereço completo exceto City.
Passo 1: /#/address/create
Passo 3: Brazil
Passo 4: Cliente Alternativo
Passo 5: 8599999999
Passo 6: 60000000
Passo 7: Rua Alternativa, 200
Passo 8: CE

## Coerente com loja de sucos?

Sim.

## Justificativa

Entrega exige endereço completo.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Preencher o formulário de novo endereço sem o campo City e tentar enviar.'. A descrição corresponde ao cenário 'Endereço sem cidade' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create | /#/address/create | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. \| 160 characters 0/160 City State navigate_before Back send Submit Placed Apple Juice (1000ml) into basket. Texto transitório capturado: ZIP Code \| Address \| 0/8 \| Max. 160 characters 0/160 \| Max. 160 characters Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Placed Apple Juice (1000ml) into basket. X \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Add |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Placed Apple Juice (1000ml) into basket. X |
| 3 | Preencher "Country" | Brazil | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Placed Apple Juice (1000ml) into basket. X \| Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Place |
| 4 | Preencher "Name" | Cliente Alternativo | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Name Mensagem transitória: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Sho |
| 5 | Preencher "Mobile Number" | 8599999999 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Name \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Mobile Number Mensagem transitória: Name \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice  |
| 6 | Preencher "ZIP Code" | 60000000 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 8/8 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| ZIP Code 8/8 \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Mobile Number \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| men |
| 7 | Preencher "Address" | Rua Alternativa, 200 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Max. 160 characters 20/160 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Address Max. 160 characters 20/160 \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit Mensagem transitória: ZIP Code 8/8 \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 Cit |
| 8 | Preencher "State" | CE | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Address \| State Mensagem transitória: Address Max. 160 characters 20/160 \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back se |
| 9 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit |
| 10 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit |
