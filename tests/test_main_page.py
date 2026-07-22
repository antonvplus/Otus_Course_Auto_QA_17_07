from pages.main_page import MainPage
from selenium.webdriver.remote.webdriver import WebDriver

LINK = ""

def test_availability_of_contact_us(browser: WebDriver, base_url: str) -> None:
    page = MainPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('contact_us')

def test_availability_of_clothes(browser: WebDriver, base_url: str) -> None:
    page = MainPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('clothes')

def test_availability_of_card_product(browser: WebDriver, base_url: str) -> None:
    page = MainPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('product')

def test_availability_of_all_products(browser: WebDriver, base_url: str) -> None:
    page = MainPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('all_products')

def test_availability_of_subscribe(browser: WebDriver, base_url: str) -> None:
    page = MainPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('subscribe')


