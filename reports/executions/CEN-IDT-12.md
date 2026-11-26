# Ficha de Cenário

**ID do cenário:** CEN-IDT-12
**Domínio:** IDT
**Nome do cenário:** Solicitação de exclusão de dados
**Ator:** Cliente
**Fluxo:** Abrir a área de privacidade e verificar a opção de exclusão.

## Pré-condição (estado inicial)

Conta de teste disponível para autenticação.

## Descrição do cenário

Cliente executa o fluxo 'Abrir a área de privacidade e verificar a opção de exclusão.'. A descrição corresponde ao cenário 'Solicitação de exclusão de dados' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/dataerasure Texto visível: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/dataErasure.js:62:18 at /juice-shop/build/routes/dataErasure.js:98:7 at Layer.handle [as handle_request] (/juice-shop/node_modules/express/lib/router/layer.js:95:5) at next (/juice-shop/node_modules/express/lib/router/route.js:149:13) at Route.dispatch (/juice-shop/node_modules/express/lib/router/route.js:119:3) at Layer.handle [as handle_request] (/juice-shop/node_modules/express/lib/router/layer.js:95:5) at /juice-shop/node_modules/express/lib/router/index.js:284:15 at router.process_params (/juice-shop/node_modules/express/lib/router/index.js:346:12) at next (/juice-shop Texto observado durante a ação: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/dataErasure.js:62:18 at /juice-shop/build/routes/dataErasure.js:98:7 at Layer.handle [as handle_request] (/juice-shop/node_modules/express/lib/router/layer.js:95:5) at next (/juice-shop/node_modules/express/lib/router/route.js:149:13) at Route.dispatch (/juice-shop/node_modules/express/lib/router/route.js:119:3) at Layer.handle [as handle_request] (/juice-shop/node_modules/express/lib/router/layer.js:95:5) at /juice-shop/node_modules/express/lib/router/index.js:284:15 at router.process_params (/juice-shop/node_modules/express/lib/router/index.js:346:12) at next (/juice-shop/node_modules/express/lib/router/index.js:280:10) at router.handle (/juice-shop/node_m

## Mensagens exibidas ao usuário

Nenhuma mensagem transitória relevante capturada.

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /dataerasure

## Coerente com loja de sucos?

Sim.

## Justificativa

A gestão de privacidade deve permitir iniciar uma solicitação de exclusão.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir a área de privacidade e verificar a opção de exclusão.'. A descrição corresponde ao cenário 'Solicitação de exclusão de dados' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /dataerasure | /dataerasure | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/dataerasure Texto visível: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/dataErasure.js:62:18 at /juice-shop/build/routes/dataErasure.js:98:7 at Layer.handle [as handle_request] (/juice-shop/node_modules/express/lib/router/layer.js:95:5) at next (/juice-shop/node_modules/express/lib/router/route.js:149:13) at Route.dispatch (/juice-shop/node_modules/express/lib/router/route.js:119:3) at Layer.handle [as handle_request] (/juice-shop/node_modules/express/lib/router/layer.js:95:5) at /juice-shop/node_modules/express/lib/router/index.js:284:15 at router.process_params (/juice-shop/node_modules/express/lib/router/index.js:346:12) at next (/juice-shop Texto observado durante a ação: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.1 |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/dataErasure.js:62:18 at /juice-shop/build/routes/dataErasure.js:98:7 at Layer.handle [as handle_request] (/juice-shop/node_modules/express/lib/router/layer.js:95:5) at next (/juice-shop/node_modules/express/lib/router/route.js:149:13) at Route.dispatch (/juice-shop/node_modules/express/lib/router/route.js:119:3) at Layer.handle [as handle_request] (/juice-shop/node_modules/express/lib/router/layer.js:95:5) at /juice-shop/node_modules/express/lib/router/index.js:284:15 at router.process_params (/juice-shop/node_modules/express/lib/router/index.js:346:12) at next (/juice-shop/node_modules/express/lib/router/index.js:280:10) at router.handle (/juice-shop/node_modules/express/lib/router/index.js:175 |
