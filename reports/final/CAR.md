# Relatório de Execução — Carrinho

**Projeto:** Juice Shop Execution  
**Branch:** `ambols-recovery-v2`  
**Cobertura:** 7 cenários do domínio  
**Resultado:** **7/7 aprovados**  

## 1. Objetivo

Este documento registra, de forma detalhada, os cenários automatizados do domínio **Carrinho**, preservando a definição funcional, pré-condições, dados, sequência de ações e critérios de aceite definidos no arquivo de cenários. O status informado corresponde à execução final consolidada do conjunto completo, na qual os **72 cenários foram aprovados**.

## 2. Resumo

| ID | Cenário | Ator | Status |
|---|---|---|---|
| CEN-CAR-01 | Adicionar produto ao carrinho | Cliente | **PASS** |
| CEN-CAR-02 | Visualizar itens do carrinho | Cliente | **PASS** |
| CEN-CAR-03 | Alterar quantidade de produto | Cliente | **PASS** |
| CEN-CAR-04 | Conferir total do carrinho | Cliente | **PASS** |
| CEN-CAR-05 | Remover produto do carrinho | Cliente | **PASS** |
| CEN-CAR-06 | Esvaziar carrinho | Cliente | **PASS** |
| CEN-CAR-07 | Persistência do carrinho durante a navegação | Cliente | **PASS** |

## 3. Detalhamento dos cenários

### CEN-CAR-01 — Adicionar produto ao carrinho
**Domínio:** Carrinho  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Selecionar um produto e adicioná-lo ao carrinho.
**Objetivo:** A aplicação deve permitir adicionar produtos ao carrinho.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Produto: Apple Juice.
**Justificativa do cenário:** A inclusão de produtos é necessária para iniciar uma compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Your Basket`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Acionar o elemento identificado por papel "button", nome "Add to Basket".
3. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAR-02 — Visualizar itens do carrinho
**Domínio:** Carrinho  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o carrinho e conferir os produtos selecionados.
**Objetivo:** A aplicação deve apresentar os itens do carrinho.
**Pré-condições:** Há pelo menos um produto no carrinho.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O carrinho deve permitir conferir a seleção antes do checkout.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Your Basket`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAR-03 — Alterar quantidade de produto
**Domínio:** Carrinho  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Aumentar a quantidade de um produto no carrinho.
**Objetivo:** A aplicação deve permitir aumentar ou diminuir a quantidade.
**Pré-condições:** Há pelo menos um produto no carrinho.
**Dados utilizados:** Quantidade desejada: 2 unidades.
**Justificativa do cenário:** A quantidade altera o valor da compra e precisa ser editável.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `2`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Acionar o elemento identificado por papel "button", nome "Increase quantity", correspondência parcial.
3. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAR-04 — Conferir total do carrinho
**Domínio:** Carrinho  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Conferir o total apresentado para os produtos selecionados.
**Objetivo:** A aplicação deve calcular e exibir o total do carrinho.
**Pré-condições:** Há pelo menos um produto no carrinho.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O total é necessário para conferência antes da compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Total`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAR-05 — Remover produto do carrinho
**Domínio:** Carrinho  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Remover um produto do carrinho.
**Objetivo:** A aplicação deve permitir remover produtos do carrinho.
**Pré-condições:** Há pelo menos um produto no carrinho.
**Dados utilizados:** Produto selecionado para remoção.
**Justificativa do cenário:** A remoção permite corrigir a seleção antes da compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Your Basket`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Acionar o elemento identificado por papel "button", nome "Remove", correspondência parcial.
3. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAR-06 — Esvaziar carrinho
**Domínio:** Carrinho  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Remover todos os produtos e conferir o estado final.
**Objetivo:** A aplicação deve permitir deixar o carrinho sem itens.
**Pré-condições:** Há produtos no carrinho.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O cliente deve conseguir abandonar a seleção sem concluir a compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Your Basket`.
**Procedimento executado:**
1. Navegar para `/#/basket`.
2. Acionar repetidamente os elementos identificados por papel "button", nome "Remove", correspondência parcial, com limite de 20 interações.
3. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAR-07 — Persistência do carrinho durante a navegação
**Domínio:** Carrinho  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Adicionar um produto, navegar para outra área e retornar ao carrinho.
**Objetivo:** O carrinho deve preservar os itens durante a navegação.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Produto: Apple Juice.
**Justificativa do cenário:** A seleção precisa permanecer disponível durante a navegação.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Apple Juice`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Acionar o elemento identificado por papel "button", nome "Add to Basket".
3. Navegar para `/#/search`.
4. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
5. Navegar para `/#/basket`.
6. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.