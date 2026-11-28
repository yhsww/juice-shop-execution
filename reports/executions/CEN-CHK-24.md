# Ficha de Cenário

**ID do cenário:** CEN-CHK-24
**Domínio:** CHK
**Nome do cenário:** Checkout sem método de entrega
**Ator:** Cliente
**Fluxo:** Acessar a etapa de entrega sem selecionar método.

## Pré-condição (estado inicial)

Endereço selecionado.

## Descrição do cenário

Cliente executa o fluxo 'Acessar a etapa de entrega sem selecionar método.'. A descrição corresponde ao cenário 'Checkout sem método de entrega' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue Texto transitório capturado: 3 Days | Standard Delivery 0.00¤ 5 Days | Standard Delivery | 0.00¤ | 5 Days Mensagem transitória: Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue | Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 | Cliente Teste

## Mensagens exibidas ao usuário

- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999
- Cliente Teste
- Rua Teste, 100, Fortaleza, CE, 60000000
- Brazil
- Phone Number 8599999999
- Delivery Address
- Phone Number
- Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days
- Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days
- Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue
- One Day Delivery 0.99¤ 1 Days
- One Day Delivery
- 0.99¤
- 1 Days
- Fast Delivery 0.50¤ 3 Days
- Fast Delivery

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/delivery-method

## Coerente com loja de sucos?

Sim.

## Justificativa

A aplicação deve exigir um método de entrega válido.

## Descrição funcional do cenário

Cliente executa o fluxo 'Acessar a etapa de entrega sem selecionar método.'. A descrição corresponde ao cenário 'Checkout sem método de entrega' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/delivery-method | /#/delivery-method | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue Texto transitório capturado: 3 Days \| Standard Delivery 0.00¤ 5 Days \| Standard Delivery \| 0.00¤ \| 5 Days Mensagem transitória: Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery navigate_before Back navigate_nextContinue \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 6000 |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Delivery Address Cliente Teste Rua Teste, 100, Fortaleza, CE, 60000000 Brazil Phone Number 8599999999 Choose a delivery speed Price Expected Delivery One Day Delivery 0.99¤ 1 Days Fast Delivery 0.50¤ 3 Days Standard Delivery 0.00¤ 5 Days navigate_before Back navigate_nextContinue |
