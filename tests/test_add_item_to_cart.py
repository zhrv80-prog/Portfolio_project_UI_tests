import re
import allure
from playwright.sync_api import expect


@allure.feature("Cart")
@allure.story("Add item to cart")
def test_add_item_to_cart(logged_in_page):
    """Проверяет, что товар добавляется в корзину и счётчик обновляется."""
    page = logged_in_page

    with allure.step("Add Sauce Labs Backpack to cart"):
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    with allure.step("Verify cart badge shows 1"):
        badge = page.locator(".shopping_cart_badge")
        expect(badge).to_be_visible()
        expect(badge).to_have_text("1")

    with allure.step("Verify button changed to 'Remove'"):
        expect(
            page.locator('[data-test="remove-sauce-labs-backpack"]')
        ).to_be_visible()

    with allure.step("Open cart page and verify item is there"):
        page.locator(".shopping_cart_link").click()
        expect(page).to_have_url(re.compile(r".*/cart\.html"))
        expect(page.locator(".cart_item")).to_have_count(1)
        expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
