from selenium import webdriver
import time


# Arrange
main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
error_text_locator = "//div[@class='alert alert-danger']"
login_button_locator = "//div/form/button[contains(text(),'Войти')]"
main_login_locator = "Войти или зарегистрироваться"
login_entry_field_locator = "id_login-username"
password_entry_field_locator = "id_login-password"
wrong_login = "test@test.com"
wrong_password = "123456789"
error_message = "Опаньки! Мы нашли какие-то ошибки - пожалуйста, проверьте сообщения об ошибках ниже и попробуйте еще раз"


def test_wrong_login_pwd():
    # Ввести неправильный логин\пароль - получить ошибку и отказ

    try:

        browser = webdriver.Chrome()
        browser.get(main_page_link)
# Act
        browser.find_element_by_link_text(main_login_locator).click()

        input_login = browser.find_element_by_id(login_entry_field_locator)
        input_login.send_keys(wrong_login)

        input_password = browser.find_element_by_id(password_entry_field_locator)
        input_password.send_keys(wrong_password)

        browser.find_element_by_xpath(login_button_locator).click()
# Assert
        error_text = browser.find_element_by_xpath(error_text_locator).text

        assert error_text == error_message, "Login should not pass with wrong data"

    finally:

        time.sleep(10)
        browser.quit()


test_wrong_login_pwd()
