from selenium import webdriver
import time


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
error_text_locator = "//div[@class='alert alert-danger']"
login_button_locator = "//div/form/button[contains(text(),'Войти')]"
main_login_locator = "Войти или зарегистрироваться"
login_entry_field_locator = "id_login-username"
password_entry_field_locator = "id_login-password"
browser = webdriver.Chrome()

def test_new_user_registration():
    try:

        browser.get(main_page_link)

        browser.find_element_by_link_text("Войти или зарегистрироваться").click()

        input1 = browser.find_element_by_id("id_login-username")
        input1.send_keys("test@test.com")

        input1 = browser.find_element_by_id("id_login-password")
        input1.send_keys("123456789")

        browser.find_element_by_xpath("//div/form/button[contains(text(),'Войти')]").click()

        error_text = browser.find_element_by_xpath("//div[@class='alert alert-danger']").text

        assert error_text == "Опаньки! Мы нашли какие-то ошибки - пожалуйста, проверьте сообщения об ошибках ниже и попробуйте еще раз"
        print("Тест 6: Невозможно залогиниться")


    finally:

        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()