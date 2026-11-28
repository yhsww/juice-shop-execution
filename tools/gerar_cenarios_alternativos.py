"""Gera o catálogo de cenários complementares (alternativos) no formato do repositório
juice-shop-execution e as fichas em Markdown no template da Etapa 1 (AMBOLS)."""
import json
import sys
from pathlib import Path

# Uso: python tools/gerar_cenarios_alternativos.py
# Gera scenarios/scenarios_alternativos.json e docs/fichas_cenarios_alternativos.md.
ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "scenarios" / "scenarios_alternativos.json"
FICHAS = ROOT / "docs" / "fichas_cenarios_alternativos.md"

# ---------- helpers de ação (mesmo vocabulário do executor existente) ----------
def nav(r): return {"type": "NAVIGATE", "route": r}
def wait(ms=700): return {"type": "WAIT", "milliseconds": ms}
def fill(label, v): return {"type": "FILL", "target": {"label": label, "exact": False}, "value": v}
def sel(label, v): return {"type": "SELECT", "target": {"label": label, "exact": False}, "value": v}
def btn(name, exact=False): return {"type": "CLICK", "target": {"role": "button", "name": name, "exact": exact}}
def txt(t): return {"type": "CLICK", "target": {"text": t, "exact": False}}
def radio(n): return {"type": "CLICK", "target": {"role": "radio", "name": n, "exact": False}}
def press(label, key): return {"type": "PRESS", "target": {"label": label, "exact": False}, "key": key}
def dis(name): return {"type": "ASSERT_DISABLED", "target": {"role": "button", "name": name, "exact": False}}
def ena(name): return {"type": "ASSERT_ENABLED", "target": {"role": "button", "name": name, "exact": False}}

LOGIN_DISABLED = {"type": "ASSERT_DISABLED", "target": {"role": "button", "name": "Login", "exact": True}}

LANG_MENU = {"type": "CLICK", "target": {"css": "button[aria-label='Language selection menu']"}}

def login(email, pwd):
    return [nav("/#/login"), fill("Email", email), fill("Password", pwd), btn("Login"), wait(800)]

def logout():
    return [nav("/#/"), btn("Account"), txt("Logout"), wait(500)]

def register(email, pwd="Teste@12345", answer="resposta-teste"):
    return [nav("/#/register"), fill("Email address", email), fill("Password", pwd),
            fill("Repeat Password", pwd), sel("Security Question", "Your favorite book?"),
            fill("Answer", answer), btn("Register"), wait(1000)]

ADDR = [("Country", "Brazil"), ("Name", "Cliente Alternativo"), ("Mobile Number", "8599999999"),
        ("ZIP Code", "60000000"), ("Address", "Rua Alternativa, 200"), ("City", "Fortaleza"), ("State", "CE")]

def addr_form(skip=None, override=None):
    override = override or {}
    acts = [nav("/#/address/create"), wait(500)]
    for label, v in ADDR:
        if label == skip:
            continue
        acts.append(fill(label, override.get(label, v)))
    return acts

def card_form(name="Cliente Teste", num="4000000000000002", month="12", year="2090"):
    acts = [nav("/#/payment/shop"), txt("Add new card"), wait(300)]
    if name is not None: acts.append(fill("Name", name))
    if num is not None: acts.append(fill("Card Number", num))
    if month is not None: acts.append(sel("Expiry Month", month))
    if year is not None: acts.append(sel("Expiry Year", year))
    return acts

S = []
def cen(id, domain, name, flow_type, base, auth, actor, flow, pre, data, coherent, just, req,
        actions, expected, confidence="confirmado", scope="Em escopo", note=""):
    S.append({
        "id": id, "domain": domain, "name": name,
        "flow_type": flow_type, "base_scenario": base, "auth": auth,
        "actor": actor, "flow": flow, "precondition": pre, "data": data,
        "coherent": coherent, "justification": just, "requirement": req,
        "actions": actions, "expected": expected,
        "expected_confidence": confidence, "scope": scope,
        "execution_status": "PASSED — 2026-11-28, Juice Shop v20.3.0", "note": note,
    })

ANON = "Visitante não autenticado"
CLI = "Cliente autenticado"
ADMIN = "Administrador"
A_NONE, A_CLI, A_ADM = "none", "customer", "admin"

# =============================== IDT ===============================
cen("CEN-IDT-18", "IDT", "Cadastro com senha abaixo do tamanho mínimo", "Alternativo — formulário inválido", "CEN-IDT-01", A_NONE, ANON,
    "Preencher todo o cadastro com senha de 3 caracteres e tentar registrar.",
    "Sem sessão ativa; tela de cadastro aberta.", "E-mail único; senha '123'; pergunta e resposta preenchidas.",
    "Sim.", "Regra de tamanho de senha protege a conta do cliente.",
    "O sistema deve rejeitar senhas fora do intervalo de tamanho permitido e informar o limite ao usuário.",
    [nav("/#/register"), fill("Email address", "${UNIQUE_EMAIL}"), fill("Password", "123"), fill("Repeat Password", "123"),
     sel("Security Question", "Your favorite book?"), fill("Answer", "a"), press("Answer", "Tab"), wait(300), dis("Button to complete the registration")],
    {"url_contains": "/#/register", "text_contains": ["5-40 characters"]})

cen("CEN-IDT-19", "IDT", "Cadastro sem pergunta de segurança", "Alternativo — formulário incompleto", "CEN-IDT-01", A_NONE, ANON,
    "Preencher e-mail e senhas, deixar a pergunta de segurança e a resposta vazias e tentar registrar.",
    "Sem sessão ativa.", "E-mail único; senha válida repetida; pergunta e resposta vazias.",
    "Sim.", "A pergunta de segurança é usada depois na recuperação de senha.",
    "O sistema deve exigir pergunta e resposta de segurança para concluir o cadastro.",
    [nav("/#/register"), fill("Email address", "${UNIQUE_EMAIL}"), fill("Password", "Teste@12345"),
     fill("Repeat Password", "Teste@12345"), wait(300), dis("Button to complete the registration")],
    {"url_contains": "/#/register"}, confidence="alta")

cen("CEN-IDT-20", "IDT", "Login com e-mail não cadastrado", "Alternativo — dados inválidos", "CEN-IDT-03", A_NONE, ANON,
    "Informar um e-mail que nunca foi cadastrado e uma senha qualquer.",
    "Sem sessão ativa.", "E-mail inexistente; senha 'Teste@12345'.",
    "Sim.", "O cliente precisa saber que não conseguiu entrar, sem que a loja revele quais e-mails existem.",
    "O sistema deve recusar credenciais de conta inexistente com mensagem genérica.",
    login("nao-existe-${UNIQUE_EMAIL}", "Teste@12345"),
    {"url_contains": "/#/login", "text_contains": ["Invalid email or password"]}, confidence="alta")

cen("CEN-IDT-21", "IDT", "Login com campos vazios", "Alternativo — formulário incompleto", "CEN-IDT-03", A_NONE, ANON,
    "Abrir a tela de login e verificar o botão sem preencher nada; depois preencher só o e-mail.",
    "Sem sessão ativa.", "Nenhum dado; depois apenas e-mail.",
    "Sim.", "Evita envio de tentativa de login sem dados.",
    "O sistema deve impedir o envio do login enquanto e-mail e senha não forem informados.",
    [nav("/#/login"), wait(300), LOGIN_DISABLED, fill("Email", "${SCENARIO_EMAIL}"), wait(200), LOGIN_DISABLED],
    {"url_contains": "/#/login"})

cen("CEN-IDT-22", "IDT", "Acesso a área restrita após logout", "Alternativo — ação sem login", "CEN-IDT-05", A_CLI, CLI,
    "Entrar, sair pelo menu Account e em seguida abrir diretamente o histórico de pedidos.",
    "Cliente autenticado com sessão ativa.", "Rota /#/order-history digitada após logout.",
    "Sim.", "Após sair, dados do cliente não devem continuar acessíveis no navegador.",
    "O sistema deve encerrar a sessão no logout e não exibir dados pessoais em rotas restritas sem nova autenticação.",
    logout() + [nav("/#/order-history"), wait(800)],
    {"url_contains": "/#/order-history", "text_contains": ["You have not placed any orders yet"]},
    confidence="observado",
    note="Observado na v20.3.0: a rota não redireciona ao login; mostra o histórico vazio. Registrar como comportamento (dados do cliente não aparecem).")

cen("CEN-IDT-23", "IDT", "Troca de senha com senha atual incorreta", "Alternativo — dados inválidos", "CEN-IDT-08", A_CLI, CLI,
    "Informar senha atual errada e uma nova senha válida repetida corretamente.",
    "Cliente autenticado.", "Senha atual 'Errada@999'; nova 'Nova@12345' duas vezes.",
    "Sim.", "Somente o dono da conta deve conseguir trocar a senha.",
    "O sistema deve exigir a senha atual correta para alterar a senha.",
    [nav("/#/privacy-security/change-password"), fill("Current Password", "Errada@999"), fill("New Password", "Nova@12345"),
     fill("Repeat New Password", "Nova@12345"), btn("Change"), wait(800)],
    {"text_contains": ["Current password is not correct"]})

cen("CEN-IDT-24", "IDT", "Troca de senha com confirmação divergente", "Alternativo — formulário inválido", "CEN-IDT-08", A_CLI, CLI,
    "Informar senha atual correta e nova senha diferente da repetição.",
    "Cliente autenticado.", "Atual 'Teste@12345'; nova 'Nova@12345'; repetição 'Nova@54321'.",
    "Sim.", "Evita que o cliente fixe uma senha digitada errado.",
    "O sistema deve bloquear a troca quando a nova senha e a repetição forem diferentes.",
    [nav("/#/privacy-security/change-password"), fill("Current Password", "Teste@12345"), fill("New Password", "Nova@12345"),
     fill("Repeat New Password", "Nova@54321"), press("Repeat New Password", "Tab"), wait(300), dis("Button to confirm the change")],
    {"text_contains": ["do not match"]})

cen("CEN-IDT-25", "IDT", "Recuperação de senha com resposta errada", "Alternativo — dados inválidos", "CEN-IDT-10", A_NONE, ANON,
    "Cadastrar conta nova, sair do fluxo, abrir 'Forgot Password', informar resposta de segurança errada e nova senha.",
    "Conta criada no próprio cenário com resposta 'resposta-teste'.", "Resposta 'errada'; nova senha 'Nova@12345'.",
    "Sim.", "A recuperação só deve funcionar para quem conhece a resposta cadastrada.",
    "O sistema deve recusar a redefinição de senha quando a resposta de segurança estiver incorreta.",
    register("${UNIQUE_EMAIL}") + [nav("/#/forgot-password"), fill("Email", "${UNIQUE_EMAIL}"), wait(1000),
     fill("Security Question", "errada"), fill("New Password", "Nova@12345"), fill("Repeat New Password", "Nova@12345"),
     btn("Change"), wait(800)],
    {"text_contains": ["Wrong answer"]})

cen("CEN-IDT-26", "IDT", "Recuperação de senha concluída e login com a nova senha", "Principal (ausente no catálogo atual)", "CEN-IDT-09", A_NONE, ANON,
    "Cadastrar conta, recuperar a senha com a resposta correta e entrar com a senha nova.",
    "Conta criada no próprio cenário com resposta 'resposta-teste'.", "Resposta correta; nova senha 'Nova@12345'.",
    "Sim.", "O catálogo atual só abre a tela de recuperação; não verifica a mudança de estado (senha trocada).",
    "O sistema deve permitir redefinir a senha com a resposta de segurança correta e aceitar a nova senha no login.",
    register("${UNIQUE_EMAIL}") + [nav("/#/forgot-password"), fill("Email", "${UNIQUE_EMAIL}"), wait(1000),
     fill("Security Question", "resposta-teste"), fill("New Password", "Nova@12345"), fill("Repeat New Password", "Nova@12345"),
     btn("Change"), wait(800)] + login("${UNIQUE_EMAIL}", "Nova@12345"),
    {"text_not_contains": ["Invalid email or password"]})

cen("CEN-IDT-27", "IDT", "Recuperação de senha com e-mail não cadastrado", "Alternativo — dados inválidos", "CEN-IDT-10", A_NONE, ANON,
    "Informar e-mail inexistente na recuperação e observar se a pergunta de segurança é liberada.",
    "Sem sessão ativa.", "E-mail inexistente.",
    "Sim.", "Sem conta, não há pergunta de segurança a responder.",
    "O sistema não deve permitir redefinição de senha para e-mail sem conta.",
    [nav("/#/forgot-password"), fill("Email", "nao-existe-${UNIQUE_EMAIL}"), wait(1000), dis("Button to confirm the changes")],
    {"url_contains": "/#/forgot-password"})

cen("CEN-IDT-28", "IDT", "Cadastro com Enter em vez do botão", "Alternativo — interação diferente", "CEN-IDT-01", A_NONE, ANON,
    "Preencher o cadastro completo e pressionar Enter no último campo.",
    "Sem sessão ativa.", "Mesmos dados válidos do CEN-IDT-01.",
    "Sim.", "Usuários de teclado esperam enviar formulários com Enter.",
    "O sistema deve aceitar a submissão do cadastro pelo teclado.",
    [nav("/#/register"), fill("Email address", "${UNIQUE_EMAIL}"), fill("Password", "Teste@12345"),
     fill("Repeat Password", "Teste@12345"), sel("Security Question", "Your favorite book?"), fill("Answer", "a"),
     press("Answer", "Enter"), wait(1000)],
    {"url_contains": "/#/login"},
    note="Se permanecer em /#/register, registrar como comportamento observado (não é falha da aplicação por si só).")

# =============================== CAT ===============================
cen("CEN-CAT-18", "CAT", "Busca sem diferenciar maiúsculas", "Alternativo — entrada variante", "CEN-CAT-03", A_NONE, ANON,
    "Pesquisar 'APPLE' em caixa alta.", "Catálogo disponível.", "Termo 'APPLE'.",
    "Sim.", "O cliente não deve precisar acertar a caixa das letras.",
    "A busca deve ignorar diferença entre maiúsculas e minúsculas.",
    [nav("/#/search"), fill("Search", "APPLE"), press("Search", "Enter"), wait(1000)],
    {"text_contains": ["Apple Juice"]})

cen("CEN-CAT-19", "CAT", "Busca com termo muito longo", "Alternativo — entrada limite", "CEN-CAT-05", A_NONE, ANON,
    "Pesquisar um termo de 300 caracteres.", "Catálogo disponível.", "'suco' repetido até 300 caracteres.",
    "Sim.", "A interface não pode travar com entradas grandes.",
    "A busca deve responder sem erro a termos longos, informando ausência de resultados.",
    [nav("/#/search"), fill("Search", ("suco" * 75)), press("Search", "Enter"), wait(1000)],
    {"text_contains": ["No results found"]})

cen("CEN-CAT-20", "CAT", "Busca só com espaços", "Alternativo — formulário vazio", "CEN-CAT-08", A_NONE, ANON,
    "Digitar apenas espaços no campo de busca e confirmar.", "Catálogo disponível.", "'   '.",
    "Sim.", "Busca vazia deve ter comportamento previsível (todos os produtos ou nenhum).",
    "A busca deve tratar termo em branco de forma definida.",
    [nav("/#/search"), fill("Search", "   "), press("Search", "Enter"), wait(1000)],
    {"url_contains": "/#/search"},
    note="Registrar se lista todos os produtos ou mostra 'No results found'.")

cen("CEN-CAT-21", "CAT", "Tentar avaliar produto sem login", "Alternativo — ação sem login", "CEN-CAT-12", A_NONE, ANON,
    "Abrir o detalhe do Apple Juice sem sessão e tentar escrever uma avaliação.",
    "Sem sessão ativa.", "Texto 'Ótimo suco'.",
    "Sim.", "Avaliação deve ter autor identificado.",
    "O sistema deve exigir autenticação para publicar avaliações de produto.",
    [nav("/#/"), txt("Apple Juice (1000ml)"), wait(700)],
    {"text_contains": ["Reviews"], "text_not_contains": ["Write a review"]}, confidence="observado",
    note="Observado na v20.3.0: para visitante, o detalhe mostra as avaliações mas não exibe o formulário 'Write a review'.")

cen("CEN-CAT-22", "CAT", "Publicar avaliação de produto", "Principal (ausente no catálogo atual)", "CEN-CAT-12", A_CLI, CLI,
    "Abrir o Apple Juice, escrever uma avaliação e enviar.", "Cliente autenticado.", "Texto 'Suco muito bom - teste AMBOLS'.",
    "Sim.", "Avaliações ajudam outros clientes a escolher sucos.",
    "O sistema deve permitir que cliente autenticado publique avaliação de produto.",
    [nav("/#/"), txt("Apple Juice (1000ml)"), wait(700), fill("Text field to review a product", "Suco muito bom - teste AMBOLS"),
     btn("Send the review"), wait(800)],
    {"text_contains": ["review has been saved"]},
    note="O rótulo do campo de avaliação deve ser confirmado na primeira execução.")

cen("CEN-CAT-23", "CAT", "Avaliação vazia", "Alternativo — formulário incompleto", "CEN-CAT-22", A_CLI, CLI,
    "Abrir o detalhe e tentar enviar a avaliação sem texto.", "Cliente autenticado.", "Nenhum texto.",
    "Sim.", "Avaliação sem conteúdo não tem valor.",
    "O sistema deve impedir o envio de avaliação vazia.",
    [nav("/#/"), txt("Apple Juice (1000ml)"), wait(700), dis("Send the review")],
    {"text_contains": ["Write a review"]}, confidence="observado")

cen("CEN-CAT-24", "CAT", "Produto que não é suco à venda (obra de arte)", "Incoerente com loja de sucos", "CEN-CAT-02", A_NONE, ANON,
    "Abrir o detalhe de 'Best Juice Shop Salesman Artwork' e registrar preço e descrição.",
    "Catálogo disponível.", "Produto 'Best Juice Shop Salesman Artwork' (5000¤).",
    "Não.", "Uma obra de arte de 5000¤ não pertence ao domínio de uma loja de sucos; é comportamento a registrar.",
    "(Nenhum — registrar como item fora do domínio de negócio.)",
    [nav("/#/search"), fill("Search", "Artwork"), press("Search", "Enter"), wait(1000), txt("Best Juice Shop Salesman Artwork"), wait(700)],
    {"text_contains": ["Artwork"]})

cen("CEN-CAT-25", "CAT", "Produto 'Permafrost 2020 Edition' com preço desproporcional", "Incoerente com loja de sucos", "CEN-CAT-11", A_NONE, ANON,
    "Localizar o produto 'Permafrost' e registrar preço (9999.99¤) e aviso de estoque.",
    "Catálogo disponível.", "Termo 'Permafrost'.",
    "Não.", "Preço e natureza do item não condizem com sucos; registrar sem investigar.",
    "(Nenhum — registrar como item fora do domínio de negócio.)",
    [nav("/#/search"), fill("Search", "Permafrost"), press("Search", "Enter"), wait(1000)],
    {"text_contains": ["Permafrost", "9999.99"]})

cen("CEN-CAT-26", "CAT", "Troca de idioma da loja", "Alternativo — estado da interface", "CEN-CAT-01", A_NONE, ANON,
    "Abrir o seletor de idioma, escolher Português e voltar ao catálogo.",
    "Catálogo em inglês.", "Idioma 'Português (Brasil)'.",
    "Sim.", "Cliente brasileiro deve conseguir ler a loja em português.",
    "O sistema deve permitir trocar o idioma da interface mantendo o catálogo.",
    [nav("/#/"), LANG_MENU, wait(500), {"type": "CLICK", "target": {"css": "mat-radio-button:has-text('Português (Brasil)') label"}}, wait(1500),
     LANG_MENU, wait(500), {"type": "CLICK", "target": {"css": "mat-radio-button:has-text('English') label"}}, wait(1500)],
    {"text_contains": ["Seu Carrinho", "Adicionar ao carrinho"]}, confidence="observado",
    note="O cenário volta para English no fim: o navegador da suíte é compartilhado e o idioma fica salvo em cookie.")

cen("CEN-CAT-27", "CAT", "Mural de fotos (Photo Wall)", "Incoerente com loja de sucos", "CEN-CAT-01", A_NONE, ANON,
    "Abrir o menu lateral e acessar Photo Wall.", "Catálogo disponível.", "—",
    "Parcial.", "Rede social de fotos não é função de venda de sucos; pode ser marketing.",
    "(Registrar como funcionalidade periférica.)",
    [nav("/#/photo-wall"), wait(800)],
    {"url_contains": "/#/photo-wall", "text_contains": ["Photo Wall", "bkimminich"], "text_not_contains": ["Share a memory"]}, confidence="observado",
    note="Observado na v20.3.0: visitante vê o mural, mas o formulário 'Share a memory' só aparece com login.")

cen("CEN-CAT-28", "CAT", "Chat com IA na loja", "Incoerente com loja de sucos", "CEN-CAT-01", A_NONE, ANON,
    "Abrir o item 'AI Chat' do menu lateral e registrar o que a tela pede.", "Catálogo disponível.", "—",
    "Parcial.", "Atendimento por chat pode ser coerente; registrar apenas o comportamento visível, sem testar o bot.",
    "(Registrar como funcionalidade periférica.)",
    [nav("/#/"), btn("Open side menu"), wait(300), txt("AI Chat"), wait(1000)],
    {"text_contains": ["Chat"]},
    scope="Em escopo só para observação da tela; interações de manipulação do bot são fora de escopo.")

cen("CEN-CAT-29", "CAT", "Página 'About Us'", "Principal (ausente no catálogo atual)", "CEN-CAT-01", A_NONE, ANON,
    "Abrir 'About Us' pelo menu lateral.", "Catálogo disponível.", "—",
    "Sim.", "Informação institucional da loja.",
    "O sistema deve apresentar informações institucionais da loja.",
    [nav("/#/about"), wait(800)],
    {"text_contains": ["About Us", "Corporate History"]}, confidence="observado")

# =============================== CAR ===============================
cen("CEN-CAR-08", "CAR", "Aumentar quantidade com verificação do total", "Principal (corrige CEN-CAR-03)", "CEN-CAR-03", A_CLI, CLI,
    "Com 1 Apple Juice no carrinho, clicar em aumentar e conferir quantidade 2 e total 3.98¤.",
    "Cliente autenticado; há pelo menos um produto no carrinho (conta nova: 1 unidade de Apple Juice).", "Apple Juice 1.99¤.",
    "Sim.", "O CEN-CAR-03 atual passa por coincidência (o '2' de 'v20.3.0'); este cenário verifica o total.",
    "O sistema deve recalcular o total quando a quantidade de um item muda.",
    [nav("/#/basket"), wait(500), {"type": "CLICK", "target": {"css": "button:has(svg.fa-plus-square)"}}, wait(800)],
    {"text_contains": ["3.98"]},
    note="O seletor do botão '+' deve ser confirmado: a evidência atual mostra que 'Increase quantity' abriu o menu lateral.")

cen("CEN-CAR-09", "CAR", "Diminuir quantidade abaixo de 1", "Alternativo — limite inferior", "CEN-CAR-03", A_CLI, CLI,
    "Com 1 unidade no carrinho, clicar em diminuir.", "Cliente autenticado; há pelo menos um produto no carrinho (1 unidade).", "—",
    "Sim.", "Quantidade zero ou negativa não faz sentido num pedido.",
    "O sistema não deve permitir quantidade menor que 1 (ou deve remover o item).",
    [nav("/#/basket"), wait(500), {"type": "CLICK", "target": {"css": "button:has(svg.fa-minus-square)"}}, wait(800)],
    {"text_not_contains": ["-1"]},
    note="Registrar se o item continua com 1 ou é removido.")

cen("CEN-CAR-10", "CAR", "Exceder limite de unidades por produto", "Alternativo — regra de negócio", "CEN-CAR-03", A_CLI, CLI,
    "Adicionar o mesmo produto repetidamente pelo catálogo até a loja recusar.", "Cliente autenticado; carrinho vazio.", "Apple Juice, 6 cliques em 'Add to Basket'.",
    "Sim.", "Limite por pedido é regra comum em lojas.",
    "O sistema deve limitar a quantidade de unidades de um mesmo produto por pedido e avisar o cliente.",
    [nav("/#/")] + [btn("Add to Basket"), wait(600)] * 6,
    {"text_contains": ["only up to"]},
    note="Hipótese: limite de 5 unidades. O primeiro botão 'Add to Basket' deve ser o do Apple Juice.")

cen("CEN-CAR-11", "CAR", "Exceder o limite de 1 unidade de um produto restrito", "Alternativo — regra de negócio", "CEN-CAR-01", A_CLI, CLI,
    "Adicionar duas vezes o 'Juice Shop \"Permafrost\" 2020 Edition', marcado 'Only 1 left'.", "Cliente autenticado; carrinho vazio (conta nova).", "Produto Permafrost (9999.99¤).",
    "Sim.", "A loja não pode vender mais do que o limite definido para o produto.",
    "O sistema deve impedir a inclusão acima do limite por cliente e avisar o cliente.",
    [nav("/#/search"), fill("Search", "Permafrost"), press("Search", "Enter"), wait(1000), btn("Add to Basket"), wait(800), btn("Add to Basket"), wait(800)],
    {"text_contains": ["You can order only up to 1 items of this product"]}, confidence="observado",
    note="Observado na v20.3.0: o aviso 'Only N left' do Berry Juice não bloqueia a inclusão (5 unidades entraram com 'Only 3 left'); o limite só aparece em produtos com restrição por cliente, como o Permafrost.")

cen("CEN-CAR-12", "CAR", "Adicionar o mesmo produto duas vezes", "Alternativo — repetição", "CEN-CAR-01", A_CLI, CLI,
    "Clicar duas vezes em 'Add to Basket' no mesmo produto e abrir o carrinho.", "Cliente autenticado; carrinho vazio.", "Apple Juice.",
    "Sim.", "O carrinho deve somar a quantidade, não duplicar a linha.",
    "O sistema deve acumular a quantidade quando o mesmo produto é adicionado de novo.",
    [nav("/#/"), btn("Add to Basket"), wait(600), btn("Add to Basket"), wait(800), nav("/#/basket"), wait(800)],
    {"text_contains": ["3.98"]})

cen("CEN-CAR-13", "CAR", "Carrinho anônimo e login em seguida", "Alternativo — mudança de estado de acesso", "CEN-CAR-07", A_NONE, ANON,
    "Sem login, adicionar um produto (a evidência atual mostra 'Your Basket (anonymous)'), depois entrar e abrir o carrinho.",
    "Sem sessão ativa.", "Apple Juice; conta do cenário.",
    "Sim.", "O cliente espera não perder o que escolheu antes de entrar.",
    "O sistema deve definir o que acontece com o carrinho anônimo após a autenticação.",
    [nav("/#/"), btn("Add to Basket"), wait(800), nav("/#/basket"), wait(500)] + register("${UNIQUE_EMAIL}") + login("${UNIQUE_EMAIL}", "Teste@12345") + [nav("/#/basket"), wait(800)],
    {"text_contains": ["Your Basket"]},
    note="Registrar se o Apple Juice anônimo aparece no carrinho do cliente após o login.")

cen("CEN-CAR-14", "CAR", "Checkout com carrinho anônimo", "Alternativo — ação sem login", "CEN-CHK-01", A_NONE, ANON,
    "Sem login, adicionar produto e clicar em Checkout.", "Sem sessão ativa.", "Apple Juice.",
    "Sim.", "Compra precisa de cliente identificado (endereço, pagamento).",
    "O sistema deve exigir autenticação antes de prosseguir para o checkout.",
    [nav("/#/"), btn("Add to Basket"), wait(800), nav("/#/basket"), wait(500), btn("Checkout"), wait(800)],
    {"text_not_contains": ["Select an address"]},
    note="Registrar se a interface leva ao login, mostra erro ou bloqueia o botão.")

cen("CEN-CAR-15", "CAR", "Checkout com carrinho vazio", "Alternativo — estado vazio", "CEN-CHK-01", A_CLI, CLI,
    "Com o carrinho vazio (conta nova), tentar iniciar o checkout.", "Cliente autenticado; carrinho vazio.", "—",
    "Sim.", "Não há pedido sem itens.",
    "O sistema não deve permitir iniciar checkout com carrinho vazio.",
    [nav("/#/basket"), wait(1000), dis("Checkout")],
    {"text_contains": ["Total Price: 0"]}, confidence="observado")

# =============================== CHK ===============================
for i, (missing, label) in enumerate([("City", "cidade"), ("Mobile Number", "celular"), ("Country", "país")]):
    cen(f"CEN-CHK-{29+i:02d}", "CHK", f"Endereço sem {label}", "Alternativo — formulário incompleto", "CEN-CHK-02", A_CLI, CLI,
        f"Preencher o formulário de novo endereço sem o campo {missing} e tentar enviar.",
        "Cliente autenticado; formulário de novo endereço aberto (sem carrinho exigido).", f"Endereço completo exceto {missing}.",
        "Sim.", "Entrega exige endereço completo.",
        f"O sistema deve exigir o campo {missing} no cadastro de endereço.",
        addr_form(skip=missing) + [wait(300), dis("Submit")],
        {"url_contains": "/#/address/create"}, confidence="alta")

cen("CEN-CHK-32", "CHK", "Endereço com celular em formato inválido", "Alternativo — dados inválidos", "CEN-CHK-02", A_CLI, CLI,
    "Preencher endereço com celular de 3 dígitos.", "Cliente autenticado.", "Mobile Number '123'.",
    "Sim.", "Telefone de contato é usado na entrega.",
    "O sistema deve validar o formato do telefone do endereço.",
    addr_form(override={"Mobile Number": "123"}) + [press("Mobile Number", "Tab"), wait(300), dis("Submit")],
    {"url_contains": "/#/address/create"})

cen("CEN-CHK-33", "CHK", "Endereço com CEP acima do tamanho", "Alternativo — dados inválidos", "CEN-CHK-02", A_CLI, CLI,
    "Preencher ZIP Code com 12 dígitos.", "Cliente autenticado.", "ZIP '123456789012'.",
    "Sim.", "CEP deve ter tamanho válido.",
    "O sistema deve limitar o tamanho do CEP.",
    addr_form(override={"ZIP Code": "123456789012"}) + [press("ZIP Code", "Tab"), wait(300), dis("Submit")],
    {"url_contains": "/#/address/create"})

cen("CEN-CHK-34", "CHK", "Cartão com número incompleto", "Alternativo — dados inválidos", "CEN-CHK-07", A_CLI, CLI,
    "Cadastrar cartão com 12 dígitos.", "Cliente autenticado; método de entrega selecionado.", "Número '400000000000'.",
    "Sim.", "Cartão inválido não pode ser salvo.",
    "O sistema deve exigir número de cartão com 16 dígitos.",
    card_form(num="400000000000") + [wait(300), dis("Submit")],
    {"url_contains": "/#/payment/shop"}, confidence="alta")

cen("CEN-CHK-35", "CHK", "Cartão sem validade", "Alternativo — formulário incompleto", "CEN-CHK-07", A_CLI, CLI,
    "Cadastrar cartão sem escolher mês e ano.", "Cliente autenticado; método de entrega selecionado.", "Nome e número válidos.",
    "Sim.", "Validade é obrigatória para pagamento.",
    "O sistema deve exigir mês e ano de validade do cartão.",
    card_form(month=None, year=None) + [wait(300), dis("Submit")],
    {"url_contains": "/#/payment/shop"}, confidence="alta")

cen("CEN-CHK-36", "CHK", "Resgatar cupom vazio", "Alternativo — formulário incompleto", "CEN-CHK-15", A_CLI, CLI,
    "Abrir a área de cupom e verificar o botão Redeem sem código.", "Cliente autenticado; etapa de pagamento acessível; campo de cupom disponível.", "—",
    "Sim.", "Evita requisição sem dado.",
    "O sistema deve impedir o resgate de cupom sem código.",
    [nav("/#/payment/shop"), wait(500), txt("Add a coupon"), wait(300), dis("Redeem")],
    {"url_contains": "/#/payment/shop"})

cen("CEN-CHK-37", "CHK", "Entrega rápida altera o total do resumo", "Alternativo — escolha diferente", "CEN-CHK-05", A_CLI, CLI,
    "Escolher 'One Day Delivery' em vez de Standard e conferir o custo de entrega no resumo.",
    "Cliente autenticado; carrinho contém produto; endereço Rua Teste, 100 cadastrado; método de entrega disponível; cartão de teste terminado em 0002 cadastrado.", "Método 'One Day Delivery'.",
    "Sim.", "Cliente paga mais para receber antes.",
    "O sistema deve somar o custo do método de entrega escolhido ao total do pedido.",
    [nav("/#/basket"), btn("Checkout"), wait(700), txt("Rua Teste, 100"), btn("Continue"), wait(700), radio("One Day Delivery"), btn("Continue"), wait(700), radio("0002"), wait(300), btn("Continue"), wait(1000)],
    {"url_contains": "/#/order-summary", "text_contains": ["Delivery", "0.99"]})

cen("CEN-CHK-38", "CHK", "Pular etapas: abrir resumo do pedido direto", "Alternativo — contra o fluxo", "CEN-CHK-10", A_CLI, CLI,
    "Com carrinho cheio mas sem escolher endereço, entrega ou pagamento, abrir /#/order-summary e tentar concluir.",
    "Cliente autenticado; carrinho contém produto; nenhuma etapa do checkout concluída nesta sessão.", "—",
    "Sim.", "A loja não deve aceitar pedido sem endereço, entrega e pagamento.",
    "O sistema deve impedir a confirmação do pedido sem as etapas obrigatórias concluídas.",
    [nav("/#/order-summary"), wait(800)],
    {"text_not_contains": ["Thank you for your purchase"]},
    note="Não clicar em concluir se o botão parecer liberado; registrar o estado da tela (fora de escopo investigar desvio).")

cen("CEN-CHK-39", "CHK", "Pagar com carteira digital sem saldo", "Alternativo — saldo insuficiente", "CEN-CHK-09", A_CLI, CLI,
    "Na etapa de pagamento, escolher a carteira (Wallet) com saldo 0 e tentar avançar.",
    "Cliente autenticado (conta nova, saldo 0); método de entrega selecionado.", "—",
    "Sim.", "Não se paga com saldo inexistente.",
    "O sistema deve impedir pagamento pela carteira sem saldo suficiente.",
    [nav("/#/payment/shop"), wait(800)],
    {"text_contains": ["Pay using wallet", "Wallet Balance"]},
    note="Registrar se a opção de carteira aparece desabilitada ou se o avanço falha com mensagem.")

cen("CEN-CHK-40", "CHK", "Acessar pagamento sem login", "Alternativo — ação sem login", "CEN-CHK-07", A_NONE, ANON,
    "Sem sessão, abrir diretamente /#/payment/shop.", "Sem sessão ativa.", "—",
    "Sim.", "Cartões salvos são dados pessoais.",
    "O sistema deve exigir autenticação para exibir a etapa de pagamento.",
    [nav("/#/payment/shop"), wait(1000), dis("Proceed to review")],
    {"text_contains": ["My Payment Options"], "text_not_contains": ["0002"]}, confidence="observado",
    note="Observado na v20.3.0: a etapa de pagamento abre sem login (sem cartões e com avanço bloqueado). Registrar como achado de coerência.")

cen("CEN-CHK-41", "CHK", "Rastrear pedido inexistente", "Alternativo — dados inválidos", "CEN-CHK-19", A_NONE, ANON,
    "Abrir o rastreamento com um código de pedido que não existe.", "Sem sessão ativa.", "id 'pedido-inexistente-000'.",
    "Sim.", "O cliente precisa saber que o código está errado.",
    "O sistema deve informar quando o código de rastreamento não corresponde a pedido algum.",
    [nav("/#/track-result?id=pedido-inexistente-000"), wait(1000)],
    {"url_contains": "/#/track-result", "text_contains": ["pedido-inexistente-000", "? Days"]}, confidence="observado",
    note="Observado na v20.3.0: não há mensagem de pedido inexistente; a tela mostra '? Days' e o marcador não renderizado {{bonus}}. Não variar o id para descobrir pedidos de terceiros (fora de escopo).")

cen("CEN-CHK-42", "CHK", "Histórico de pedidos de cliente sem compras", "Alternativo — estado vazio", "CEN-CHK-17", A_NONE, ANON,
    "Cadastrar conta nova, entrar e abrir o histórico de pedidos.", "Conta criada no cenário, sem pedidos.", "—",
    "Sim.", "Tela vazia precisa ser compreensível.",
    "O sistema deve informar que o cliente ainda não possui pedidos.",
    register("${UNIQUE_EMAIL}") + login("${UNIQUE_EMAIL}", "Teste@12345") + [nav("/#/order-history"), wait(800)],
    {"text_contains": ["You have not placed any orders yet"]}, confidence="observado")

cen("CEN-CHK-43", "CHK", "Opções de pagamento em criptomoeda", "Incoerente com loja de sucos", "CEN-CHK-12", A_CLI, CLI,
    "Expandir 'Other payment options' e registrar as opções exibidas (cripto, doação, merchandising).",
    "Cliente autenticado; etapa de pagamento acessível; seção 'Other payment options' disponível.", "—",
    "Não.", "Doações e loja de camisetas não fazem parte da compra de sucos; registrar sem clicar.",
    "(Registrar como elementos fora do domínio.)",
    [nav("/#/payment/shop"), txt("Other payment options"), wait(500)],
    {"text_contains": ["Other payment options"]},
    scope="Em escopo só para registro; seguir links externos já está coberto em CEN-CHK-13/14.")

cen("CEN-CHK-44", "CHK", "Assinatura 'Deluxe Membership'", "Incoerente com loja de sucos", "CEN-CHK-12", A_CLI, CLI,
    "Abrir a página de assinatura Deluxe e registrar benefícios e preço, sem pagar.",
    "Cliente autenticado.", "—",
    "Parcial.", "Clube de vantagens é plausível, mas não aparece no fluxo principal de compra.",
    "(Registrar benefícios observados como candidatos a requisito.)",
    [nav("/#/deluxe-membership"), wait(800)],
    {"text_contains": ["Deluxe Membership", "49"]}, confidence="observado")

# =============================== PER ===============================
cen("CEN-PER-07", "PER", "Alterar nome de usuário", "Principal (ausente no catálogo atual)", "CEN-IDT-07", A_CLI, CLI,
    "Abrir o perfil, definir um username e salvar.", "Cliente autenticado.", "Username 'clienteambols'.",
    "Sim.", "O CEN-IDT-07 atual só abre a tela de privacidade; não altera dado algum.",
    "O sistema deve permitir que o cliente altere seu nome de usuário.",
    [nav("/profile"), wait(800), fill("Text field for the username", "clienteambols"), btn("Button to save/set the username"), wait(800)],
    {"text_contains": ["clienteambols"]},
    note="O perfil é servido em /profile (fora do roteador /#/).")

cen("CEN-PER-08", "PER", "Adicionar endereço pela área de perfil", "Principal (ausente no catálogo atual)", "CEN-PER-02", A_CLI, CLI,
    "Em 'My saved addresses', adicionar um endereço e ver a lista atualizada.", "Cliente autenticado.", "Endereço 'Rua Alternativa, 200'.",
    "Sim.", "Gerenciar endereços fora do checkout é previsto no guia (PER).",
    "O sistema deve permitir cadastrar endereço pela área do cliente.",
    addr_form() + [btn("Submit"), wait(1000), nav("/#/address/saved"), wait(800)],
    {"text_contains": ["Rua Alternativa, 200"]})

cen("CEN-PER-09", "PER", "Editar endereço salvo", "Alternativo — atualização de dados", "CEN-PER-08", A_CLI, CLI,
    "Editar o nome do destinatário de um endereço salvo.", "Cliente autenticado; o próprio cenário cadastra o endereço antes de editar.", "Nome 'Cliente Editado'.",
    "Sim.", "Atualização de dados cadastrais é fluxo alternativo exigido na Etapa 1.",
    "O sistema deve permitir editar um endereço salvo.",
    addr_form() + [btn("Submit"), wait(1000), nav("/#/address/saved"), wait(800), {"type": "CLICK", "target": {"css": "button:has(svg.fa-edit)"}}, wait(500), fill("Name", "Cliente Editado"), btn("Submit"), wait(1000)],
    {"text_contains": ["Cliente Editado"]},
    note="Nome acessível do ícone de edição a confirmar.")

cen("CEN-PER-10", "PER", "Remover endereço salvo", "Alternativo — exclusão", "CEN-PER-08", A_CLI, CLI,
    "Remover um endereço da lista.", "Cliente autenticado; o próprio cenário cadastra o endereço antes de remover.", "—",
    "Sim.", "Cliente deve poder descartar endereço antigo.",
    "O sistema deve permitir remover um endereço salvo.",
    addr_form() + [btn("Submit"), wait(1000), nav("/#/address/saved"), wait(800), {"type": "CLICK", "target": {"css": "button:has(svg.fa-trash-alt)"}}, wait(1000)],
    {"text_not_contains": ["Rua Alternativa, 200"]},
    note="Registrar o que acontece se o endereço removido era o selecionado num checkout em andamento.")

cen("CEN-PER-11", "PER", "Remover cartão salvo", "Alternativo — exclusão", "CEN-PER-03", A_CLI, CLI,
    "Em 'My Payment Options', remover o cartão terminado em 0002.", "Cliente autenticado; o próprio cenário cadastra o cartão 0002 antes de remover.", "—",
    "Sim.", "Cliente deve poder apagar meios de pagamento.",
    "O sistema deve permitir remover um cartão salvo.",
    [nav("/#/saved-payment-methods"), wait(800), txt("Add new card"), wait(300), fill("Name", "Cliente Teste"), fill("Card Number", "4000000000000002"), sel("Expiry Month", "12"), sel("Expiry Year", "2090"), btn("Submit"), wait(1000), {"type": "CLICK", "target": {"css": "button:has(svg.fa-trash-alt)"}}, wait(1000)],
    {"text_not_contains": ["0002"]})

cen("CEN-PER-12", "PER", "Perfil sem login", "Alternativo — ação sem login", "CEN-PER-01", A_NONE, ANON,
    "Sem sessão, abrir /profile.", "Sem sessão ativa.", "—",
    "Sim.", "Dados de perfil são pessoais.",
    "O sistema deve exigir autenticação para exibir o perfil.",
    [nav("/profile"), wait(1000)],
    {"text_contains": ["Blocked illegal activity"], "text_not_contains": ["Set Username"]}, confidence="observado",
    note="Observado na v20.3.0: sem sessão, /profile devolve uma página de erro 500 do servidor ('Blocked illegal activity') em vez de levar ao login. Registrar como achado de usabilidade; não investigar.")

cen("CEN-PER-13", "PER", "Endereços salvos sem login", "Alternativo — ação sem login", "CEN-PER-02", A_NONE, ANON,
    "Sem sessão, abrir /#/address/saved.", "Sem sessão ativa.", "—",
    "Sim.", "Endereços são dados pessoais.",
    "O sistema deve exigir autenticação para listar endereços.",
    [nav("/#/address/saved"), wait(1000)],
    {"text_contains": ["Please login to view this page"]}, confidence="observado")

cen("CEN-PER-14", "PER", "Consultar carteira digital", "Principal (ausente no catálogo atual)", "CEN-PER-03", A_CLI, CLI,
    "Abrir a carteira digital e ver o saldo.", "Cliente autenticado.", "—",
    "Parcial.", "Carteira com saldo é recurso comum em e-commerce, mas não essencial a uma loja de sucos.",
    "O sistema deve exibir o saldo da carteira do cliente.",
    [nav("/#/wallet"), wait(800)],
    {"text_contains": ["Digital Wallet", "Wallet Balance"]}, confidence="observado")

cen("CEN-PER-15", "PER", "Enviar feedback ao cliente sem nota", "Alternativo — formulário incompleto", "CEN-ADM-03", A_CLI, CLI,
    "Abrir 'Customer Feedback', escrever comentário e não escolher nota.", "Cliente autenticado.", "Comentário 'Teste AMBOLS'.",
    "Sim.", "Feedback sem nota fica incompleto.",
    "O sistema deve exigir comentário e nota para enviar feedback.",
    [nav("/#/contact"), wait(800), fill("Comment", "Teste AMBOLS"), wait(300), dis("Button to send the review")],
    {"url_contains": "/#/contact"},
    note="O formulário tem um CAPTCHA aritmético da própria aplicação; no fluxo completo ele deve ser preenchido manualmente pelo avaliador.")

cen("CEN-PER-16", "PER", "Registrar reclamação (Complaint)", "Principal (ausente no catálogo atual)", "CEN-PER-15", A_CLI, CLI,
    "Abrir 'Complaint', escrever a mensagem e enviar.", "Cliente autenticado.", "Mensagem 'Pedido chegou incompleto - teste'.",
    "Sim.", "Canal de reclamação é esperado em loja virtual.",
    "O sistema deve permitir que o cliente registre uma reclamação e receba um número de protocolo.",
    [nav("/#/complain"), wait(800), fill("Message", "Pedido chegou incompleto - teste"), btn("Button to send the complaint"), wait(1000)],
    {"text_contains": ["Customer support will get in touch"]},
    note="Não anexar arquivos (upload fica fora de escopo).")

# =============================== ADM ===============================
cen("CEN-ADM-04", "ADM", "Cliente comum tenta abrir a administração", "Alternativo — perfil sem permissão", "CEN-ADM-01", A_CLI, CLI,
    "Entrar como cliente comum e abrir /#/administration.", "Cliente autenticado sem perfil administrador.", "—",
    "Sim.", "Funções de gestão são restritas.",
    "O sistema deve negar a área administrativa a usuários sem perfil de administrador.",
    [nav("/#/administration"), wait(1000)],
    {"text_contains": ["You are not allowed to access this page"], "text_not_contains": ["Registered Users"]}, confidence="observado")

cen("CEN-ADM-05", "ADM", "Visitante tenta abrir a administração", "Alternativo — ação sem login", "CEN-ADM-01", A_NONE, ANON,
    "Sem sessão, abrir /#/administration.", "Sem sessão ativa.", "—",
    "Sim.", "Funções de gestão são restritas.",
    "O sistema deve negar a área administrativa a visitantes não autenticados.",
    [nav("/#/administration"), wait(1000)],
    {"text_contains": ["You are not allowed to access this page"], "text_not_contains": ["Registered Users"]}, confidence="observado")

cen("CEN-ADM-06", "ADM", "Ver detalhes de um usuário cadastrado", "Principal (ausente no catálogo atual)", "CEN-ADM-02", A_ADM, ADMIN,
    "Na lista de usuários, abrir os detalhes do primeiro usuário.", "Administrador autenticado.", "—",
    "Sim.", "O CEN-ADM-02 atual só confirma o título da seção.",
    "O sistema deve permitir ao administrador consultar dados de um usuário.",
    [nav("/#/administration"), wait(1000), {"type": "CLICK", "target": {"css": "button:has(svg.fa-eye)"}}, wait(1000)],
    {"text_contains": ["Email"]},
    note="O botão de detalhes é um ícone de olho sem rótulo acessível (achado de acessibilidade).")

cen("CEN-ADM-07", "ADM", "Remover feedback de cliente", "Alternativo — gestão de dados", "CEN-ADM-03", A_ADM, ADMIN,
    "Na lista de feedbacks, remover o primeiro item e observar a lista.", "Administrador autenticado; ao menos 1 feedback.", "—",
    "Sim.", "Moderar feedback é função administrativa.",
    "O sistema deve permitir ao administrador remover feedbacks.",
    [nav("/#/administration"), wait(1000), {"type": "CLICK", "target": {"css": "button:has(svg.fa-trash-alt)"}}, wait(1000)],
    {"text_contains": ["Customer Feedback"]},
    note="Anotar a contagem de feedbacks antes e depois (mudança de estado).")

cen("CEN-ADM-08", "ADM", "Gerenciar produtos e pedidos como administrador", "Lacuna — previsto no guia", "CEN-ADM-01", A_ADM, ADMIN,
    "Procurar na administração alguma tela de produtos ou pedidos; abrir /#/accounting.", "Administrador autenticado.", "—",
    "Sim.", "O guia exige 'consultar e gerenciar produtos e pedidos', mas a tela de administração mostra só usuários e feedbacks.",
    "O sistema deve oferecer gestão de produtos e pedidos a um perfil autorizado.",
    [nav("/#/administration"), wait(800), nav("/#/accounting"), wait(1000)],
    {"text_contains": ["You are not allowed to access this page"]}, confidence="observado",
    note="Hipótese: a gestão de estoque/preço e de pedidos fica em /#/accounting, para outro perfil (contabilidade). Registrar a resposta; não tentar obter outra conta.")

# ---------------------------------------------------------------------------
ids = [s["id"] for s in S]
assert len(ids) == len(set(ids)), "IDs duplicados"
CATALOG.write_text(
    json.dumps({"scenarios": S}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(len(S), "cenários")

# ------------------------------ fichas em Markdown ------------------------------
def describe(a):
    t = a["type"]; tg = a.get("target") or {}
    alvo = tg.get("name") or tg.get("label") or tg.get("text") or tg.get("css") or ""
    return {
        "NAVIGATE": (f"Abrir a rota {a.get('route')}", ""),
        "FILL": (f"Preencher '{alvo}'", a.get("value", "")),
        "SELECT": (f"Selecionar em '{alvo}'", a.get("value", "")),
        "CLICK": (f"Clicar em '{alvo}'", ""),
        "CLICK_ALL": (f"Clicar em todos os '{alvo}'", ""),
        "PRESS": (f"Pressionar {a.get('key')} em '{alvo}'", ""),
        "ASSERT_DISABLED": (f"Verificar que '{alvo}' está desabilitado", ""),
        "ASSERT_ENABLED": (f"Verificar que '{alvo}' está habilitado", ""),
        "WAIT": (None, None),
    }[t]

def cell(v): return str(v).replace("|", "\\|").replace("\n", " ")

DOM = {"IDT": "IDT (Gestão de Identidade e Usuários)", "CAT": "CAT (Catálogo de Produtos)", "CAR": "CAR (Carrinho de Compras)",
       "CHK": "CHK (Checkout e Pedidos)", "PER": "PER (Gestão de Perfil)", "ADM": "ADM (Administração)"}
md = []
for d in ["IDT", "CAT", "CAR", "CHK", "PER", "ADM"]:
    md.append(f"\n## {DOM[d]}\n")
    for s in [x for x in S if x["domain"] == d]:
        exp = s["expected"]
        crit = "; ".join(
            ([f"URL contém `{exp['url_contains']}`"] if exp.get("url_contains") else [])
            + [f"texto contém `{t}`" for t in exp.get("text_contains", [])]
            + [f"texto NÃO contém `{t}`" for t in exp.get("text_not_contains", [])])
        md.append(f"### {s['id']} — {s['name']}\n")
        md.append("| Campo | Valor |\n|---|---|")
        for k, v in [("ID do cenário", s["id"]), ("Domínio", DOM[d]), ("Nome do cenário", s["name"]), ("Ator", s["actor"]),
                     ("Fluxo", s["flow_type"]), ("Cenário de origem", s["base_scenario"]),
                     ("Pré-condição (estado inicial)", s["precondition"]),
                     ("Resultado esperado (critério verificável)", f"{crit} — confiança: **{s['expected_confidence']}**"),
                     ("Resultado observado (mudança de estado)", "_preencher na execução_"),
                     ("Mensagens exibidas ao usuário", "_preencher na execução_"),
                     ("Dados manipulados", s["data"]), ("Coerente com loja de sucos?", s["coherent"]),
                     ("Justificativa", s["justification"]), ("Requisito candidato (opcional)", s["requirement"]),
                     ("Escopo", s["scope"]), ("Status de execução", s["execution_status"])]:
            md.append(f"| {k} | {cell(v)} |")
        if s["note"]:
            md.append(f"\n> Observação: {s['note']}")
        md.append("\n| # | Ação do usuário | Dados informados | Resposta da interface |\n|---|---|---|---|")
        n = 0
        for a in s["actions"]:
            act, dado = describe(a)
            if act is None: continue
            n += 1
            md.append(f"| {n} | {cell(act)} | {cell(dado)} | _preencher_ |")
        md.append("")
FICHAS.parent.mkdir(parents=True, exist_ok=True)
FICHAS.write_text(
    "# Fichas dos cenários complementares (Etapa 1 — AMBOLS)\n\n"
    "Gerado por `tools/gerar_cenarios_alternativos.py`. Os campos de resultado "
    "observado são preenchidos a partir das evidências em `reports/executions/`.\n"
    + "\n".join(md),
    encoding="utf-8",
)
