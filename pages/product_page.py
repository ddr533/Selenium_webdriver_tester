from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def user_can_add_product_to_basket(self):
        self.add_to_basket() #добавляем в корзину
        self.solve_quiz_and_get_code() #решаем задачу в алерте
        self.should_be_message_about_adding_product() #проверяем сообщение о добавлении товара в корзину
        self.should_be_message_about_basket_total() #проверяем сообщение о стоимсти корзины
        self.should_name_of_product_in_message() #проверяем имя товара в корзине
        self.product_price_in_basket_total_message() #проверяем цену товара в корзине
    def add_to_basket(self):
        go_to_basket=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    def should_be_message_about_adding_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), 'Message about adding is not present'
    def should_name_of_product_in_message(self):
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        text_in_message_about_adding=self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert  product_name==text_in_message_about_adding, 'Product_name not in Message_about_adding'
    def should_be_message_about_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_OF_TOTAL_COST_OF_BASKET), 'Message about total cost of basket doesnt exist'
    def product_price_in_basket_total_message(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_basket=self.browser.find_element(*ProductPageLocators.MESSAGE_OF_TOTAL_COST_OF_BASKET).text
        assert  product_price in price_in_basket, 'Product price not in total basket cost message'

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), 'Message about adding present but shound not be'
    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), 'Success message but shound not be'
    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), 'Message about adding disaapear but shound not be'




