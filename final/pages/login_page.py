from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self,email, password):
        field_for_email = self.browser.find_element(*LoginPageLocators.EMAIL_REG_LOCATOR)
        field_for_password = self.browser.find_element(*LoginPageLocators.PASSWORD_REG_LOCATOR)
        field_for_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_LOCATOR)

        field_for_email.clear()
        field_for_email.send_keys(email)
        field_for_password.clear()
        field_for_password.send_keys(password)
        field_for_confirm_password.clear()
        field_for_confirm_password.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN).click()

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        cur_url = self.browser.current_url
        assert 'login' in cur_url, "Url doesn't contain 'login'"
