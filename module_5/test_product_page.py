from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
# link_new_year = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class TestProductPage:

    def test_guest_can_add_product_to_basket(self, browser):
        # Data
        template = "{} has been added to your basket."
        product_name = "The shellcoder's handbook"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()

    def test_guest_can_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.check_add_to_basket_notification()

    @pytest.mark.xfail(reason="fixing in progress")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_disappeared()

    @pytest.mark.xfail(reason='won`t fix')
    def test_delete_item_from_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.delete_item_from_basket()



