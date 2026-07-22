from pages.catalog_page import CatalogPage
from selenium.webdriver.remote.webdriver import WebDriver

LINK = "2-home"

def test_availability_of_art(browser: WebDriver, base_url: str) -> None:
    page = CatalogPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('art')

def test_availability_of_home(browser: WebDriver, base_url: str) -> None:
    page = CatalogPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('home')

def test_availability_of_sort_by(browser: WebDriver, base_url: str) -> None:
    page = CatalogPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('sort_by')

def test_availability_of_like_in_card_product(browser: WebDriver, base_url: str) -> None:
    page = CatalogPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('like_in_card_product')

def test_availability_of_next(browser: WebDriver, base_url: str) -> None:
    page = CatalogPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('next')