from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.current_url()
        assert "login" in self.browser.current_url, "String 'login' is not in current url of browser"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
        # assert True