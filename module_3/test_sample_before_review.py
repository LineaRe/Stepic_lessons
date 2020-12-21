from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://selenium1py.pythonanywhere.com/ru/"
# 1. Поиск по Book - найти все эл-ты категории
try:
    browser = webdriver.Chrome()
    browser.get(link)

# ввести в поиск book,
    input0 = browser.find_element_by_xpath("//form/div/input[@id='id_q']")
    input0.send_keys("Book")
    browser.find_element_by_xpath("//form/input[@class='btn btn-default']").click()


# ищем все добавленные товары
    goods = browser.find_element_by_xpath("//div/form/strong[1]").text


# проверяем, что количество товаров равно 43
    assert goods == "43"
    print("Тест 1: Найдены все элементы категории Book")


finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# 2. Добавить товар в корзину # 3. Удалить товар из корзины
try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_link_text('Все товары').click()
    time.sleep(1)
    browser.find_element_by_link_text("The shellcoder's handbook")
    browser.find_element_by_xpath("//h3/a[contains(text(),'shellcoder')]").click()
    browser.find_element_by_xpath("//form/button[@class='btn btn-lg btn-primary btn-add-to-basket']").click()
    confirmation = browser.find_element_by_xpath("//div[@class='alertinner ']").text

    assert confirmation == "The shellcoder's handbook был добавлен в вашу корзину."

    print("Тест 2: Товар был добавлен в корзину")

    browser.find_element_by_link_text("Посмотреть корзину").click()
    browser.find_element_by_link_text("Удалить").click()
    cart = browser.find_element_by_xpath("//div/h2[contains(text(),'Товары в корзине')]").text

    if cart == 'Товары в корзине':
        print("Тест 3: Товар не удален из корзины")
    else:
        print("Тест 3: Товар удален из корзины")





finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# 4, 5 Сменить язык на английский и обратно

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath("//div/select[@name='language']").click()
    # находим элемент, содержащий текст
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("en-gb")

    browser.find_element_by_xpath("//div/form/button[contains(text(),'Выполнить')]").click()

    en_test = browser.find_element_by_tag_name('h2').text

    assert en_test == "Welcome!"
    print("Тест 4: Язык успешно изменен на английский")

    # обратная замена на русский
    browser.find_element_by_xpath("//div/select[@name='language']").click()
    # находим элемент, содержащий текст
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("ru")

    browser.find_element_by_xpath("//div/form/button[contains(text(),'Go')]").click()

# тут, наверное, необходимо добавить на сам сайт приветствие на русском языке, но проверку можно выполнить любым словом
    ru_test = browser.find_element_by_xpath("//div/strong[contains(text(),'Всего в корзине')]").text

    assert ru_test == "Всего в корзине:"
    print("Тест 5: Язык успешно изменен на русский")


finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# 6. Ввести неправильный логин\пароль - получить ошибку и отказ

try:

    browser = webdriver.Chrome()
    browser.get(link)

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
