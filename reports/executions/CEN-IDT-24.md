# Ficha de Cenário

**ID do cenário:** CEN-IDT-24
**Domínio:** IDT
**Nome do cenário:** Troca de senha com confirmação divergente
**Ator:** Cliente autenticado
**Fluxo:** Informar senha atual correta e nova senha diferente da repetição.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Informar senha atual correta e nova senha diferente da repetição.'. A descrição corresponde ao cenário 'Troca de senha com confirmação divergente' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. | 0/40 Repeat New Password 0/20 Change Texto transitório capturado: Repeat New Password | Password must be 5-40 characters long. 0/40 | 0/20 | Password must be 5-40 characters long. | Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change Registration completed successfully. You can now log in. X | Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | Change Password | Change
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password must be 5-40 characters long. 10/40 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change | New Password Password must be 5-40 characters long. 10/40 | Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change | Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change Mensagem transitória: Current Password | Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | New Password Password must be 5-40 characters long. 0/40
3. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado:

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change Registration completed successfully. You can now log in. X
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
- Registration completed successfully. You can now log in. X
- 10/40
- Password must be 5-40 characters long. 10/40
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change
- New Password Password must be 5-40 characters long. 10/40
- Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change

## Dados manipulados

Dados declarados no cenário: Atual 'Teste@12345'; nova 'Nova@12345'; repetição 'Nova@54321'.
Passo 1: /#/privacy-security/change-password
Passo 2: Teste@12345
Passo 3: Nova@12345
Passo 4: Nova@54321

## Coerente com loja de sucos?

Sim.

## Justificativa

Evita que o cliente fixe uma senha digitada errado.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Informar senha atual correta e nova senha diferente da repetição.'. A descrição corresponde ao cenário 'Troca de senha com confirmação divergente' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/privacy-security/change-password | /#/privacy-security/change-password | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. \| 0/40 Repeat New Password 0/20 Change Texto transitório capturado: Repeat New Password \| Password must be 5-40 characters long. 0/40 \| 0/20 \| Password must be 5-40 characters long. \| Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 languag |
| 2 | Preencher "Current Password" | Teste@12345 | Nenhuma mudança visual relevante detectada. Texto transitório capturado: Current Password \| Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change Mensagem transitória: Current Password \| Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| menu OWASP Juice Shop search search close account_circle Account shopp |
| 3 | Preencher "New Password" | Nova@12345 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password must be 5-40 characters long. 10/40 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change \| New Password Password must be 5-40 characters long. 10/40 \| Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change Mensagem transitória: Current Password \| Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat |
| 4 | Preencher "Repeat New Password" | Nova@54321 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: 10/20 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 10/20 Change \| Repeat New Password 10/20 \| Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 10/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 10/20 Change Mensagem transitória: New Password Password must be 5-40 characters long. 10/40 \| Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change |
| 5 | Pressionar Tab |  | Texto visível: 10/40 Repeat New Password Passwords do not match Change Texto transitório capturado: Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password Passwords do not match Change \| Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password Passwords do not match Change \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password Passwords do not match Change \| Repeat New Password \| Passwords do not match Mensagem transitória: Repeat New Password Passwords do not match \| Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password Passwords do not match Change \| Change Password Current Password New  |
| 6 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password Passwords do not match Change |
| 7 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password Passwords do not match Change |
