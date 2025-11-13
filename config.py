# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # загружает переменные из .env

BASE_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

EMAIL_INPUT_SELECTOR = '//div[@data-testid="login-form-email-input"]//div//input'
PASSWORD_INPUT_SELECTOR = '//div[@data-testid="login-form-password-input"]//div//input'
LOGIN_BUTTON_SELECTOR = '//button[@data-testid="login-page-login-button"]'
ALERT_SELECTOR = '//div[@data-testid="login-page-wrong-email-or-password-alert"]'
ALERT_TEXT = "Wrong email or password"