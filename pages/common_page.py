""" Переменные и методы сайта ticketland.ru """

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CommonPage:
    """ Переменные и методы сайта ticketland.ru """

    def __init__(self, logger, browser):
        self.logger = logger
        self.browser = browser

    base_url = "http://www.ticketland.ru"
    test_case_url = "https://testrail.net/index.php?/cases/view/"

    login_icon = (By.CSS_SELECTOR, ".gray.user")

    def wait_element_present(self, locator):
        """ Метод ожидания появления элемента """

        with allure.step("Ожидание появления элемента" + str(locator)):

            wait = WebDriverWait(self.browser, 10)

            try:
                return wait.until(ec.presence_of_all_elements_located(locator))
            except Exception as exc:
                exc.msg = 'Unable to locate element by selector ' + str(locator)
                raise
