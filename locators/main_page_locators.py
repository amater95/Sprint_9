from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка [Создать рецепт]
    CREATE_RECIPE_TAB = (By.XPATH, "//a[text()='Создать рецепт']")
    # Кнопка [Выход]
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")
