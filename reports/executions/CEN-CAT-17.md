# Ficha de Cenário

**ID do cenário:** CEN-CAT-17
**Domínio:** CAT
**Nome do cenário:** Acesso ao score board
**Ator:** Cliente
**Fluxo:** Abrir o Score Board e verificar a listagem de desafios.

## Pré-condição (estado inicial)

Catálogo disponível.

## Descrição do cenário

Cliente executa o fluxo 'Abrir o Score Board e verificar a listagem de desafios.'. A descrição corresponde ao cenário 'Acesso ao score board' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/score-board Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Score Board (Find the carefully hidden 'Score Board' page.) code Jump to related coding challenge X 4% Hacking Challenges 0% Coding Challenges 5/186 Challenges Solved 1 2/27 2 3/29 3 0/51 4 0/40 5 0/25 6 0/14 search Search Difficulty Status All Tags settings All Broken Access Control XSS Observability Failures Improper Input Validation Unvalidated Redirects Vulnerable Components Broken Authentication Security through Obscurity Insecure Deserialization Broken Anti Automation Injection Sensitive Data Exposure Security Misconfiguration Cryptographic Issue Texto transitório capturado: You successfully solved a challenge: Score Board (Find the carefully hidden 'Score Board' page.) code Jump to related coding challenge | code Jump to related coding challenge | code | Jump to related coding challenge | X Mensagem transitória: Shenanigans Code Analysis | Shenanigans Code Analysis lightbulb_outlined 0/5 | lightbulb_outlined 0/5 | Shenanigans | lightbulb_outlined

## Mensagens exibidas ao usuário

- Shenanigans Code Analysis
- Shenanigans Code Analysis lightbulb_outlined 0/5
- lightbulb_outlined 0/5
- Shenanigans
- lightbulb_outlined
- Security Misconfiguration Login Support Team Log in with the support team's original user credentials without applying SQL Injection or any other bypass. Brute Force Code Analysis lightbulb_outlined 0/5
- Login Support Team
- Log in with the support team's original user credentials without applying SQL Injection or any other bypass.
- Brute Force Code Analysis
- Brute Force Code Analysis lightbulb_outlined 0/5
- Broken Anti Automation Multiple Likes Like any review at least three times as the same user. lightbulb_outlined 0/4
- Multiple Likes
- Like any review at least three times as the same user.
- Cryptographic Issues Premium Paywall 💎💎💎💎💎 ₿ Unlock Premium Challenge to access exclusive content. Shenanigans lightbulb_outlined 0/4
- Premium Paywall
- 💎💎💎💎💎 ₿ Unlock Premium Challenge to access exclusive content.
- ₿ Unlock Premium Challenge
- Shenanigans lightbulb_outlined 0/4
- Broken Access Control SSRF Request a hidden resource on server through server. Code Analysis lightbulb_outlined 0/4
- Broken Access Control

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/score-board

## Coerente com loja de sucos?

Sim.

## Justificativa

O Score Board integra a interface do Juice Shop e é acessível pela aplicação.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir o Score Board e verificar a listagem de desafios.'. A descrição corresponde ao cenário 'Acesso ao score board' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/score-board | /#/score-board | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/score-board Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Score Board (Find the carefully hidden 'Score Board' page.) code Jump to related coding challenge X 4% Hacking Challenges 0% Coding Challenges 5/186 Challenges Solved 1 2/27 2 3/29 3 0/51 4 0/40 5 0/25 6 0/14 search Search Difficulty Status All Tags settings All Broken Access Control XSS Observability Failures Improper Input Validation Unvalidated Redirects Vulnerable Components Broken Authentication Security through Obscurity Insecure Deserialization Broken Anti Automation Injection Sensitive Data Exposure Security Misconfiguration Cryptographic Issue Texto transitório capturado: You successfully solved a challenge: Score Board (Find the carefully hidden 'Score Boar |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Score Board (Find the carefully hidden 'Score Board' page.) code Jump to related coding challenge X 4% Hacking Challenges 0% Coding Challenges 5/186 Challenges Solved 1 2/27 2 3/29 3 0/51 4 0/40 5 0/25 6 0/14 search Search Difficulty Status All Tags settings All Broken Access Control XSS Observability Failures Improper Input Validation Unvalidated Redirects Vulnerable Components Broken Authentication Security through Obscurity Insecure Deserialization Broken Anti Automation Injection Sensitive Data Exposure Security Misconfiguration Cryptographic Issues Miscellaneous |
