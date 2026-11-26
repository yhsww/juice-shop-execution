# Ficha de Cenário

**ID do cenário:** CEN-CAT-16
**Domínio:** CAT
**Nome do cenário:** Acesso à política de privacidade
**Ator:** Cliente
**Fluxo:** Abrir a política de privacidade pela interface da loja.

## Pré-condição (estado inicial)

Catálogo disponível.

## Descrição do cenário

Cliente executa o fluxo 'Abrir a política de privacidade pela interface da loja.'. A descrição corresponde ao cenário 'Acesso à política de privacidade' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/privacy-policy Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Privacy Policy (Read our privacy policy.) X Privacy Policy Effective date: March 15, 2019 OWASP Juice Shop ("us", "we", or "our") operates the http://127.0.0.1 website (the "Service"). | This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our Service and the choices you have associated with that data. | Our Privacy Policy for OWASP Juice Shop is created with the help of the Free Privacy Policy website. | We use your data to provide and improve the Service. | By using the Service, you agree t Texto transitório capturado: By email: | By email: donotreply@owasp-juice.shop | You successfully solved a challenge: Privacy Policy (Read our privacy policy.) X | You successfully solved a challenge: Privacy Policy (Read our privacy policy.) | X Mensagem transitória: Privacy Policy | OWASP Juice Shop ("us", "we", or "our") operates the http://127.0.0.1 website (the "Service"). | http://127.0.0.1 | This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our Service and the choices you have associated with that data. Our Privacy Policy for OWASP Juice Shop is created with the help of the Free Privacy Policy website. | We use your data to provide and improve the Service. By using the Service, you agree to the collection and 

## Mensagens exibidas ao usuário

- Privacy Policy
- OWASP Juice Shop ("us", "we", or "our") operates the http://127.0.0.1 website (the "Service").
- http://127.0.0.1
- This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our Service and the choices you have associated with that data. Our Privacy Policy for OWASP Juice Shop is created with the help of the Free Privacy Policy website.
- We use your data to provide and improve the Service. By using the Service, you agree to the collection and use of information in accordance with this policy. Unless otherwise defined in this Privacy Policy, terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, accessible from http://127.0.0.1 .
- OWASP Juice Shop uses the collected data for various purposes:
- OWASP Juice Shop will take all steps reasonably necessary to ensure that your data is treated securely and in accordance with this Privacy Policy and no transfer of your Personal Data will take place to an organization or a country unless there are adequate controls in place including the security of your data and other personal information.
- OWASP Juice Shop may disclose your Personal Data in the good faith belief that such action is necessary to:
- To protect and defend the rights or property of OWASP Juice Shop
- To comply with a legal obligation To protect and defend the rights or property of OWASP Juice Shop To prevent or investigate possible wrongdoing in connection with the Service To protect the personal safety of users of the Service or the public To protect against legal liability
- By email:
- By email: donotreply@owasp-juice.shop
- You successfully solved a challenge: Privacy Policy (Read our privacy policy.) X
- You successfully solved a challenge: Privacy Policy (Read our privacy policy.)
- X

## Dados manipulados

Dados declarados no cenário: Nenhum dado adicional.
Passo 1: /#/privacy-security/privacy-policy

## Coerente com loja de sucos?

Sim.

## Justificativa

A política é uma informação institucional acessível ao cliente.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir a política de privacidade pela interface da loja.'. A descrição corresponde ao cenário 'Acesso à política de privacidade' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/privacy-security/privacy-policy | /#/privacy-security/privacy-policy | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/privacy-policy Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Privacy Policy (Read our privacy policy.) X Privacy Policy Effective date: March 15, 2019 OWASP Juice Shop ("us", "we", or "our") operates the http://127.0.0.1 website (the "Service"). \| This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our Service and the choices you have associated with that data. \| Our Privacy Policy for OWASP Juice Shop is created with the help of the Free Privacy Policy website. \| We use your data to provide and improve the Service. \| By using the Service, you agree t Texto transitório capturado: By email: \| By email: donotreply@owasp-juice.shop \| You |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN You successfully solved a challenge: Privacy Policy (Read our privacy policy.) X Privacy Policy Effective date: March 15, 2019 OWASP Juice Shop ("us", "we", or "our") operates the http://127.0.0.1 website (the "Service"). This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our Service and the choices you have associated with that data. Our Privacy Policy for OWASP Juice Shop is created with the help of the Free Privacy Policy website. We use your data to provide and improve the Service. By using the Service, you agree to the collection and us |
