import allure
import urls
from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    @allure.step('Отображения формы регистрации')
    def visibility_registration_form(self):
        return self.find_element_with_wait(RegistrationPageLocators.REGISTRATION_FORM)

    @allure.step('Заполнение [Имя]')
    def add_first_name(self, user_data):
        self.add_text_to_element(RegistrationPageLocators.FIRST_NAME_INPUT, user_data["firstname"])

    @allure.step('Заполнение [Фамилия]')
    def add_last_name(self, user_data):
        self.add_text_to_element(RegistrationPageLocators.LAST_NAME_INPUT, user_data["lastname"])

    @allure.step('Заполнение [Имя пользователя]')
    def add_username(self, user_data):
        self.add_text_to_element(RegistrationPageLocators.USERNAME_INPUT, user_data["username"])

    @allure.step('Заполнение [Адрес электронной почты]')
    def add_email(self, user_data):
        self.add_text_to_element(RegistrationPageLocators.EMAIL_INPUT, user_data["email"])

    @allure.step('Заполнение [Пароль]')
    def add_password(self, user_data):
        self.add_text_to_element(RegistrationPageLocators.PASSWORD_INPUT, user_data["password"])

    @allure.step('Нажатие на [Создать аккаунт]')
    def click_registeration_button(self):
        self.click_to_element(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        self.wait_until_url_is_changed(urls.URL_LOGIN)

    @allure.step('Регистрация пользователя')
    def registration_user(self, user_data):
        self.visibility_registration_form()
        self.add_first_name(user_data)
        self.add_last_name(user_data)
        self.add_username(user_data)
        self.add_email(user_data)
        self.add_password(user_data)
        self.click_registeration_button()
