from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from config import BASE_URL, username, password
from helpers.auth_helper import login_via_ui

STATE_FILE = Path(__file__).parent / "state.json"


@pytest.fixture(scope="function")
def clean_page():
    """Чистая страница (без логина) — для тестов логина."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def logged_in_page():
    """Страница с логином (state.json или fallback) — для остальных тестов."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        if STATE_FILE.exists():
            context = browser.new_context(storage_state=str(STATE_FILE))
            page = context.new_page()
            page.goto(f"{BASE_URL}inventory.html")
            if "/inventory.html" not in page.url:
                context.close()
                context = browser.new_context()
                page = context.new_page()
                login_via_ui(page, username(), password())
        else:
            context = browser.new_context()
            page = context.new_page()
            login_via_ui(page, username(), password())

        yield page
        context.close()
        browser.close()
