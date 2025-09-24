from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    # Форма создания рецепта
    CREATE_RECIPE_FORM = (By.XPATH, "//form[@class='styles_form__2nwxz styles_form__3XFkE']")
    # Поле [Название рецепта]
    RECIPE_NAME_INPUT = (By.XPATH, "//div[@class='styles_input__2Dg_j']//input[@class='styles_inputField__3eqTj']")
    # Поле [Ингредиенты]
    INGREDIENT_NAME_INPUT = (By.XPATH, "//input[@class='styles_inputField__3eqTj styles_ingredientsInput__1zzql']")
    # Первый ингредиент в выпадающем списке
    INGREDIENT_IN_DROPDOWN = (By.XPATH, "//div[.='{}']")
    # Поле [Количество]
    COUNT_INPUT = (By.XPATH, "//input[@class='styles_inputField__3eqTj styles_ingredientsAmountValue__2matT']")
    # Кнопка [Добавить ингредиент]
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    # Поле [Время приготовления]
    COOKING_TIME_INPUT = (By.XPATH, "//div[@class='styles_input__2Dg_j styles_ingredientsTimeInput__3oqdd']//input[@class='styles_inputField__3eqTj']")
    # Поле [Описание рецепта]
    RECIPE_DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@class='styles_textareaField__1wfhC']")
    # Кнопка [Загрузить фото]
    ADD_PHOTO_BUTTON = (By.XPATH, "//input[@type='file']")
    # Кнопка [Создать рецепт]
    CREATE_RECIPE_BUTTON = (By.CSS_SELECTOR, ".style_button__1FFWl")
