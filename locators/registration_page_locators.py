from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    # Форма регистрации
    REGISTRATION_FORM = (By.XPATH, "//form[@class='styles_form__2nwxz styles_form__24nV3']")
    # Поле [Имя]
    FIRST_NAME_INPUT = (By.XPATH, "//input[@name='first_name']")
    # Поле [Фамилия]
    LAST_NAME_INPUT = (By.XPATH, "//input[@name='last_name']")
    # Поле [Имя пользователя]
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    # Поле [Адрес электронной почты]
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    # Поле [Пароль]
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    # Кнопка [Создать аккаунт]
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
