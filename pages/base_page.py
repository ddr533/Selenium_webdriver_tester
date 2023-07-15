import math

from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    """Основные методы для работы со страницами сайта."""

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # Явное ожидание появления элемента в течение 10 секунд.
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Переход по ссылке."""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Элемент представлен на странице."""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Элемент исчезает со страницы."""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), (
            "User icon is not presented," " probably unauthorised user"
        )

    def solve_quiz_and_get_code(self):
        """Вычисление проверочного кода из задания в алерте при
            добавлении товара в корзину."""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
