from pages.product_page import ProductPage
from selenium.webdriver.remote.webdriver import WebDriver

LINK = "women/2-9-brown-bear-printed-sweater.html#/1-size-s"

def test_availability_of_image_product(browser: WebDriver, base_url: str) -> None:
    page = ProductPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_and_clickable_element('image_product')

def test_availability_of_price(browser: WebDriver, base_url: str) -> None:
    page = ProductPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('price')

def test_availability_of_add_to_cart(browser: WebDriver, base_url: str) -> None:
    page = ProductPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_and_clickable_element('add_to_cart')

def test_availability_of_facebook(browser: WebDriver, base_url: str) -> None:
    page = ProductPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_and_clickable_element('facebook')

def test_availability_of_product_details(browser: WebDriver, base_url: str) -> None:
    page = ProductPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_and_clickable_element('product_details')