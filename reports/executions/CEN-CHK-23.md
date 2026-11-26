# Ficha de Cenário

**ID do cenário:** CEN-CHK-23
**Domínio:** CHK
**Nome do cenário:** Checkout sem endereço
**Ator:** Cliente
**Fluxo:** Iniciar checkout sem possuir endereço selecionado.

## Pré-condição (estado inicial)

Carrinho com produto; nenhum endereço selecionado.

## Descrição do cenário

Cliente executa o fluxo 'Iniciar checkout sem possuir endereço selecionado.'. A descrição corresponde ao cenário 'Checkout sem endereço' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/delivery-method → http://127.0.0.1:3000/#/address/select Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue Texto transitório capturado: Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue | Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil | Cliente Teste | Rua Teste, 100, Fortaleza, CE, 60000000 | Brazil Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue | Select an address addAdd New Address navigate_nextContinue | Select an address | addAdd New Address

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue
- Select an address addAdd New Address navigate_nextContinue
- Select an address
- addAdd New Address
- navigate_nextContinue
- add
- Add New Address
- navigate_next
- Continue
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue
- Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue
- Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil
- Cliente Teste
- Rua Teste, 100, Fortaleza, CE, 60000000
- Brazil

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/address/select

## Coerente com loja de sucos?

Sim.

## Justificativa

A aplicação deve impedir o avanço sem destino de entrega válido.

## Descrição funcional do cenário

Cliente executa o fluxo 'Iniciar checkout sem possuir endereço selecionado.'. A descrição corresponde ao cenário 'Checkout sem endereço' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/select | /#/address/select | URL: http://127.0.0.1:3000/#/delivery-method → http://127.0.0.1:3000/#/address/select Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue Texto transitório capturado: Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue \| Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil \| Cliente Teste \| Rua Teste, 100, Fortaleza, CE, 60000000 \| Brazil Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address addAdd New Address navigate_nextContinue \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me wa |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 1 language EN Select an address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil addAdd New Address navigate_nextContinue |
