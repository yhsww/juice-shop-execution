# Ficha de Cenário

**ID do cenário:** CEN-PER-15
**Domínio:** PER
**Nome do cenário:** Enviar feedback ao cliente sem nota
**Ator:** Cliente autenticado
**Fluxo:** Abrir 'Customer Feedback', escrever comentário e não escolher nota.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir 'Customer Feedback', escrever comentário e não escolher nota.'. A descrição corresponde ao cenário 'Enviar feedback ao cliente sem nota' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/contact Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. | 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? | Result send Submit Texto transitório capturado: 1*6+9 | CAPTCHA: What is 1*6+9 ? | Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit | Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is ? Result send Submit | Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is ? Result send Submit | CAPTCHA: What is ? | Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is ? Result send Submit | send
2. Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Max. 160 characters 12/160 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 12/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit | Comment Max. 160 characters 12/160 | Author Comment Max. 160 characters 12/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit | Customer Feedback Author Comment Max. 160 characters 12/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit Mensagem transitória: Comment Max. 160 characters 0/160 | Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit | Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit | Comment

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is ? Result send Submit
- Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is ? Result send Submit
- CAPTCHA: What is ?
- Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is ? Result send Submit
- send
- send Submit
- Submit
- Author
- Comment Max. 160 characters 0/160
- Result
- Comment
- 1★
- Rating 1★
- Max. 160 characters 0/160
- Customer Feedback
- Max. 160 characters
- Rating
- What is
- 1*6+9
- CAPTCHA: What is 1*6+9 ?

## Dados manipulados

Dados declarados no cenário: Comentário 'Teste AMBOLS'.
Passo 1: /#/contact
Passo 3: Teste AMBOLS

## Coerente com loja de sucos?

Sim.

## Justificativa

Feedback sem nota fica incompleto.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir 'Customer Feedback', escrever comentário e não escolher nota.'. A descrição corresponde ao cenário 'Enviar feedback ao cliente sem nota' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/contact | /#/contact | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/contact Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. \| 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? \| Result send Submit Texto transitório capturado: 1*6+9 \| CAPTCHA: What is 1*6+9 ? \| Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit \| Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shoppi |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit |
| 3 | Preencher "Comment" | Teste AMBOLS | Conteúdo/estrutura visível da página foi alterado. Texto transitório capturado: Max. 160 characters 12/160 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 12/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit \| Comment Max. 160 characters 12/160 \| Author Comment Max. 160 characters 12/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit \| Customer Feedback Author Comment Max. 160 characters 12/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit Mensagem transitória: Comment Max. 160 characters 0/160 \| Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit \| Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit \| menu OWASP Juice Shop search search close ac |
| 4 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 12/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit |
| 5 | ASSERT_DISABLED |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 12/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit |
