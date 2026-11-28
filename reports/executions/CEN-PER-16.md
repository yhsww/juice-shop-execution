# Ficha de Cenário

**ID do cenário:** CEN-PER-16
**Domínio:** PER
**Nome do cenário:** Registrar reclamação (Complaint)
**Ator:** Cliente autenticado
**Fluxo:** Abrir 'Complaint', escrever a mensagem e enviar.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir 'Complaint', escrever a mensagem e enviar.'. A descrição corresponde ao cenário 'Registrar reclamação (Complaint)' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/complain Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. | 4096 characters 0 /4096 Invoice: send Submit Texto transitório capturado: Message Max. 4096 characters 0 /4096 | Message | Max. 4096 characters 0 /4096 | Max. 4096 characters | Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit Registration completed successfully. You can now log in. X | Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit | Complaint | Invoice:
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 32 /4096 Invoice: send Submit | Message Max. 4096 characters 32 /4096 | Customer Message Max. 4096 characters 32 /4096 Invoice: send Submit | Complaint Customer Message Max. 4096 characters 32 /4096 Invoice: send Submit | send Submit Mensagem transitória: Message Max. 4096 characters 0 /4096 | Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit | Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit | Message
3. Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer support will get in touch with you soon! | Your complaint reference is #3 Customer Message Please provide a text. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer support will get in touch with you soon! Your complaint reference is #3 Customer Message Please provide a text. Invoice: send Submit | Message Please provide a text. | Customer Message Please provide a text. Invoice: send Submit | Com

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit Registration completed successfully. You can now log in. X
- Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit
- Complaint
- Invoice:
- Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit
- send
- send Submit
- Submit
- Customer
- Message Max. 4096 characters 0 /4096
- Message
- Max. 4096 characters 0 /4096
- Max. 4096 characters
- Registration completed successfully. You can now log in. X
- 32
- 32 /4096
- Max. 4096 characters 32 /4096
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 32 /4096 Invoice: send Submit
- Message Max. 4096 characters 32 /4096

## Dados manipulados

Dados declarados no cenário: Mensagem 'Pedido chegou incompleto - teste'.
Passo 1: /#/complain
Passo 3: Pedido chegou incompleto - teste

## Coerente com loja de sucos?

Sim.

## Justificativa

Canal de reclamação é esperado em loja virtual.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir 'Complaint', escrever a mensagem e enviar.'. A descrição corresponde ao cenário 'Registrar reclamação (Complaint)' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/complain | /#/complain | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/complain Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. \| 4096 characters 0 /4096 Invoice: send Submit Texto transitório capturado: Message Max. 4096 characters 0 /4096 \| Message \| Max. 4096 characters 0 /4096 \| Max. 4096 characters \| Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit Registration completed successfully. You can  |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit |
| 3 | Preencher "Message" | Pedido chegou incompleto - teste | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 32 /4096 Invoice: send Submit \| Message Max. 4096 characters 32 /4096 \| Customer Message Max. 4096 characters 32 /4096 Invoice: send Submit \| Complaint Customer Message Max. 4096 characters 32 /4096 Invoice: send Submit \| send Submit Mensagem transitória: Message Max. 4096 characters 0 /4096 \| Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit \| Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit \| Message |
| 4 | Clicar em "Button to send the complaint" |  | Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer support will get in touch with you soon! \| Your complaint reference is #3 Customer Message Please provide a text. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer support will get in touch with you soon! Your complaint reference is #3 Customer Message Please provide a text. Invoice: send Submit \| Message Please provide a text. \| Customer Message Please provide a text. Invoice: send Submit \| Complaint Customer support will get in touch with you soon! Your complaint reference is #3 Customer Message Please provide a text. Invoice: send Submit \| Please provide a text. Mensagem transitória: send Submit \| Customer Message Max. 4096 characters 32 /40 |
| 5 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer support will get in touch with you soon! Your complaint reference is #3 Customer Message Please provide a text. Invoice: send Submit |
