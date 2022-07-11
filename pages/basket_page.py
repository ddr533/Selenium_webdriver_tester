from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def user_can_see_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MSG_EMPTY_BASKET), 'Message about basket empty is not present,but should be'
    def is_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BLOCK_WITH_ITEMS_IN_BASKET), 'Basket has some Itemes, but should has not'
