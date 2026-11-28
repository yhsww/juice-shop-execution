# Ficha de Cenário

**ID do cenário:** CEN-IDT-11
**Domínio:** IDT
**Nome do cenário:** Exportação de dados pessoais
**Ator:** Cliente
**Fluxo:** Abrir a área de privacidade e solicitar exportação de dados.

## Pré-condição (estado inicial)

Conta de teste disponível para autenticação.

## Descrição do cenário

Cliente executa o fluxo 'Abrir a área de privacidade e solicitar exportação de dados.'. A descrição corresponde ao cenário 'Exportação de dados pessoais' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/data-export Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.) Texto transitório capturado: PDF | Excel | Request Data Export | Export Format : | (Your data export will open in a new Browser window.) Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.) | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.) | Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.) | Request | Export Format : JSON PDF Excel

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.)
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.)
- Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.)
- Request
- Export Format : JSON PDF Excel
- JSON
- PDF
- Excel
- Request Data Export
- Export Format :
- (Your data export will open in a new Browser window.)

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/privacy-security/data-export

## Coerente com loja de sucos?

Sim.

## Justificativa

O cliente deve conseguir consultar seus dados pessoais exportáveis.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir a área de privacidade e solicitar exportação de dados.'. A descrição corresponde ao cenário 'Exportação de dados pessoais' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/privacy-security/data-export | /#/privacy-security/data-export | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/data-export Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.) Texto transitório capturado: PDF \| Excel \| Request Data Export \| Export Format : \| (Your data export will open in a new Browser window.) Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.) \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Request Data Export Export Format : JSON PDF Excel Request (Your data export will open in a new Browser window.) |
