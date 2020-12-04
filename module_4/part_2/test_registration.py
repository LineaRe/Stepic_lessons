from selenium import webdriver
import time
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Arrange
fake = Faker()
reg_email = fake.email()
reg_password = "zxcvbnm1234567"

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
welcome_text_locator = "div.alertinner.wicon"
register_button_locator = "//div/form/button[contains(text(),'Зарегистрироваться')]"
main_login_locator = "Войти или зарегистрироваться"
email_entry_field_locator = "id_registration-email"
password_entry_field_locator = "id_registration-password1"
rep_password_entry_field_locator = "id_registration-password2"
welcome_text = "Спасибо за регистрацию!"
browser = webdriver.Chrome()


def test_new_user_registration():
    try:

        browser.get(main_page_link)
# Act
        browser.find_element_by_link_text(main_login_locator).click()

        input_login = browser.find_element_by_id(email_entry_field_locator)
        input_login.send_keys(reg_email)

        input_password = browser.find_element_by_id(password_entry_field_locator)
        input_password.send_keys(reg_password)

        input_repeat_password = browser.find_element_by_id(rep_password_entry_field_locator)
        input_repeat_password.send_keys(reg_password)

        browser.find_element_by_xpath(register_button_locator).click()

        welcome = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.alertinner.wicon"), "Спасибо за регистрацию!")
        )
# Assert
        welcome_message = browser.find_element_by_css_selector("div.alertinner.wicon").text

        assert welcome_text == welcome_message, "New user could not register"

    finally:
        time.sleep(7)
        browser.quit()


test_new_user_registration()
