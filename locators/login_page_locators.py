from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Форма логина
    LOGIN_FORM = (By.XPATH,"//form[@class='styles_form__2nwxz styles_form__2_42b']")
    # Поле [Электронная почта]
    EMAIL_INPUT = (By.XPATH,"//input[@name='email']")
    # Поле [Пароль]
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    # Кнопка [Войти]
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Кнопки [Создать аккаунт]
    CREATE_NEW_ACCOUNT_BUTTON = (By.XPATH, "//a[text()='Создать аккаунт']")
    # Кнопка [Войти]
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")
