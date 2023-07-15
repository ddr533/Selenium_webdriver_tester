"""
Основные фикстуры для тестов pytest.
Фикстуры подгружаются pytest-ом автоматически и используются в тестовых модулях.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    Встроенная функция для добавления опций в командную строку для pytest.
    Добавляем параметр для выбора браузера для тестов
    --browser_name=firefox или --browser_name=chrome. И выбор языка --language
     =ru или --language=en.
    """
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language",
        action="store",
        default="ru",
        help="Choose languege: ru or en",
    )


@pytest.fixture(scope="function")
def browser(request):
    """Функция создает фикстуру браузера."""
    # Получаем данные из командной строки из --browser_name и --language
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        # Очистка вывода от сообщений USB: usb_device_handle_win.cc:1048....
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
