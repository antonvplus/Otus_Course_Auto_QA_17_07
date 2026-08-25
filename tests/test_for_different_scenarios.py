from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.login_administration_page import LoginAdministrationPage
from pages.admin_panel_page import AdminPanelPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.registration_page import RegistrationPage
from pages.admin_catalog_products_page import AdminCatalogProductsPage
from selenium.webdriver.remote.webdriver import WebDriver
import allure

LINK_LOGIN_ADMINISTRATION = "administration/"
LINK_MAIN_PAGE = ""
LINK_CATALOG_PAGE = "2-home"
LINK_REGISTRATION = "registration"

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест проверяет логин и логаут в админ панель")
def test_login_and_logout_of_admin_panel(browser: WebDriver, base_url: str, admin_panel_page: AdminPanelPage,
                                         login_administration_page: LoginAdministrationPage) -> None:
    with allure.step("Подготавливаем браузер"):
        page = LoginAdministrationPage(browser, base_url, LINK_LOGIN_ADMINISTRATION)
        page.open()
    with allure.step("Логинимся в админ панель"):
        page = page.login_in_admin_panel(admin_panel_page)
        page.check_admin_panel_page()
    with allure.step("Логаут из админ панель"):
        page = page.logout_from_admin_panel(login_administration_page)
        page.check_login_admin_page()

@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест проверяет добавление товара в корзину")
def test_add_item_to_cart_and_check_that_it_is_in_cart(browser: WebDriver, base_url: str, product_page: ProductPage, cart_page: CartPage) -> None:
    with allure.step("Подготавливаем браузер"):
        page = MainPage(browser, base_url, LINK_MAIN_PAGE)
        page.open()
    with allure.step("Добавляем товар в корзину"):
        page = page.click_on_product(product_page)
        page = page.add_item_to_cart(cart_page)
    with allure.step("Проверяем товар в корзине"):
        page.check_item_in_cart()

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет переключение валюты на главной странице")
def test_when_switching_currencies_prices_change_main_page(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = MainPage(browser, base_url, LINK_MAIN_PAGE)
        page.open()
    with allure.step("Проверка цены"):
        page.check_price('EUR')
    with allure.step("Переключение валюты"):
        page.change_currency()
    with allure.step("Проверка цены"):
        page.check_price('USD')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет переключение валюты на странице каталога")
def test_when_switching_currencies_prices_change_catalog_page(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = CatalogPage(browser, base_url, LINK_CATALOG_PAGE)
        page.open()
    with allure.step("Проверка цены"):
        page.check_price('EUR')
    with allure.step("Переключение валюты"):
        page.change_currency()
    with allure.step("Проверка цены"):
        page.check_price('USD')

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест проверяет регистрацию нового пользователя")
def test_new_user_registration(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = RegistrationPage(browser, base_url, LINK_REGISTRATION)
        page.open()
    with allure.step("Регистрируем нового пользователя"):
        name, last_name = page.fill_in_all_fields()
        page.check_new_user(name, last_name)

@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест проверяет добавление нового товара в админ панели")
def test_add_new_product_in_admin_section(browser: WebDriver, base_url: str,
                                          admin_panel_page: AdminPanelPage, admin_catalog_products_page: AdminCatalogProductsPage) -> None:
    with allure.step("Подготавливаем браузер"):
        page = LoginAdministrationPage(browser, base_url, LINK_LOGIN_ADMINISTRATION)
        page.open()
    with allure.step("Логин в админ панель"):
        page = page.login_in_admin_panel(admin_panel_page)
    with allure.step("Добавление нового товара"):
        page = page.go_to_admin_catalog_products_page(admin_catalog_products_page)
        page.add_new_product()
    with allure.step("Проверка нового товара"):
        page.check_new_product()

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет удаление товара в админ панели")
def test_delete_product_in_admin_section(browser: WebDriver, base_url: str,
                                          admin_panel_page: AdminPanelPage, admin_catalog_products_page: AdminCatalogProductsPage) -> None:
    with allure.step("Подготавливаем браузер"):
        page = LoginAdministrationPage(browser, base_url, LINK_LOGIN_ADMINISTRATION)
        page.open()
    with allure.step("Логин в админ панель"):
        page = page.login_in_admin_panel(admin_panel_page)
    with allure.step("Удаление товара"):
        page = page.go_to_admin_catalog_products_page(admin_catalog_products_page)
        page.delete_product()
    with allure.step("Проверка удаленного товара"):
        page.check_delete_product()
