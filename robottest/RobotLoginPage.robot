"""  Фикстуры robotframework тестов сайта ticketland.ru """

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from robot.api.deco import keyword


login = 'koksharova3093@gmail.com'
password = '999999'

# login_input = (By.NAME, 'LoginForm[contact]')
password_input = (By.NAME, 'LoginForm[password]')

@keyword('Login input')
def get_login_input():
    login_input = (By.NAME, 'LoginForm[contact]')
    return login_input


@keyword('Chrome browser')
def chromedriver():
    """ Драйвер для запуска тестов> """

    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options)

    return driver


@keyword('Open site')
def chrome_get(url):

    chrome = chromedriver()
    chrome.get(url)
    time.sleep(3)
    chrome.quit()


@keyword('Send keys to')
def chrome_send_keys(input, value):
    """ Логгер браузера """
    chrome = chromedriver()
    chrome.get('http://www.ticketland.ru/login')
    chrome.find_element(input).send_keys(value)
    time.sleep(30)


@keyword ('Click on')
def chrome_click(element):
    """ Логгер браузера """
    chrome = chromedriver ()
    chrome.find_element(element).click()
