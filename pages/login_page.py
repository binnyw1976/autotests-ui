from config import BASE_URL


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')

    def navigate(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.login_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()