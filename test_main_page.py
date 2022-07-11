from .pages.main_page import MainPage
from .pages.login_page import LoginPage #для перехода с main_page на login_page
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем PageObject, передаем в конструктор экземпляра драйвер браузера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод класса MainPage — переходим на страницу логина
    login_page=LoginPage(browser, browser.current_url) #после перехода создаем экземляр класса LoginPage драйвером браузера и текущим url
    login_page.should_be_login_page() #выполняем метод из класса

def test_guest_should_see_login_link(browser): # выполняем метод класса MainPage - проверяем наличие ссылки на логин
    page=MainPage(browser,link)
    page.open()
    page.should_be_login_link()

