#в классе BasePage технические детали — реализация поиска элементов, метод для открытия страницы и прохождения капчи
# C BasePage будут унаследовать методы другие страницы
from selenium.common.exceptions import NoSuchElementException  #импортируем имя для except
from selenium.common.exceptions import NoAlertPresentException #исключение для solve_quiz_and_get_code
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators
import math

class BasePage():
    # описываем методы взаимодействия с драйвером
    def __init__(self, browser, url): #добавим конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10) #добавим команду для неявного ожидания со значением по умолчанию в 10
    def open(self): #заходим на страницу
        self.browser.get(self.url)
    def go_to_login_page(self): #В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click() #символ указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
        try: #принять алерт, если он есть
            alert = self.browser.switch_to.alert
            alert.accept()
        except (NoAlertPresentException):
            return True
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Loging Link is not present'
    def is_element_present(self,how,what): #реализуем метод поиска элемента, в котором будем перехватывать исключения
        try:
            self.browser.find_element(how,what)
        except (NoSuchElementException):
            return False
        return True
    def is_not_element_present(self, how, what, timeout=4): #проверка на ОТСУТСВИЕ элемента на странице
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    def is_disappeared(self, how, what, timeout=4): #проверка на исчезание элемента
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    def solve_quiz_and_get_code(self):
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