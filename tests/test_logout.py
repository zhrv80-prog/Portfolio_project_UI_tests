import re

import allure
from playwright.sync_api import expect

from config import BASE_URL


@allure.feature("Logout")
@allure.story("Successful logout")
def test_logout(logged_in_page):
    """Проверяет, что logout возвращает на страницу логина."""
    page = logged_in_page

    with allure.step("Verify user is on inventory page"):
        expect(page).to_have_url(re.compile(r".*/inventory\.html"))

    with allure.step("Open burger menu"):
        page.locator("#react-burger-menu-btn").click()

    with allure.step("Click Logout"):
        page.locator("#logout_sidebar_link").click()

    with allure.step("Verify redirect to login page"):
        expect(page).to_have_url(f"{BASE_URL}")

    with allure.step("Verify login form is visible"):
        expect(page.locator('[data-test="login-button"]')).to_be_visible()
        expect(page.locator('[data-test="username"]')).to_be_visible()

    with allure.step("Verify user is NOT logged in"):
        assert "/inventory.html" not in page.url, (
            f"User should be logged out, but got {page.url}"
        )