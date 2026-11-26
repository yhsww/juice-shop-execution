# Relatório de Execução — Catálogo

**Projeto:** Juice Shop Execution  
**Branch:** `ambols-recovery-v2`  
**Cobertura:** 17 cenários do domínio  
**Resultado:** **17/17 aprovados**  

## 1. Objetivo

Este documento registra, de forma detalhada, os cenários automatizados do domínio **Catálogo**, preservando a definição funcional, pré-condições, dados, sequência de ações e critérios de aceite definidos no arquivo de cenários. O status informado corresponde à execução final consolidada do conjunto completo, na qual os **72 cenários foram aprovados**.

## 2. Resumo

| ID | Cenário | Ator | Status |
|---|---|---|---|
| CEN-CAT-01 | Acesso ao catálogo | Cliente | **PASS** |
| CEN-CAT-02 | Abertura de produto | Cliente | **PASS** |
| CEN-CAT-03 | Pesquisa por nome | Cliente | **PASS** |
| CEN-CAT-04 | Pesquisa por termo parcial | Cliente | **PASS** |
| CEN-CAT-05 | Pesquisa sem resultado | Cliente | **PASS** |
| CEN-CAT-06 | Pesquisa com caracteres acentuados | Cliente | **PASS** |
| CEN-CAT-07 | Pesquisa com caracteres especiais | Cliente | **PASS** |
| CEN-CAT-08 | Pesquisa vazia | Cliente | **PASS** |
| CEN-CAT-09 | Navegação do catálogo | Cliente | **PASS** |
| CEN-CAT-10 | Navegação entre páginas do catálogo | Cliente | **PASS** |
| CEN-CAT-11 | Visualização de preço do produto | Cliente | **PASS** |
| CEN-CAT-12 | Visualização de avaliação do produto | Cliente | **PASS** |
| CEN-CAT-13 | Pesquisa com combinação de acentos e caracteres especiais | Cliente | **PASS** |
| CEN-CAT-14 | Abertura do carrinho a partir do catálogo | Cliente | **PASS** |
| CEN-CAT-15 | Navegação para login pelo catálogo | Cliente | **PASS** |
| CEN-CAT-16 | Acesso à política de privacidade | Cliente | **PASS** |
| CEN-CAT-17 | Acesso ao score board | Cliente | **PASS** |

## 3. Detalhamento dos cenários

### CEN-CAT-01 — Acesso ao catálogo
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Acessar a página inicial e verificar a disponibilidade do catálogo.
**Objetivo:** A aplicação deve apresentar produtos navegáveis.
**Pré-condições:** Juice Shop em execução.
**Dados utilizados:** Nenhum dado de entrada.
**Justificativa do cenário:** O catálogo é o ponto central de navegação da loja.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Apple`, `Juice`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-02 — Abertura de produto
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Selecionar um produto e abrir sua visualização.
**Objetivo:** A aplicação deve permitir abrir um produto.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Produto: Apple Juice.
**Justificativa do cenário:** A visualização do produto permite consultar detalhes antes da compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Acionar o elemento identificado por papel "link", nome "Apple Juice".
3. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-03 — Pesquisa por nome
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Pesquisar um produto pelo nome.
**Objetivo:** A aplicação deve retornar produtos compatíveis com a pesquisa.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Termo: Apple.
**Justificativa do cenário:** A busca facilita a localização de produtos.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Apple Juice`.
**Procedimento executado:**
1. Navegar para `/#/search`.
2. Preencher o campo identificado por rótulo "Search", correspondência parcial com o valor `Apple`.
3. Pressionar a tecla `Enter` no elemento identificado por rótulo "Search", correspondência parcial.
4. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-04 — Pesquisa por termo parcial
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Pesquisar utilizando apenas parte do nome.
**Objetivo:** A aplicação deve aceitar termos parciais.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Termo: Appl.
**Justificativa do cenário:** A pesquisa parcial amplia a facilidade de localização.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Apple Juice`.
**Procedimento executado:**
1. Navegar para `/#/search`.
2. Preencher o campo identificado por rótulo "Search", correspondência parcial com o valor `Appl`.
3. Pressionar a tecla `Enter` no elemento identificado por rótulo "Search", correspondência parcial.
4. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-05 — Pesquisa sem resultado
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Pesquisar por termo sem correspondência.
**Objetivo:** A aplicação deve informar ausência de produtos correspondentes.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Termo: ProdutoInexistenteXYZ.
**Justificativa do cenário:** O usuário precisa receber um estado claro quando não houver resultado.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `No results found`.
**Procedimento executado:**
1. Navegar para `/#/search`.
2. Preencher o campo identificado por rótulo "Search", correspondência parcial com o valor `ProdutoInexistenteXYZ`.
3. Pressionar a tecla `Enter` no elemento identificado por rótulo "Search", correspondência parcial.
4. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-06 — Pesquisa com caracteres acentuados
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Pesquisar utilizando caracteres acentuados.
**Objetivo:** A pesquisa não deve quebrar com caracteres acentuados.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Termo: Limão.
**Justificativa do cenário:** A interface deve aceitar entradas textuais comuns em português.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/search`.
**Procedimento executado:**
1. Navegar para `/#/search`.
2. Preencher o campo identificado por rótulo "Search", correspondência parcial com o valor `Limão`.
3. Pressionar a tecla `Enter` no elemento identificado por rótulo "Search", correspondência parcial.
4. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-07 — Pesquisa com caracteres especiais
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Pesquisar utilizando caracteres especiais sem interromper a interface.
**Objetivo:** A pesquisa deve tratar caracteres especiais sem erro de interface.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Termo: Açaí / Limão.
**Justificativa do cenário:** Entradas especiais são uma variação real de uso da pesquisa.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/search`.
**Procedimento executado:**
1. Navegar para `/#/search`.
2. Preencher o campo identificado por rótulo "Search", correspondência parcial com o valor `Açaí / Limão`.
3. Pressionar a tecla `Enter` no elemento identificado por rótulo "Search", correspondência parcial.
4. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-08 — Pesquisa vazia
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a pesquisa e confirmar o comportamento sem termo informado.
**Objetivo:** A aplicação deve manter um estado válido quando a pesquisa estiver vazia.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Termo vazio.
**Justificativa do cenário:** A busca vazia deve manter a navegação utilizável.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/search`.
**Procedimento executado:**
1. Navegar para `/#/search`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-09 — Navegação do catálogo
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Avançar na paginação da listagem de produtos.
**Objetivo:** A aplicação deve permitir avançar na listagem paginada.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A paginação permite explorar o catálogo quando há mais produtos do que cabem na página.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Apple Juice`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Acionar o elemento identificado por papel "button", nome "Next", correspondência parcial.
3. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-10 — Navegação entre páginas do catálogo
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Avançar e retornar entre páginas da listagem.
**Objetivo:** A aplicação deve permitir mudar de página quando a paginação estiver disponível.
**Pré-condições:** Catálogo com quantidade suficiente para paginação.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** Paginação permite navegar por catálogos maiores.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Apple Juice`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Acionar o elemento identificado por papel "button", nome "Next", correspondência parcial.
3. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-11 — Visualização de preço do produto
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Conferir o preço exibido para um produto.
**Objetivo:** A aplicação deve exibir o preço do produto.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Produto: Apple Juice.
**Justificativa do cenário:** O preço é informação essencial para a decisão de compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Apple Juice`, `¤`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-12 — Visualização de avaliação do produto
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir um produto e verificar sua área de avaliações.
**Objetivo:** A aplicação deve apresentar avaliações quando existentes.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Produto: Apple Juice.
**Justificativa do cenário:** As avaliações fazem parte da informação disponível ao cliente.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Reviews`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Acionar o elemento identificado por papel "link", nome "Apple Juice".
3. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-13 — Pesquisa com combinação de acentos e caracteres especiais
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Pesquisar por termo contendo acento, barra e caracteres especiais.
**Objetivo:** A aplicação deve permanecer utilizável diante de caracteres especiais.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Termo: Limão / Açaí.
**Justificativa do cenário:** O fluxo amplia a verificação de robustez da entrada de pesquisa.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/search`.
**Procedimento executado:**
1. Navegar para `/#/search`.
2. Preencher o campo identificado por rótulo "Search", correspondência parcial com o valor `Limão / Açaí`.
3. Pressionar a tecla `Enter` no elemento identificado por rótulo "Search", correspondência parcial.
4. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-14 — Abertura do carrinho a partir do catálogo
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Adicionar um produto e acessar o carrinho pela navegação da loja.
**Objetivo:** A aplicação deve permitir acessar o carrinho após selecionar produtos.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Produto: Apple Juice.
**Justificativa do cenário:** O catálogo precisa conectar-se ao fluxo de compra.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/basket`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Acionar o elemento identificado por papel "button", nome "Add to Basket".
3. Acionar o elemento identificado por papel "button", nome "Your Basket".
4. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-15 — Navegação para login pelo catálogo
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Acessar a área de login a partir da navegação da loja.
**Objetivo:** A aplicação deve disponibilizar acesso à área de login.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O cliente precisa conseguir iniciar autenticação sem abandonar a loja.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/login`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Acionar o elemento identificado por papel "button", nome "Account", correspondência parcial.
3. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
4. Acionar o elemento identificado por papel "menuitem", nome "Login", correspondência parcial.
5. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-16 — Acesso à política de privacidade
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a política de privacidade pela interface da loja.
**Objetivo:** A aplicação deve permitir consultar a política de privacidade.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A política é uma informação institucional acessível ao cliente.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Privacy Policy`.
**Procedimento executado:**
1. Navegar para `/#/privacy-security/privacy-policy`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-CAT-17 — Acesso ao score board
**Domínio:** Catálogo  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o Score Board e verificar a listagem de desafios.
**Objetivo:** A aplicação deve apresentar o Score Board quando acessado pela navegação.
**Pré-condições:** Catálogo disponível.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O Score Board integra a interface do Juice Shop e é acessível pela aplicação.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Score Board`.
**Procedimento executado:**
1. Navegar para `/#/score-board`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.