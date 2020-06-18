"""Методы и локаторы страницы SearchPage и элементов, относящихся к поиску"""

import allure
from selenium.webdriver.common.by import By
from pages.common_page import CommonPage


class SearchPage(CommonPage):
    """Методы и локаторы страницы SearchPage и элементов, относящихся к поиску"""

    search_button = (By.CSS_SELECTOR, ".find_button btn3")
    search_input = (By.CSS_SELECTOR, "#searchForm .old-input")

    def search(self):
        """ Метод поиска на сайта ticketlane.ru """

        self.browser.find_element(self.login_icon).click()

    def enter_search_phrase(self, phrase):

        self.browser.find_element(self.search_input).send_keys(phrase)
