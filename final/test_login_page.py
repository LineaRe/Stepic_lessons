import pytest
from .pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.english
class TestLoginPage:
    def test_guest_can_create_account(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.fill_registration_fields_and_register_eng()





