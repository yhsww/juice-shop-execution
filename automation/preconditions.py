from __future__ import annotations

from automation.executor import _click, _fill, _select_option
from automation.locator import resolve
from config.settings import settings


AUTHENTICATED_IDT = {
    "CEN-IDT-03", "CEN-IDT-04", "CEN-IDT-05", "CEN-IDT-06",
    "CEN-IDT-07", "CEN-IDT-08", "CEN-IDT-09", "CEN-IDT-10",
    "CEN-IDT-11", "CEN-IDT-12", "CEN-IDT-13",
}


def scenario_email(scenario: dict) -> str:
    return f"cen-{scenario['id'].lower()}@example.com"


def scenario_password(scenario: dict) -> str:
    return "Teste@12345"


def needs_authentication(scenario: dict) -> bool:
    domain = str(scenario.get("domain", "")).upper()
    scenario_id = scenario["id"]
    return (
        domain in {"ADM", "PER", "CHK"}
        or scenario_id in AUTHENTICATED_IDT
    )


async def _register_user(page, email: str, password: str) -> bool:
    await page.goto(f"{settings.base_url}/#/register", wait_until="domcontentloaded")

    fields = [
        ({"label": "Email address", "exact": False}, email),
        ({"label": "Password", "exact": False}, password),
        ({"label": "Repeat Password", "exact": False}, password),
        ({"label": "Answer", "exact": False}, "a"),
    ]
    for target, value in fields:
        locator = await resolve(page, target)
        if locator is None:
            return False
        await _fill(locator, value)

    question = await resolve(page, {"label": "Security Question", "exact": False})
    if question is None:
        return False
    await _select_option(question, "Your favorite book?")

    register = await resolve(
        page,
        {"role": "button", "name": "Register", "exact": False},
    )
    if register is None:
        return False

    await _click(register)
    await page.wait_for_timeout(800)
    return "/#/login" in page.url


async def _login(page, email: str, password: str) -> bool:
    await page.goto(f"{settings.base_url}/#/login", wait_until="domcontentloaded")

    email_field = await resolve(page, {"label": "Email", "exact": False})
    password_field = await resolve(page, {"label": "Password", "exact": False})
    login = await resolve(
        page,
        {"role": "button", "name": "Login", "exact": False},
    )

    if not email_field or not password_field or not login:
        return False

    await _fill(email_field, email)
    await _fill(password_field, password)
    await _click(login)
    await page.wait_for_timeout(700)

    return "/#/login" not in page.url


async def ensure_user(page, email: str, password: str) -> bool:
    if await _login(page, email, password):
        return True

    registered = await _register_user(page, email, password)
    if not registered:
        return False

    return await _login(page, email, password)


async def ensure_authentication(page, scenario: dict) -> bool:
    if not needs_authentication(scenario):
        return True

    if str(scenario.get("domain", "")).upper() == "ADM":
        return await _login(
            page,
            settings.admin_email,
            settings.admin_password,
        )

    return await ensure_user(
        page,
        scenario_email(scenario),
        scenario_password(scenario),
    )


async def ensure_base_user(page) -> bool:
    return await ensure_user(page, "teste@example.com", "Teste@12345")


async def _add_address_if_needed(page) -> bool:
    add = await resolve(
        page,
        {"role": "button", "name": "Add New Address", "exact": False},
    )
    if add is None:
        add = await resolve(
            page,
            {"role": "button", "name": "Add a new address", "exact": False},
        )

    if add is not None:
        await _click(add)
        await page.wait_for_timeout(300)

        values = [
            ("Country", "Brazil"),
            ("Name", "Cliente Teste"),
            ("Mobile Number", "85999999999"),
            ("ZIP Code", "60000000"),
            ("Address", "Rua Teste, 100"),
            ("City", "Fortaleza"),
            ("State", "CE"),
        ]
        for label, value in values:
            field = await resolve(page, {"label": label, "exact": False})
            if field is None:
                return False
            await _fill(field, value)

        submit = await resolve(
            page,
            {"role": "button", "name": "Submit", "exact": False},
        )
        if submit is None:
            return False

        await _click(submit)
        await page.wait_for_timeout(700)

    return True


async def ensure_basket(page) -> bool:
    await page.goto(f"{settings.base_url}/#/", wait_until="domcontentloaded")
    add = await resolve(
        page,
        {"role": "button", "name": "Add to Basket", "exact": False},
    )
    if add is None:
        return False
    await _click(add)
    await page.wait_for_timeout(400)
    return True


async def ensure_address(page, select: bool = False) -> bool:
    await page.goto(f"{settings.base_url}/#/address/select", wait_until="domcontentloaded")
    if not await _add_address_if_needed(page):
        return False

    if select:
        radio = await resolve(
            page,
            {"role": "radio", "name": "Address", "exact": False},
        )
        if radio is None:
            return False
        await _click(radio)
        continue_button = await resolve(
            page,
            {"role": "button", "name": "Continue", "exact": False},
        )
        if continue_button is None:
            return False
        await _click(continue_button)
        await page.wait_for_timeout(500)

    return True


async def ensure_delivery(page) -> bool:
    if not await ensure_address(page, select=True):
        return False

    if "/#/delivery-method" not in page.url:
        return False

    delivery = await resolve(
        page,
        {"role": "radio", "name": "Standard Delivery", "exact": False},
    )
    if delivery is None:
        delivery = await resolve(
            page,
            {"role": "radio", "name": "Standard", "exact": False},
        )
    if delivery is None:
        return False

    await _click(delivery)

    continue_button = await resolve(
        page,
        {"role": "button", "name": "Continue", "exact": False},
    )
    if continue_button is None:
        return False

    await _click(continue_button)
    await page.wait_for_timeout(500)
    return "/#/payment/shop" in page.url


async def ensure_card(page) -> bool:
    if "/#/payment/shop" not in page.url:
        return False

    existing = await resolve(
        page,
        {"role": "radio", "name": "1111", "exact": False},
    )
    if existing is not None:
        return True

    add_card = await resolve(
        page,
        {"text": "Add new card", "exact": False},
    )
    if add_card is None:
        add_card = await resolve(
            page,
            {"text": "Add New Card", "exact": False},
        )
    if add_card is None:
        return False

    await _click(add_card)
    await page.wait_for_timeout(200)

    values = [
        ("Name", "Cliente Teste"),
        ("Card Number", "1111222233334444"),
    ]
    for label, value in values:
        field = await resolve(page, {"label": label, "exact": False})
        if field is None:
            return False
        await _fill(field, value)

    month = await resolve(page, {"label": "Expiry Month", "exact": False})
    year = await resolve(page, {"label": "Expiry Year", "exact": False})
    if month is None or year is None:
        return False

    await _select_option(month, "12")
    await _select_option(year, "2030")

    submit = await resolve(
        page,
        {"role": "button", "name": "Submit", "exact": False},
    )
    if submit is None:
        return False
    await _click(submit)
    await page.wait_for_timeout(700)

    return await resolve(
        page,
        {"role": "radio", "name": "1111", "exact": False},
    ) is not None


async def ensure_payment(page) -> bool:
    if not await ensure_delivery(page):
        return False
    return await ensure_card(page)


async def ensure_order_summary(page) -> bool:
    if not await ensure_payment(page):
        return False

    card = await resolve(
        page,
        {"role": "radio", "name": "1111", "exact": False},
    )
    if card is None:
        return False
    await _click(card)

    continue_button = await resolve(
        page,
        {"role": "button", "name": "Continue", "exact": False},
    )
    if continue_button is None:
        return False
    await _click(continue_button)
    await page.wait_for_timeout(700)
    return "/#/order-summary" in page.url


async def ensure_completed_order(page) -> bool:
    if not await ensure_order_summary(page):
        return False

    place = await resolve(
        page,
        {"role": "button", "name": "Place your order and pay", "exact": False},
    )
    if place is None:
        return False
    await _click(place)
    await page.wait_for_timeout(1000)
    return "/#/order-completion" in page.url


async def prepare_precondition(page, scenario: dict) -> tuple[bool, str]:
    if not await ensure_authentication(page, scenario):
        return False, "Pré-condição de autenticação não pôde ser preparada."

    scenario_id = scenario["id"]

    if scenario_id == "CEN-IDT-14":
        if not await ensure_base_user(page):
            return False, "Não foi possível preparar o usuário existente exigido pelo cenário."

    if scenario_id in {
        "CEN-CAR-02", "CEN-CAR-03", "CEN-CAR-04", "CEN-CAR-05", "CEN-CAR-06",
        "CEN-CHK-01", "CEN-CHK-02", "CEN-CHK-03", "CEN-CHK-04", "CEN-CHK-05",
        "CEN-CHK-06", "CEN-CHK-07", "CEN-CHK-08", "CEN-CHK-09", "CEN-CHK-10",
        "CEN-CHK-11", "CEN-CHK-12", "CEN-CHK-13", "CEN-CHK-14", "CEN-CHK-15",
        "CEN-CHK-28",
    }:
        if not await ensure_basket(page):
            return False, "Pré-condição de carrinho não pôde ser preparada."

    if scenario_id in {"CEN-CHK-05", "CEN-CHK-06", "CEN-CHK-07",
                        "CEN-CHK-08", "CEN-CHK-09", "CEN-CHK-10",
                        "CEN-CHK-11", "CEN-CHK-12", "CEN-CHK-13",
                        "CEN-CHK-14", "CEN-CHK-15"}:
        if not await ensure_payment(page):
            return False, "Pré-condição de pagamento não pôde ser preparada."

    if scenario_id in {"CEN-CHK-10", "CEN-CHK-11", "CEN-CHK-26", "CEN-CHK-27"}:
        if not await ensure_order_summary(page):
            return False, "Pré-condição de resumo do pedido não pôde ser preparada."

    if scenario_id in {"CEN-CHK-17", "CEN-CHK-18", "CEN-CHK-19",
                        "CEN-CHK-20", "CEN-CHK-21", "CEN-CHK-22"}:
        if not await ensure_completed_order(page):
            return False, "Pré-condição de pedido concluído não pôde ser preparada."

    if scenario_id == "CEN-CHK-24":
        if not await ensure_address(page, select=True):
            return False, "Pré-condição de endereço selecionado não pôde ser preparada."

    if scenario_id == "CEN-CHK-25":
        if not await ensure_payment(page):
            return False, "Pré-condição de pagamento não pôde ser preparada."

    return True, ""
