import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import FirefoxProfile


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Language for autotests")
    parser.addoption("--browser", action="store", default="chrome", help="Browser for webdriver usage")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language not in ["ru", "en-GB", "es", "fr"]:
        raise pytest.UsageError("Test should contain language")

    driver = request.config.getoption("browser")

    if driver not in ["chrome", "firefox"]:
        raise pytest.UsageError("I don't know your browser, bitch!")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    profile = FirefoxProfile()
    profile.set_preference("intl.accept_languages", language)

    print("\nstart " + driver + " for test..")
    if driver == "chrome":
        web_page = webdriver.Chrome(options=options)
    else:
        web_page = webdriver.Firefox(firefox_profile=profile)
        # web_page.implicitly_wait(5)
    web_page.user_language = language

    yield web_page

    print("\nquit browser..")
    web_page.quit()
