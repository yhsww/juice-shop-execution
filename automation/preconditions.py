from __future__ import annotations

import json
import uuid

from automation.executor import _click, _fill, _select_option
from automation.locator import resolve
from config.settings import settings



def _normalize_text(value: object) -> str:
    """Normalize visible UI text for precondition checks."""
    return " ".join(str(value or "").split()).strip()


def scenario_email(scenario: dict) -> str:
    return f"cen-{scenario['id'].lower()}@example.com"


def scenario_password(scenario: dict) -> str:
    return "Teste@12345"


def needs_authentication(scenario: dict) -> bool:
    domain = str(scenario.get("domain", "")).upper()
    precondition = str(scenario.get("precondition", "")).casefold()
    actions = scenario.get("actions", []) or []
    first_route = str(actions[0].get("route", "")).casefold() if actions else ""
    return (
        "autenticad" in precondition
        or domain in {"PER", "CHK"}
        or first_route.startswith(("/#/profile", "/#/privacy-security", "/#/address/", "/#/saved-payment-methods", "/#/order-history", "/#/order-completion", "/#/payment/", "/#/delivery-method"))
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
    deadline = __import__("time").monotonic() + settings.action_timeout_ms / 1000

    while __import__("time").monotonic() < deadline:
        if "/#/login" in page.url:
            return True
        await page.wait_for_timeout(100)

    return "/#/login" in page.url


async def _login(page, email: str, password: str) -> bool:
    """
    Authenticate through the real Juice Shop login flow.

    Authentication is validated from the login response/session state, not by
    navigating to a particular profile page or requiring a profile locator.
    This keeps the precondition independent from page-specific UI changes.

    The Juice Shop is an Angular SPA backed by REST endpoints. The documented
    login flow uses /#/login and the backend exposes /rest/user/login and
    /rest/user/whoami. The latter is useful as a protected-session signal, but
    the login response itself is the primary success criterion here because
    the browser application's Authorization state is managed by the frontend.
    """
    try:
        await page.goto(
            f"{settings.base_url}/#/login",
            wait_until="domcontentloaded",
            timeout=settings.navigation_timeout_ms,
        )

        email_field = await resolve(
            page, {"label": "Email", "exact": False}
        )
        password_field = await resolve(
            page, {"label": "Password", "exact": False}
        )
        login = await resolve(
            page,
            {"role": "button", "name": "Login", "exact": False},
        )

        if email_field is None or password_field is None or login is None:
            return False

        await _fill(email_field, email)
        await _fill(password_field, password)

        # The login request is the authoritative UI->backend authentication
        # boundary. Do not infer authentication merely from a URL transition.
        try:
            async with page.expect_response(
                lambda response: (
                    response.request.method == "POST"
                    and "/rest/user/login" in response.url
                ),
                timeout=settings.action_timeout_ms,
            ) as response_info:
                await _click(login)

            response = await response_info.value

            if not response.ok:
                return False

            try:
                payload = await response.json()
            except Exception:
                payload = {}

            # Current Juice Shop login responses contain authentication/token
            # information. Accept either the current nested representation or
            # a flat token field so the precondition remains version-tolerant.
            authentication = (
                payload.get("authentication")
                if isinstance(payload, dict)
                else None
            )
            token = None

            if isinstance(authentication, dict):
                token = authentication.get("token")

            if token is None and isinstance(payload, dict):
                token = payload.get("token")

            if not token:
                return False

        except Exception:
            # If the response observer missed the request because the local
            # browser/application completed it before the observer attached,
            # do not silently declare authentication successful. Give the SPA
            # a short settle period and verify its authenticated state instead.
            await page.wait_for_timeout(250)

            if "/#/login" in page.url:
                return False

            token = await page.evaluate(
                """() => {
                    try {
                        return localStorage.getItem('token') || null;
                    } catch (_) {
                        return null;
                    }
                }"""
            )

            if not token:
                return False

        # Give Angular a chance to finish updating the authenticated session.
        await page.wait_for_timeout(150)

        # /rest/user/whoami is an authenticated Juice Shop endpoint and is a
        # useful secondary consistency check. We intentionally do not require
        # its response to be parsed through page.request because the Angular
        # application may add its Authorization header through an interceptor.
        #
        # Instead, verify that the browser has the token that the frontend
        # stores after a successful login.
        browser_token = await page.evaluate(
            """() => {
                try {
                    return localStorage.getItem('token') || null;
                } catch (_) {
                    return null;
                }
            }"""
        )

        return bool(browser_token or token)

    except Exception:
        return False

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

    actions_text = json.dumps(scenario.get("actions", []), ensure_ascii=False)
    if (
        str(scenario.get("domain", "")).upper() == "IDT"
        and "${SCENARIO_EMAIL}" not in actions_text
    ):
        runtime = scenario.setdefault("_runtime_data", {})
        runtime.setdefault(
            "auth_email",
            f"cen-{scenario['id'].lower()}-{uuid.uuid4().hex[:10]}@example.com",
        )
        return await ensure_user(
            page,
            runtime["auth_email"],
            scenario_password(scenario),
        )

    return await ensure_user(
        page,
        scenario_email(scenario),
        scenario_password(scenario),
    )


async def ensure_base_user(page) -> bool:
    return await ensure_user(
        page,
        settings.user_email,
        settings.user_password,
    )



async def _ensure_card_via_api(page) -> bool:
    """Ensure a reusable test card exists without exercising the card-creation UI."""
    headers = await _auth_headers(page)
    payload = {
        "fullName": "Cliente Teste",
        "cardNum": 4000000000000002,
        "expMonth": 12,
        "expYear": 2030,
    }
    try:
        result = await page.evaluate(
            """async ({ url, payload, headers }) => {
                const request = async (options) => {
                    const controller = new AbortController();
                    const timer = setTimeout(() => controller.abort(), 5000);
                    try {
                        return await fetch(url, {
                            credentials: "include",
                            ...options,
                            signal: controller.signal
                        });
                    } finally {
                        clearTimeout(timer);
                    }
                };

                try {
                    const getResponse = await request({
                        method: "GET",
                        headers
                    });

                    if (getResponse.ok) {
                        const body = await getResponse.json();
                        const cards = body && Array.isArray(body.data) ? body.data : [];
                        if (cards.some(card => String(card.cardNum).endsWith("0002"))) {
                            return { ok: true };
                        }
                    }

                    const postResponse = await request({
                        method: "POST",
                        headers: {
                            ...headers,
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(payload)
                    });
                    return { ok: postResponse.ok };
                } catch (_) {
                    return { ok: false };
                }
            }""",
            {
                "url": f"{settings.base_url}/api/Cards/",
                "payload": payload,
                "headers": headers,
            },
        )
        return bool(result and result.get("ok"))
    except Exception:
        return False


async def _auth_headers(page) -> dict:
    token = await page.evaluate(
        """() => localStorage.getItem('token') || null"""
    )
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    email = await page.evaluate(
        """() => localStorage.getItem('email') || null"""
    )
    if email:
        headers["X-User-Email"] = str(email)
    return headers


async def _ensure_address_via_api(page) -> bool:
    """Seed a valid address through the same REST API used by the UI.
    
    This is a precondition helper, not the behavior under test. It is used only
    when the UI form cannot persist the required fixture, keeping checkout
    scenarios independent from the current address-form presentation.
    """
    headers = await _auth_headers(page)
    payload = {
        "country": "Brazil",
        "fullName": "Cliente Teste",
        "mobileNum": 8599999999,
        "zipCode": "60000000",
        "streetAddress": "Rua Teste, 100",
        "city": "Fortaleza",
        "state": "CE",
    }
    try:
        # Use the browser context so the request shares the same session as
        # the Angular application (cookie + localStorage + auth headers).
        # Every request is independently bounded so a stalled backend cannot
        # block the whole CHK domain.
        result = await page.evaluate(
            """async ({ url, payload, headers }) => {
                const request = async (options) => {
                    const controller = new AbortController();
                    const timer = setTimeout(() => controller.abort(), 5000);
                    try {
                        return await fetch(url, {
                            credentials: "include",
                            ...options,
                            signal: controller.signal
                        });
                    } finally {
                        clearTimeout(timer);
                    }
                };

                try {
                    const getResponse = await request({
                        method: "GET",
                        headers
                    });

                    if (getResponse.ok) {
                        const body = await getResponse.json();
                        const addresses = body && Array.isArray(body.data)
                            ? body.data
                            : [];
                        if (addresses.length > 0) {
                            return { ok: true };
                        }
                    }

                    const postResponse = await request({
                        method: "POST",
                        headers: {
                            ...headers,
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(payload)
                    });

                    return { ok: postResponse.ok };
                } catch (_) {
                    return { ok: false };
                }
            }""",
            {
                "url": f"{settings.base_url}/api/Addresss/",
                "payload": payload,
                "headers": headers,
            },
        )
        return bool(result and result.get("ok"))
    except Exception:
        return False


async def _add_address_if_needed(page) -> bool:
    """Ensure an address is persisted using the real address UI first.

    The checkout precondition must exercise the application's own address
    form whenever possible. REST is retained only as a bounded fallback for
    environments where the form cannot persist the fixture.
    """
    existing = page.locator("mat-radio-button, [role='radio']")
    try:
        for index in range(await existing.count()):
            radio = existing.nth(index)
            if not await radio.is_visible():
                continue
            text = _normalize_text(await radio.inner_text())
            if text:
                return True
    except Exception:
        pass

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
        await page.wait_for_timeout(250)

        values = [
            ("Country", "Brazil"),
            ("Name", "Cliente Teste"),
            ("Mobile Number", "8599999999"),
            ("ZIP Code", "60000000"),
            ("Address", "Rua Teste, 100"),
            ("City", "Fortaleza"),
            ("State", "CE"),
        ]

        for label, value in values:
            field = await resolve(page, {"label": label, "exact": False})
            if field is None:
                break
            await _fill(field, value)
        else:
            submit = await resolve(
                page,
                {"role": "button", "name": "Submit", "exact": False},
            )
            if submit is None:
                submit = await resolve(page, {"css": "#submitButton"})

            if submit is not None:
                deadline = __import__("time").monotonic() + settings.action_timeout_ms / 1000
                while __import__("time").monotonic() < deadline:
                    try:
                        if await submit.is_enabled():
                            break
                    except Exception:
                        pass
                    await page.wait_for_timeout(100)

                try:
                    if await submit.is_enabled():
                        await _click(submit)
                        deadline = __import__("time").monotonic() + settings.action_timeout_ms / 1000
                        while __import__("time").monotonic() < deadline:
                            if "/#/address/create" not in page.url:
                                break
                            await page.wait_for_timeout(100)

                        # The real AddressComponent reloads the saved-address
                        # list after navigation. Verify the row, not merely the
                        # route transition.
                        if "/#/address/create" not in page.url:
                            try:
                                radios = page.locator("mat-radio-button, [role='radio']")
                                for index in range(await radios.count()):
                                    radio = radios.nth(index)
                                    if await radio.is_visible() and _normalize_text(await radio.inner_text()):
                                        return True
                            except Exception:
                                pass
                        # Some versions return to the selection screen with
                        # Angular still loading. Reload only after the form has
                        # actually left /address/create.
                        if "/#/address/create" not in page.url:
                            await page.wait_for_timeout(250)
                except Exception:
                    pass

    # Bounded fallback: use the same REST resource AddressService uses.
    # This is only fixture recovery and never the primary interaction.
    if await _ensure_address_via_api(page):
        await page.goto(
            f"{settings.base_url}/#/address/select",
            wait_until="domcontentloaded",
        )
        deadline = __import__("time").monotonic() + settings.action_timeout_ms / 1000
        while __import__("time").monotonic() < deadline:
            try:
                radios = page.locator("mat-radio-button, [role='radio']")
                for index in range(await radios.count()):
                    radio = radios.nth(index)
                    if await radio.is_visible() and _normalize_text(await radio.inner_text()):
                        return True
            except Exception:
                pass
            await page.wait_for_timeout(150)

    return False

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
    await page.goto(
        f"{settings.base_url}/#/address/select",
        wait_until="domcontentloaded",
    )
    if not await _add_address_if_needed(page):
        return False

    if not select:
        return True

    # Angular stores the selected address id in component state and enables
    # Continue only after that state changes. Prefer the real radio, then
    # use its table row as the generic interaction fallback.
    radio = None
    for _ in range(20):
        radio = await resolve(
            page,
            {"role": "radio", "name": "Address", "exact": False},
        )
        if radio is not None:
            break
        await page.wait_for_timeout(150)

    if radio is None:
        return False

    await _click(radio)

    # Current Juice Shop wires selection through the radio click and the
    # containing Material table row. Verify the component state via Continue;
    # if Angular has not propagated it yet, re-click the row once.
    continue_button = None
    for _ in range(20):
        continue_button = await resolve(
            page,
            {"role": "button", "name": "Continue", "exact": False},
        )
        if continue_button is not None:
            try:
                if await continue_button.is_enabled():
                    break
            except Exception:
                pass
        await page.wait_for_timeout(150)

    if continue_button is None:
        return False

    try:
        if not await continue_button.is_enabled():
            row = radio.locator(
                "xpath=ancestor::*[self::mat-row or self::tr or @role='row'][1]"
            )
            if await row.count() and await row.first.is_visible():
                await row.first.click(timeout=1500)
                await page.wait_for_timeout(150)
    except Exception:
        pass

    continue_button = await resolve(
        page,
        {"role": "button", "name": "Continue", "exact": False},
    )
    if continue_button is None:
        return False

    try:
        if not await continue_button.is_enabled():
            return False
    except Exception:
        return False

    await _click(continue_button)

    deadline = __import__("time").monotonic() + settings.action_timeout_ms / 1000
    while __import__("time").monotonic() < deadline:
        if "/#/delivery-method" in page.url:
            return True
        await page.wait_for_timeout(100)

    return False

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

    # DeliveryMethodComponent updates deliveryMethodId from the radio click
    # and from the containing mat-row. The row is the generic recovery path
    # for Angular Material event propagation delays.
    continue_button = None
    for _ in range(20):
        continue_button = await resolve(
            page,
            {"role": "button", "name": "Continue", "exact": False},
        )
        if continue_button is not None:
            try:
                if await continue_button.is_enabled():
                    break
            except Exception:
                pass
        await page.wait_for_timeout(150)

    if continue_button is None:
        return False

    # Angular Material can render the radio host before its selection state
    # reaches the checkout component. Re-click its row only when Continue
    # remains disabled; this is a generic state-recovery mechanism.
    try:
        if not await continue_button.is_enabled():
            row = delivery.locator(
                "xpath=ancestor::*[self::mat-row or self::tr or @role='row'][1]"
            )
            if await row.count() and await row.first.is_visible():
                await row.first.click(timeout=1500)
                await page.wait_for_timeout(150)
    except Exception:
        pass

    continue_button = await resolve(
        page,
        {"role": "button", "name": "Continue", "exact": False},
    )
    if continue_button is None:
        return False
    try:
        if not await continue_button.is_enabled():
            return False
    except Exception:
        return False

    await _click(continue_button)
    deadline = __import__("time").monotonic() + settings.action_timeout_ms / 1000
    while __import__("time").monotonic() < deadline:
        if "/#/payment/shop" in page.url:
            return True
        await page.wait_for_timeout(100)

    return False

async def ensure_card(page) -> bool:
    if "/#/payment/shop" not in page.url:
        return False

    existing = await resolve(
        page,
        {"role": "radio", "name": "0002", "exact": False},
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
        ("Card Number", "4000000000000002"),
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
        {"role": "radio", "name": "0002", "exact": False},
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
        {"role": "radio", "name": "0002", "exact": False},
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
    """
    Prepare only the state explicitly required by the scenario precondition.

    The rules are metadata-driven (domain + precondition text), so no scenario
    ID is used as a locator or as a special execution branch.
    """
    if not await ensure_authentication(page, scenario):
        return False, "Pré-condição de autenticação não pôde ser preparada."

    domain = str(scenario.get("domain", "")).upper()
    precondition = str(scenario.get("precondition", "")).casefold()

    if domain == "IDT" and "e-mail informado" in precondition:
        if not await ensure_base_user(page):
            return False, "Não foi possível preparar o usuário existente exigido pelo cenário."

    if domain == "CAR" and (
        "carrinho" in precondition
        and ("produto" in precondition or "produtos" in precondition)
    ):
        if not await ensure_basket(page):
            return False, "Pré-condição de carrinho não pôde ser preparada."

    if domain == "CHK":
        # Checkout preconditions describe the minimum state needed to reach
        # the scenario. They must not execute the behavior under test.
        # In particular, a scenario about adding/selecting a card must not
        # silently create/select a card before its own actions run.
        if "carrinho" in precondition or "produto no carrinho" in precondition:
            if not await ensure_basket(page):
                return False, "Pré-condição de carrinho não pôde ser preparada."

        if "há endereço cadastrado" in precondition:
            if not await ensure_address(page, select=False):
                return False, "Pré-condição de endereço cadastrado não pôde ser preparada."

        needs_selected_address = (
            "endereço de entrega selecionado" in precondition
            or "endereço selecionado" in precondition
        )
        if needs_selected_address:
            if not await ensure_address(page, select=True):
                return False, "Pré-condição de endereço selecionado não pôde ser preparada."

        needs_delivery = (
            "método de entrega selecionado" in precondition
            or "entrega selecionada" in precondition
            or "checkout acessível" in precondition
            or "checkout na etapa de pagamento" in precondition
            or "etapa de pagamento" in precondition
            or "pagamento acessível" in precondition
            or "seção de outras opções" in precondition
            or "checkout iniciado" in precondition
        )
        if needs_delivery:
            if not await ensure_delivery(page):
                return False, "Pré-condição de entrega/pagamento não pôde ser preparada."

        # Only scenarios that explicitly require an existing card should
        # prepare the payment method. This preserves the intended behavior
        # of CHK-07 (add card) and CHK-25 (payment without selection).
        if "cartão de teste cadastrado" in precondition:
            if not await ensure_card(page):
                return False, "Pré-condição de cartão cadastrado não pôde ser preparada."

        if (
            "pedido com endereço" in precondition
            or "pedido pronto para confirmação" in precondition
            or "resumo do pedido acessível" in precondition
            or "checkout preparados" in precondition
            or "checkout parcialmente preenchido" in precondition
            or "endereço, entrega e pagamento definidos" in precondition
            or "endereço, entrega e pagamento disponíveis" in precondition
        ):
            if not await ensure_order_summary(page):
                return False, "Pré-condição de resumo do pedido não pôde ser preparada."

        if (
            "pedido concluído" in precondition
            or "pedido no histórico" in precondition
            or "há pelo menos um pedido no histórico" in precondition
        ):
            if not await ensure_completed_order(page):
                return False, "Pré-condição de pedido concluído não pôde ser preparada."
    return True, ""
