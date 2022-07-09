from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser): #ключевое слово test позволяет pytest подхватить переменную browser из conftest.py
    link='http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page=ProductPage(browser,link) #создаем экземпляр теста ProductPage через передачу browser (из  conftest.py) в класс BasePage
    page.open() #используем метод open из BasePage для открытия страницы в созданном экземпляре теста
    page.go_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_product()
    page.should_be_message_about_basket_total()
    page.should_name_of_product_in_message()
    page.product_price_in_basket_total_message()