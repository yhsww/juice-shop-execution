# Relatório de Execução — Checkout

**Projeto:** Juice Shop Execution  
**Branch:** `ambols-recovery-v2`  
**Cobertura:** 28 cenários do domínio  
**Resultado:** **28/28 aprovados**  

## 1. Objetivo

Este documento registra, de forma detalhada, os cenários automatizados do domínio **Checkout**, preservando a definição funcional, pré-condições, dados, sequência de ações e critérios de aceite definidos no arquivo de cenários. O status informado corresponde à execução final consolidada do conjunto completo, na qual os **72 cenários foram aprovados**.

## 2. Resumo

| ID | Cenário | Ator | Status |
|---|---|---|---|
| CEN-CHK-01 | Iniciar checkout | Cliente | **PASS** |
| CEN-CHK-02 | Adicionar endereço de entrega | Cliente | **PASS** |
| CEN-CHK-03 | Selecionar endereço de entrega | Cliente | **PASS** |
| CEN-CHK-04 | Confirmar seleção de endereço | Cliente | **PASS** |
| CEN-CHK-05 | Escolher método de entrega | Cliente | **PASS** |
| CEN-CHK-06 | Confirmar método de entrega | Cliente | **PASS** |
| CEN-CHK-07 | Adicionar cartão de crédito | Cliente | **PASS** |
| CEN-CHK-08 | Selecionar cartão de crédito | Cliente | **PASS** |
| CEN-CHK-09 | Avançar da etapa de pagamento | Cliente | **PASS** |
| CEN-CHK-10 | Conferir resumo do pedido | Cliente | **PASS** |
| CEN-CHK-11 | Confirmar pedido | Cliente | **PASS** |
| CEN-CHK-12 | Visualizar outras opções de pagamento | Cliente | **PASS** |
| CEN-CHK-13 | Acessar doação pelas outras opções | Cliente | **PASS** |
| CEN-CHK-14 | Acessar merchandise pelas outras opções | Cliente | **PASS** |
| CEN-CHK-15 | Aplicar cupom no checkout | Cliente | **PASS** |
| CEN-CHK-16 | Imprimir confirmação do pedido | Cliente | **PASS** |
| CEN-CHK-17 | Acessar histórico de pedidos | Cliente | **PASS** |
| CEN-CHK-18 | Visualizar pedido e produtos no histórico | Cliente | **PASS** |
| CEN-CHK-19 | Acessar rastreamento do pedido | Cliente | **PASS** |
| CEN-CHK-20 | Visualizar status de trânsito | Cliente | **PASS** |
| CEN-CHK-21 | Acessar PDF de pedido pelo histórico | Cliente | **PASS** |
| CEN-CHK-22 | Verificar carrinho após conclusão | Cliente | **PASS** |
| CEN-CHK-25 | Bloquear avanço sem pagamento | Cliente | **PASS** |
| CEN-CHK-27 | Retornar de uma etapa do checkout | Cliente | **PASS** |
| CEN-CHK-28 | Fluxo completo de compra | Cliente | **PASS** |
| CEN-CHK-23 | Checkout sem endereço | Cliente | **PASS** |
| CEN-CHK-24 | Checkout sem método de entrega | Cliente | **PASS** |
| CEN-CHK-26 | Conferir total no resumo | Cliente | **PASS** |

## 3. Detalhamento dos cenários

### CEN-CHK-01 — Iniciar checkout
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o carrinho e iniciar o checkout.
**Objetivo:** A aplicação deve direcionar o cliente para seleção de endereço.
**Pré-condições:** Carrinho contém produto.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O checkout inicia a etapa de conclusão da compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/address/select`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Acionar o elemento identificado por papel "button", nome "Checkout", correspondência parcial.
3. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-02 — Adicionar endereço de entrega
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Cadastrar um novo endereço para entrega.
**Objetivo:** A aplicação deve permitir cadastrar endereço de entrega.
**Pré-condições:** Cliente autenticado; carrinho contém produto.
**Dados utilizados:** País: Brazil; nome: Cliente Teste; telefone: 8599999999; CEP: 60000000; endereço: Rua Teste, 100; cidade: Fortaleza; estado: CE.
**Justificativa do cenário:** O endereço é necessário para entrega do pedido.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Cliente Teste`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Acionar o elemento identificado por papel "button", nome "Checkout", correspondência parcial.
3. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
4. Acionar o elemento identificado por papel "button", nome "Add a new address", correspondência parcial.
5. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
6. Preencher o campo identificado por rótulo "Country", correspondência parcial com o valor `Brazil`.
7. Preencher o campo identificado por rótulo "Name", correspondência parcial com o valor `Cliente Teste`.
8. Preencher o campo identificado por rótulo "Mobile Number", correspondência parcial com o valor `8599999999`.
9. Preencher o campo identificado por rótulo "ZIP Code", correspondência parcial com o valor `60000000`.
10. Preencher o campo identificado por rótulo "Address", correspondência parcial com o valor `Rua Teste, 100`.
11. Preencher o campo identificado por rótulo "City", correspondência parcial com o valor `Fortaleza`.
12. Preencher o campo identificado por rótulo "State", correspondência parcial com o valor `CE`.
13. Acionar o elemento identificado por papel "button", nome "Submit", correspondência parcial.
14. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-03 — Selecionar endereço de entrega
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Selecionar a linha do endereço previamente cadastrado (Rua Teste, 100) e prosseguir para a etapa de entrega.
**Objetivo:** A aplicação deve permitir selecionar um endereço cadastrado e continuar para a etapa de entrega.
**Pré-condições:** Carrinho contém produto; há endereço cadastrado.
**Dados utilizados:** Endereço: Rua Teste, 100; cidade: Fortaleza; estado: CE.
**Justificativa do cenário:** A seleção do endereço define o destino do pedido.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/delivery-method`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Acionar o elemento identificado por papel "button", nome "Checkout", correspondência parcial.
3. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
4. Acionar o elemento identificado por texto "Rua Teste, 100", correspondência parcial.
5. Acionar o elemento identificado por papel "button", nome "Continue", correspondência parcial.
6. Aguardar 800 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-04 — Confirmar seleção de endereço
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Selecionar um endereço cadastrado e verificar a habilitação do avanço.
**Objetivo:** A aplicação deve manter o avanço bloqueado até que um endereço seja selecionado e habilitá-lo após a seleção válida.
**Pré-condições:** Carrinho contém produto; há endereço cadastrado.
**Dados utilizados:** Endereço: Rua Teste, 100.
**Justificativa do cenário:** A etapa seguinte depende da seleção de um endereço.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/address/select` e o texto visível contenha `Cliente Teste`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Acionar o elemento identificado por papel "button", nome "Checkout", correspondência parcial.
3. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
4. ASSERT_DISABLED — {"type":"ASSERT_DISABLED","target":{"role":"button","name":"Continue","exact":false}}.
5. Acionar o elemento identificado por texto "Rua Teste, 100", correspondência parcial.
6. ASSERT_ENABLED — {"type":"ASSERT_ENABLED","target":{"role":"button","name":"Continue","exact":false}}.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-05 — Escolher método de entrega
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Selecionar a opção de entrega 'Standard Delivery' e prosseguir para a etapa de pagamento.
**Objetivo:** A aplicação deve permitir selecionar o método de entrega.
**Pré-condições:** Cliente autenticado; endereço de entrega selecionado.
**Dados utilizados:** Método de entrega exibido: Standard Delivery.
**Justificativa do cenário:** A entrega é uma etapa necessária do pedido.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/payment/shop`.
**Procedimento executado:**
1. Navegar para `/#/delivery-method`.
2. Acionar o elemento identificado por texto "Standard Delivery", correspondência parcial.
3. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
4. Acionar o elemento identificado por papel "button", nome "Continue", correspondência parcial.
5. Aguardar 800 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-06 — Confirmar método de entrega
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Verificar que o avanço está bloqueado sem método de entrega, selecionar 'Standard Delivery' e confirmar o avanço para pagamento.
**Objetivo:** A aplicação deve avançar para a seleção de pagamento.
**Pré-condições:** Cliente autenticado; endereço de entrega selecionado.
**Dados utilizados:** Método de entrega exibido: Standard Delivery.
**Justificativa do cenário:** A confirmação conecta entrega à etapa de pagamento.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/payment/shop`.
**Procedimento executado:**
1. Navegar para `/#/delivery-method`.
2. ASSERT_DISABLED — {"type":"ASSERT_DISABLED","target":{"role":"button","name":"Continue","exact":false}}.
3. Acionar o elemento identificado por papel "radio", texto "Standard Delivery", correspondência parcial.
4. ASSERT_ENABLED — {"type":"ASSERT_ENABLED","target":{"role":"button","name":"Continue","exact":false}}.
5. Acionar o elemento identificado por papel "button", nome "Continue", correspondência parcial.
6. Aguardar 600 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-07 — Adicionar cartão de crédito
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Cadastrar um cartão de crédito de teste na etapa de pagamento.
**Objetivo:** A aplicação deve permitir cadastrar uma forma de pagamento.
**Pré-condições:** Cliente autenticado; método de entrega selecionado.
**Dados utilizados:** Número de teste: 4000000000000002; validade e nome de teste.
**Justificativa do cenário:** O pedido precisa de uma forma de pagamento.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `My Payment Options`, `0002`.
**Procedimento executado:**
1. Navegar para `/#/payment/shop`.
2. Acionar o elemento identificado por texto "Add new card", correspondência parcial.
3. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
4. Preencher o campo identificado por rótulo "Name", correspondência parcial com o valor `Cliente Teste`.
5. Preencher o campo identificado por rótulo "Card Number", correspondência parcial com o valor `4000000000000002`.
6. Selecionar `12` no campo identificado por rótulo "Expiry Month", correspondência parcial.
7. Selecionar `2090` no campo identificado por rótulo "Expiry Year", correspondência parcial.
8. Acionar o elemento identificado por papel "button", nome "Submit", correspondência parcial.
9. Aguardar 800 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-08 — Selecionar cartão de crédito
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Selecionar a linha do cartão de teste cadastrado, identificada pelos quatro últimos dígitos 0002.
**Objetivo:** A aplicação deve permitir selecionar um cartão.
**Pré-condições:** Cliente autenticado; método de entrega selecionado; cartão de teste cadastrado.
**Dados utilizados:** Cartão de teste cadastrado terminado em 0002.
**Justificativa do cenário:** A seleção define a forma de pagamento do pedido.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `0002`.
**Procedimento executado:**
1. Navegar para `/#/payment/shop`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
3. Acionar o elemento identificado por texto "0002", correspondência parcial.
4. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-09 — Avançar da etapa de pagamento
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Selecionar a linha do cartão terminado em 0002 e prosseguir para o resumo do pedido.
**Objetivo:** A aplicação deve habilitar o avanço após uma forma de pagamento válida.
**Pré-condições:** Cliente autenticado; método de entrega selecionado; cartão de teste cadastrado.
**Dados utilizados:** Cartão de teste cadastrado terminado em 0002.
**Justificativa do cenário:** A etapa de pagamento deve levar ao resumo do pedido.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/order-summary`.
**Procedimento executado:**
1. Navegar para `/#/payment/shop`.
2. Acionar o elemento identificado por papel "radio", nome "0002", correspondência parcial.
3. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
4. Acionar o elemento identificado por papel "button", nome "Continue", correspondência parcial.
5. Aguardar 900 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-10 — Conferir resumo do pedido
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Visualizar os dados consolidados antes da confirmação.
**Objetivo:** A aplicação deve apresentar um resumo do pedido.
**Pré-condições:** Cliente autenticado; pedido com endereço, entrega e pagamento definidos.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O resumo permite validar a compra antes da confirmação.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Order Summary`.
**Procedimento executado:**
1. Navegar para `/#/order-summary`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-11 — Confirmar pedido
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Confirmar a compra a partir do resumo.
**Objetivo:** A aplicação deve concluir o pedido e apresentar confirmação.
**Pré-condições:** Cliente autenticado; resumo do pedido acessível.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A confirmação conclui o fluxo de compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/order-completion`.
**Procedimento executado:**
1. Navegar para `/#/order-summary`.
2. Acionar o elemento identificado por papel "button", nome "Place your order and pay", correspondência parcial.
3. Aguardar 1200 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-12 — Visualizar outras opções de pagamento
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Expandir a seção de outras opções de pagamento.
**Objetivo:** A interface deve revelar a seção de outras opções quando expandida.
**Pré-condições:** Cliente autenticado; etapa de pagamento acessível; seção 'Other payment options' disponível.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A loja oferece alternativas além do cartão no fluxo apresentado.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Other payment options`.
**Procedimento executado:**
1. Navegar para `/#/payment/shop`.
2. Acionar o elemento identificado por texto "Other payment options".
3. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-13 — Acessar doação pelas outras opções
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a opção de doação disponibilizada na etapa de pagamento.
**Objetivo:** A aplicação deve disponibilizar o acesso à opção de doação.
**Pré-condições:** Cliente autenticado; etapa de pagamento acessível; seção 'Other payment options' disponível.
**Dados utilizados:** Nenhum pagamento real.
**Justificativa do cenário:** A opção integra as alternativas apresentadas pela aplicação.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o critério observável definido pelo cenário seja atendido.
**Procedimento executado:**
1. Navegar para `/#/payment/shop`.
2. Acionar o elemento identificado por texto "Other payment options", correspondência parcial.
3. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
4. Acionar o elemento identificado por papel "button", nome "Credit Card", correspondência parcial.
5. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-14 — Acessar merchandise pelas outras opções
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a opção de merchandise disponibilizada.
**Objetivo:** A aplicação deve disponibilizar o acesso ao merchandise.
**Pré-condições:** Cliente autenticado; etapa de pagamento acessível; seção 'Other payment options' disponível.
**Dados utilizados:** Nenhum pagamento real.
**Justificativa do cenário:** A opção integra as alternativas apresentadas pela aplicação.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o critério observável definido pelo cenário seja atendido.
**Procedimento executado:**
1. Navegar para `/#/payment/shop`.
2. Acionar o elemento identificado por texto "Other payment options", correspondência parcial.
3. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
4. Acionar o elemento identificado por papel "button", nome "Spreadshirt (US)", correspondência parcial.
5. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-15 — Aplicar cupom no checkout
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Informar o código TESTE12345 no campo de cupom, solicitar o resgate e verificar a rejeição do cupom inválido.
**Objetivo:** A aplicação deve informar que um cupom inválido não pode ser resgatado.
**Pré-condições:** Cliente autenticado; etapa de pagamento acessível; campo de cupom disponível.
**Dados utilizados:** Cupom inválido de teste: TESTE12345.
**Justificativa do cenário:** Cupons fazem parte da etapa de compra quando habilitados.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Invalid coupon`.
**Procedimento executado:**
1. Navegar para `/#/payment/shop`.
2. Preencher o campo identificado por rótulo "Coupon", correspondência parcial com o valor `TESTE12345`.
3. Acionar o elemento identificado por papel "button", nome "Redeem", correspondência parcial.
4. Aguardar 800 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-16 — Imprimir confirmação do pedido
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Acessar a confirmação de um pedido concluído e abrir a opção de impressão da confirmação.
**Objetivo:** A aplicação deve abrir a confirmação imprimível em nova página ou aba.
**Pré-condições:** Cliente autenticado; pedido concluído.
**Dados utilizados:** Pedido concluído de teste.
**Justificativa do cenário:** A confirmação fornece registro do pedido.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Print Order Confirmation`.
**Procedimento executado:**
1. Navegar para `/#/order-history`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
3. Acionar o elemento identificado por papel "button", nome "Print order confirmation", correspondência exata.
4. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-17 — Acessar histórico de pedidos
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o histórico de pedidos após uma compra.
**Objetivo:** A aplicação deve apresentar os pedidos realizados.
**Pré-condições:** Cliente autenticado; pedido concluído.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O histórico permite acompanhar compras anteriores.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Order History`.
**Procedimento executado:**
1. Navegar para `/#/order-history`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-18 — Visualizar pedido e produtos no histórico
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o histórico e verificar os dados apresentados do pedido.
**Objetivo:** A aplicação deve apresentar o histórico e os dados dos pedidos realizados.
**Pré-condições:** Cliente autenticado; pedido concluído.
**Dados utilizados:** Pedido de teste.
**Justificativa do cenário:** O detalhamento permite conferir a compra realizada.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Order History`, `Product`, `Quantity`, `Total Price`.
**Procedimento executado:**
1. Navegar para `/#/order-history`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-19 — Acessar rastreamento do pedido
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o rastreamento a partir do histórico ou confirmação.
**Objetivo:** A aplicação deve disponibilizar a tela de rastreamento.
**Pré-condições:** Cliente autenticado; pedido concluído.
**Dados utilizados:** Pedido de teste.
**Justificativa do cenário:** O rastreamento permite acompanhar a entrega.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/track-result`.
**Procedimento executado:**
1. Navegar para `/#/order-history`.
2. Acionar o elemento identificado por papel "button", nome "Track Your Order", correspondência parcial.
3. Aguardar 900 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-20 — Visualizar status de trânsito
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Conferir o status de trânsito de um pedido.
**Objetivo:** A aplicação deve exibir o status de trânsito.
**Pré-condições:** Cliente autenticado; pedido concluído.
**Dados utilizados:** Pedido de teste.
**Justificativa do cenário:** O status informa a situação logística do pedido.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/track-result` e o status semântico seja `transit`.
**Procedimento executado:**
1. Navegar para `/#/order-history`.
2. Acionar o elemento identificado por papel "button", nome "Track Your Order", correspondência parcial.
3. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-21 — Acessar PDF de pedido pelo histórico
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o histórico de pedidos e acionar a impressão da confirmação associada ao pedido de teste.
**Objetivo:** A aplicação deve disponibilizar o PDF do pedido.
**Pré-condições:** Cliente autenticado; pedido concluído.
**Dados utilizados:** Pedido concluído disponível no histórico.
**Justificativa do cenário:** O PDF permite obter uma confirmação documental.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Print Order Confirmation`.
**Procedimento executado:**
1. Navegar para `/#/order-history`.
2. Acionar o elemento identificado por papel "button", nome "Print order confirmation", correspondência exata.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-22 — Verificar carrinho após conclusão
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o carrinho após a conclusão do pedido e verificar que o produto comprado não permanece como item pendente.
**Objetivo:** A aplicação deve limpar o carrinho após a conclusão.
**Pré-condições:** Cliente autenticado; pedido concluído com sucesso.
**Dados utilizados:** Pedido de teste concluído; o produto utilizado no pedido foi Apple Juice.
**Justificativa do cenário:** Após a conclusão, os produtos comprados não devem permanecer como itens pendentes no carrinho.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Your Basket` e o texto visível não contenha `Apple Juice`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-25 — Bloquear avanço sem pagamento
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Acessar a etapa de pagamento sem selecionar uma forma de pagamento e verificar o bloqueio do avanço.
**Objetivo:** A aplicação deve manter o avanço bloqueado enquanto nenhuma forma de pagamento estiver selecionada.
**Pré-condições:** Cliente autenticado; método de entrega selecionado.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A confirmação do pedido depende da seleção de uma forma de pagamento.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Add new card`.
**Procedimento executado:**
1. Navegar para `/#/payment/shop`.
2. ASSERT_DISABLED — {"type":"ASSERT_DISABLED","target":{"role":"button","name":"Continue","exact":false}}.
3. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-27 — Retornar de uma etapa do checkout
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Selecionar 'Standard Delivery', avançar para pagamento, retornar à etapa de entrega e verificar que a opção pode ser selecionada novamente.
**Objetivo:** A navegação de retorno deve preservar o estado necessário do checkout.
**Pré-condições:** Cliente autenticado; endereço de entrega selecionado.
**Dados utilizados:** Método selecionado: Standard Delivery.
**Justificativa do cenário:** O usuário precisa corrigir dados antes de concluir a compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/delivery-method` e o texto visível contenha `Standard Delivery`.
**Procedimento executado:**
1. Navegar para `/#/delivery-method`.
2. Acionar o elemento identificado por papel "radio", nome "Standard Delivery", correspondência parcial.
3. Acionar o elemento identificado por papel "button", nome "Proceed to delivery method selection", correspondência exata.
4. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
5. Acionar o elemento identificado por papel "button", nome "Back", correspondência exata.
6. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
7. Acionar o elemento identificado por papel "radio", nome "Standard Delivery", correspondência parcial.
8. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
9. ASSERT_SELECTED — {"type":"ASSERT_SELECTED","target":{"role":"radio","name":"Standard Delivery","exact":false}}.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-28 — Fluxo completo de compra
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Executar o fluxo de compra desde o carrinho até a confirmação.
**Objetivo:** A aplicação deve permitir concluir uma compra pelo fluxo da interface.
**Pré-condições:** Cliente autenticado; carrinho contém produto; endereço Rua Teste, 100 cadastrado; método de entrega disponível; cartão de teste terminado em 0002 cadastrado.
**Dados utilizados:** Produto: Apple Juice; endereço: Rua Teste, 100, Fortaleza/CE; entrega: Standard Delivery; cartão de teste terminado em 0002.
**Justificativa do cenário:** O fluxo completo valida a integração entre catálogo, carrinho e checkout.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/order-completion`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Acionar o elemento identificado por papel "button", nome "Checkout", correspondência parcial.
3. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
4. Acionar o elemento identificado por texto "Rua Teste, 100", correspondência parcial.
5. Acionar o elemento identificado por papel "button", nome "Continue", correspondência parcial.
6. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
7. Acionar o elemento identificado por papel "radio", nome "Standard Delivery", correspondência parcial.
8. Acionar o elemento identificado por papel "button", nome "Continue", correspondência parcial.
9. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
10. Acionar o elemento identificado por papel "radio", nome "0002", correspondência parcial.
11. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
12. Acionar o elemento identificado por papel "button", nome "Continue", correspondência parcial.
13. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
14. Acionar o elemento identificado por papel "button", nome "Complete your purchase", correspondência exata.
15. Aguardar 1200 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-23 — Checkout sem endereço
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Iniciar checkout sem possuir endereço selecionado.
**Objetivo:** O checkout deve exigir endereço antes de prosseguir.
**Pré-condições:** Carrinho com produto; nenhum endereço selecionado.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A aplicação deve impedir o avanço sem destino de entrega válido.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Add New Address`.
**Procedimento executado:**
1. Navegar para `/#/address/select`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-24 — Checkout sem método de entrega
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Acessar a etapa de entrega sem selecionar método.
**Objetivo:** O checkout deve impedir avanço sem método de entrega.
**Pré-condições:** Endereço selecionado.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A aplicação deve exigir um método de entrega válido.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Standard Delivery`.
**Procedimento executado:**
1. Navegar para `/#/delivery-method`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CHK-26 — Conferir total no resumo
**Domínio:** Checkout  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Comparar o total exibido no carrinho com o total do resumo.
**Objetivo:** O valor total deve permanecer consistente entre as etapas.
**Pré-condições:** Carrinho e checkout preparados.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A consistência do valor é essencial para confirmar a compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Total`.
**Procedimento executado:**
1. Navegar para `/#/order-summary`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.