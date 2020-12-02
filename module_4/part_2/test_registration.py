from selenium import webdriver
import time
import pytest

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
welcome_text_locator = "alertinner"
register_button_locator = "//div/form/button[contains(text(),'Зарегистрироваться')]"
main_login_locator = "Войти или зарегистрироваться"
email_entry_field_locator = "id_registration-email"
password_entry_field_locator = "id_registration-password1"
reg_email = "opopopopo@test.com"
reg_password = "zxcvbnm1234567"

welcome_text = "Спасибо за регистрацию!"
browser = webdriver.Chrome()


def test_new_user_registration():
    try:

        browser.get(main_page_link)

        browser.find_element_by_link_text(main_login_locator).click()

        input_login = browser.find_element_by_id(email_entry_field_locator)
        input_login.send_keys(reg_email)

        input_password = browser.find_element_by_id(password_entry_field_locator)
        input_password.send_keys(reg_password)

        input_repeat_password = browser.find_element_by_id()
        input_repeat_password.send_keys(reg_password)

        browser.find_element_by_xpath(register_button_locator).click()

        #waiting for welcome text

        welcome_message = browser.find_element_by_css_selector(welcome_text_locator).text

        assert welcome_text == welcome_message, "New user"

    finally:
        time.sleep(10)
        browser.quit()