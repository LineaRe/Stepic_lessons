import pytest
from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"


class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
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

