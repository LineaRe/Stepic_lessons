from .locators import LoginPageLocators
from .locators import MainPageLocators
from .base_page import BasePage
from faker import Faker

#Data
fake = Faker()
reg_email = fake.email()
reg_password = "zxcvbnm1234567"
welcome_text = "Thanks for registering!"


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

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def fill_registration_fields_and_register_eng(self):
        self.browser.find_element(*LoginPageLocators.EMAIL_ENTRY_FIELD).send_keys(reg_email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_ENTRY_FIELD).send_keys(reg_password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_ENTRY_FIELD).send_keys(reg_password)

        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        welcome_message = self.browser.find_element(*LoginPageLocators.WELCOME_MESSAGE_ALERT).text

        assert welcome_text == welcome_message, "New user could not register"

