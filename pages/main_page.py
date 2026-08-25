from pages.base_page import BasePage
import allure
import logging
from typing import TYPE_CHECKING
from selenium.webdriver.common.by import By

if TYPE_CHECKING:
    from pages.product_page import ProductPage

class MainPage(BasePage):
    CONTACT_US = (By.ID, 'contact-link')
    CLOTHES = (By.ID, 'category-3')
    PRODUCT_HUMMINGBIRD_PRINTED_SWEATER = (By.CSS_SELECTOR,
                                           '#content > section:nth-child(2) > div > div:nth-child(2) > article > div > div.thumbnail-top > a')
    ALL_PRODUCTS = (By.CSS_SELECTOR, '#content > section:nth-child(2) > a')
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, 'input.btn.btn-primary.float-xs-right.hidden-xs-down')
    PRICE_FIRST_PRODUCT = (By.CSS_SELECTOR,
                           'section:nth-child(2) > div > div:nth-child(1) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    PRICE_SECOND_PRODUCT = (By.CSS_SELECTOR,
                            'div:nth-child(2) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    PRICE_THIRD_PRODUCT = (By.CSS_SELECTOR,
                           'section:nth-child(2) > div > div:nth-child(3) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    CURRENCY = (By.CSS_SELECTOR, '#_desktop_currency_selector > div > button')
    CURRENCY_USD = (By.CSS_SELECTOR, '#_desktop_currency_selector > div > ul > li:nth-child(2) > a')

    dict_elements_on_page = {'contact_us': CONTACT_US,
                             'clothes': CLOTHES,
                             'product': PRODUCT_HUMMINGBIRD_PRINTED_SWEATER,
                             'all_products': ALL_PRODUCTS,
                             'subscribe': SUBSCRIBE_BUTTON}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("Logger.MainPage")

    def open(self) -> None:
        self.logger.info(f"Открыт браузер: {self.url}")
        super().open()

    def check_clickable_element(self, element: str) -> None:
        self.logger.info(f"Проверка, что элемент {element} кликабельный")
        assert self.is_element_clickable(self.dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def click_on_product(self, product_page: ProductPage) -> ProductPage:
        self.logger.info("Нажимаем на товар")
        self.click_on_element(self.PRODUCT_HUMMINGBIRD_PRINTED_SWEATER)
        with allure.step("Переходим на страницу товара"):
            self.logger.info("Переход на страницу ProductPage")
            return product_page


    def check_price(self, currency: str) -> None:
        if currency == 'EUR':
            self.logger.info("Проверка цены в EUR")
            with allure.step("Проверяем цену в EUR"):
                assert self.get_text_element(self.PRICE_FIRST_PRODUCT) == '€19.12', \
                    f"Expect: '€19.12', Actual: '{self.get_text_element(self.PRICE_FIRST_PRODUCT)}'"
                assert self.get_text_element(self.PRICE_SECOND_PRODUCT) == '€28.72', \
                    f"Expect: '€28.72', Actual: '{self.get_text_element(self.PRICE_SECOND_PRODUCT)}'"
                assert self.get_text_element(self.PRICE_THIRD_PRODUCT) == '€29.00', \
                    f"Expect: '€29.00', Actual: '{self.get_text_element(self.PRICE_THIRD_PRODUCT)}'"
        elif currency == 'USD':
            self.logger.info("Проверка цены в USD")
            with allure.step("Проверяем цену в USD"):
                assert self.get_text_element(self.PRICE_FIRST_PRODUCT) == '$21.80', \
                    f"Expect: '$21.86', Actual: '{self.get_text_element(self.PRICE_FIRST_PRODUCT)}'"
                assert self.get_text_element(self.PRICE_SECOND_PRODUCT) == '$32.75', \
                    f"Expect: '$32.83', Actual: '{self.get_text_element(self.PRICE_SECOND_PRODUCT)}'"
                assert self.get_text_element(self.PRICE_THIRD_PRODUCT) == '$33.07', \
                    f"Expect: '$33.15', Actual: '{self.get_text_element(self.PRICE_THIRD_PRODUCT)}'"

    def change_currency(self):
        self.logger.info("Смена валюты")
        with allure.step("Смена валюты"):
            self.click_on_element(self.CURRENCY)
            self.click_on_element(self.CURRENCY_USD)
