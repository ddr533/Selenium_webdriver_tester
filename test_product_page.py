from .pages.product_page import ProductPage
import pytest
import time
base_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls=[f'{base_link}/?promo=offer{num}' for num in range(10)] #Создаем список ссылок для проверки
urls[7]=pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7', marks=pytest.mark.xfail) #помечаем ссылку
# с провальным тестом как XFAIL
@pytest.mark.parametrize('links',urls) #Фиктсура для прогона тестов по всем страницам из списка
def test_guest_can_add_product_to_basket(browser, links): #ключевое слово test позволяет pytest подхватить переменную browser из conftest.py
    page=ProductPage(browser,links) #создаем экземпляр теста ProductPage через передачу browser (из  conftest.py) в класс BasePage
    page.open() #используем метод open из BasePage для открытия страницы в созданном экземпляре теста
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_product()
    page.should_be_message_about_basket_total()
    page.should_name_of_product_in_message()
    page.product_price_in_basket_total_message()


# @pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==?, reason='')) for i in range(10)])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"