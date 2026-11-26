# Ficha de Cenário

**ID do cenário:** CEN-PER-05
**Domínio:** PER
**Nome do cenário:** Acesso à alteração de senha
**Ator:** Cliente autenticado
**Fluxo:** Abrir a tela de alteração de senha.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir a tela de alteração de senha.'. A descrição corresponde ao cenário 'Acesso à alteração de senha' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Mensagem: Password must be 5-40 characters long. 0/40 | 0/20 Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. | 0/40 Repeat New Password 0/20 Change Texto transitório capturado: New Password | Repeat New Password | Password must be 5-40 characters long. 0/40 | 0/20 | Password must be 5-40 characters long. Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! | Password must be 5-40 characters long. 0/40 | 0/20 | 0 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it!
- Password must be 5-40 characters long. 0/40
- 0/20
- 0
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
- Password must be 5-40 characters long.

## Dados manipulados

Dados declarados no cenário: Nenhuma senha real deve ser registrada no relatório.
Passo 1: /#/privacy-security/change-password

## Coerente com loja de sucos?

Sim.

## Justificativa

O usuário precisa conseguir atualizar a própria senha pela interface.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir a tela de alteração de senha.'. A descrição corresponde ao cenário 'Acesso à alteração de senha' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a tela de alteração de senha | /#/privacy-security/change-password | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Mensagem: Password must be 5-40 characters long. 0/40 \| 0/20 Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. \| 0/40 Repeat New Password 0/20 Change Texto transitório capturado: New Password \| Repeat New Password \| Password must be 5-40 characters long. 0/40 \| 0/20 \| Password must be 5-40 characters long. Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! \| Password must be 5-40 characters long. 0/40 \| 0/20 \| 0 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New  |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! \| Password must be 5-40 characters long. 0/40 \| 0/20 \| 0 |
