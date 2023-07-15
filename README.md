# Selenium_webdriver_tester
Автоматизация тестирования интернет-магазина.

#### Технологии
* Selenium Webdriver
* Pytest

#### Установка
* Клонировать репозиторий
  ```
  git clone https://github.com/ddr533/Selenium_webdriver_tester
  ```
* Cоздать и активировать виртуальное окружение:

```
python -m venv env
source env/scripts/activate
```

* Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

* Скачать webdriver для браузера Chrome и разместить его в папке C:\chromedriver
* Скачать geckodriver для браузера FireFox и разместить его в папке C:\geckodriver
* Добавить папки C:\chromedriver, C:\geckodriver в переменную PATH системы Windows

#### Запуск тестов в Chrome при активированном виртуальном окружении:
```
pytest -v -s --tb=line --browser_name=chrome --language=en test_main_page.py
pytest -v -s --tb=line --browser_name=chrome --language=en test_product_page.py
```
