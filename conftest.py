from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from config import BASE_URL, username, password
from helpers.auth_helper import login_via_ui

STATE_FILE = Path(__file__).parent / "state.json"


@pytest.fixture(scope="function")
def logged_in_page():
    """
    Возвращает страницу с уже выполненным логином.

    Логика:
    - Если state.json существует — используем его (быстро, без UI-логина).
    - Если нет — логинимся через UI (fallback для локального запуска).
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        if STATE_FILE.exists():
            # Быстрый путь: сессия из state.json
            context = browser.new_context(storage_state=str(STATE_FILE))
            page = context.new_page()
            page.goto(f"{BASE_URL}inventory.html")

            # Проверяем, что сессия валидна (не редиректнуло на логин)
            if "/inventory.html" not in page.url:
                # Сессия протухла — логинимся заново
                context.close()
                context = browser.new_context()
                page = context.new_page()
                login_via_ui(page, username(), password())
        else:
            # Fallback: логин через UI
            context = browser.new_context()
            page = context.new_page()
            login_via_ui(page, username(), password())

        yield page

        context.close()
        browser.close()