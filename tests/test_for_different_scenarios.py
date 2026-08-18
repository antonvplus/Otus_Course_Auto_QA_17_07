from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.login_administration_page import LoginAdministrationPage
from pages.admin_panel_page import AdminPanelPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.registration_page import RegistrationPage
from pages.admin_catalog_products_page import AdminCatalogProductsPage
from selenium.webdriver.remote.webdriver import WebDriver


LINK_LOGIN_ADMINISTRATION = "administration/"
LINK_MAIN_PAGE = ""
LINK_CATALOG_PAGE = "2-home"
LINK_REGISTRATION = "registration"

def test_login_and_logout_of_admin_panel(browser: WebDriver, base_url: str, admin_panel_page: AdminPanelPage,
                                         login_administration_page: LoginAdministrationPage) -> None:
    page = LoginAdministrationPage(browser, base_url, LINK_LOGIN_ADMINISTRATION)
    page.open()
    page = page.login_in_admin_panel(admin_panel_page)
    page.check_admin_panel_page()
    page = page.logout_from_admin_panel(login_administration_page)
    page.check_login_admin_page()

def test_add_item_to_cart_and_check_that_it_is_in_cart(browser: WebDriver, base_url: str, product_page: ProductPage, cart_page: CartPage) -> None:
    page = MainPage(browser, base_url, LINK_MAIN_PAGE)
    page.open()
    page = page.click_on_product(product_page)
    page = page.add_item_to_cart(cart_page)
    page.check_item_in_cart()

def test_when_switching_currencies_prices_change_main_page(browser: WebDriver, base_url: str) -> None:
    page = MainPage(browser, base_url, LINK_MAIN_PAGE)
    page.open()
    page.check_price('EUR')
    page.change_currency()
    page.check_price('USD')

def test_when_switching_currencies_prices_change_catalog_page(browser: WebDriver, base_url: str) -> None:
    page = CatalogPage(browser, base_url, LINK_CATALOG_PAGE)
    page.open()
    page.check_price('EUR')
    page.change_currency()
    page.check_price('USD')

def test_new_user_registration(browser: WebDriver, base_url: str) -> None:
    page = RegistrationPage(browser, base_url, LINK_REGISTRATION)
    page.open()
    name, last_name = page.fill_in_all_fields()
    page.check_new_user(name, last_name)

def test_add_new_product_in_admin_section(browser: WebDriver, base_url: str,
                                          admin_panel_page: AdminPanelPage, admin_catalog_products_page: AdminCatalogProductsPage) -> None:
    page = LoginAdministrationPage(browser, base_url, LINK_LOGIN_ADMINISTRATION)
    page.open()
    page = page.login_in_admin_panel(admin_panel_page)
    page = page.go_to_admin_catalog_products_page(admin_catalog_products_page)
    page.add_new_product()
    page.check_new_product()

def test_delete_product_in_admin_section(browser: WebDriver, base_url: str,
                                          admin_panel_page: AdminPanelPage, admin_catalog_products_page: AdminCatalogProductsPage) -> None:
    page = LoginAdministrationPage(browser, base_url, LINK_LOGIN_ADMINISTRATION)
    page.open()
    page = page.login_in_admin_panel(admin_panel_page)
    page = page.go_to_admin_catalog_products_page(admin_catalog_products_page)
    page.delete_product()
    page.check_delete_product()
