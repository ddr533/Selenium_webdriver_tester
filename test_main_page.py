import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage #для перехода с main_page на login_page
import time
#@pytest.mark.skip
@pytest.mark.login_guest #можно запустить только тесты в классе, используя метку -m login_guest
class TestLoginFromMainPage(): #Объеденили в класс несколько тестов, связанных с одним элементом сайта
    def test_guest_can_go_to_login_page(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)  # инициализируем PageObject, передаем в конструктор экземпляра драйвер браузера и url
        self.page.open()  # открываем страницу
        self.page.go_to_login_page()  # выполняем метод класса MainPage — переходим на страницу логина
        self.login_page = LoginPage(browser, browser.current_url)  # после перехода создаем экземляр класса LoginPage драйвером браузера и текущим url
        self.login_page.should_be_login_page()  # выполняем метод из класса
    def test_guest_should_see_login_link(self,browser):  # выполняем метод класса MainPage - проверяем наличие ссылки на логин
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.should_be_login_link()

#@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link='http://selenium1py.pythonanywhere.com/ru/'
    page=MainPage(browser,link)
    page.open()
    page.go_to_basket()
    time.sleep(5)
