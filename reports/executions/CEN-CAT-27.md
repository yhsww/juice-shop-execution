# Ficha de Cenário

**ID do cenário:** CEN-CAT-27
**Domínio:** CAT
**Nome do cenário:** Mural de fotos (Photo Wall)
**Ator:** Visitante não autenticado
**Fluxo:** Abrir o menu lateral e acessar Photo Wall.

## Pré-condição (estado inicial)

Catálogo disponível.

## Descrição do cenário

Visitante não autenticado executa o fluxo 'Abrir o menu lateral e acessar Photo Wall.'. A descrição corresponde ao cenário 'Mural de fotos (Photo Wall)' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/photo-wall Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Photo Wall 😼 #zatschi #whoneedsfourlegs Magn(et)ificent! | (© bkimminich) My rare collectors item! | [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] (© bkimminich) Welcome to the Bee Haven (/#/bee-haven)🐝 (© evmrox) Sorted the pieces, starting assembly process... | Building something literally bottom up... | Putting in the hardware... | Everything up and running! | I love going hiking here... | (© j0hNny) My old workplace... | (© E=ma²) Texto transitório capturado: Building something literally bottom up... | Putting in the hardware... | Everything up and running! | I love going hiking here... (© j0hNny) | My old workplace... (© E=ma²) Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder Photo Wall No results found No memories have been shared yet. | Photo Wall No results found No memories have been shared yet. | Photo Wall | No results found No memories have been shared yet. | No results found

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder Photo Wall No results found No memories have been shared yet.
- Photo Wall No results found No memories have been shared yet.
- Photo Wall
- No results found No memories have been shared yet.
- No results found
- No memories have been shared yet.
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Photo Wall No results found No memories have been shared yet.
- EN
- language EN
- account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
- 😼 #zatschi #whoneedsfourlegs Magn(et)ificent! (© bkimminich) My rare collectors item! [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] (© bkimminich) Welcome to the Bee Haven (/#/bee-haven)🐝 (© evmrox) Sorted the pieces, starting assembly process... Building something literally bottom up... Putting in the hardware... Everything up and running! I love going hiking here... (© j0hNny) My old workplace... (© E=ma²)
- Photo Wall 😼 #zatschi #whoneedsfourlegs Magn(et)ificent! (© bkimminich) My rare collectors item! [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] (© bkimminich) Welcome to the Bee Haven (/#/bee-haven)🐝 (© evmrox) Sorted the pieces, starting assembly process... Building something literally bottom up... Putting in the hardware... Everything up and running! I love going hiking here... (© j0hNny) My old workplace... (© E=ma²)
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Photo Wall 😼 #zatschi #whoneedsfourlegs Magn(et)ificent! (© bkimminich) My rare collectors item! [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] (© bkimminich) Welcome to the Bee Haven (/#/bee-haven)🐝 (© evmrox) Sorted the pieces, starting assembly process... Building something literally bottom up... Putting in the hardware... Everything up and running! I love going hiking here... (© j0hNny) My old workplace... (© E=ma²)
- 😼 #zatschi #whoneedsfourlegs
- Magn(et)ificent! (© bkimminich)
- My rare collectors item! [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] (© bkimminich)
- Welcome to the Bee Haven (/#/bee-haven)🐝 (© evmrox)
- Sorted the pieces, starting assembly process...
- Building something literally bottom up...

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/photo-wall

## Coerente com loja de sucos?

Parcial.

## Justificativa

Rede social de fotos não é função de venda de sucos; pode ser marketing.

## Descrição funcional do cenário

Visitante não autenticado executa o fluxo 'Abrir o menu lateral e acessar Photo Wall.'. A descrição corresponde ao cenário 'Mural de fotos (Photo Wall)' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/photo-wall | /#/photo-wall | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/photo-wall Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Photo Wall 😼 #zatschi #whoneedsfourlegs Magn(et)ificent! \| (© bkimminich) My rare collectors item! \| [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] (© bkimminich) Welcome to the Bee Haven (/#/bee-haven)🐝 (© evmrox) Sorted the pieces, starting assembly process... \| Building something literally bottom up... \| Putting in the hardware... \| Everything up and running! \| I love going hiking here... \| (© j0hNny) My old workplace... \| (© E=ma²) Texto transitório capturado: Building something literally bottom up... \| Putting in the hardware... \| Everything up and running! \| I love going hiking here... (© j0hNny) \| My old workplace... (© E=ma²) Mensagem transitória: menu OWASP Juice Shop search search close account_circle |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Photo Wall 😼 #zatschi #whoneedsfourlegs Magn(et)ificent! (© bkimminich) My rare collectors item! [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] (© bkimminich) Welcome to the Bee Haven (/#/bee-haven)🐝 (© evmrox) Sorted the pieces, starting assembly process... Building something literally bottom up... Putting in the hardware... Everything up and running! I love going hiking here... (© j0hNny) My old workplace... (© E=ma²) |
