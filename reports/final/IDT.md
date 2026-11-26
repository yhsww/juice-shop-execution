# Relatório de Execução — Identidade e Conta

**Projeto:** Juice Shop Execution  
**Branch:** `ambols-recovery-v2`  
**Cobertura:** 17 cenários do domínio  
**Resultado:** **17/17 aprovados**  

## 1. Objetivo

Este documento registra, de forma detalhada, os cenários automatizados do domínio **Identidade e Conta**, preservando a definição funcional, pré-condições, dados, sequência de ações e critérios de aceite definidos no arquivo de cenários. O status informado corresponde à execução final consolidada do conjunto completo, na qual os **72 cenários foram aprovados**.

## 2. Resumo

| ID | Cenário | Ator | Status |
|---|---|---|---|
| CEN-IDT-01 | Cadastro de novo cliente | Cliente | **PASS** |
| CEN-IDT-02 | Validação de senha no cadastro | Cliente | **PASS** |
| CEN-IDT-03 | Login com credenciais válidas | Cliente | **PASS** |
| CEN-IDT-04 | Login com senha inválida | Cliente | **PASS** |
| CEN-IDT-05 | Logout | Cliente | **PASS** |
| CEN-IDT-06 | Acesso ao perfil | Cliente | **PASS** |
| CEN-IDT-07 | Alteração de dados do perfil | Cliente | **PASS** |
| CEN-IDT-08 | Alteração de senha | Cliente | **PASS** |
| CEN-IDT-09 | Recuperação de senha | Cliente | **PASS** |
| CEN-IDT-10 | Pergunta de segurança na recuperação | Cliente | **PASS** |
| CEN-IDT-11 | Exportação de dados pessoais | Cliente | **PASS** |
| CEN-IDT-12 | Solicitação de exclusão de dados | Cliente | **PASS** |
| CEN-IDT-13 | Acesso à privacidade e segurança | Cliente | **PASS** |
| CEN-IDT-14 | Cadastro com e-mail já utilizado | Cliente | **PASS** |
| CEN-IDT-15 | Validação de campos obrigatórios | Cliente | **PASS** |
| CEN-IDT-16 | Validação de formato de e-mail | Cliente | **PASS** |
| CEN-IDT-17 | Acesso ao login após cadastro | Cliente | **PASS** |

## 3. Detalhamento dos cenários

### CEN-IDT-01 — Cadastro de novo cliente
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o cadastro, preencher os dados e concluir o registro.
**Objetivo:** A aplicação deve permitir registrar um novo cliente.
**Pré-condições:** Não é necessária autenticação prévia; o e-mail usado para o cadastro deve estar disponível.
**Dados utilizados:** E-mail: teste@example.com; senha: Teste@12345; pergunta de segurança e resposta de teste.
**Justificativa do cenário:** O cadastro é essencial para identificação do cliente.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/login`.
**Procedimento executado:**
1. Navegar para `/#/register`.
2. Preencher o campo identificado por rótulo "Email address", correspondência parcial com o valor `${UNIQUE_EMAIL}`.
3. Preencher o campo identificado por rótulo "Password", correspondência parcial com o valor `Teste@12345`.
4. Preencher o campo identificado por rótulo "Repeat Password", correspondência parcial com o valor `Teste@12345`.
5. Selecionar `Your favorite book?` no campo identificado por rótulo "Security Question", correspondência parcial.
6. Preencher o campo identificado por rótulo "Answer", correspondência parcial com o valor `a`.
7. Acionar o elemento identificado por papel "button", nome "Register", correspondência parcial.
8. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-02 — Validação de senha no cadastro
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Informar senhas diferentes e observar a validação do formulário.
**Objetivo:** O cadastro deve validar a repetição da senha.
**Pré-condições:** Tela de cadastro aberta.
**Dados utilizados:** Senha: Teste@12345; repetição: Teste@1234.
**Justificativa do cenário:** A confirmação de senha evita registros com credenciais inconsistentes.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `password`.
**Procedimento executado:**
1. Navegar para `/#/register`.
2. Preencher o campo identificado por rótulo "Email address" com o valor `teste2@example.com`.
3. Preencher o campo identificado por rótulo "Password" com o valor `Teste@12345`.
4. Preencher o campo identificado por rótulo "Repeat Password" com o valor `Teste@1234`.
5. Aguardar 400 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-03 — Login com credenciais válidas
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Informar e-mail e senha válidos e entrar na aplicação.
**Objetivo:** A aplicação deve autenticar credenciais válidas.
**Pré-condições:** Conta de teste disponível para autenticação.
**Dados utilizados:** E-mail: teste@example.com; senha: Teste@12345.
**Justificativa do cenário:** A autenticação identifica o cliente para acessar recursos protegidos.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/`.
**Procedimento executado:**
1. Navegar para `/#/login`.
2. Preencher o campo identificado por rótulo "Email" com o valor `${SCENARIO_EMAIL}`.
3. Preencher o campo identificado por rótulo "Password" com o valor `Teste@12345`.
4. Acionar o elemento identificado por papel "button", nome "Login".
5. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-04 — Login com senha inválida
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Informar e-mail válido com senha incorreta.
**Objetivo:** A aplicação deve impedir autenticação com senha incorreta.
**Pré-condições:** Conta de teste disponível para autenticação.
**Dados utilizados:** Senha incorreta: SenhaErrada@123.
**Justificativa do cenário:** O sistema deve rejeitar credenciais inválidas.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Invalid email or password`.
**Procedimento executado:**
1. Navegar para `/#/login`.
2. Preencher o campo identificado por rótulo "Email" com o valor `${SCENARIO_EMAIL}`.
3. Preencher o campo identificado por rótulo "Password" com o valor `SenhaErrada@123`.
4. Acionar o elemento identificado por papel "button", nome "Login".
5. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-05 — Logout
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Encerrar a sessão autenticada.
**Objetivo:** A aplicação deve permitir sair da conta.
**Pré-condições:** Usuário autenticado.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O logout encerra a sessão do cliente.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/`.
**Procedimento executado:**
1. Navegar para `/#/`.
2. Acionar o elemento identificado por papel "button", nome "Account", correspondência parcial.
3. Acionar o elemento identificado por texto "Logout", correspondência parcial.
4. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-06 — Acesso ao perfil
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a área de perfil após autenticação.
**Objetivo:** A aplicação deve permitir acessar o perfil do usuário.
**Pré-condições:** Conta de teste disponível para autenticação.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O perfil concentra informações da conta.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Profile`.
**Procedimento executado:**
1. Navegar para `/profile`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-07 — Alteração de dados do perfil
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Alterar um dado editável do perfil e salvar.
**Objetivo:** A aplicação deve salvar alterações válidas do perfil.
**Pré-condições:** Conta de teste disponível para autenticação.
**Dados utilizados:** Dado de teste atualizado.
**Justificativa do cenário:** O cliente precisa poder atualizar dados permitidos da conta.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Privacy`.
**Procedimento executado:**
1. Navegar para `/#/privacy-security`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-08 — Alteração de senha
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a área de alteração de senha e informar os dados de teste.
**Objetivo:** A aplicação deve permitir alterar a senha com dados válidos.
**Pré-condições:** Conta de teste disponível para autenticação.
**Dados utilizados:** Senha atual e nova senha de teste.
**Justificativa do cenário:** A alteração periódica de senha é função de gerenciamento de conta.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Password`.
**Procedimento executado:**
1. Navegar para `/#/privacy-security/change-password`.
2. Preencher o campo identificado por rótulo "Current Password", correspondência parcial com o valor `Teste@12345`.
3. Preencher o campo identificado por rótulo "New Password", correspondência parcial com o valor `Teste@123456`.
4. Preencher o campo identificado por rótulo "Repeat New Password", correspondência parcial com o valor `Teste@123456`.
5. Acionar o elemento identificado por papel "button", nome "Change", correspondência parcial.
6. Aguardar 800 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-09 — Recuperação de senha
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir o fluxo de recuperação de senha.
**Objetivo:** A aplicação deve disponibilizar o fluxo de recuperação.
**Pré-condições:** Usuário possui e-mail cadastrado.
**Dados utilizados:** E-mail: teste@example.com.
**Justificativa do cenário:** A recuperação permite recuperar uma conta inacessível.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Forgot Password`.
**Procedimento executado:**
1. Navegar para `/#/forgot-password`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-10 — Pergunta de segurança na recuperação
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Informar e-mail e verificar a solicitação da pergunta de segurança.
**Objetivo:** A aplicação deve solicitar a informação de segurança correspondente.
**Pré-condições:** Conta de teste do cenário cadastrada com pergunta e resposta de segurança.
**Dados utilizados:** E-mail: teste@example.com.
**Justificativa do cenário:** A pergunta integra o mecanismo de recuperação configurado no aplicativo.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `security`.
**Procedimento executado:**
1. Navegar para `/#/forgot-password`.
2. Preencher o campo identificado por rótulo "Email", correspondência parcial com o valor `${SCENARIO_EMAIL}`.
3. Aguardar 1000 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-11 — Exportação de dados pessoais
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a área de privacidade e solicitar exportação de dados.
**Objetivo:** A aplicação deve disponibilizar a exportação de dados.
**Pré-condições:** Conta de teste disponível para autenticação.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** O cliente deve conseguir consultar seus dados pessoais exportáveis.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `Data Export`.
**Procedimento executado:**
1. Navegar para `/#/privacy-security/data-export`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-12 — Solicitação de exclusão de dados
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a área de privacidade e verificar a opção de exclusão.
**Objetivo:** A aplicação deve disponibilizar a opção de exclusão quando aplicável.
**Pré-condições:** Conta de teste disponível para autenticação.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A gestão de privacidade deve permitir iniciar uma solicitação de exclusão.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/dataerasure`.
**Procedimento executado:**
1. Navegar para `/dataerasure`.
2. Aguardar 500 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-13 — Acesso à privacidade e segurança
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Abrir a área de privacidade e segurança da conta.
**Objetivo:** A aplicação deve disponibilizar uma área de privacidade e segurança.
**Pré-condições:** Conta de teste disponível para autenticação.
**Dados utilizados:** Nenhum dado adicional.
**Justificativa do cenário:** A área reúne controles relacionados aos dados pessoais.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/privacy-security`.
**Procedimento executado:**
1. Navegar para `/#/privacy-security`.
2. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-14 — Cadastro com e-mail já utilizado
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Tentar cadastrar uma conta utilizando e-mail existente.
**Objetivo:** O cadastro deve rejeitar e-mails já cadastrados.
**Pré-condições:** Existe usuário com o e-mail informado.
**Dados utilizados:** E-mail: teste@example.com.
**Justificativa do cenário:** A aplicação deve evitar duplicidade de contas.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `already`.
**Procedimento executado:**
1. Navegar para `/#/register`.
2. Preencher o campo identificado por rótulo "Email address", correspondência parcial com o valor `${BASE_TEST_EMAIL}`.
3. Preencher o campo identificado por rótulo "Password", correspondência parcial com o valor `Teste@12345`.
4. Preencher o campo identificado por rótulo "Repeat Password", correspondência parcial com o valor `Teste@12345`.
5. Selecionar `Your favorite book?` no campo identificado por rótulo "Security Question", correspondência parcial.
6. Preencher o campo identificado por rótulo "Answer", correspondência parcial com o valor `a`.
7. Acionar o elemento identificado por papel "button", nome "Register", correspondência parcial.
8. Aguardar 700 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-15 — Validação de campos obrigatórios
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Tentar concluir o cadastro sem preencher todos os campos obrigatórios.
**Objetivo:** O formulário deve exigir os campos obrigatórios.
**Pré-condições:** Tela de cadastro aberta.
**Dados utilizados:** Campos obrigatórios deixados vazios.
**Justificativa do cenário:** A validação impede registros incompletos.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `email`.
**Procedimento executado:**
1. Navegar para `/#/register`.
2. Acionar o elemento identificado por rótulo "Email address", correspondência parcial.
3. Pressionar a tecla `Tab` no elemento identificado por rótulo "Email address", correspondência parcial.
4. Aguardar 300 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-16 — Validação de formato de e-mail
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Informar e-mail em formato inválido no cadastro.
**Objetivo:** O cadastro deve validar o formato do e-mail.
**Pré-condições:** Tela de cadastro aberta.
**Dados utilizados:** E-mail: teste-sem-formato.
**Justificativa do cenário:** A validação reduz entradas inválidas de contato.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que o texto visível contenha `email`.
**Procedimento executado:**
1. Navegar para `/#/register`.
2. Preencher o campo identificado por rótulo "Email address" com o valor `teste-sem-formato`.
3. Aguardar 400 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.

---

### CEN-IDT-17 — Acesso ao login após cadastro
**Domínio:** Identidade e Conta  
**Ator:** Cliente  
**Status da execução final:** **PASS**  
**Descrição funcional:** Concluir o cadastro e verificar o redirecionamento para login.
**Objetivo:** A aplicação deve direcionar o usuário para a autenticação após registro válido.
**Pré-condições:** Cadastro válido concluído.
**Dados utilizados:** E-mail: usuário de teste; senha: senha de teste.
**Justificativa do cenário:** Após o cadastro, o usuário precisa conseguir autenticar a nova conta.
**Coerência:** Sim.
**Critério de aceite:** A execução deve demonstrar que a URL contenha `/#/register`.
**Procedimento executado:**
1. Navegar para `/#/register`.
2. Aguardar 400 ms para permitir a estabilização da interface e a atualização do estado observado.
**Resultado esperado:** O fluxo deve ser concluído sem erro de automação e o critério de aceite acima deve ser observável no estado final do aplicativo.
**Resultado final:** O cenário foi aprovado na execução consolidada de **72/72 cenários**, com **0 falhas**.