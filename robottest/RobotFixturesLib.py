"""  Фикстуры robotframework тестов сайта ticketland.ru """

import logging
from selenium import webdriver
from tools.listener_log import LogListener


def browser():
    """ Драйвер для запуска тестов> """

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


def logger():
    """ Логгер браузера """

    log = logging.logging.getLogger("TEST NAME")
    return log
