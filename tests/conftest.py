import pytest
from pages.login_administration_page import LoginAdministrationPage
from pages.admin_panel_page import AdminPanelPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.admin_catalog_products_page import AdminCatalogProductsPage
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture
def login_administration_page(browser:WebDriver, base_url:str) -> LoginAdministrationPage:
    return LoginAdministrationPage(browser=browser, base_url=base_url, url="administration/")

@pytest.fixture
def admin_panel_page(browser:WebDriver, base_url:str) -> AdminPanelPage:
    return AdminPanelPage(browser=browser, base_url=base_url, url="administration/")

@pytest.fixture
def product_page(browser:WebDriver, base_url:str) -> ProductPage:
    return ProductPage(browser=browser, base_url=base_url, url="women/2-9-brown-bear-printed-sweater.html#/1-size-s")

@pytest.fixture
def cart_page(browser:WebDriver, base_url:str) -> CartPage:
    return CartPage(browser=browser, base_url=base_url, url="cart")

@pytest.fixture
def admin_catalog_products_page(browser:WebDriver, base_url:str) -> AdminCatalogProductsPage:
    return AdminCatalogProductsPage(browser=browser, base_url=base_url, url="sell/catalog/products-v2")