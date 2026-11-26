# Ficha de Cenário

**ID do cenário:** CEN-PER-04
**Domínio:** PER
**Nome do cenário:** Acesso à privacidade e segurança
**Ator:** Cliente autenticado
**Fluxo:** Abrir a área de privacidade e segurança da conta.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir a área de privacidade e segurança da conta.'. A descrição corresponde ao cenário 'Acesso à privacidade e segurança' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/privacy-security

## Coerente com loja de sucos?

Sim.

## Justificativa

A conta possui funções de privacidade e segurança acessíveis ao usuário autenticado.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir a área de privacidade e segurança da conta.'. A descrição corresponde ao cenário 'Acesso à privacidade e segurança' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/privacy-security | /#/privacy-security | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN |
