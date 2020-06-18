""" Методы и локаторы страницы MainPage """

import allure
from selenium.webdriver.common.by import By
from pages.common_page import CommonPage


class MainPage(CommonPage):
    """ Переменные и методы сайта ticketland.ru """

    promo_block = (By.CSS_SELECTOR, ".promo-side-banners-top")
