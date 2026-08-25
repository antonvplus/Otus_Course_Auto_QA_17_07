from pages.main_page import MainPage
from selenium.webdriver.remote.webdriver import WebDriver
import allure

LINK = ""

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'contact_us' на странице")
def test_availability_of_contact_us(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = MainPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'contact_us'"):
        page.check_clickable_element('contact_us')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'clothes' на странице")
def test_availability_of_clothes(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = MainPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'clothes'"):
        page.check_clickable_element('clothes')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'card_product' на странице")
def test_availability_of_card_product(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = MainPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'product'"):
        page.check_clickable_element('product')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'all_products' на странице")
def test_availability_of_all_products(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = MainPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'all_products'"):
        page.check_clickable_element('all_products')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'subscribe' на странице")
def test_availability_of_subscribe(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = MainPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'subscribe'"):
        page.check_clickable_element('subscribe')


