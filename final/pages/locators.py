from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    PRODUCT_FORM = (By.CSS_SELECTOR, ".product.main")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")

    ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    PRODUCT_NAME_ACTUAL = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    MESSAGE_TEXT = ()
    SUCCESS_MESSAGE = ()
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner>p>strong")


    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
