import allure
from playwright.sync_api import expect

from config import username, password
from helpers.auth_helper import login_via_ui


@allure.feature("Login")
@allure.story("Successful login")
def test_login_success(clean_page):
    """Проверяет, что логин с валидными данными работает."""
    login_via_ui(clean_page, username(), password())

    with allure.step("Verify redirect to inventory"):
        assert "/inventory.html" in clean_page.url, f"Got {clean_page.url}"

    with allure.step("Verify inventory items are visible"):
        expect(clean_page.locator(".inventory_item").first).to_be_visible()