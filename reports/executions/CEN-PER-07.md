# Ficha de Cenário

**ID do cenário:** CEN-PER-07
**Domínio:** PER
**Nome do cenário:** Alterar nome de usuário
**Ator:** Cliente autenticado
**Fluxo:** Abrir o perfil, definir um username e salvar.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir o perfil, definir um username e salvar.'. A descrição corresponde ao cenário 'Alterar nome de usuário' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

Durante a execução, foram observadas as seguintes mudanças na interface:
1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/profile Texto visível: arrow_back Back OWASP Juice Shop User Profile File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username Texto observado durante a ação: arrow_back Back OWASP Juice Shop User Profile File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username
2. Conteúdo/estrutura visível da página foi alterado. Texto observado durante a ação: arrow_back Back OWASP Juice Shop User Profile clienteambols File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username

## Mensagens exibidas ao usuário

Nenhuma mensagem transitória relevante capturada.

## Dados manipulados

Dados declarados no cenário: Username 'clienteambols'.
Passo 1: /profile
Passo 3: clienteambols

## Coerente com loja de sucos?

Sim.

## Justificativa

O CEN-IDT-07 atual só abre a tela de privacidade; não altera dado algum.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir o perfil, definir um username e salvar.'. A descrição corresponde ao cenário 'Alterar nome de usuário' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /profile | /profile | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/profile Texto visível: arrow_back Back OWASP Juice Shop User Profile File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username Texto observado durante a ação: arrow_back Back OWASP Juice Shop User Profile File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: arrow_back Back OWASP Juice Shop User Profile File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username |
| 3 | Preencher "Text field for the username" | clienteambols | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: arrow_back Back OWASP Juice Shop User Profile File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username |
| 4 | Clicar em "Button to save/set the username" |  | Conteúdo/estrutura visível da página foi alterado. Texto observado durante a ação: arrow_back Back OWASP Juice Shop User Profile clienteambols File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username |
| 5 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: arrow_back Back OWASP Juice Shop User Profile clienteambols File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username |
