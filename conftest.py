import pytest
import helpers
import urls

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.create_recipe_page import CreateRecipePage
from pages.registration_page import RegistrationPage
from pages.recipe_page import RecipePage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False
    })
    driver = webdriver.Remote(command_executor="http://selenoid:4444/wd/hub", options=options)
    driver.get(urls.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture()
def create_recipe_page(driver):
    return CreateRecipePage(driver)

@pytest.fixture()
def main_page(driver):
    return MainPage(driver)

@pytest.fixture()
def registration_page(driver):
    return RegistrationPage(driver)

@pytest.fixture()
def recipe_page(driver):
    return RecipePage(driver)

@pytest.fixture()
def new_user():
    return helpers.generate_user_data()

@pytest.fixture()
def registrated_user(registration_page, login_page, new_user):
    login_page.click_to_registration_button()
    registration_page.registration_user(new_user)
    return new_user

@pytest.fixture()
def login_user(login_page, registrated_user):
    login_page.login_user(registrated_user)
    return registrated_user
