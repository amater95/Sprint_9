import allure
import data


class TestLoginPage:
    @allure.title("Создание рецепта блюда")
    def test_create_recipe(self, login_user, main_page, create_recipe_page, recipe_page):
        main_page.click_to_create_recipe_tab()
        create_recipe_page.create_recipe()
        assert recipe_page.visibility_of_recipe_page() is not None
        assert recipe_page.check_recipe_name() == data.RECIPE_DATA["dish"]
