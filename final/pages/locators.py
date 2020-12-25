from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEARCH_BOX = (By.XPATH, "//form/div/input[@id='id_q']")
    SEARCH_BUTTON = (By.XPATH, "//form/input[@class='btn btn-default']")
    NUMBER_OF_ITEMS = (By.XPATH, "//div/form/strong[1]")
    LANGUAGE_LIST = (By.XPATH, "//div/select[@name='language']")
    LANGUAGE_SELECT = (By.TAG_NAME, "select")
    GO_BUTTON = (By.CSS_SELECTOR, "#language_selector > button")
    RU_TEXT = (By.XPATH, "//div/strong[contains(text(),'Всего в корзине')]")
    ENG_TEXT = (By.TAG_NAME, "h2")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ENTRY_FIELD = (By.ID, "id_registration-email")
    PASSWORD_ENTRY_FIELD = (By.ID, "id_registration-password1")
    REPEAT_PASSWORD_ENTRY_FIELD = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    WELCOME_MESSAGE_ALERT = (By.CSS_SELECTOR, "div.alertinner.wicon")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    PRODUCT_FORM = (By.CSS_SELECTOR, ".product.main")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")

    ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")

    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner>p>strong")

    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    VIEW_BASKET = (By.XPATH, "//*[@id=\"default\"]/header/div[1]/div/div[2]/span/a")
    DELETE_FROM_BASKET = (By.XPATH, "//*[@id=\"basket_formset\"]/div/div/div[3]/div[2]/a")
    BASKET_RESULT = (By.XPATH, "//*[@id=\"basket_formset\"]")
