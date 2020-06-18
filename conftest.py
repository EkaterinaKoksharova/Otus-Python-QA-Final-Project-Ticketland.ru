"""  Фикстуры тестов сайта ticketland.ru """

import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver
from tools.listener_log import LogListener


def pytest_addoption(parser):
    """  Параметры, передаваемые в командную строку при запуске тестов """

    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome, firefox, safari or remote, "
                          "remote_standalone, remote_browserstack or remote selenoid")
    parser.addoption("--implicitly_wait",
                     default=1,
                     help="This is time parameter for driver implicitly wait")
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

    implicitly_wait_parameter = request.config.getoption('--implicitly_wait')
    browser_name = request.config.getoption("--browser_name")
    executor = request.config.getoption("--executor")

    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        options.add_argument("--window-size=1920x1080")
        options.add_experimental_option('w3c', False)
        DesiredCapabilities.CHROME['loggingPrefs'] = {'browser': 'ALL', 'driver': 'ALL'}
        driver = EventFiringWebDriver\
            (webdriver.Chrome(desired_capabilities=DesiredCapabilities.CHROME,
                              options=options),
             LogListener(request))
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        options.add_argument("--window-size=1920x1080")
        driver = EventFiringWebDriver(webdriver.Firefox(options=options), LogListener(request))
    elif browser_name == "remote_selenoid":
        capabilities = {
            'browserName': 'chrome',
            'version': '70.0',
            'enableVNC': True,
            'enableVideo': False,
            'enableLog': False}
        driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                                  desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--browser_name should be chrome, "
                                "firefox or remote selenoid")

    driver.implicitly_wait(implicitly_wait_parameter)

    yield driver
    driver.quit()

    logging.info('====Browser Fixture Finished====')
