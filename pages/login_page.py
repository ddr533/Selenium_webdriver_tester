from .locators import LoginPageLocators
from .main_page import MainPage


class LoginPage(MainPage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка нахождения на странице логина."""
        assert (
            "login" in self.browser.current_url
        ), "Login button not at login_page"

    def should_be_login_form(self):
        """На странице логина есть форма."""
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "No login form"

    def should_be_register_form(self):
        """На странице логина есть форма регистрации."""
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM
        ), "No registration form"

    def register_new_user(self, email, password):
        """Работает регистрация нового пользователя."""
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.EMAIL_FORM).send_keys(
            email
        )
        self.browser.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys(
            password
        )
        self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD_FORM
        ).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
