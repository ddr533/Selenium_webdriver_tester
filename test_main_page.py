from .pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод класса MainPage — переходим на страницу логина
    page.should_be_login_link() # выполняем метоl класса MainPage - проверяем наличие ссылки на логин