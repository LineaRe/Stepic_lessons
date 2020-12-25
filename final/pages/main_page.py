from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def url_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def find_items(self):
        self.browser.find_element(*MainPageLocators.SEARCH_BOX).send_keys("Book")
        self.browser.find_element(*MainPageLocators.SEARCH_BUTTON).click()
        goods = self.browser.find_element(*MainPageLocators.NUMBER_OF_ITEMS).text
        assert goods == "43"

    def change_language_to_russian(self):
        self.browser.find_element(*MainPageLocators.LANGUAGE_LIST).click()
        select = Select(self.browser.find_element(*MainPageLocators.LANGUAGE_SELECT))
        select.select_by_value("ru")
        self.browser.find_element(*MainPageLocators.GO_BUTTON).click()
        ru_test = self.browser.find_element(*MainPageLocators.RU_TEXT).text
        assert ru_test == "Всего в корзине:"

    def change_language_to_english(self):
        self.browser.find_element(*MainPageLocators.LANGUAGE_LIST).click()
        select = Select(self.browser.find_element(*MainPageLocators.LANGUAGE_SELECT))
        select.select_by_value("en-gb")
        self.browser.find_element(*MainPageLocators.GO_BUTTON).click()
        eng_test = self.browser.find_element(*MainPageLocators.ENG_TEXT).text
        assert eng_test == "Welcome!"


