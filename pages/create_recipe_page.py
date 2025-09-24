import allure
from pages.base_page import BasePage
from locators.create_recipe_page_locators import CreateRecipePageLocators
import data


class CreateRecipePage(BasePage):
    @allure.step('Отображения формы создания рецепта')
    def visibility_create_recipe_form(self):
        return self.find_element_with_wait(CreateRecipePageLocators.CREATE_RECIPE_FORM)

    @allure.step('Заполнение [Название рецепта]')
    def add_recipe_name(self):
        self.add_text_to_element(CreateRecipePageLocators.RECIPE_NAME_INPUT, data.RECIPE_DATA["dish"])

    @allure.step('Заполнение [Ингредиенты]')
    def add_recipe_ingredients(self):
        for ingredient in data.RECIPE_DATA["ingredients"]:
            self.add_text_to_element(CreateRecipePageLocators.INGREDIENT_NAME_INPUT, ingredient)
            locator = self.format_locator(CreateRecipePageLocators.INGREDIENT_IN_DROPDOWN, ingredient)
            self.click_to_element(locator)
            self.add_text_to_element(CreateRecipePageLocators.COUNT_INPUT, data.RECIPE_DATA["count"])
            self.click_to_element(CreateRecipePageLocators.ADD_INGREDIENT_BUTTON)

    @allure.step('Заполнение [Время приготовления]')
    def add_recipe_cooking_time(self):
        self.add_text_to_element(CreateRecipePageLocators.COOKING_TIME_INPUT, data.RECIPE_DATA["cooking_time"])

    @allure.step('Заполнение [Описание рецепта]')
    def add_recipe_description(self):
        self.add_text_to_element(CreateRecipePageLocators.RECIPE_DESCRIPTION_TEXTAREA, data.RECIPE_DATA["description"])

    @allure.step('Заполнение [Загрузить фото]')
    def add_recipe_photo(self):
        self.add_photo_to_uploader(CreateRecipePageLocators.ADD_PHOTO_BUTTON, data.RECIPE_DATA["photo"])

    @allure.step('Нажатие на [Создать рецепт]')
    def click_add_recipe_button(self):
        self.click_to_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)

    @allure.step('Создание рецепта')
    def create_recipe(self):
        self.visibility_create_recipe_form()
        self.add_recipe_name()
        self.add_recipe_ingredients()
        self.add_recipe_cooking_time()
        self.add_recipe_description()
        self.add_recipe_photo()
        self.click_add_recipe_button()
