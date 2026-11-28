# Ficha de Cenário

**ID do cenário:** CEN-PER-14
**Domínio:** PER
**Nome do cenário:** Consultar carteira digital
**Ator:** Cliente autenticado
**Fluxo:** Abrir a carteira digital e ver o saldo.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir a carteira digital e ver o saldo.'. A descrição corresponde ao cenário 'Consultar carteira digital' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/wallet Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit Texto transitório capturado: Wallet Balance 0.00 | Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit Registration completed successfully. You can now log in. X | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit | Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance Amount monetization_on Deposit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance Amount monetization_on Deposit Registration completed successfully. You can now log in. X | Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance Amount monetization_on Deposit | Di

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance Amount monetization_on Deposit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance Amount monetization_on Deposit Registration completed successfully. You can now log in. X
- Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance Amount monetization_on Deposit
- Digital Wallet
- Digital Wallet Try out our new Crypto Wallet
- Try out our new Crypto Wallet
- Add Money
- Wallet Balance
- monetization_on
- monetization_on Deposit
- Deposit
- Amount
- 0.00
- Wallet Balance 0.00
- Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit Registration completed successfully. You can now log in. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit
- Registration completed successfully. You can now log in. X

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/wallet

## Coerente com loja de sucos?

Parcial.

## Justificativa

Carteira com saldo é recurso comum em e-commerce, mas não essencial a uma loja de sucos.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir a carteira digital e ver o saldo.'. A descrição corresponde ao cenário 'Consultar carteira digital' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/wallet | /#/wallet | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/wallet Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit Texto transitório capturado: Wallet Balance 0.00 \| Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit Registration completed successfully. You can now log in. X \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Bala |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit |
