from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pages.login_administration_page import LoginAdministrationPage
    from pages.admin_catalog_products_page import AdminCatalogProductsPage

class AdminPanelPage(BasePage):

    DEMO_MODE = (By.ID, 'page-header-desc-configuration-switch_demo')
    FORECAST = (By.ID, 'dashgoals')
    DASHBOARD = (By.ID, 'dashtrends')
    PRODUCTS_AND_SALES = (By.ID, 'dashproducts')
    USER_BUTTON = (By.ID, 'header_employee_box')
    SIGN_OUT_BUTTON = (By.ID, 'header_logout')
    LIST_CATALOG = (By.ID, "subtab-AdminCatalog")
    LIST_PRODUCTS = (By.ID, "subtab-AdminProducts")
    SIDEBAR = (By.CSS_SELECTOR, "#header_infos > i")

    def check_admin_panel_page(self) -> None:
        assert all([self.is_element_present(self.DEMO_MODE),
                    self.is_element_present(self.FORECAST),
                    self.is_element_present(self.DASHBOARD),
                    self.is_element_present(self.PRODUCTS_AND_SALES)]), "The admin panel page did not open."

    def logout_from_admin_panel(self, login_administration_page: LoginAdministrationPage) -> LoginAdministrationPage:
        self.click_on_element(self.USER_BUTTON)
        self.click_on_element(self.SIGN_OUT_BUTTON)
        return login_administration_page

    def go_to_admin_catalog_products_page(self, admin_catalog_products_page: AdminCatalogProductsPage) -> AdminCatalogProductsPage:
        self.click_on_element(self.LIST_CATALOG)
        self.click_on_element(self.LIST_PRODUCTS)
        return admin_catalog_products_page