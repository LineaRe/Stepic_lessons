import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Language for autotests")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language not in ["ru", "en-GB", "es", "fr"]:
        raise pytest.UsageError("Test should contain language")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    print("\nstart browser for test..")
    web_page = webdriver.Chrome(options=options)
    # web_page.implicitly_wait(5)
    web_page.user_language = language

    yield web_page

    print("\nquit browser..")
    web_page.quit()
