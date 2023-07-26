import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
urls = [f'{base_link}/?promo=offer{num}' for num in range(10)]
urls[7] = pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
                       marks=pytest.mark.xfail)

@pytest.mark.parametrize('links', urls)
def test_user_can_add_product_to_basket_for_few_links(browser, links):
    """Тестирование всех промо-ссылок из спиcка urls."""
    page = ProductPage(browser, links)
    page.open()
    page.user_can_add_product_to_basket()


class TestUserAddToBasketFromProductPage:
    """Тестирование работы корзины."""

    # Перед каждым тестом будет регистрировать пользователя
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = LoginPage(browser, self.link)
        self.page.open()
        email = str(time.time()) + "@fakemails.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.guest_cant_see_success_message()

    @pytest.mark.product_page
    def test_user_can_add_product_to_basket(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, self.link)
        page.open()
        page.user_can_add_product_to_basket()


@pytest.mark.product_page
class TestProductPage:
    """Тестирование страницы c продуктом."""

    def test_guest_can_add_product_to_basket(self, browser):
        link = ('http://selenium1py.pythonanywhere.com/catalogue'
                '/the-shellcoders-handbook_209/?promo=newYear')
        page = ProductPage(browser, link)
        page.open()
        page.user_can_add_product_to_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(
            self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message_after_adding_product_to_basket()

    def test_guest_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.message_disappeared_after_adding_product_to_basket()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.product_page
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.product_page
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.user_can_see_message_about_empty_basket()
        basket_page.is_items_in_basket()
