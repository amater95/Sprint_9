from selenium.webdriver.common.by import By


class RecipePageLocators:
    # Карточка рецепта
    RECIPE_CARD_INFO = (By.XPATH, "//div[@class='styles_single-card__info__2_cny']")
    # Название рецепта в карточке
    RECIPE_NAME = (By.XPATH, "//h1[@class='styles_single-card__title__2QMPq']")
