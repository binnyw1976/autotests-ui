from playwright.sync_api import sync_playwright, expect
from config import BASE_URL, LOGIN, PASSWORD

class TestUserLogin:
    def test_empty_login(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(BASE_URL)

            # Заполняем login
            login_input = page.get_by_test_id('login-form-email-input').locator('input')
            login_input.fill(LOGIN)

            # Заполняем пароль
            password_input = page.get_by_test_id('login-form-password-input').locator('input')
            password_input.fill(PASSWORD)

            # Нажимаем кнопку входа
            login_button = page.get_by_test_id('login-page-login-button')
            login_button.click()

    def test_empty_password(self):
        ...

    def test_valid_login(self):
        ...