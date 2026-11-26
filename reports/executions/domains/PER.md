# Relatório do domínio PER

**Cenários executados:** 6
**Cenários aprovados:** 6
**Status do conjunto:** PASSED

## Cenários

| ID | Cenário | Status | Comportamento observado |
|---|---|---|---|
| CEN-PER-01 | Visualização dos dados da conta | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/profile Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping Texto transitório capturado: 1 – 16 of 46 \| 16 \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circ |
| CEN-PER-02 | Acesso aos endereços salvos | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/saved Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address Texto transitório capturado: My saved addresses addAdd New Address \| My saved addresses \| addAdd New Address \| add \| Add New Address Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address \| My saved addresses addAdd New Address \| My saved addresses \| addAdd New Address |
| CEN-PER-03 | Acesso às opções de pagamento | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/saved-payment-methods Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Texto transitório capturado: My Payment Options Add new card Add a credit or debit card \| My Payment Options \| Add new card \| Add new card Add a credit or debit card \| Add a credit or debit card Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card \| My Payment  |
| CEN-PER-04 | Acesso à privacidade e segurança | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN |
| CEN-PER-05 | Acesso à alteração de senha | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. \| 0/40 Repeat New Password 0/20 Change Texto transitório capturado: New Password \| Repeat New Password \| Password must be 5-40 characters long. 0/40 \| 0/20 \| Password must be 5-40 characters long. Mensagem transitória: This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ |
| CEN-PER-06 | Visualização do histórico de pedidos | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. Texto transitório capturado: Order History No results found You have not placed any orders yet. \| Order History \| No results found You have not placed any orders yet. \| No results found \| You have not placed any orders yet. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. \| Order History No results fou |

## Mensagens observadas

- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Items per page: 15 0 of 0
- All Products Items per page: 15 0 of 0
- All Products
- Items per page: 15 0 of 0
- Items per page: 15
- 0 of 0
- Items per page:
- 15
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Items per page: 15 1 – 15 of 46
- Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket
- All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Items per page: 15 1 – 15 of 46
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket Fruit Press 89.99¤ add_shopping_cart Add to Basket Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Green Smoothie 1.99¤ add_shopping_cart Add to Basket Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket Items per page: 15 1 – 15 of 46
- Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket
- Apple Pomace 0.89¤ add_shopping_cart Add to Basket
- Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket
- Basil Smoothie 2.99¤ add_shopping_cart Add to Basket
- Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket
- Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket
- Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address
- My saved addresses addAdd New Address
- My saved addresses
- addAdd New Address
- add
- Add New Address
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card
- My Payment Options Add new card Add a credit or debit card
- My Payment Options
- Add new card
- Add new card Add a credit or debit card
- Add a credit or debit card
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN
- Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket
- Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket
- Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket
- Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket
- Fruit Press 89.99¤ add_shopping_cart Add to Basket
- Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket
- Green Smoothie 1.99¤ add_shopping_cart Add to Basket
- Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket
- Apple Juice (1000ml)
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet.
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet.
- Order History No results found You have not placed any orders yet.
- Order History
- No results found You have not placed any orders yet.
- No results found
- You have not placed any orders yet.

## Rastreabilidade

Cada descrição acima é derivada dos passos e evidências da execução do respectivo cenário; nenhum comportamento é inferido a partir de END, COMP ou REQ.
