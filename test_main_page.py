import time

import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage


# Можно запустить только тесты в классе, используя метку -m main_page
@pytest.mark.login_guest
class TestMainPage:
    """Тестирование главной страницы сайта."""

    def test_guest_can_go_to_login_page(self, browser):
        """Пользователь может перейти на страницу логина, залогиниться
        или зарегистрироваться."""
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """На главной странице есть ссылка на логин."""
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.should_be_login_link()

    # @pytest.mark.skip
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        time.sleep(5)
