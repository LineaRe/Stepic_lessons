#Arrange
#Data
main_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
basket_text_locator = "//div[2]/form/button"
language_locator = "[selected='selected']"

exp_btn_text_dict = {
    "ru": "Добавить в корзину",
    "en-GB": "Add to basket",
    "es": "Añadir al carrito",
    "fr": "Ajouter au panier"
}


def test_add_to_basket_btn(browser):
    expected_lang_code = browser.user_language
    exp_btn_text = exp_btn_text_dict[expected_lang_code]

    browser.get(main_page_link)
#Act
    button_add_to_basket = browser.find_element_by_xpath(basket_text_locator)
    successful_button_text = button_add_to_basket.text
#Assert
    assert exp_btn_text in successful_button_text, "Button text is incorrect"
