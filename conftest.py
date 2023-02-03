import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', default='ru',
                     help="Choose browser: chrome or firefox")


@pytest.fixture
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    yield browser
    browser.quit()
