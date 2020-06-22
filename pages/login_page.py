"""Методы и локаторы страницы LoginPage"""

import allure
from selenium.webdriver.common.by import By
from common_page import CommonPage


class LoginPage(CommonPage):
    """Методы и локаторы страницы LoginPage"""

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    login = 'koksharova3093@gmail.com'
    password = '999999'

    login_input = (By.NAME, 'LoginForm[contact]')
    password_input = (By.NAME, 'LoginForm[password]')
    error_login_message = (By.CSS_SELECTOR, '.login-msg')
    login_submit_button = (By.CSS_SELECTOR, '.registration-button')

    password_recovery_link = (By.CSS_SELECTOR, '.password-recovery a')
    registration_link = (By.CSS_SELECTOR, '.register-page-btn a')

    mailru_login = (By.CSS_SELECTOR, '.auth-link.mailru')
    google_login = (By.CSS_SELECTOR, '.auth-link.google_oauth')
    facebook_login = (By.CSS_SELECTOR, '.auth-link.facebook')
    vk_login = (By.CSS_SELECTOR, '.auth-link.vkontakte')

    def go_to_login_page(self):
        """ Метод перехода на страницу авторизации"""

        with allure.step("Переход на страницу aвторизации"):
            print(self.browser)
            self.browser.get(self.base_url + "/login/")

    def login_to_site(self, login=login, password=password):
        """ Метод авторизации пользователя на сайте ticketland.ru """

        with allure.step("Авторизация на сайте. Логин: " + login + "Пароль:" + password):
            self.go_to_login_page()
            self.browser.find_element(*self.login_input).send_keys(login)
            self.browser.find_element(*self.password_input).send_keys(password)
            self.browser.find_element(*self.login_submit_button).click()
