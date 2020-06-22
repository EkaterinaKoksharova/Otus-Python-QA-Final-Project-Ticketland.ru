""" Тесты для страницы поиска на сайте ticketland.ru"""

import allure
import pytest
from tools.page_container import PageContainer


class TestSearchPage:
    """ Тесты для страницы поиска на сайте ticketland.ru """

    page = PageContainer(browser=None)

    @allure.testcase(page.common.test_case_url + 'test_case_id', 'Наименование тест-кейса')
    @allure.title("Проверка страница поиска открывается с главной страницы")
    def test_search_page_is_open(self, browser):
        """ Проверка страница поиска открывается с главной страницы """

        page = PageContainer(browser)
        page.tests_logger.info('test_search_page_is_open')

        browser.get(page.common.base_url)
        page.search.make_search()
        page.common.wait_element_present(page.search.search_page_title)

        assert 'search' in browser.current_url, 'Ошибка открытия страницы поиска с главной!'
