# Ficha de Cenário

**ID do cenário:** CEN-ADM-04
**Domínio:** ADM
**Nome do cenário:** Cliente comum tenta abrir a administração
**Ator:** Cliente autenticado
**Fluxo:** Entrar como cliente comum e abrir /#/administration.

## Pré-condição (estado inicial)

Cliente autenticado sem perfil administrador.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Entrar como cliente comum e abrir /#/administration.'. A descrição corresponde ao cenário 'Cliente comum tenta abrir a administração' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Registration completed successfully. You can now log in. X | 403 You are not allowed to access this page! | You are not allowed to access this page! | 403 | Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Registration completed successfully. You can now log in. X | 403 You are not allowed to access this page! | You are not allowed to access this page! | 403

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page!
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Registration completed successfully. You can now log in. X
- 403 You are not allowed to access this page!
- You are not allowed to access this page!
- 403
- Registration completed successfully. You can now log in. X

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/administration

## Coerente com loja de sucos?

Sim.

## Justificativa

Funções de gestão são restritas.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Entrar como cliente comum e abrir /#/administration.'. A descrição corresponde ao cenário 'Cliente comum tenta abrir a administração' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/administration | /#/administration | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/administration Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! Registration completed successfully. You can now log in. X \| 403 You are not allowed to access this page! \| You are not allowed to access this page! \| 403 \| Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your  |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 You are not allowed to access this page! |
