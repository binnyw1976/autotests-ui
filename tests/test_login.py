import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from config import LOGIN, PASSWORD

class TestUserLogin:
    def test_empty_login(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("", PASSWORD)
        # Добавьте проверку сообщения об ошибке:
        expect(page.get_by_text("Email is required")).to_be_visible()

    def test_empty_password(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(LOGIN, "")
        expect(page.get_by_text("Password is required")).to_be_visible()

    def test_valid_login(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(LOGIN, PASSWORD)
        # Проверка успешного входа — например, появление аватара или редирект
        expect(page.get_by_role("link", name="Profile")).to_be_visible()