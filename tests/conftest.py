import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def browser_set():
    options = webdriver.FirefoxOptions()

    browser.config.driver_options = options
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    browser.config.base_url = 'https://bps-iss.ru'