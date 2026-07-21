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

    def if_element_present(self, how: str, what: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how: str , what: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def if_element_clickable(self, how: str, what: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def fill_in_text_field(self, how: str, what: str, text: str, timeout: int = 5) -> None:
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what))).send_keys(text)
        except TimeoutException:
            assert False, "There is no element on the page"

    def click_on_element(self, how: str, what: str, timeout: int = 5) -> None:
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what))).click()
        except TimeoutException:
            assert False, "There is no element on the page"

    def get_text_element(self, how: str, what: str, timeout: int = 5) -> str:
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            assert False, "There is no element on the page"
        return element.text