# Relatório de Execução — Administração

**Projeto:** Juice Shop Execution  
**Branch:** `ambols-recovery-v2`  
**Cobertura:** 3 cenários do domínio  
**Resultado:** **3/3 aprovados**  

## 1. Objetivo

Este documento registra, de forma detalhada, os cenários automatizados do domínio **Administração**, preservando a definição funcional, pré-condições, dados, sequência de ações e critérios de aceite definidos no arquivo de cenários. O status informado corresponde à execução final consolidada do conjunto completo, na qual os **72 cenários foram aprovados**.

## 2. Resumo

| ID | Cenário | Ator | Status |
|---|---|---|---|
| CEN-ADM-01 | Acesso à área administrativa | Administrador | **PASS** |
| CEN-ADM-02 | Visualização de usuários cadastrados | Administrador | **PASS** |
| CEN-ADM-03 | Visualização e gestão de feedbacks | Administrador | **PASS** |

## 3. Detalhamento dos cenários

### CEN-ADM-01 — Acesso à área administrativa
**Domínio:** Administração  
**Ator:** Administrador  
**Status da execução final:** **PASS**  
**Descrição funcional:** Acessar a área de administração com uma conta administrativa válida.
**Objetivo:** A aplicação deve permitir acesso administrativo a usuário com perfil administrador.
**Pré-condições:** Juice Shop em execução; usuário administrador disponível.
**Dados utilizados:** E-mail: admin@juice-sh.op; senha: admin123.
**Justificativa do cenário:** A administração reúne funções restritas de gestão da loja.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/administration`.
**Procedimento executado:**
1. Navegar para `/#/login`.
2. Preencher o campo identificado por rótulo "Email" com o valor `admin@juice-sh.op`.
3. Preencher o campo identificado por rótulo "Password" com o valor `admin123`.
4. Acionar o elemento identificado por papel "button", nome "Login".
5. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
6. Navegar para `/#/administration`.
7. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-ADM-02 — Visualização de usuários cadastrados
**Domínio:** Administração  
**Ator:** Administrador  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a administração e verificar a área de usuários.
**Objetivo:** A área administrativa deve apresentar os usuários cadastrados.
**Pré-condições:** Administrador autenticado.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A gestão de usuários é uma função administrativa da loja.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Registered Users`.
**Procedimento executado:**
1. Navegar para `/#/administration`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-ADM-03 — Visualização e gestão de feedbacks
**Domínio:** Administração  
**Ator:** Administrador  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a administração e verificar a área de feedback dos clientes.
**Objetivo:** A área administrativa deve apresentar os feedbacks recebidos.
**Pré-condições:** Administrador autenticado.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O feedback integra a gestão operacional da loja.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Customer Feedback`.
**Procedimento executado:**
1. Navegar para `/#/administration`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.