from pages.base_page import BasePage
from pages.locators import RegistrationPageLocators
from faker import Faker
import random

dict_elements_on_page = {'first_name': RegistrationPageLocators.FIRST_NAME,
                        'last_name': RegistrationPageLocators.LAST_NAME,
                        'email': RegistrationPageLocators.EMAIL,
                        'password': RegistrationPageLocators.PASSWORD,
                        'birthdate': RegistrationPageLocators.BIRTHDATE,
                        'save_button': RegistrationPageLocators.SAVE_BUTTON}

class RegistrationPage(BasePage):


    def check_clickable_element(self, element: str) -> None:
        assert self.is_element_clickable(dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.is_element_present(dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def fill_in_all_fields(self) -> tuple[str, str]:
        fake = Faker('en_US')
        name = fake.name()
        self.fill_in_text_field(RegistrationPageLocators.FIRST_NAME, name)
        last_name = fake.last_name()
        self.fill_in_text_field(RegistrationPageLocators.LAST_NAME, last_name)
        self.fill_in_text_field(RegistrationPageLocators.EMAIL, fake.email())
        self.fill_in_text_field(RegistrationPageLocators.PASSWORD, fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
        self.fill_in_text_field(RegistrationPageLocators.BIRTHDATE, f"{random.randint(1,12)}/{random.randint(1,28)}/{random.randint(1970, 2000)}")
        self.click_on_checkbox(RegistrationPageLocators.CHECK_BUTTON_I_AGREE)
        self.click_on_checkbox(RegistrationPageLocators.CHECK_BUTTON_CUSTOMER_DATA_PRIVACY)
        self.click_on_element(RegistrationPageLocators.SAVE_BUTTON)
        return name, last_name

    def check_new_user(self, name: str, last_name: str) -> None:
        user = self.get_text_element(RegistrationPageLocators.USER)
        assert user == f"{name} {last_name}", ("The names don't match: "
                                               f"Expect for a user named: '{name} {last_name}'"
                                               f"The user name is displayed: '{user}'")
