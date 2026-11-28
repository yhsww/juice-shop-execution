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

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/score-board Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 6% Hacking Challenges 0% Coding Challenges 7/186 Challenges Solved 1 3/27 2 4/29 3 0/51 4 0/40 5 0/25 6 0/14 search Search Difficulty Status All Tags settings All Broken Access Control XSS Observability Failures Improper Input Validation Unvalidated Redirects Vulnerable Components Broken Authentication Security through Obscurity Insecure Deserialization Broken Anti Automation Injection Sensitive Data Exposure Security Misconfiguration Cryptographic Issues Miscellaneous XXE 18 challenges are unavailable on Docker due to security concerns or technical incompatibility! | Hide disabled challe Texto transitório capturado: Good for Demos With Coding Challenge code policy_outline school_outline lightbulb_outlined 0/5 | Broken Access Control Admin Section Access the administration section of the store. Good for Demos With Coding Challenge code policy_outline school_outline lightbulb_outlined 0/5 | school_outline lightbulb_outlined 0/4 | Good Practice Tutorial Good for Demos school_outline lightbulb_outlined 0/4 | Miscellaneous Privacy Policy Read our privacy policy. Good Practice Tutorial Good for Demos school_outline lightbulb_outlined 0/4 Mensagem transitória: Broken Access Control SSRF Request a hidden resource on server through server. Code Analysis lightbulb_outlined 0/4 | Broken Access Control | SSRF | Request a hidden resource on server through server. | Code Analysis lightbulb_outlined 0/4

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
| 1 | Abrir a rota /#/score-board | /#/score-board | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/score-board Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 6% Hacking Challenges 0% Coding Challenges 7/186 Challenges Solved 1 3/27 2 4/29 3 0/51 4 0/40 5 0/25 6 0/14 search Search Difficulty Status All Tags settings All Broken Access Control XSS Observability Failures Improper Input Validation Unvalidated Redirects Vulnerable Components Broken Authentication Security through Obscurity Insecure Deserialization Broken Anti Automation Injection Sensitive Data Exposure Security Misconfiguration Cryptographic Issues Miscellaneous XXE 18 challenges are unavailable on Docker due to security concerns or technical incompatibility! \| Hide disabled challe Texto transitório capturado: Good for Demos With Coding Challenge code policy_outline school_outline lightbulb_outl |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 6% Hacking Challenges 0% Coding Challenges 7/186 Challenges Solved 1 3/27 2 4/29 3 0/51 4 0/40 5 0/25 6 0/14 search Search Difficulty Status All Tags settings All Broken Access Control XSS Observability Failures Improper Input Validation Unvalidated Redirects Vulnerable Components Broken Authentication Security through Obscurity Insecure Deserialization Broken Anti Automation Injection Sensitive Data Exposure Security Misconfiguration Cryptographic Issues Miscellaneous XXE 18 challenges are unavailable on Docker due to security concerns or technical incompatibility! Hide disabled challenges Miscellaneou |
