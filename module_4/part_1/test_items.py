#тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину с корректным текстом.
# Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.

from selenium import webdriver
import time
import pytest


main_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
basket_text_locator = "//div[2]/form/button"

basket_tr_text = "Добавить в корзину"
browser = webdriver.Chrome()


def test_basket_text():
    try:

        browser.get(main_page_link)

        basket_text = browser.find_element_by_xpath(basket_text_locator).text

        assert basket_tr_text == basket_text, "Test passed"

    finally:
        time.sleep(10)
        browser.quit()


test_basket_text()