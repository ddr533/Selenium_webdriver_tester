from .base_page import BasePage #импорт базового класса
from .locators import MainPageLocators #импорт класса с локаторами для главной страницы
from selenium.common.exceptions import NoAlertPresentException

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
# Метод __init__ вызывается при создании объекта.
# Конструктор выше с ключевым словом super вызывает конструктор класса предка (Base Page)
# и передает ему все те аргументы, которые мы передали в конструктор MainPage.




# class MainPage(BasePage): #Создаем новый класс наследник. MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
#     def go_to_login_page(self): #В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
#         login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) #символ указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
#         login_link.click()


