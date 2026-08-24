from pages.catalog_page import CatalogPage
from selenium.webdriver.remote.webdriver import WebDriver
import allure

LINK = "2-home"

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'art' на странице")
def test_availability_of_art(browser: WebDriver, base_url: str, request) -> None:
    with allure.step("Подготавливаем браузер"):
        page = CatalogPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'art'"):
        page.check_clickable_element('art')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'home' на странице")
def test_availability_of_home(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = CatalogPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'home'"):
        page.check_visibility_element('home')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'sort_by' на странице")
def test_availability_of_sort_by(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = CatalogPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'sort_by'"):
        page.check_clickable_element('sort_by')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'like_in_card_product' на странице")
def test_availability_of_like_in_card_product(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = CatalogPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'like_in_card_product'"):
        page.check_clickable_element('like_in_card_product')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'next' на странице")
def test_availability_of_next(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = CatalogPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'next'"):
        page.check_clickable_element('next')
