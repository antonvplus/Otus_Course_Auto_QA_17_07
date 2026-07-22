from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, browser: WebDriver, base_url: str, url: str):
        self.browser = browser
        self.url = f"{base_url}{url}"

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, locator: tuple[str, str], timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, locator: tuple[str, str], timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_element_clickable(self, locator: tuple[str, str], timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    def fill_in_text_field(self, locator: tuple[str, str], text: str, timeout: int = 5) -> None:
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)
        except TimeoutException:
            raise AssertionError(
                f"Element with locator {locator} was not found "
                f"after {timeout} seconds on page {self.browser.current_url}"
            )

    def click_on_element(self, locator: tuple[str, str], timeout: int = 5) -> None:
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            raise AssertionError(
                f"Element with locator {locator} was not found "
                f"after {timeout} seconds on page {self.browser.current_url}"
            )

    def get_text_element(self, locator: tuple[str, str], timeout: int = 5) -> str:
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(
                f"Element with locator {locator} was not found "
                f"after {timeout} seconds on page {self.browser.current_url}"
            )
        return element.text