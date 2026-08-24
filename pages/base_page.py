from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import logging
import allure

class BasePage:
    def __init__(self, browser: WebDriver, base_url: str, url: str):
        self.browser = browser
        self.url = f"{base_url}{url}"
        self.logger = logging.getLogger("Logger.BasePage")

    @allure.step("Открываем браузер")
    def open(self) -> None:
        self.browser.get(self.url)

    @allure.step("Выполняем проверку, что элемент отображается")
    def is_element_present(self, locator: tuple[str, str], timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    @allure.step("Выполняем проверку, что элемент не отображается")
    def is_not_element_present(self, locator: tuple[str, str], timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    @allure.step("Выполняем проверку, что элемент кликабельный")
    def is_element_clickable(self, locator: tuple[str, str], timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    @allure.step("Заполняем поле")
    def fill_in_text_field(self, locator: tuple[str, str], text: str, timeout: int = 5) -> None:
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)
        except TimeoutException:
            raise AssertionError(
                f"Element with locator {locator} was not found "
                f"after {timeout} seconds on page {self.browser.current_url}"
            )

    @allure.step("Очищаем поле и заполняем")
    def fill_in_text_field_which_are_introduced_from_end(self, locator: tuple[str, str], text: str, timeout: int = 5) -> None:
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            element = self.browser.find_element(*locator)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.BACK_SPACE)
            element.send_keys(text)
        except TimeoutException:
            raise AssertionError(
                f"Element with locator {locator} was not found "
                f"after {timeout} seconds on page {self.browser.current_url}"
            )

    @allure.step("Кликаем на элемент")
    def click_on_element(self, locator: tuple[str, str], timeout: int = 5) -> None:
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            raise AssertionError(
                f"Element with locator {locator} was not found "
                f"after {timeout} seconds on page {self.browser.current_url}"
            )

    @allure.step("Кликаем на чекбокс")
    def click_on_checkbox(self, locator: tuple[str, str], timeout: int = 5) -> None:
        try:
            element = self.browser.find_element(*locator)
            self.browser.execute_script("arguments[0].click();",element)
        except TimeoutException:
            raise AssertionError(
                f"Element with locator {locator} was not found "
                f"after {timeout} seconds on page {self.browser.current_url}"
            )

    @allure.step("Получаем текст элемента")
    def get_text_element(self, locator: tuple[str, str], timeout: int = 5) -> str:
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(
                f"Element with locator {locator} was not found "
                f"after {timeout} seconds on page {self.browser.current_url}"
            )
        return element.text