from .base_page import BasePage
from .locators import ProductPageLocators


link_promo = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.open(link_promo)
        button_add_to_basket = self.browser.find.element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()

        self.solve_quiz_and_get_code()

        # self.should_be_name_product()
        # self.should_be_price()

    # def should_be_name_product(self):
    #     product_form = self.browser.find_element(*ProductPageLocators.PRODUCT_FORM)
    #     product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    #
    #
    # def should_be_price(self):



    # def check_add_to_basket_notification(self, expected_product_name, expected_notif_template):
    #     expected_notif_text = expected_notif_template.format(expected_product_name)
    #     actual_notif_text = self.browser.find_element(By.CSS_SELECTOR, ".alert:nth-child(1) aletinner").text
    #     assert actual_notif_text == expected_notif_text



