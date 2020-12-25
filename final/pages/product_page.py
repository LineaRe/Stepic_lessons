from .base_page import BasePage
from .locators import ProductPageLocators


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.get(link)
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()

        self.should_be_name_product()
        self.should_be_price()

    def should_be_name_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text

        assert product_name == name_in_message

    def should_be_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE)
        price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text

        assert product_price == price_in_message

    def check_add_to_basket_notification(self):
        expected_notification_text = "has been added to your basket."
        actual_notification_text = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE).text
        print(actual_notification_text)

        assert expected_notification_text in actual_notification_text

    def should_be_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_MESSAGE)

    def delete_item_from_basket(self):
        self.browser.find_element(*ProductPageLocators.VIEW_BASKET).click()
        self.browser.find_element(*ProductPageLocators.DELETE_FROM_BASKET).click()

        assert self.is_not_element_present(*ProductPageLocators.BASKET_RESULT)











