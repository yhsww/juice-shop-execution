# Relatório do domínio PER

**Cenários executados:** 16
**Cenários aprovados:** 16
**Status do conjunto:** PASSED

## Cenários

| ID | Cenário | Status | Comportamento observado |
|---|---|---|---|
| CEN-PER-01 | Visualização dos dados da conta | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/profile Texto transitório capturado: 1 – 16 of 46 \| 16 \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopping_cart Add to Basket Bragă (500ml) 2.49¤ add_shopping_cart Add to Basket Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket Elderflower Cordial (500ml) 3.29¤ add_shopping_car |
| CEN-PER-02 | Acesso aos endereços salvos | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/saved Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address Texto transitório capturado: My saved addresses addAdd New Address \| My saved addresses \| addAdd New Address \| add \| Add New Address Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My saved addresses addAdd New Address \| My saved addresses addAdd New Address \| My saved addresses \| addAdd New Address |
| CEN-PER-03 | Acesso às opções de pagamento | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/saved-payment-methods Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Texto transitório capturado: My Payment Options Add new card Add a credit or debit card \| My Payment Options \| Add new card \| Add new card Add a credit or debit card \| Add a credit or debit card Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card \| My Payment Options Add new card Add a credit or debit card \| My Payment  |
| CEN-PER-04 | Acesso à privacidade e segurança | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN |
| CEN-PER-05 | Acesso à alteração de senha | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/privacy-security/change-password Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. \| 0/40 Repeat New Password 0/20 Change Texto transitório capturado: New Password \| Repeat New Password \| Password must be 5-40 characters long. 0/40 \| 0/20 \| Password must be 5-40 characters long. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password |
| CEN-PER-06 | Visualização do histórico de pedidos | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/order-history Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. Texto transitório capturado: Order History No results found You have not placed any orders yet. \| Order History \| No results found You have not placed any orders yet. \| No results found \| You have not placed any orders yet. Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. \| This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet. \| Order History No results fou |
| CEN-PER-07 | Alterar nome de usuário | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/profile Texto visível: arrow_back Back OWASP Juice Shop User Profile File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username Texto observado durante a ação: arrow_back Back OWASP Juice Shop User Profile File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username 2. Conteúdo/estrutura visível da página foi alterado. Texto observado durante a ação: arrow_back Back OWASP Juice Shop User Profile clienteambols File Upload: Upload Picture or Image URL: Link Image Email: Role: diamond Become a deluxe member Username: Set Username |
| CEN-PER-08 | Adicionar endereço pela área de perfil | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. \| 160 characters 0/160 City State navigate_before Back send Submit Texto transitório capturado: ZIP Code \| Address \| 0/8 \| Max. 160 characters 0/160 \| Max. 160 characters Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address \| navigate_before \| navigate_before Back 2. Conteúdo/estrutura  |
| CEN-PER-09 | Editar endereço salvo | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. \| 160 characters 0/160 City State navigate_before Back send Submit Texto transitório capturado: ZIP Code \| Address \| 0/8 \| Max. 160 characters 0/160 \| Max. 160 characters Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN All Products Apple Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Apple Pomace 0.89¤ add_shopping_cart Add to Basket Banana Juice (1000ml) 1.99¤ add_shopping_cart Add to Basket Basil Smoothie 2.99¤ add_shopping_cart Add to Basket Berry Juice (1000ml) 3.49¤ add_shopping_cart Add to Basket Only 1 left Best Juice Shop Salesman Artwork 5000¤ add_shopp |
| CEN-PER-10 | Remover endereço salvo | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/address/create Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. \| 160 characters 0/160 City State navigate_before Back send Submit Texto transitório capturado: ZIP Code \| Address \| 0/8 \| Max. 160 characters 0/160 \| Max. 160 characters Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit \| Add New Address \| navigate_before \| navigate_before Back 2. Conteúdo/estrutura  |
| CEN-PER-11 | Remover cartão salvo | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/saved-payment-methods Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Texto transitório capturado: My Payment Options \| Add new card \| Add new card Add a credit or debit card \| Add a credit or debit card \| Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Registration completed successfully. You can now log in. X \| My Payment Options Add new card Add a credit or |
| CEN-PER-12 | Perfil sem login | PASSED | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/profile Texto visível: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/userProfile.js:69:18 Texto observado durante a ação: OWASP Juice Shop (Express ^4.22.1) 500 Error: Blocked illegal activity by ::ffff:172.18.0.1 at /juice-shop/build/routes/userProfile.js:69:18 |
| CEN-PER-13 | Endereços salvos sem login | PASSED | URL: http://127.0.0.1:3000/#/ → http://127.0.0.1:3000/#/address/saved Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page. Texto transitório capturado: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page. \| EN \| language EN \| account_circle Account shopping_cart Your Basket 0 language EN \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 Please login to view this page. \| 403 Please login to view this page. \| Please login to view this page. \| 403 \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page. |
| CEN-PER-14 | Consultar carteira digital | PASSED | URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/wallet Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit Texto transitório capturado: Wallet Balance 0.00 \| Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit Registration completed successfully. You can now log in. X \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit \| Registration completed successfully. You can now log in.  |
| CEN-PER-15 | Enviar feedback ao cliente sem nota | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/contact Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. \| 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? \| Result send Submit Texto transitório capturado: 1*6+9 \| CAPTCHA: What is 1*6+9 ? \| Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit \| Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is 1*6+9 ? Result send Submit Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 la |
| CEN-PER-16 | Registrar reclamação (Complaint) | PASSED | Durante a execução, foram observadas as seguintes mudanças na interface: 1. URL: http://127.0.0.1:3000/#/search → http://127.0.0.1:3000/#/complain Texto visível: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. \| 4096 characters 0 /4096 Invoice: send Submit Texto transitório capturado: Message Max. 4096 characters 0 /4096 \| Message \| Max. 4096 characters 0 /4096 \| Max. 4096 characters \| Registration completed successfully. You can now log in. X Mensagem transitória: menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit \| menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit Registration completed successfully. You can now log in. X \| Complai |

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
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change
- Change Password Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change
- Change Password
- Change
- Current Password New Password Password must be 5-40 characters long. 0/40 Repeat New Password 0/20 Change
- Current Password
- New Password Password must be 5-40 characters long. 0/40
- Repeat New Password 0/20
- New Password
- Repeat New Password
- Password must be 5-40 characters long. 0/40
- 0/20
- Password must be 5-40 characters long.
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet.
- This website uses fruit cookies to ensure you get the juiciest tracking experience. But me wait! Me want it! menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Order History No results found You have not placed any orders yet.
- Order History No results found You have not placed any orders yet.
- Order History
- No results found You have not placed any orders yet.
- No results found
- You have not placed any orders yet.
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit
- Add New Address Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit
- navigate_before
- navigate_before Back
- navigate_before Back send Submit
- Country Name Mobile Number ZIP Code 0/8 Address Max. 160 characters 0/160 City State navigate_before Back send Submit
- Back
- send
- send Submit
- Submit
- Country
- Name
- Mobile Number
- ZIP Code 0/8
- Address Max. 160 characters 0/160
- City
- State
- ZIP Code
- Address
- Carrot Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket
- Dragonfruit Juice (500ml) 3.99¤ add_shopping_cart Add to Basket
- Eggfruit Juice (500ml) 8.99¤ add_shopping_cart Add to Basket
- Elderflower Cordial (500ml) 3.29¤ add_shopping_cart Add to Basket
- Fruit Press 89.99¤ add_shopping_cart Add to Basket
- Grape Juice (1000ml) 2.99¤ add_shopping_cart Add to Basket
- Green Smoothie 1.99¤ add_shopping_cart Add to Basket
- Only 1 left Juice Shop "Permafrost" 2020 Edition 9999.99¤ add_shopping_cart Add to Basket
- Apple Juice (1000ml)
- 1.99¤
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Registration completed successfully. You can now log in. X
- Registration completed successfully. You can now log in. X
- Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099
- Name Card Number 0/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- Card Number 0/16
- Card Number
- 16/16
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN My Payment Options Add new card Add a credit or debit card Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 send Submit
- Card Number 16/16
- Name Card Number 16/16 Expiry Month 1 2 3 4 5 6 7 8 9 10 11 12 Expiry Year 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language placeholder 403 Please login to view this page.
- 403 Please login to view this page.
- Please login to view this page.
- 403
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN 403 Please login to view this page.
- EN
- language EN
- account_circle Account shopping_cart Your Basket 0 language EN
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance Amount monetization_on Deposit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance Amount monetization_on Deposit Registration completed successfully. You can now log in. X
- Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance Amount monetization_on Deposit
- Digital Wallet
- Digital Wallet Try out our new Crypto Wallet
- Try out our new Crypto Wallet
- Add Money
- Wallet Balance
- monetization_on
- monetization_on Deposit
- Deposit
- Amount
- 0.00
- Wallet Balance 0.00
- Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit Registration completed successfully. You can now log in. X
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Digital Wallet Try out our new Crypto Wallet Add Money Wallet Balance 0.00 Amount monetization_on Deposit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is ? Result send Submit
- Customer Feedback Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is ? Result send Submit
- CAPTCHA: What is ?
- Author Comment Max. 160 characters 0/160 Rating 1★ CAPTCHA: What is ? Result send Submit
- Author
- Comment Max. 160 characters 0/160
- Result
- Comment
- 1★
- Rating 1★
- Max. 160 characters 0/160
- Customer Feedback
- Max. 160 characters
- Rating
- What is
- 1*6+9
- CAPTCHA: What is 1*6+9 ?
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit Registration completed successfully. You can now log in. X
- Complaint Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit
- Complaint
- Invoice:
- Customer Message Max. 4096 characters 0 /4096 Invoice: send Submit
- Customer
- Message Max. 4096 characters 0 /4096
- Message
- Max. 4096 characters 0 /4096
- Max. 4096 characters
- 32
- 32 /4096
- Max. 4096 characters 32 /4096
- menu OWASP Juice Shop search search close account_circle Account shopping_cart Your Basket 0 language EN Complaint Customer Message Max. 4096 characters 32 /4096 Invoice: send Submit
- Message Max. 4096 characters 32 /4096

## Rastreabilidade

Cada descrição acima é derivada dos passos e evidências da execução do respectivo cenário; nenhum comportamento é inferido a partir de END, COMP ou REQ.
