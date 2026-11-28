# Ficha de Cenário

**ID do cenário:** CEN-CHK-32
**Domínio:** CHK
**Nome do cenário:** Endereço com celular em formato inválido
**Ator:** Cliente autenticado
**Fluxo:** Preencher endereço com celular de 3 dígitos.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Preencher endereço com celular de 3 dígitos.'. A descrição corresponde ao cenário 'Endereço com celular em formato inválido' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. | 160 characters 0/160 City State navigate_before Back send Submit Texto transitório capturado: Address | 0/8 | Max. 160 characters 0/160 | Max. 160 characters | Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Registration completed successfully. You can now log in. X | Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address | navigate_before
2. Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. | ZIP Code 8/8 Address Max. Texto transitório capturado: 8/8 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | ZIP Code 8/8 | Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Mobile Number Mobile number must match 1000000-9999999999 format. | Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. 

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Registration completed successfully. You can now log in. X
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

Dados declarados no cenário: Mobile Number '123'.
Passo 1: /#/address/create
Passo 3: Brazil
Passo 4: Cliente Alternativo
Passo 5: 123
Passo 6: 60000000
Passo 7: Rua Alternativa, 200
Passo 8: Fortaleza
Passo 9: CE

## Coerente com loja de sucos?

Sim.

## Justificativa

Telefone de contato é usado na entrega.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Preencher endereço com celular de 3 dígitos.'. A descrição corresponde ao cenário 'Endereço com celular em formato inválido' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create | /#/address/create | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. \| 160 characters 0/160 City State navigate_before Back send Submit Texto transitório capturado: Address \| 0/8 \| Max. 160 characters 0/160 \| Max. 160 characters \| Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Num |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit |
| 3 | Preencher "Country" | Brazil | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search |
| 4 | Preencher "Name" | Cliente Alternativo | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Name Mensagem transitória: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Sho |
| 5 | Preencher "Mobile Number" | 123 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Name \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Mobile Number Mensagem transitória: Name \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice  |
| 6 | Preencher "ZIP Code" | 60000000 | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. \| ZIP Code 8/8 Address Max. Texto transitório capturado: 8/8 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| ZIP Code 8/8 \| Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 0 |
| 7 | Preencher "Address" | Rua Alternativa, 200 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Max. 160 characters 20/160 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Address Max. 160 characters 20/160 \| Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit Mensagem transitória: ZIP Code 8/8 \| Country Name Mobile Number Mobile number must match 100000 |
| 8 | Preencher "City" | Fortaleza | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Address \| City Mensagem transitória: Address Max. 160 characters 20/160 \| Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8  |
| 9 | Preencher "State" | CE | Nenhuma mudança visual relevante detectada. Texto transitório capturado: City \| Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| State Mensagem transitória: City \| Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/1 |
| 10 | Pressionar Tab |  | Nenhuma mudança visual relevante detectada. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Mobile Number Mobile number must match 1000000-9999999999 format. \| Mobile Number \| ZIP Code 8/8 \| ZIP Code Mensagem transitória: State \| Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop sear |
| 11 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit |
| 12 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number Mobile number must match 1000000-9999999999 format. ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit |
