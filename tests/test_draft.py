# tests/test_inventory.py
import allure


@allure.feature("Inventory")
def test_inventory_page_has_items(logged_in_page):
    """Проверяет, что на странице товаров есть товары."""
    count = logged_in_page.locator(".inventory_item").count()
    assert count > 0, f"Expected items, got {count}"


def test_add_to_cart(logged_in_page):
    """Проверяет добавление товара в корзину."""
    logged_in_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    badge = logged_in_page.locator(".shopping_cart_badge").text_content()
    assert badge == "1"