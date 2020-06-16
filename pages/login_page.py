""" Локаторы и методы страницы логина администратора сайта opencart """

import allure
from selenium.webdriver.common.by import By
from pages.common_page import CommonPage


class LoginPage(CommonPage):
    """Методы и локаторы страницы LoginPage"""

    login = 'ticketland.QA@yandex.ru'
    password = '123456'

    input_login = (By.NAME, 'LoginForm[contact]')
    password_input = (By.NAME, 'LoginForm[password]')
    error_login_message = (By.CSS_SELECTOR, '.login-msg')
    login_submit_button = (By.CSS_SELECTOR, '.registration-button')

    password_recovery_link = (By.CSS_SELECTOR, 'password-recovery a')
    registration_link = (By.CSS_SELECTOR, '.register-page-btn a')

    mailru_login = (By.CSS_SELECTOR, '.auth-link.mailru')
    google_login = (By.CSS_SELECTOR, '.auth-link.google_oauth')
    facebook_login = (By.CSS_SELECTOR, '.auth-link.facebook')
    vk_login = (By.CSS_SELECTOR, '.auth-link.vkontakte')

    def go_to_login_page(self):
        """ Метод перехода на страницу логина """

        self.browser.find_element(*self.common_items.).click()

    def login(self, login=login, password=password):
        """ Метод авторизации пользователя на сайте ticketland.ru """

        driver = self.app.driver
        self.app.nav.go_to_login_page()
        usernameInput = self.app.waitFor.wait_for_element ('input[name="LoginForm[contact]"]')
        usernameInput.send_keys (username)
        driver.find_element_by_name ('LoginForm[password]').send_keys (password)
        button = driver.find_element_by_css_selector ('button.registration-button')
        button.click ()
        self.app.waitFor.wait_for_login_result (button)

    def logout(self):
        driver = self.app.driver
        result = False
        number_of_logout_efforts = 0
        while number_of_logout_efforts <= 3:
            number_of_logout_efforts += 1
            # чтобы не грузить заказы, перейдем на вкладку "Персональные данные"
            self.app.nav.go_to_personal_page ()
            logoutBtn = driver.find_element_by_css_selector ('#tab_logout b')
            logoutBtn.click ()
            self.app.waitFor.wait_for_staleness_element (logoutBtn)
            userIcon = self.app.waitFor.wait_for_element ('header a.user')
            if userIcon.get_attribute ('href').find ('/private') == -1:
                result = True
                break

        assert result == True, 'ошибка деавторизации'