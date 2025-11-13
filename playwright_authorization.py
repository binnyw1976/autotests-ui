from playwright.sync_api import sync_playwright, expect
from config import BASE_URL, ALERT_TEXT, EMAIL, PASSWORD

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL)

    # Заполняем email
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(EMAIL)

    # Заполняем пароль
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(PASSWORD)

    # Нажимаем кнопку входа
    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    # Проверяем появление алерта
    wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text(ALERT_TEXT)

    page.wait_for_timeout(5000)
