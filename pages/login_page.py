import allure

import urls
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step('Нажатие кнопки [Войти] в шапке')
    def click_open_login_form(self):
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Отображение формы авторизации')
    def visibility_login_form(self):
        return self.find_element_with_wait(LoginPageLocators.LOGIN_FORM)

    @allure.step('Нажатие кнопки [Создать аккаунт]')
    def click_to_registration_button(self):
        self.click_to_element(LoginPageLocators.CREATE_NEW_ACCOUNT_BUTTON)

    @allure.step('Заполнение [Email]')
    def add_email(self, user_data):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT, user_data["email"])
    
    @allure.step('Заполнение [Пароль]')
    def add_password(self, user_data):
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT, user_data["password"])

    @allure.step('Нажатие на [Войти]')
    def click_login_button(self):
        self.click_to_element(LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        self.wait_until_url_is_changed(urls.URL_RECIPES)    

    @allure.step('Авторизация пользователя')
    def login_user(self, user_data):
        self.click_open_login_form()
        self.visibility_login_form()
        self.add_email(user_data)
        self.add_password(user_data)
        self.click_login_button()
