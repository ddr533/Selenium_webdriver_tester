from selenium.webdriver.common.by import By
class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")
class LoginPageLocators:
    REGISTRATION_FORM=(By.CSS_SELECTOR,'#register_form')
    LOGIN_FORM=(By.CSS_SELECTOR,'#login_form')
class ProductPageLocators:
    BASKET=(By.CSS_SELECTOR,'[class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_NAME=(By.CSS_SELECTOR,'.product_main h1')
    PRODUCT_PRICE=(By.CSS_SELECTOR,'.product_main p.price_color')
    MESSAGE_ABOUT_ADDING=(By.CSS_SELECTOR,'#messages > div:nth-child(1) > div > strong')
    MESSAGE_OF_TOTAL_COST_OF_BASKET=(By.CSS_SELECTOR,'#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div')