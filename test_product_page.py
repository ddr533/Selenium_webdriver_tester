from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time
@pytest.mark.skip
def test_user_can_add_product_to_basket(browser): #ключевое слово test позволяет pytest подхватить переменную browser из conftest.py
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page=ProductPage(browser,link) #создаем экземпляр класса ProductPage и передаем browser (из conftest.py),link в класс BasePage
    page.open() #используем метод open из BasePage для открытия страницы в созданном экземпляре теста
    page.user_can_add_product_to_basket() #используем метод класса ProductPage

base_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls=[f'{base_link}/?promo=offer{num}' for num in range(10)] #Создаем список ссылок для теста
urls[7]=pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail) #список ссылок
##для теста с пометкой провального теста с помощью xfail
@pytest.mark.skip
@pytest.mark.parametrize('links',urls) #Фиктсура для прогона тестов по всем страницам из списка
def test_user_can_add_product_to_basket_for_few_links(browser,links): #тест нескольких страниц с одним сценарием
    page=ProductPage(browser,links)
    page.open()
    page.user_can_add_product_to_basket()
@pytest.mark.skip
@pytest.mark.xfail #помечаем ссылку с провальным тестом как XFAIL
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): #отрицательный тест "чего не должно быть на странице"
    link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser,link)
    page.open()
    page.guest_cant_see_success_message_after_adding_product_to_basket()
@pytest.mark.skip
@pytest.mark.skip
def test_guest_cant_see_success_message(browser): #отрицательный тест "чего не должно быть на странице"
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()
@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): #тест на исчезание элеиента со страницы
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.message_disappeared_after_adding_product_to_basket()
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=ProductPage(browser,link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=ProductPage(browser,link)
    page.open()
    page.go_to_basket()
    basket_page=BasketPage(browser,browser.current_url)
    basket_page.user_can_see_message_about_empty_basket()
    basket_page.is_items_in_basket()

# @pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==?, reason='')) for i in range(10)])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
# link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"