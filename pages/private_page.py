"""Методы и локаторы страницы PrivatePage"""

import allure
from selenium.webdriver.common.by import By
from pages.common_page import CommonPage


class PrivatePage(CommonPage):
    """Методы и локаторы страницы PrivatePage"""

    logout_button = (By.CSS_SELECTOR, "#tab_logout b")

    def go_to_private_page(self):
        """ Метод перехода на страницу логина """

        with allure.step ("Переход на страницу личного кабинета"):
            self.browser.find_element(*self.login_icon).click()

    def logout_from_site(self):
        """ Метод выхода из личного кабинета """

        with allure.step ("Выход из личного кабинета"):
            self.browser.find_element(*self.logout_button).click()
