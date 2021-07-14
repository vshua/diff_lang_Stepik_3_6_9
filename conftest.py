import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, es, fr")

@pytest.fixture(scope="function")
def browser(request):
    user_lang = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
    print("\nStart Chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nExit browser..")
    browser.quit()
