from pages.registration_page import RegistrationPage
from selenium.webdriver.remote.webdriver import WebDriver

LINK = "registration"

def test_availability_of_first_name(browser: WebDriver, base_url: str) -> None:
    page = RegistrationPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('first_name')

def test_availability_of_last_name(browser: WebDriver, base_url: str) -> None:
    page = RegistrationPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('last_name')

def test_availability_of_email(browser: WebDriver, base_url: str) -> None:
    page = RegistrationPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('email')

def test_availability_of_password(browser: WebDriver, base_url: str) -> None:
    page = RegistrationPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('password')

def test_availability_of_birthdate(browser: WebDriver, base_url: str) -> None:
    page = RegistrationPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('birthdate')

def test_availability_of_save_button(browser: WebDriver, base_url: str) -> None:
    page = RegistrationPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('save_button')