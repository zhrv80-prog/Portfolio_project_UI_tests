from playwright.sync_api import sync_playwright

from config import username, password
from helpers.auth_helper import login_via_ui, save_storage_state


def main():
    login = username()
    pwd = password()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        login_via_ui(page, login, pwd)
        save_storage_state(page)  # ← сохранит в корень проекта

        print("✅ state.json сгенерирован")
        browser.close()


if __name__ == "__main__":
    main()