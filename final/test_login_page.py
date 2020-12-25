from .pages.main_page import MainPage
from .pages.login_page import LoginPageLocators


link = ""


class TestLoginPage:
    def test_guest_can_create_account(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

