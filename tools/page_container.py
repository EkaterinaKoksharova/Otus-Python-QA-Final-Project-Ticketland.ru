""" Класс с экземплярами классов всех страниц """

import logging
from pages.common_page import CommonPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.private_page import PrivatePage


class PageContainer:
    """ Класс с экземплярами классов всех страниц """

    def __init__(self, browser):
        self.logger = logging.getLogger("PAGE NAME")
        self.tests_logger = logging.getLogger("TEST NAME")
        self.common = CommonPage(self.logger, browser)
        self.login = LoginPage(self.logger, browser)
        self.main = MainPage(self.logger, browser)
        self.private = PrivatePage(self.logger, browser)
