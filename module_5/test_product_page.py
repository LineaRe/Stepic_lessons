from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest

class TestProductPage:

    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()


