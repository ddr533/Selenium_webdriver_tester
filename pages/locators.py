from selenium.webdriver.common.by import By
class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")
class LoginPageLocators:
    REGISTRATION_FORM=(By.CSS_SELECTOR,'#register_form')
    LOGIN_FORM=(By.CSS_SELECTOR,'#login_form')
    EMAIL_FORM=(By.CSS_SELECTOR,'#id_registration-email')
    PASSWORD_FORM=(By.CSS_SELECTOR,'#id_registration-password1')
    CONFIRM_PASSWORD_FORM=(By.CSS_SELECTOR,'#id_registration-password2')
    REG_BUTTON=(By.CSS_SELECTOR,'#register_form > button')
class ProductPageLocators:
    ADD_TO_BASKET=(By.CSS_SELECTOR,'[class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_NAME=(By.CSS_SELECTOR,'.product_main h1')
    PRODUCT_PRICE=(By.CSS_SELECTOR,'.product_main p.price_color')
    MESSAGE_ABOUT_ADDING=(By.CSS_SELECTOR,'#messages > div:nth-child(1) > div > strong')
    MESSAGE_OF_TOTAL_COST_OF_BASKET=(By.CSS_SELECTOR,'#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div')
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CSS_SELECTOR, 'span > a.btn.btn-default')
    USER_ICON=(By.CSS_SELECTOR,'.icon-user')
class BasketPageLocators:
    MSG_EMPTY_BASKET=(By.CSS_SELECTOR, '#content_inner > p')
    BLOCK_WITH_ITEMS_IN_BASKET=(By.CSS_SELECTOR,'#basket_formset > div > div.row')




