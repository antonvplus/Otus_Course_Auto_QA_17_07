from pages.product_page import ProductPage
from selenium.webdriver.remote.webdriver import WebDriver
import allure

LINK = "women/2-9-brown-bear-printed-sweater.html#/1-size-s"

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'image_product' на странице")
def test_availability_of_image_product(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = ProductPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'image_product'"):
        page.check_clickable_element('image_product')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'price' на странице")
def test_availability_of_price(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = ProductPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'price'"):
        page.check_visibility_element('price')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'add_to_cart' на странице")
def test_availability_of_add_to_cart(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = ProductPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'add_to_cart'"):
        page.check_clickable_element('add_to_cart')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'facebook' на странице")
def test_availability_of_facebook(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = ProductPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'facebook'"):
        page.check_clickable_element('facebook')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'product_details' на странице")
def test_availability_of_product_details(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = ProductPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'product_details'"):
        page.check_clickable_element('product_details')