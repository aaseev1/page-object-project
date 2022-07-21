import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "'/login/' in url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email.send_keys(email)
        password = str(time.time()) + "qwertyu"
        reg_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        reg_password.send_keys(password)
        reg_password_repeat = self.browser.find_element(*LoginPageLocators.REG_REPEAT_PAS)
        reg_password_repeat.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BTN)
        reg_button.click()
