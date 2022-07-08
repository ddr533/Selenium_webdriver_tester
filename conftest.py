import selenium
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options #Добавляем класс Option

def pytest_addoption(parser): #встроенная функция для добавления опций в командную строку для pytest
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox") #опция выбора браузера для теста --browser_name=firefox или --browser_name=chrome
    parser.addoption('--language', action='store', default='ru', help="Choose languege: ru or en") #добавляем выбор языка


@pytest.fixture(scope='function')
def browser(request):
    browser_name=request.config.getoption("browser_name") #request - получаем данные из командной строки из --browser_name
    user_language=request.config.getoption("language")      #request - получаем данные из командной строки из --language
    browser=None

    if browser_name=="chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) #передаем язык в Хром
        browser=webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language) #передаем язык в Firefox
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

