# Ficha de Cenário

**ID do cenário:** CEN-PER-12
**Domínio:** PER
**Nome do cenário:** Perfil sem login
**Ator:** Visitante não autenticado
**Fluxo:** Sem sessão, abrir /profile.

## Pré-condição (estado inicial)

Sem sessão ativa.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Sem sessão, abrir /profile.'. A descrição corresponde ao cenário 'Perfil sem login' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/profile Texto visível: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/userProfile.js:69:18 Texto observado durante a ação: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/userProfile.js:69:18

## Mensagens exibidas ao usuário

Nenhuma mensagem transitória relevante capturada.

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /profile

## Coerente com loja de sucos?

Sim.

## Justificativa

Dados de perfil são pessoais.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Sem sessão, abrir /profile.'. A descrição corresponde ao cenário 'Perfil sem login' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /profile | /profile | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/profile Texto visível: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/userProfile.js:69:18 Texto observado durante a ação: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/userProfile.js:69:18 |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/userProfile.js:69:18 |
