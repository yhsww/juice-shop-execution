# Ficha de Cenário

**ID do cenário:** CEN-CHK-44
**Domínio:** CHK
**Nome do cenário:** Assinatura 'Deluxe Membership'
**Ator:** Cliente autenticado
**Fluxo:** Abrir a página de assinatura Deluxe e registrar benefícios e preço, sem pagar.

## Pré-condição (estado inicial)

Cliente autenticado.

## Descrição do cenário

Cliente autenticado executa o fluxo 'Abrir a página de assinatura Deluxe e registrar benefícios e preço, sem pagar.'. A descrição corresponde ao cenário 'Assinatura 'Deluxe Membership'' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Resultado observado (mudança de estado)

URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/deluxe-membership Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. | Check out what is included with your membership. | 49¤ Become a member Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers. | Free Fast Delivery Get unlimited free Fast Delivery for all products in the shop. | Unlimited Purchase Enjoy unrestricted purchase of your favourite products. Texto transitório capturado: Deluxe Membership | 49¤ | Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 49¤ Become a member | Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 49¤ Become a member Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers. Free Fast Delivery Get unlimited free Fast Delivery for all products in the shop. Unlimited Purchase Enjoy unrestricted purchase of your favourite products. | menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 49¤ Become a member Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers. Free Fast Delivery

## Mensagens exibidas ao usuário

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 0¤ Become a member Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers. Free Fast Delivery Get unlimited free Fast Delivery for all products in the shop. Unlimited Purchase Enjoy unrestricted purchase of your favourite products.
- Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 0¤ Become a member Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers. Free Fast Delivery Get unlimited free Fast Delivery for all products in the shop. Unlimited Purchase Enjoy unrestricted purchase of your favourite products.
- Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership.
- Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 0¤ Become a member
- 0¤
- Become a member
- Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers. Free Fast Delivery Get unlimited free Fast Delivery for all products in the shop. Unlimited Purchase Enjoy unrestricted purchase of your favourite products.
- Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers.
- Free Fast Delivery Get unlimited free Fast Delivery for all products in the shop.
- Unlimited Purchase Enjoy unrestricted purchase of your favourite products.
- Deals and Offers
- As a deluxe member, you get access to exclusive deals and irresistible offers.
- Free Fast Delivery
- Get unlimited free Fast Delivery for all products in the shop.
- Unlimited Purchase
- Enjoy unrestricted purchase of your favourite products.
- Deluxe Membership
- 49¤
- Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 49¤ Become a member
- Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 49¤ Become a member Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers. Free Fast Delivery Get unlimited free Fast Delivery for all products in the shop. Unlimited Purchase Enjoy unrestricted purchase of your favourite products.

## Dados manipulados

Dados declarados no cenário: —
Passo 1: /#/deluxe-membership

## Coerente com loja de sucos?

Parcial.

## Justificativa

Clube de vantagens é plausível, mas não aparece no fluxo principal de compra.

## Descrição funcional do cenário

Cliente autenticado executa o fluxo 'Abrir a página de assinatura Deluxe e registrar benefícios e preço, sem pagar.'. A descrição corresponde ao cenário 'Assinatura 'Deluxe Membership'' e deve ser interpretada em conjunto com as evidências registradas nos passos.

## Passos Executados

| # | Ação do usuário | Dados informados | Resposta da interface |
|---|---|---|---|
| 1 | Abrir a rota /#/deluxe-membership | /#/deluxe-membership | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/deluxe-membership Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. \| Check out what is included with your membership. \| 49¤ Become a member Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers. \| Free Fast Delivery Get unlimited free Fast Delivery for all products in the shop. \| Unlimited Purchase Enjoy unrestricted purchase of your favourite products. Texto transitório capturado: Deluxe Membership \| 49¤ \| Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 49¤ Become a member \| Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP  |
| 2 | Aguardar a atualização da interface |  | Nenhuma mudança visual relevante detectada. Texto observado durante a ação: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Deluxe Membership Enjoy amazing benefits as a deluxe customer of OWASP Juice Shop. Check out what is included with your membership. 49¤ Become a member Deals and Offers As a deluxe member, you get access to exclusive deals and irresistible offers. Free Fast Delivery Get unlimited free Fast Delivery for all products in the shop. Unlimited Purchase Enjoy unrestricted purchase of your favourite products. |
