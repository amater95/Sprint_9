import allure
import urls


class TestLoginPage:
    @allure.title("Регистрация пользователя")
    def test_registration(self, login_page, registration_page, new_user, driver):
        login_page.click_to_registration_button()
        registration_page.registration_user(new_user)
        assert driver.current_url == urls.URL_LOGIN
        assert login_page.visibility_login_form() is not None
