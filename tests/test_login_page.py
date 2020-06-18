""" Тесты для страницы авторизации на сайте ticketland.ru"""

import allure
import pytest
from selenium.webdriver.common.by import By
from pages.page_container import PageContainer


class TestLoginPage:
    """ Тесты для страницы авторизации на сайте """

    page = PageContainer(browser=None)
    admin_wrong_pasword = "blabla"

    @allure.testcase (page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title ("Проверка наличия основных элементов на странице авторизации")
    def test_login_page_find_elements(self, browser):
        """ Проверка наличия основных элементов на странице авторизации """

        page = PageContainer(browser)
        page.tests_logger.info('test_admin_login_page_find_elements')

        page.login.go_to_login_page()

        assert browser.find_element(*page.login.login_input).is_displayed()
        assert browser.find_element(*page.login.password_input).is_displayed()
        assert browser.find_element(*page.login.login_submit_button).is_displayed()
        assert browser.find_element(*page.login.password_recovery_link).is_displayed()
        assert browser.find_element(*page.login.registration_link).is_displayed()
        assert browser.find_element(*page.login.mailru_login).is_displayed()
        assert browser.find_element(*page.login.google_login).is_displayed()
        assert browser.find_element(*page.login.facebook_login).is_displayed()
        assert browser.find_element(*page.login.vk_login).is_displayed()

    @allure.testcase (page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title ("Проверка корректной авторизации пользователя")
    def test_login_right(self, browser):
        """ Проверка корректной авторизации пользователя """

        page = PageContainer (browser)
        page.tests_logger.info('test_login_right')

        page.login.go_to_login_page()
        page.login.login_to_site()
        page.common.wait_element_present(page.private.logout_button)

        page.private.go_to_private_page()

        assert 'private' in browser.current_url, 'Ошибка авторизации!'

    @allure.testcase (page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title ("Проверка ошибки авторизации пользователя")
    @pytest.mark.parametrize('login', [' ', '@mail.ru', 'koksharova3093@gmailcom'])
    def test_login_wrong(self, browser, login):
        """ Проверка ошибки авторизации пользователя """

        page = PageContainer(browser)
        page.tests_logger.info('test_login_wrong')

        page.login.go_to_login_page()

        page.login.login_to_site(login, password=page.login.password)

        assert browser.find_element(*page.login.error_login_message).is_displayed()
