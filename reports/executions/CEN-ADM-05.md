# Ficha de Cenário

**ID do cenário:** CEN-ADM-05
**Domínio:** ADM
**Nome do cenário:** Visitante tenta abrir a administração
**Ator:** Visitante não autenticado
**Fluxo:** Sem sessão, abrir /#/administration.

## Pré-condição (estado inicial)

Sem sessão ativa.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Sem sessão, abrir /#/administration.'. A descrição corresponde ao cenário 'Visitante tenta abrir a administração' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! | EN | language EN | account_circle Account shopping_cart Your Basket 0 language EN | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 You are not allowed to access this page! | 403 You are not allowed to access this page! | You are not allowed to access this page! | 403 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page!

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 You are not allowed to access this page!
- 403 You are not allowed to access this page!
- You are not allowed to access this page!
- 403
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page!
- EN
- language EN
- account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/administration

## Coerente com loja de sucos?

Sim.

## Justificativa

Funções de gestão são restritas.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Sem sessão, abrir /#/administration.'. A descrição corresponde ao cenário 'Visitante tenta abrir a administração' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration | /#/administration | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! \| EN \| language EN \| account_circle Account shopping_cart Your Basket 0 language EN \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 You are not allowed to access this page! \| 403 You are not allowed to access this page! \| You are not allowed to access this page! \| 403 \| menu OW |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! |
