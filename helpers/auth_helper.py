from pathlib import Path

from playwright.sync_api import Page

from config import BASE_URL


from playwright.sync_api import Page, expect

def login_via_ui(page: Page, username: str, password: str) -> None:
    """Логинит пользователя через UI saucedemo.com."""
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()
    page.wait_for_url("**/inventory.html")
    expect(page.locator(".inventory_item").first).to_be_visible()

def save_storage_state(page: Page, path: str | Path | None = None) -> None:
    """Сохраняет cookies + localStorage в файл (по умолчанию — в корень проекта)."""
    if path is None:
        path = Path(__file__).parent.parent / "state.json"
    page.context.storage_state(path=str(path))