from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self, email: str, password: str) -> None:
        self.page.fill(LoginLocators.EMAIL_INPUT, email)
        self.page.fill(LoginLocators.PASSWORD_INPUT, password)
        self.page.click(LoginLocators.LOGIN_BUTTON)
