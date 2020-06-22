""" Тесты для страницы личного кабинета на сайте ticketland.ru"""

import time
import allure
import pytest
from tools.page_container import PageContainer


class TestPrivatePage:
    """ Тесты для страницы личного кабинета на сайте ticketland.ru """

    page = PageContainer(browser=None)

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title("Проверка выхода из учетной записи сайта ticketland.ru")
    def test_logout(self, browser):
        """ Проверка выхода из учетной записи сайта ticketland.ru """

        page = PageContainer(browser)
        page.tests_logger.info('test_logout')

        page.login.go_to_login_page()
        page.login.login_to_site()
        page.common.wait_element_present(page.private.logout_button)

        page.private.go_to_private_page()
        page.private.logout_from_site()
        page.common.wait_element_present(page.main.promo_block)

        page.login.go_to_login_page()

        assert 'login' in browser.current_url, 'Ошибка выхода из аккаунта!'
