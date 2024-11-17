import pytest
import os

from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='120.0'
    )
    parser.addoption(
        '--browser_url'
    )


def set_local_browser():
    options = webdriver.FirefoxOptions()
    browser.config.driver_options = options


def set_remote_browser(url, browser_version):
    DEFAULT_BROWSER_VERSION = "120.0"

    selenoid_login = os.getenv('LOGIN')
    selenoid_pass = os.getenv('PASSWORD')

    browser_version = browser_version if browser_version else DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{url}/wd/hub",
        options=options)
    browser.config.driver = driver


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def browser_set(request, load_env):
    selenoid_url = request.config.getoption('--browser_url')
    if selenoid_url:
        set_remote_browser(selenoid_url, request.config.getoption('--browser_version'))
    else:
        set_local_browser()

    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    browser.config.base_url = 'https://bps-iss.ru'

    yield
    if selenoid_url:
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)

    browser.quit()
