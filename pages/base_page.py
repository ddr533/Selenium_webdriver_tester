#Создаем базовую страницу, с которой будут унаследоваться все остальные классы
from selenium.common.exceptions import NoSuchElementException  #импортируем имя для except
from selenium.common.exceptions import NoAlertPresentException #исключение для solve_quiz_and_get_code
import math

class BasePage():
    # описываем методы взаимодействия с драйвером
    def __init__(self, browser, url): #добавим конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10) #добавим команду для неявного ожидания со значением по умолчанию в 10
    def open(self): #заходим на страницу
        self.browser.get(self.url)
    def is_element_present(self,how,what): #реализуем метод поиска элемента, в котором будем перехватывать исключения
        try:
            self.browser.find_element(how,what)
        except (NoSuchElementException):
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