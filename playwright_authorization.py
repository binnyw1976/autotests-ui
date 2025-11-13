from playwright.sync_api import sync_playwright, expect
from config import BASE_URL, EMAIL, PASSWORD, EMAIL_INPUT_SELECTOR, PASSWORD_INPUT_SELECTOR, LOGIN_BUTTON_SELECTOR, ALERT_SELECTOR, ALERT_TEXT

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL)

    # Заполняем email
    email_input = page.locator(EMAIL_INPUT_SELECTOR)
    email_input.fill(EMAIL)

    # Заполняем пароль
    password_input = page.locator(PASSWORD_INPUT_SELECTOR)
    password_input.fill(PASSWORD)

    # Нажимаем кнопку входа
    login_button = page.locator(LOGIN_BUTTON_SELECTOR)
    login_button.click()

    # Проверяем появление алерта
    wrong_email_or_password_alert = page.locator(ALERT_SELECTOR)
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text(ALERT_TEXT)

    page.wait_for_timeout(5000)
