import allure
import urls


class TestLoginPage:
    @allure.title("Авторизация пользователя")
    def test_login(self, registrated_user, login_page, main_page, driver):
        login_page.login_user(registrated_user)
        assert main_page.visibility_of_logout_button() is not None
        assert driver.current_url == urls.URL_RECIPES
