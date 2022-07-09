from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_basket(self):
        basket=self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()
    def should_be_message_about_adding_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), 'Message about adding is not present'
    def should_name_of_product_in_message(self):
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        text_in_message_about_adding=self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert  product_name in text_in_message_about_adding, 'Product_name not in Message_about_adding'
    def should_be_message_about_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_OF_TOTAL_COST_OF_BASKET), 'Message about total cost of basket doesnt exist'
    def product_price_in_basket_total_message(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_basket=self.browser.find_element(*ProductPageLocators.MESSAGE_OF_TOTAL_COST_OF_BASKET).text
        assert  product_price in price_in_basket, 'Product price not in total basket cost message'



