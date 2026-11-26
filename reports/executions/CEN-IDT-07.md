# Ficha de Cenário

**ID do cenário:** CEN-IDT-07
**Domínio:** IDT
**Nome do cenário:** Alteração de dados do perfil
**Ator:** Cliente
**Fluxo:** Alterar um dado editável do perfil e salvar.

## Pré-condição (estado inicial)

Conta de teste disponível para autenticação.

## Descrição do cenário

Cliente executa o fluxo 'Alterar um dado editável do perfil e salvar.'. A descrição corresponde ao cenário 'Alteração de dados do perfil' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.) X | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.) X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.) X | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.) X

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.) X
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.) X

## Dados manipulados

Dados declarados no cenário: Dado de teste atualizado.
Passo 1: /#/privacy-security

## Coerente com loja de sucos?

Sim.

## Justificativa

O cliente precisa poder atualizar dados permitidos da conta.

## Descrição funcional do cenário

Cliente executa o fluxo 'Alterar um dado editável do perfil e salvar.'. A descrição corresponde ao cenário 'Alteração de dados do perfil' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/privacy-security | /#/privacy-security | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.) X \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.) X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is nei |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.) X |
