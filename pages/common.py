""" Переменные и методы сайта opencart """

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class CommonItems:
    """ Переменные и методы сайта opencart """

    def __init__(self, logger, browser):
        self.logger = logger
        self.browser = browser
        self.login_icon = (By.CSS_SELECTOR, ".gray.user")


    base_url = "http://www.ticketland.ru/"
    test_case_url = "https://testrail.net/index.php?/cases/view/"

    print('TEST')
    login_icon = (By.CSS_SELECTOR, ".gray.user")

    def wait_element_present(self, wait, locator):
        """ Метод ожидания появления элемента """

        try:
            return wait.until(ec.presence_of_all_elements_located(locator))
        except Exception as exc:
            exc.msg = 'Unable to locate element by selector ' + str(locator)
            raise
