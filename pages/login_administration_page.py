from pages.base_page import BasePage
from pages.locators import LoginAdministrationPageLocators
from pages.locators import AdminPanelPageLocators

dict_elements_on_page = {'image': LoginAdministrationPageLocators.IMAGE,
                        'email': LoginAdministrationPageLocators.EMAIL,
                        'password': LoginAdministrationPageLocators.PASSWORD,
                        'log_in_button': LoginAdministrationPageLocators.LOG_IN_BUTTON,
                        'forgot_password_button': LoginAdministrationPageLocators.I_FORGOT_MY_PASSWORD_BUTTON}

class LoginAdministrationPage(BasePage):


    def check_visibility_and_clickable_element(self, element: str) -> None:
        assert self.if_element_present(*dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."
        assert self.if_element_clickable(*dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.if_element_present(*dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def login_in_admin_panel(self) -> None:
        self.fill_in_text_field(*LoginAdministrationPageLocators.EMAIL, 'admin@example.com')
        self.fill_in_text_field(*LoginAdministrationPageLocators.PASSWORD, 'Admin123!')
        self.click_on_element(*LoginAdministrationPageLocators.LOG_IN_BUTTON)

    def login_check_was_completed(self) -> None:
        assert all([self.if_element_present(*AdminPanelPageLocators.DEMO_MODE),
                    self.if_element_present(*AdminPanelPageLocators.FORECAST),
                    self.if_element_present(*AdminPanelPageLocators.DASHBOARD),
                    self.if_element_present(*AdminPanelPageLocators.PRODUCTS_AND_SALES)]), "The wrong page opened"

    def check_current_page(self) -> None:
        assert all([self.if_element_present(*LoginAdministrationPageLocators.EMAIL),
                    self.if_element_present(*LoginAdministrationPageLocators.PASSWORD),
                    self.if_element_present(*LoginAdministrationPageLocators.LOG_IN_BUTTON)]), "This is not a login page"

    def logout_from_admin_panel(self) -> None:
        self.click_on_element(*AdminPanelPageLocators.USER_BUTTON)
        self.click_on_element(*AdminPanelPageLocators.SIGN_OUT_BUTTON)


