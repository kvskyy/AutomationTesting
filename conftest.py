import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
from pom.index_page import Authorization


@pytest.fixture(scope='function')
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.binary_location = r"/Users/new/Library/Application Support/Google/Chrome/Default"  # chrome binary location specified here
    options.add_argument("--start-maximized")  # open Browser in maximized mode
    options.add_argument("--no-sandbox")  # bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    return options


@pytest.fixture(scope='function')
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome()
    return driver


# this fixture helps us to open/quit driver after every tests
@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def setup_auth(get_webdriver):
    driver = get_webdriver
    auth = Authorization(driver)
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    auth.perform_login()
    yield driver
    driver.quit()


# this fixture helps us to get screenshot of UI tests only in case of failed result
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:
            try:
                allure.attach(item.instance.driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)      #?
            except Exception as e:
                print(e)
