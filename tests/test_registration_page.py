from pages.registration_page import RegistrationPage
from selenium.webdriver.remote.webdriver import WebDriver
import allure

LINK = "registration"

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'first_name' на странице")
def test_availability_of_first_name(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = RegistrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'first_name'"):
        page.check_visibility_element('first_name')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'last_name' на странице")
def test_availability_of_last_name(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = RegistrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'last_name'"):
        page.check_visibility_element('last_name')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'email' на странице")
def test_availability_of_email(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = RegistrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'email'"):
        page.check_visibility_element('email')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'password' на странице")
def test_availability_of_password(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = RegistrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'password'"):
        page.check_visibility_element('password')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'birthdate' на странице")
def test_availability_of_birthdate(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = RegistrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'birthdate'"):
        page.check_visibility_element('birthdate')

@allure.severity(allure.severity_level.MINOR)
@allure.title("Тест проверяет наличие элемента 'save' на странице")
def test_availability_of_save_button(browser: WebDriver, base_url: str) -> None:
    with allure.step("Подготавливаем браузер"):
        page = RegistrationPage(browser, base_url,  LINK)
        page.open()
    with allure.step("Проверяем элемент 'save_button'"):
        page.check_clickable_element('save_button')