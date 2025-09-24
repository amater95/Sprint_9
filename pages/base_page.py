import allure
import data

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие: {url}")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, data.WAITING_TIME).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Нажатие на элемент")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, data.WAITING_TIME).until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step("Ввод текста в элемент")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получение текста из элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Ожидание изменения URL")
    def wait_until_url_is_changed(self, url):
        return WebDriverWait(self.driver, data.WAITING_TIME).until(expected_conditions.url_to_be(url))

    @allure.step("Добавление фото в загрузчик")
    def add_photo_to_uploader(self, locator, photo):
        WebDriverWait(self.driver, data.WAITING_TIME).until(expected_conditions.presence_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(photo)

    @staticmethod
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)
