from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pages.admin_panel_page import AdminPanelPage

class LoginAdministrationPage(BasePage):

    IMAGE = (By.ID, 'shop-img')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    LOG_IN_BUTTON = (By.ID, 'submit_login')
    I_FORGOT_MY_PASSWORD_BUTTON = (By.ID, 'forgot-password-link')

    dict_elements_on_page = {'image': IMAGE,
                             'email': EMAIL,
                             'password': PASSWORD,
                             'log_in_button': LOG_IN_BUTTON,
                             'forgot_password_button': I_FORGOT_MY_PASSWORD_BUTTON}

    def check_clickable_element(self, element: str) -> None:
        assert self.is_element_clickable(self.dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.is_element_present(self.dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def login_in_admin_panel(self, admin_panel_page: AdminPanelPage) -> AdminPanelPage:
        self.fill_in_text_field(self.EMAIL, 'admin@example.com')
        self.fill_in_text_field(self.PASSWORD, 'Admin123!')
        self.click_on_element(self.LOG_IN_BUTTON)
        return admin_panel_page


    def check_login_admin_page(self) -> None:
        assert all([self.is_element_present(self.EMAIL),
                    self.is_element_present(self.PASSWORD),
                    self.is_element_present(self.LOG_IN_BUTTON)]), "This is not a login page"

