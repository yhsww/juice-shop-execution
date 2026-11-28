# Ficha de Cenário

**ID do cenário:** CEN-PER-13
**Domínio:** PER
**Nome do cenário:** Endereços salvos sem login
**Ator:** Visitante não autenticado
**Fluxo:** Sem sessão, abrir /#/address/saved.

## Pré-condição (estado inicial)

Sem sessão ativa.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Sem sessão, abrir /#/address/saved.'. A descrição corresponde ao cenário 'Endereços salvos sem login' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/address/saved Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page. | EN | language EN | account_circle Account shopping_cart Your Basket 0 language EN | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 Please login to view this page. | 403 Please login to view this page. | Please login to view this page. | 403 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page.

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 Please login to view this page.
- 403 Please login to view this page.
- Please login to view this page.
- 403
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page.
- EN
- language EN
- account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/address/saved

## Coerente com loja de sucos?

Sim.

## Justificativa

Endereços são dados pessoais.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Sem sessão, abrir /#/address/saved.'. A descrição corresponde ao cenário 'Endereços salvos sem login' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/address/saved | /#/address/saved | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/address/saved Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page. \| EN \| language EN \| account_circle Account shopping_cart Your Basket 0 language EN \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 Please login to view this page. \| 403 Please login to view this page. \| Please login to view this page. \| 403 \| menu OWASP Juice Shop search search close account_cir |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page. |
