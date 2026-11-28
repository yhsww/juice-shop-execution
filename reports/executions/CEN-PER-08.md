# Ficha de Cenário

**ID do cenário:** CEN-PER-08
**Domínio:** PER
**Nome do cenário:** Adicionar endereço pela área de perfil
**Ator:** Cliente autenticado
**Fluxo:** Em 'My saved addresses', adicionar um endereço e ver a lista atualizada.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Em 'My saved addresses', adicionar um endereço e ver a lista atualizada.'. A descrição corresponde ao cenário 'Adicionar endereço pela área de perfil' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. | 160 characters 0/160 City State navigate_before Back send Submit Texto transitório capturado: ZIP Code | Address | 0/8 | Max. 160 characters 0/160 | Max. 160 characters Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address | navigate_before | navigate_before Back
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 8/8 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | ZIP Code 8/8 | Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Mobile Number | Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit | ZIP Code 0/8
3. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Max. 160 characters 20/160 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit | Address Max. 160 characters 20/160 | Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigat

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

Dados declarados no cenário: Endereço 'Rua Alternativa, 200'.
Passo 1: /#/address/create
Passo 3: Brazil
Passo 4: Cliente Alternativo
Passo 5: 8599999999
Passo 6: 60000000
Passo 7: Rua Alternativa, 200
Passo 8: Fortaleza
Passo 9: CE
Passo 12: /#/address/saved

## Coerente com loja de sucos?

Sim.

## Justificativa

Gerenciar endereços fora do checkout é previsto no guia (PER).

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Em 'My saved addresses', adicionar um endereço e ver a lista atualizada.'. A descrição corresponde ao cenário 'Adicionar endereço pela área de perfil' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/create | /#/address/create | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. \| 160 characters 0/160 City State navigate_before Back send Submit Texto transitório capturado: ZIP Code \| Address \| 0/8 \| Max. 160 characters 0/160 \| Max. 160 characters Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address \| navigate_before \| navigate_before Bac |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit |
| 3 | Preencher "Country" | Brazil | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search |
| 4 | Preencher "Name" | Cliente Alternativo | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Name Mensagem transitória: Country \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Sho |
| 5 | Preencher "Mobile Number" | 8599999999 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Name \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Mobile Number Mensagem transitória: Name \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| menu OWASP Juice  |
| 6 | Preencher "ZIP Code" | 60000000 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 8/8 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| ZIP Code 8/8 \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit Mensagem transitória: Mobile Number \| Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| men |
| 7 | Preencher "Address" | Rua Alternativa, 200 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Max. 160 characters 20/160 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Address Max. 160 characters 20/160 \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit Mensagem transitória: ZIP Code 8/8 \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 0/160 Cit |
| 8 | Preencher "City" | Fortaleza | Nenhuma mudança visual relevante detectada. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Address \| City \| send Submit \| navigate_before Back send Submit Mensagem transitória: Address Max. 160 characters 20/160 \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 C |
| 9 | Preencher "State" | CE | Nenhuma mudança visual relevante detectada. Texto transitório capturado: City \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| State Mensagem transitória: City \| Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 8/8 Address Max. 160 characters 20/160 City State navigate_before Back send Submit \| menu OWASP Juice Sho |
| 10 | Clicar em "Submit" |  | URL: http://127.0.0.1:3000/#/address/create → http://127.0.0.1:3000/#/search Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping Texto transitório capturado: 1 – 16 of 46 \| 16 \| menu OWASP Juice Shop search search close account_circle |
| 11 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart A |
| 12 | Abrir a rota /#/address/saved | /#/address/saved | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/saved Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses Cliente Alternativo Rua Alternativa, 200, Fortaleza, CE, 60000000 Brazil addAdd New Address Texto transitório capturado: Cliente Alternativo Rua Alternativa, 200, Fortaleza, CE, 60000000 Brazil \| Cliente Alternativo \| Rua Alternativa, 200, Fortaleza, CE, 60000000 \| Brazil \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses Cliente Alternativo Rua Alternativa, 200, Fortaleza, CE, 60000000 Brazil addAdd New Address Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address \| menu OWASP Juice Shop  |
| 13 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses Cliente Alternativo Rua Alternativa, 200, Fortaleza, CE, 60000000 Brazil addAdd New Address |
