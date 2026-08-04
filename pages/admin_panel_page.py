from pages.base_page import BasePage
from pages.locators import AdminPanelPageLocators
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pages.login_administration_page import LoginAdministrationPage
    from pages.admin_catalog_products_page import AdminCatalogProductsPage

class AdminPanelPage(BasePage):

    def check_admin_panel_page(self) -> None:
        assert all([self.is_element_present(AdminPanelPageLocators.DEMO_MODE),
                    self.is_element_present(AdminPanelPageLocators.FORECAST),
                    self.is_element_present(AdminPanelPageLocators.DASHBOARD),
                    self.is_element_present(AdminPanelPageLocators.PRODUCTS_AND_SALES)]), "The admin panel page did not open."

    def logout_from_admin_panel(self, login_administration_page: LoginAdministrationPage) -> LoginAdministrationPage:
        self.click_on_element(AdminPanelPageLocators.USER_BUTTON)
        self.click_on_element(AdminPanelPageLocators.SIGN_OUT_BUTTON)
        return login_administration_page

    def go_to_admin_catalog_products_page(self, admin_catalog_products_page: AdminCatalogProductsPage) -> AdminCatalogProductsPage:
        self.click_on_element(AdminPanelPageLocators.LIST_CATALOG)
        self.click_on_element(AdminPanelPageLocators.LIST_PRODUCTS)
        return admin_catalog_products_page