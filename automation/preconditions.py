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
    """Return an email unique to this scenario execution.

    The runtime fixture is intentionally scoped to the scenario object, so
    one scenario never reuses the account created by another scenario or by a
    previous execution. This keeps authentication-dependent tests isolated
    without hard-coding scenario-specific behavior.
    """
    runtime = scenario.setdefault("_runtime_data", {})
    return runtime.setdefault(
        "scenario_email",
        f"cen-{scenario['id'].lower()}-{uuid.uuid4().hex[:10]}@example.com",
    )


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

        # Juice Shop still exposes legacy server-rendered routes (for example
        # /profile) that authenticate through the historical token cookie,
        # while the Angular SPA stores the same JWT in localStorage. Bridge
        # the two representations after a real login.
        if browser_token or token:
            try:
                await page.context.add_cookies([{
                    "name": "token",
                    "value": str(browser_token or token),
                    "url": settings.base_url,
                    "path": "/",
                }])
            except Exception:
                pass

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
        "expYear": 2090,
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


async def _ensure_address_via_api(page, required_street: str | None = None) -> bool:
    """Ensure one persisted address exists for the authenticated fixture user.

    The checkout UI reads addresses from GET /api/Addresss. The official
    Juice Shop API creates an address with POST /api/Addresss and returns the
    created record with HTTP 201. Therefore this fixture only reports success
    after verifying that exact persisted record can be read back by the same
    authenticated browser session.
    """
    headers = await _auth_headers(page)
    payload = {
        "fullName": "Cliente Teste",
        "mobileNum": 8599999999,
        "zipCode": "60000000",
        "streetAddress": required_street or "Rua Teste, 100",
        "city": "Fortaleza",
        "state": "CE",
        "country": "Brazil",
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

                const readAddresses = async () => {
                    const response = await request({
                        method: "GET",
                        headers
                    });
                    if (!response.ok) {
                        return {
                            ok: false,
                            status: response.status,
                            addresses: []
                        };
                    }

                    let body = null;
                    try {
                        body = await response.json();
                    } catch (_) {}

                    return {
                        ok: true,
                        status: response.status,
                        addresses:
                            body && Array.isArray(body.data)
                                ? body.data
                                : []
                    };
                };

                try {
                    // Reuse an already persisted address. The checkout
                    // precondition is satisfied by existence of at least one
                    // address owned by the authenticated user.
                    const existing = await readAddresses();
                    if (existing.ok && existing.addresses.length > 0) {
                        const wantedStreet = String(requiredStreet || "").trim().toLowerCase();
                        const match = wantedStreet
                            ? existing.addresses.find(address =>
                                String(address && address.streetAddress || "").trim().toLowerCase() === wantedStreet
                              )
                            : existing.addresses[0];

                        if (match) {
                            return {
                                ok: true,
                                reused: true,
                                id: match.id
                            };
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

                    let postBody = null;
                    try {
                        postBody = await postResponse.json();
                    } catch (_) {}

                    // Juice Shop's address API creates the record with 201.
                    // A generic 2xx response is not sufficient evidence that
                    // the address is available to the checkout component.
                    if (postResponse.status !== 201) {
                        return {
                            ok: false,
                            status: postResponse.status,
                            body: postBody
                        };
                    }

                    const created =
                        postBody &&
                        postBody.data &&
                        postBody.data.id != null
                            ? postBody.data
                            : null;

                    if (!created) {
                        return {
                            ok: false,
                            status: postResponse.status,
                            body: postBody,
                            error: "A API não retornou o id do endereço criado."
                        };
                    }

                    const createdId = String(created.id);
                    const deadline = Date.now() + 4000;

                    while (Date.now() < deadline) {
                        const verification = await readAddresses();

                        if (verification.ok) {
                            const persisted = verification.addresses.some(
                                address =>
                                    address &&
                                    address.id != null &&
                                    String(address.id) === createdId
                            );

                            if (persisted) {
                                return {
                                    ok: true,
                                    created: true,
                                    id: created.id
                                };
                            }
                        }

                        await new Promise(resolve => setTimeout(resolve, 150));
                    }

                    return {
                        ok: false,
                        status: postResponse.status,
                        body: postBody,
                        error:
                            "O endereço foi aceito pelo POST, mas o mesmo id " +
                            "não apareceu no GET /api/Addresss."
                    };
                } catch (error) {
                    return {
                        ok: false,
                        error: String(error && error.message || error)
                    };
                }
            }""",
            {
                "url": f"{settings.base_url}/api/Addresss/",
                "payload": payload,
                "headers": headers,
                "requiredStreet": required_street,
            },
        )

        return bool(result and result.get("ok"))
    except Exception:
        return False

async def _add_address_if_needed(page, required_street: str | None = None) -> bool:
    """Ensure a persisted address exists for the current authenticated user.

    This helper prepares the DATA precondition only. It deliberately does not
    require the checkout radio/table to be rendered here, because scenarios
    such as CHK-03 test the address-selection UI themselves. Requiring a radio
    during fixture provisioning made the precondition depend on a particular
    Angular checkout rendering state and could leave the SPA on /#/address/create.
    """
    # 1) Prefer the authenticated REST API. A persisted address is the actual
    # precondition; rendering/selection is handled later by ensure_address().
    if await _ensure_address_via_api(page, required_street):
        return True

    # 2) UI fallback for environments where the REST fixture is unavailable.
    # The current Juice Shop address form uses Angular Signal Forms and the
    # submit control is #submitButton. Do not infer success from a route change:
    # verify that the authenticated API can read the saved address afterwards.
    await page.goto(
        f"{settings.base_url}/#/address/select",
        wait_until="domcontentloaded",
    )

    add = await resolve(
        page,
        {"role": "button", "name": "Add New Address", "exact": False},
    )
    if add is None:
        add = await resolve(
            page,
            {"role": "button", "name": "Add a new address", "exact": False},
        )
    if add is None:
        return False

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
            return False
        await _fill(field, value)

    submit = await resolve(page, {"css": "#submitButton"})
    if submit is None:
        submit = await resolve(
            page,
            {"role": "button", "name": "Submit", "exact": False},
        )
    if submit is None:
        return False

    deadline = __import__("time").monotonic() + settings.action_timeout_ms / 1000
    clicked = False
    while __import__("time").monotonic() < deadline:
        try:
            if await submit.is_enabled():
                await _click(submit)
                clicked = True
                break
        except Exception:
            pass
        await page.wait_for_timeout(100)

    if not clicked:
        return False

    # Signal Forms submit asynchronously through AddressService.save(). Give
    # the SPA time to finish the request, then verify persistence directly.
    deadline = __import__("time").monotonic() + settings.action_timeout_ms / 1000
    while __import__("time").monotonic() < deadline:
        if await _ensure_address_via_api(page):
            # The Signal Forms save uses Location.back(), but browser history
            # can leave the SPA on /#/address/create when the fallback was
            # entered from a redirected checkout state. The fixture contract is
            # only "address persisted"; return explicitly to the checkout
            # selection route so the scenario starts from a deterministic UI
            # state without depending on history behavior.
            await page.goto(
                f"{settings.base_url}/#/address/select",
                wait_until="domcontentloaded",
            )
            return True
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


async def _wait_for_address_option(page, timeout_ms: int | None = None):
    """Wait until the checkout address table exposes a selectable radio."""
    timeout = timeout_ms or settings.action_timeout_ms
    deadline = __import__("time").monotonic() + timeout / 1000
    while __import__("time").monotonic() < deadline:
        # The real address radio has no accessible name. Its identity is the
        # address row, so resolve the first visible radio in the checkout table
        # instead of inventing a name from the column header.
        radios = page.locator(
            "table mat-radio-button, table [role='radio'], "
            "mat-table mat-radio-button, mat-table [role='radio']"
        )
        try:
            for index in range(await radios.count()):
                radio = radios.nth(index)
                if await radio.is_visible():
                    return radio
        except Exception:
            pass
        await page.wait_for_timeout(150)
    return None

async def _restore_address_selection_ui(page) -> bool:
    """Recover a missing checkout address option without selecting it.

    The API fixture guarantees persistence, but the checkout component can
    still be rendered before Angular refreshes its address collection. When
    that happens, reload the real selector route and wait for the UI state
    instead of assuming that API success means the page is ready.
    """
    for _ in range(2):
        await page.goto(
            f"{settings.base_url}/#/address/select",
            wait_until="domcontentloaded",
        )
        radio = await _wait_for_address_option(page)
        if radio is not None:
            return True
        await page.reload(wait_until="domcontentloaded")
    return False


async def ensure_address(page, select: bool = False, required_street: str | None = None) -> bool:
    await page.goto(
        f"{settings.base_url}/#/address/select",
        wait_until="domcontentloaded",
    )
    if not await _add_address_if_needed(page, required_street):
        return False

    # A persisted address is not enough for checkout automation: the Angular
    # address selector must also be able to render it. This verification is
    # deliberately independent from scenario IDs and from the action under
    # test. If the selector is still empty, refresh the selector route rather
    # than letting Checkout redirect later to /#/address/create.
    if not await _restore_address_selection_ui(page):
        return False

    if not select:
        return True

    # Angular stores the selected address id in component state and enables
    # Continue only after that state changes. Prefer the real radio, then
    # use its table row as the generic interaction fallback.
    radio = await _wait_for_address_option(page)
    if radio is None:
        return False

    await _click(radio)

    # The radio's own click handler is the authoritative selection event.
    # Do not click the containing row as a second interaction: Angular
    # SelectionModel can toggle the same row twice and clear addressId().
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

    # No row fallback here. If Continue is still disabled, the selection
    # did not reach the component state and reporting the precondition as
    # unavailable is safer than toggling the selection back off.
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
        {"role": "radio", "text": "Standard Delivery", "exact": False},
    )
    if delivery is None:
        delivery = await resolve(
            page,
            {"role": "radio", "text": "Standard", "exact": False},
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
        {"role": "radio", "text": "0002", "exact": False},
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
    await _select_option(year, "2090")

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
        {"role": "radio", "text": "0002", "exact": False},
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
        {"role": "radio", "text": "0002", "exact": False},
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

        # Concrete address names in the precondition are treated as
        # data requirements, not scenario-specific automation rules.
        required_street = None
        street_match = __import__("re").search(r"endereço\s+([^;,.]+(?:,\s*\d+)?)", precondition, flags=__import__("re").IGNORECASE)
        if street_match:
            required_street = street_match.group(1).strip()

        if "há endereço cadastrado" in precondition:
            if not await ensure_address(page, select=False, required_street=required_street):
                return False, "Pré-condição de endereço cadastrado não pôde ser preparada."

        needs_selected_address = (
            "endereço de entrega selecionado" in precondition
            or "endereço selecionado" in precondition
        )
        if needs_selected_address:
            if not await ensure_address(page, select=True, required_street=required_street):
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
