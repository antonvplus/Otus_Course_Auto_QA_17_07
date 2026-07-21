from pages.login_administration_page import LoginAdministrationPage
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from selenium.webdriver.remote.webdriver import WebDriver


LINK_LOGIN_ADMINISTRATION = "administration/"
LINK_MAIN_PAGE = ""
LINK_CATALOG_PAGE = "2-home"

def test_login_and_logout_of_admin_panel(browser: WebDriver, base_url: str) -> None:
    page = LoginAdministrationPage(browser, base_url, LINK_LOGIN_ADMINISTRATION)
    page.open()
    page.login_in_admin_panel()
    page.login_check_was_completed()
    page.logout_from_admin_panel()
    page.check_current_page()

def test_add_item_to_cart_and_check_that_it_is_in_cart(browser: WebDriver, base_url: str) -> None:
    page = MainPage(browser, base_url, LINK_MAIN_PAGE)
    page.open()
    page.add_item_to_cart()
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