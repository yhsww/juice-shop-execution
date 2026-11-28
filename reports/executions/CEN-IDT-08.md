# Ficha de Cenário

**ID do cenário:** CEN-IDT-08
**Domínio:** IDT
**Nome do cenário:** Alteração de senha
**Ator:** Cliente
**Fluxo:** Abrir a área de alteração de senha e informar os dados de teste.

## Pré-condição (estado inicial)

Conta de teste disponível para autenticação.

## Descrição do cenário

Cliente executa o fluxo 'Abrir a área de alteração de senha e informar os dados de teste.'. A descrição corresponde ao cenário 'Alteração de senha' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. | 0/40 Repeat New Password 0/20 Change Texto transitório capturado: New Password | Repeat New Password | Password must be 5-40 characters long. 0/40 | 0/20 | Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | Change Password | Change
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password must be 5-40 characters long. 12/40 | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change | New Password Password must be 5-40 characters long. 12/40 | Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change | Change Password Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change Mensagem transitória: Current Password | Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Pass

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change
- Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change
- Change Password
- Change
- Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change
- Current Password
- New Password Password must be 5-40 characters long. 0/40
- Repeat New Password 0/20
- New Password
- Repeat New Password
- Password must be 5-40 characters long. 0/40
- 0/20
- Password must be 5-40 characters long.
- 12/40
- Password must be 5-40 characters long. 12/40
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change
- New Password Password must be 5-40 characters long. 12/40
- Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change
- Change Password Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change

## Dados manipulados

Dados declarados no cenário: Senha atual e nova senha de teste.
Passo 1: /#/privacy-security/change-password
Passo 2: Teste@12345
Passo 3: Teste@123456
Passo 4: Teste@123456

## Coerente com loja de sucos?

Sim.

## Justificativa

A alteração periódica de senha é função de gerenciamento de conta.

## Descrição funcional do cenário

Cliente executa o fluxo 'Abrir a área de alteração de senha e informar os dados de teste.'. A descrição corresponde ao cenário 'Alteração de senha' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/privacy-security/change-password | /#/privacy-security/change-password | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. \| 0/40 Repeat New Password 0/20 Change Texto transitório capturado: New Password \| Repeat New Password \| Password must be 5-40 characters long. 0/40 \| 0/20 \| Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search c |
| 2 | Preencher "Current Password" | Teste@12345 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Current Password \| Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change Mensagem transitória: Current Password \| Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 0 |
| 3 | Preencher "New Password" | Teste@123456 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password must be 5-40 characters long. 12/40 \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change \| New Password Password must be 5-40 characters long. 12/40 \| Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change Mensagem transitória: Current Password \| Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/ |
| 4 | Preencher "Repeat New Password" | Teste@123456 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 12/20 Change \| Repeat New Password 12/20 \| Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 12/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 12/20 Change \| Change Mensagem transitória: New Password Password must be 5-40 characters long. 12/40 \| Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 0/20 Change \| Change Passw |
| 5 | Clicar em "Change" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Your password was successfully changed. \| 0/40 Repeat New Password 0/20 Change Texto transitório capturado: Current Password \| Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| New Password Password must be 5-40 characters long. 0/40 \| Repeat New Password 0/20 \| New Password Mensagem transitória: Repeat New Password 12/20 \| Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 12/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 12/40 Repeat New Password 12/20 Change \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop searc |
| 6 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Your password was successfully changed. Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change |
