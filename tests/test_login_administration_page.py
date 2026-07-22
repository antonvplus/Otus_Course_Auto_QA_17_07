from pages.login_administration_page import LoginAdministrationPage
from selenium.webdriver.remote.webdriver import WebDriver

LINK = "administration/"

def test_availability_of_image(browser: WebDriver, base_url: str) -> None:
    page = LoginAdministrationPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('image')

def test_availability_of_email(browser: WebDriver, base_url: str) -> None:
    page = LoginAdministrationPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('email')

def test_availability_of_password(browser: WebDriver, base_url: str) -> None:
    page = LoginAdministrationPage(browser, base_url,  LINK)
    page.open()
    page.check_visibility_element('password')

def test_availability_of_log_in_button(browser: WebDriver, base_url: str) -> None:
    page = LoginAdministrationPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('log_in_button')

def test_availability_of_forgot_password_button(browser: WebDriver, base_url: str) -> None:
    page = LoginAdministrationPage(browser, base_url,  LINK)
    page.open()
    page.check_clickable_element('forgot_password_button')