""" Методы и локаторы страницы MainPage """

import allure
from selenium.webdriver.common.by import By
from pages.common_page import CommonPage


class MainPage(CommonPage):
    """ Методы и локаторы страницы MainPage """

    promo_block = (By.CSS_SELECTOR, ".promo-side-banners-top")
