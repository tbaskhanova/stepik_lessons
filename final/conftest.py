import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose language: ru,en-GB,fr or es")


@pytest.fixture()
def language(request):
    return request.config.getoption("--language")


@pytest.fixture()
def browser(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    # now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # browser.save_screenshot('screenshot-%s.png' % now)
    browser.quit()
