# Ficha de Cenário

**ID do cenário:** CEN-PER-02
**Domínio:** PER
**Nome do cenário:** Acesso aos endereços salvos
**Ator:** Cliente autenticado
**Fluxo:** Abrir a área de endereços salvos e verificar os endereços disponíveis.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir a área de endereços salvos e verificar os endereços disponíveis.'. A descrição corresponde ao cenário 'Acesso aos endereços salvos' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/saved Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address Texto transitório capturado: My saved addresses addAdd New Address | My saved addresses | addAdd New Address | add | Add New Address Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! | 0 | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address | This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address | My saved addresses addAdd New Address

## Mensagens exibidas ao usuário

- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it!
- 0
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address
- My saved addresses addAdd New Address
- My saved addresses
- addAdd New Address
- add
- Add New Address

## Dados manipulados

Dados declarados no cenário: Nenhum dado pessoal real.
Passo 1: /#/address/saved

## Coerente com loja de sucos?

Sim.

## Justificativa

O cliente precisa consultar os endereços utilizados para entrega.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir a área de endereços salvos e verificar os endereços disponíveis.'. A descrição corresponde ao cenário 'Acesso aos endereços salvos' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a área de endereços salvos | /#/address/saved | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/saved Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address Texto transitório capturado: My saved addresses addAdd New Address \| My saved addresses \| addAdd New Address \| add \| Add New Address Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! \| 0 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New  |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! \| 0 |
