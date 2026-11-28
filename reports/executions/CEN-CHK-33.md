# Ficha de Cenário

**ID do cenário:** CEN-CHK-33
**Domínio:** CHK
**Nome do cenário:** Endereço com CEP acima do tamanho
**Ator:** Cliente autenticado
**Fluxo:** Preencher ZIP Code com 12 dígitos.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Preencher ZIP Code com 12 dígitos.'. A descrição corresponde ao cenário 'Endereço com CEP acima do tamanho' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. | 160 characters 0/160 City State navigate_before Back send Submit Texto transitório capturado: ZIP Code | Address | 0/8 | Max. 160 characters 0/160 | Max. 160 characters Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address | navigate_before | navigate_before Back
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 12/8 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | ZIP Code 12/8 | Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Mobile Number | Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | ZIP Code 0/8
3. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Max. 160 characters 20/160 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit | Address Max. 160 characters 20/160 | Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State 

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit
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
- Address

## Dados manipulados

Dados declarados no cenário: ZIP '123456789012'.
Passo 1: /#/address/create
Passo 3: Brazil
Passo 4: Cliente Alternativo
Passo 5: 8599999999
Passo 6: 123456789012
Passo 7: Rua Alternativa, 200
Passo 8: Fortaleza
Passo 9: CE

## Coerente com loja de sucos?

Sim.

## Justificativa

CEP deve ter tamanho válido.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Preencher ZIP Code com 12 dígitos.'. A descrição corresponde ao cenário 'Endereço com CEP acima do tamanho' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create | /#/address/create | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. \| 160 characters 0/160 City State navigate_before Back send Submit Texto transitório capturado: ZIP Code \| Address \| 0/8 \| Max. 160 characters 0/160 \| Max. 160 characters Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address \| navigate_before \| navigate_before Bac |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit |
| 3 | Preencher "Country" | Brazil | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search |
| 4 | Preencher "Name" | Cliente Alternativo | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Name Mensagem transitória: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Sho |
| 5 | Preencher "Mobile Number" | 8599999999 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Name \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Mobile Number Mensagem transitória: Name \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice  |
| 6 | Preencher "ZIP Code" | 123456789012 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 12/8 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| ZIP Code 12/8 \| Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Mobile Number \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \ |
| 7 | Preencher "Address" | Rua Alternativa, 200 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Max. 160 characters 20/160 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Address Max. 160 characters 20/160 \| Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit Mensagem transitória: ZIP Code 12/8 \| Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 0/1 |
| 8 | Preencher "City" | Fortaleza | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Address \| City Mensagem transitória: Address Max. 160 characters 20/160 \| Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Bac |
| 9 | Preencher "State" | CE | Nenhuma mudança visual relevante detectada. Texto transitório capturado: City \| Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| State Mensagem transitória: City \| Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juic |
| 10 | Pressionar Tab |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| ZIP Code 12/8 \| ZIP Code \| Address Max. 160 characters 20/160 \| Address Mensagem transitória: State \| Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigat |
| 11 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit |
| 12 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 12/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit |
