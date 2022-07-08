from .base_page import BasePage #импорт базового класса
from selenium.webdriver.common.by import By
class MainPage(BasePage): #Создаем новый класс наследник. MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
    def go_to_login_page(self): #В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, '#login_linkg'), 'Loging Link is not present'