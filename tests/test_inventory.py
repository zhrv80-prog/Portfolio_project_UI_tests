# tests/test_inventory.py
import allure


@allure.feature("Inventory")
def test_inventory_page_has_items(logged_in_page):
    """Проверяет, что на странице товаров есть товары."""
    count = logged_in_page.locator(".inventory_item").count()
    assert count > 0, f"Expected items, got {count}"
