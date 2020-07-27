"""  Настройки для сбора логов браузера """

import logging
from selenium.webdriver.support.events import AbstractEventListener


class LogListener(AbstractEventListener):
    """ Настройки для сбора логов браузера """

    def __init__(self, request):
        logging.basicConfig(filename=request.config.getoption("log_file"),
                            level=request.config.getoption("log_level"))

    def after_navigate_to(self, url, driver):
        logging.info('Driver navigated on %s', url)

    def after_find(self, by, value, driver):
        logging.info('Driver found %s with %s', value, by)

    def after_click(self, element, driver):
        logging.info('Driver clicked on %s', element)

    def after_execute_script(self, script, driver):
        logging.info('Driver executed %s', script)

    def after_quit(self, driver):
        logging.info('Driver quit')

    # def on_exception(self, exception, driver):
    #     logging.error('Exception: %s', exception)
    #     driver.get_screenshot_as_file(f'logs/{exception}.png')
