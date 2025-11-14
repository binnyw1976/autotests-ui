from playwright.sync_api import sync_playwright, expect
from config import BASE_URL, LOGIN, PASSWORD

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL)

    # Заполняем login
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(LOGIN)

    # Заполняем пароль
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(PASSWORD)

    # Нажимаем кнопку входа
    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    page.wait_for_timeout(5000)
