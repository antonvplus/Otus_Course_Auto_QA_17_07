from pages.base_page import BasePage
from pages.locators import RegistrationPageLocators

dict_elements_on_page = {'first_name': RegistrationPageLocators.FIRST_NAME,
                        'last_name': RegistrationPageLocators.LAST_NAME,
                        'email': RegistrationPageLocators.EMAIL,
                        'password': RegistrationPageLocators.PASSWORD,
                        'birthdate': RegistrationPageLocators.BIRTHDATE,
                        'save_button': RegistrationPageLocators.SAVE_BUTTON}

class RegistrationPage(BasePage):


    def check_visibility_and_clickable_element(self, element: str) -> None:
        assert self.if_element_present(*dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."
        assert self.if_element_clickable(*dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.if_element_present(*dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."