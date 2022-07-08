#Создаем базовую страницу, с которой будут унаследоваться все остальные классы
from selenium.common.exceptions import NoSuchElementException  #импортируем имя для except
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
