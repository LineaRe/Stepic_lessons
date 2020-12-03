from selenium import webdriver
import time
import pytest


main_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
basket_text_locator = "//div[2]/form/button"

basket_tr_text = "Добавить в корзину"
browser = webdriver.Chrome()
ru_basket_text = ""
en_basket_test = ""
es_basket_test = ""
fr_basket_test = ""



@pytest.mark.parametrize('language', ["ru", "en-gb", "es", "fr"])
def test_basket_text(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{language}/"
    browser.get(link)
    browser.find_element_by_xpath(basket_text_locator)
    try:
        basket_text = browser.find_element_by_xpath(basket_text_locator).text
        assert basket_tr_text == basket_text, "Test passed"

    finally:
        time.sleep(10)
        browser.quit()


test_basket_text()