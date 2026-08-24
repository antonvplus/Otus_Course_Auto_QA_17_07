from pages.login_administration_page import LoginAdministrationPage
from selenium.webdriver.remote.webdriver import WebDriver
import allure

LINK = "administration/"

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'image' на странице")
def test_availability_of_image(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = LoginAdministrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'image'"):
        page.check_visibility_element('image')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'email' на странице")
def test_availability_of_email(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = LoginAdministrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'email'"):
        page.check_visibility_element('email')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'password' на странице")
def test_availability_of_password(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = LoginAdministrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'password'"):
        page.check_visibility_element('password')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'log_in' на странице")
def test_availability_of_log_in_button(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = LoginAdministrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'log_in_button'"):
        page.check_clickable_element('log_in_button')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'password_button' на странице")
def test_availability_of_forgot_password_button(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = LoginAdministrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'forgot_password_button'"):
        page.check_clickable_element('forgot_password_button')