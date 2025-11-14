# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # загружает переменные из .env

BASE_URL = "http://dezodemius.ru:7001/"

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")