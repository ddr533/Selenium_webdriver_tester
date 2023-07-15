from selenium.common import NoAlertPresentException

from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):
    """Класс главной страницы магазина."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def go_to_login_page(self):
        """Переход на страницу логина."""
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            return True

    def should_be_login_link(self):
        """На главной странице есть ссылка на логин."""
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
        ), "Loging Link is not present"

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET).click()
