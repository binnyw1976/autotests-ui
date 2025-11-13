# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # загружает переменные из .env

BASE_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

ALERT_TEXT = "Wrong email or password"