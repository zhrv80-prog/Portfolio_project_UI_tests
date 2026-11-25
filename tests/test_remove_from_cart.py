import re

import allure
from playwright.sync_api import expect


@allure.feature("Cart")
@allure.story("Remove item from cart (inventory page)")
def test_remove_item_from_cart_on_inventory(logged_in_page):
    """Проверяет удаление товара через кнопку 'Remove' на странице товаров."""
    page = logged_in_page

    with allure.step("Add Sauce Labs Backpack to cart"):
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    with allure.step("Verify button changed to 'Remove'"):
        expect(
            page.locator('[data-test="remove-sauce-labs-backpack"]')
        ).to_be_visible()

    with allure.step("Click 'Remove' on inventory page"):
        page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    with allure.step("Verify cart badge is gone"):
        expect(page.locator(".shopping_cart_badge")).to_have_count(0)

    with allure.step("Verify button changed back to 'Add to cart'"):
        expect(
            page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        ).to_be_visible()

    with allure.step("Open cart and verify it is empty"):
        page.locator(".shopping_cart_link").click()
        expect(page).to_have_url(re.compile(r".*/cart\.html"))
        expect(page.locator(".cart_item")).to_have_count(0)