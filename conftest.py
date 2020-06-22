"""  Фикстуры тестов сайта ticketland.ru """

import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from tools.listener_log import LogListener


def pytest_addoption(parser):
    """  Параметры, передаваемые в командную строку при запуске тестов """

    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption("--log_file",
                     default=None,
                     help="This is a file adress, where selenium logs will be")
    parser.addoption("--log_level",
                     default="INFO",
                     help="This is a log level parameter")
    parser.addoption("--executor", action="store", default="10.0.2.15",
                     help="This is ip for browser.Remote executor")


@pytest.fixture(scope="function")
def browser(request):
    """ Значение параметра --browser_name, переданного в команде pytest """

    logging.info('====Browser Fixture Started====')

    browser_name = request.config.getoption("--browser_name")

    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920x1080")
        options.add_experimental_option('w3c', False)
        driver = EventFiringWebDriver(webdriver.Chrome(options=options), LogListener(request))
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        options.add_argument("--window-size=1920x1080")
        driver = EventFiringWebDriver(webdriver.Firefox(options=options), LogListener(request))

    yield driver
    driver.quit()

    logging.info('====Browser Fixture Finished====')
