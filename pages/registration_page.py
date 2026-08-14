from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from faker import Faker
import random

class RegistrationPage(BasePage):

    FIRST_NAME = (By.ID, 'field-firstname')
    LAST_NAME = (By.ID, 'field-lastname')
    EMAIL = (By.ID, 'field-email')
    PASSWORD = (By.ID, 'field-password')
    BIRTHDATE = (By.ID, 'field-birthday')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'footer > button')
    CHECK_BUTTON_I_AGREE = (By.CSS_SELECTOR, 'input[name="psgdpr"]')
    CHECK_BUTTON_CUSTOMER_DATA_PRIVACY = (By.CSS_SELECTOR, 'input[name="customer_privacy"]')
    USER = (By.CSS_SELECTOR, "#_desktop_user_info > div > a.account > span")

    dict_elements_on_page = {'first_name': FIRST_NAME,
                             'last_name': LAST_NAME,
                             'email': EMAIL,
                             'password': PASSWORD,
                             'birthdate': BIRTHDATE,
                             'save_button': SAVE_BUTTON}

    def check_clickable_element(self, element: str) -> None:
        assert self.is_element_clickable(self.dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.is_element_present(self.dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def fill_in_all_fields(self) -> tuple[str, str]:
        fake = Faker('en_US')
        name = fake.name()
        self.fill_in_text_field(self.FIRST_NAME, name)
        last_name = fake.last_name()
        self.fill_in_text_field(self.LAST_NAME, last_name)
        self.fill_in_text_field(self.EMAIL, fake.email())
        self.fill_in_text_field(self.PASSWORD, fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
        self.fill_in_text_field(self.BIRTHDATE, f"{random.randint(1,12)}/{random.randint(1,28)}/{random.randint(1970, 2000)}")
        self.click_on_checkbox(self.CHECK_BUTTON_I_AGREE)
        self.click_on_checkbox(self.CHECK_BUTTON_CUSTOMER_DATA_PRIVACY)
        self.click_on_element(self.SAVE_BUTTON)
        return name, last_name

    def check_new_user(self, name: str, last_name: str) -> None:
        user = self.get_text_element(self.USER)
        assert user == f"{name} {last_name}", ("The names don't match: "
                                               f"Expect for a user named: '{name} {last_name}'"
                                               f"The user name is displayed: '{user}'")
