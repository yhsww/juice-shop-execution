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

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/score-board Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 5% Hacking Challenges 0% Coding Challenges 6/186 Challenges Solved 1 3/27 2 3/29 3 0/51 4 0/40 5 0/25 6 0/14 search Search Difficulty Status All Tags settings All Broken Access Control XSS Observability Failures Improper Input Validation Unvalidated Redirects Vulnerable Components Broken Authentication Security through Obscurity Insecure Deserialization Broken Anti Automation Injection Sensitive Data Exposure Security Misconfiguration Cryptographic Issues Miscellaneous XXE 18 challenges are unavailable on Docker due to security concerns or technical incompatibility! | Hide disabled challe Texto transitório capturado: Broken Authentication Password Strength Log in with the administrator's user credentials without previously changing them or applying SQL Injection. Brute Force Tutorial With Coding Challenge code policy_outline school_outline lightbulb_outlined 0/4 | Shenanigans Tutorial With Coding Challenge code school_outline lightbulb_outlined 0/3 | XSS Bonus Payload Use the bonus payload <iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe> in the DOM XSS challenge. Shenanigans Tutorial With Coding Challenge code school_outline lightbulb_outlin

## Mensagens exibidas ao usuário

- Broken Access Control SSRF Request a hidden resource on server through server. Code Analysis lightbulb_outlined 0/4
- Broken Access Control
- SSRF
- Request a hidden resource on server through server.
- Code Analysis lightbulb_outlined 0/4
- Injection SSTi Infect the server with juicy malware by abusing arbitrary command execution. (This challenge is potentially harmful on Docker!) Contraption Danger Zone Code Analysis info_outline lightbulb_outlined 0/4
- Injection
- SSTi
- Infect the server with juicy malware by abusing arbitrary command execution. (This challenge is potentially harmful on Docker!)
- Contraption Danger Zone Code Analysis
- Contraption Danger Zone Code Analysis info_outline lightbulb_outlined 0/4
- Contraption
- Insecure Deserialization Successful RCE DoS Perform a Remote Code Execution that occupies the server for a while without using infinite loops. (This challenge is potentially harmful on Docker!) Danger Zone info_outline lightbulb_outlined 0/2
- Insecure Deserialization
- Successful RCE DoS
- Perform a Remote Code Execution that occupies the server for a while without using infinite loops. (This challenge is potentially harmful on Docker!)
- Danger Zone info_outline lightbulb_outlined 0/2
- info_outline lightbulb_outlined 0/2
- lightbulb_outlined 0/2
- XSS Video XSS Embed an XSS payload </script><script>alert(`xss`)</script> into our promo video. (This challenge is potentially harmful on Docker!) Danger Zone info_outline lightbulb_outlined 0/4

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
| 1 | Abrir a rota /#/score-board | /#/score-board | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/score-board Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 5% Hacking Challenges 0% Coding Challenges 6/186 Challenges Solved 1 3/27 2 3/29 3 0/51 4 0/40 5 0/25 6 0/14 search Search Difficulty Status All Tags settings All Broken Access Control XSS Observability Failures Improper Input Validation Unvalidated Redirects Vulnerable Components Broken Authentication Security through Obscurity Insecure Deserialization Broken Anti Automation Injection Sensitive Data Exposure Security Misconfiguration Cryptographic Issues Miscellaneous XXE 18 challenges are unavailable on Docker due to security concerns or technical incompatibility! \| Hide disabled challe Texto transitório capturado: Broken Authentication Password Strength Log in with the administrator's user credentia |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 5% Hacking Challenges 0% Coding Challenges 6/186 Challenges Solved 1 3/27 2 3/29 3 0/51 4 0/40 5 0/25 6 0/14 search Search Difficulty Status All Tags settings All Broken Access Control XSS Observability Failures Improper Input Validation Unvalidated Redirects Vulnerable Components Broken Authentication Security through Obscurity Insecure Deserialization Broken Anti Automation Injection Sensitive Data Exposure Security Misconfiguration Cryptographic Issues Miscellaneous XXE 18 challenges are unavailable on Docker due to security concerns or technical incompatibility! Hide disabled challenges Miscellaneou |
