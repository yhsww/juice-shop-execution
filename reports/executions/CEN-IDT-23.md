# Ficha de Cenário

**ID do cenário:** CEN-IDT-23
**Domínio:** IDT
**Nome do cenário:** Troca de senha com senha atual incorreta
**Ator:** Cliente autenticado
**Fluxo:** Informar senha atual errada e uma nova senha válida repetida corretamente.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Informar senha atual errada e uma nova senha válida repetida corretamente.'. A descrição corresponde ao cenário 'Troca de senha com senha atual incorreta' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. | 0/40 Repeat New Password 0/20 Change Registration completed successfully. Texto transitório capturado: New Password | Repeat New Password | Password must be 5-40 characters long. 0/40 | 0/20 | Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change Registration completed successfully. You can now log in. X | Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | Change Password | Change
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change Registration completed successfully. You can now log in. X | Registration completed successfully. You can now log in. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change Mensagem transitória: Current Password | Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password 

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

Dados declarados no cenário: Senha atual 'Errada@999'; nova 'Nova@12345' duas vezes.
Passo 1: /#/privacy-security/change-password
Passo 2: Errada@999
Passo 3: Nova@12345
Passo 4: Nova@12345

## Coerente com loja de sucos?

Sim.

## Justificativa

Somente o dono da conta deve conseguir trocar a senha.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Informar senha atual errada e uma nova senha válida repetida corretamente.'. A descrição corresponde ao cenário 'Troca de senha com senha atual incorreta' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/privacy-security/change-password | /#/privacy-security/change-password | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. \| 0/40 Repeat New Password 0/20 Change Registration completed successfully. Texto transitório capturado: New Password \| Repeat New Password \| Password must be 5-40 characters long. 0/40 \| 0/20 \| Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Chan |
| 2 | Preencher "Current Password" | Errada@999 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change Registration completed successfully. You can now log in. X \| Registration completed successfully. You can now log in. X \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change Mensagem |
| 3 | Preencher "New Password" | Nova@12345 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Password must be 5-40 characters long. 10/40 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change \| New Password Password must be 5-40 characters long. 10/40 \| Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change Mensagem transitória: Current Password \| Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat |
| 4 | Preencher "Repeat New Password" | Nova@12345 | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 10/20 Change \| Repeat New Password 10/20 \| Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 10/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 10/20 Change \| Change Mensagem transitória: New Password Password must be 5-40 characters long. 10/40 \| Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 0/20 Chang |
| 5 | Clicar em "Change" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current password is not correct. \| 0/40 Repeat New Password 0/20 Change Texto transitório capturado: Current Password \| Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| New Password Password must be 5-40 characters long. 0/40 \| Repeat New Password 0/20 \| New Password Mensagem transitória: Change \| Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 10/20 Change \| Change Password Current Password New Password Password must be 5-40 characters long. 10/40 Repeat New Password 10/20 Change \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password mu |
| 6 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current password is not correct. Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change |
