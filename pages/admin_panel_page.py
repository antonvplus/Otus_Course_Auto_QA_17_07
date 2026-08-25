from __future__ import annotations
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
import logging
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("Logger.AdminPanelPage")

    def open(self) -> None:
        self.logger.info(f"Открыт браузер: {self.url}")
        super().open()

    @allure.step("Выполняем проверку, что открылась страница админ панель")
    def check_admin_panel_page(self) -> None:
        self.logger.info("Проверка, что открылась страница админ панель")
        assert all([self.is_element_present(self.DEMO_MODE),
                    self.is_element_present(self.FORECAST),
                    self.is_element_present(self.DASHBOARD),
                    self.is_element_present(self.PRODUCTS_AND_SALES)]), "The admin panel page did not open."

    @allure.step("Выходим из админ панели")
    def logout_from_admin_panel(self, login_administration_page: LoginAdministrationPage) -> LoginAdministrationPage:
        self.logger.info("Выход, из админ панели")
        self.logger.info("Клик на элемент 'USER_BUTTON'")
        self.click_on_element(self.USER_BUTTON)
        self.logger.info("Клик на элемент 'SIGN_OUT_BUTTON'")
        self.click_on_element(self.SIGN_OUT_BUTTON)
        self.logger.info("Переход на страницу LoginAdministrationPage")
        return login_administration_page

    @allure.step("Переходим на страницу админ каталог")
    def go_to_admin_catalog_products_page(self, admin_catalog_products_page: AdminCatalogProductsPage) -> AdminCatalogProductsPage:
        self.logger.info("Клик на элемент 'LIST_CATALOG'")
        self.click_on_element(self.LIST_CATALOG)
        self.logger.info("Клик на элемент 'LIST_PRODUCTS'")
        self.click_on_element(self.LIST_PRODUCTS)
        self.logger.info("Переход на страницу AdminCatalogProductsPage")
        return admin_catalog_products_page