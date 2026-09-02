from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
import allure

class CatalogPage(BasePage):
    ART = (By.CSS_SELECTOR, '#subcategories > ul > li:nth-child(3) > div.subcategory-image > a')
    HOME = (By.ID, 'js-product-list-header')
    SORT_BY = (By.CSS_SELECTOR, 'div.col-xs-8.col-sm-7.col-md-9.products-sort-order.dropdown > button')
    LIKE_HUMMINGBIRD_PRINTED_SWEATER = (By.CSS_SELECTOR, 'div.products.row > div:nth-child(2) > article > div > button')
    NEXT = (By.CSS_SELECTOR, 'div.col-md-6.offset-md-2.pr-0 > ul > li:nth-child(3) > a')
    PRICE_FIRST_PRODUCT = (By.CSS_SELECTOR,
                           'div.products.row > div:nth-child(1) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    PRICE_SECOND_PRODUCT = (By.CSS_SELECTOR,
                            'div.products.row > div:nth-child(2) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    PRICE_THIRD_PRODUCT = (By.CSS_SELECTOR,
                           'div.products.row > div:nth-child(3) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    CURRENCY = (By.CSS_SELECTOR, '#_desktop_currency_selector > div > button')
    CURRENCY_USD = (By.CSS_SELECTOR, '#_desktop_currency_selector > div > ul > li:nth-child(2) > a')

    dict_elements_on_page = {'art': ART,
                             'home': HOME,
                             'sort_by': SORT_BY,
                             'like_in_card_product': LIKE_HUMMINGBIRD_PRINTED_SWEATER,
                             'next': NEXT}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("Logger.CatalogPage")

    def open(self) -> None:
        self.logger.info(f"Открыт браузер: {self.url}")
        super().open()

    def check_clickable_element(self, element: str) -> None:
        self.logger.info(f"Проверка, что элемент {element} кликабельный")
        assert self.is_element_clickable(self.dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        self.logger.info(f"Проверка, что элемент {element} отображается на странице")
        assert self.is_element_present(self.dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

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
                assert self.get_text_element(self.PRICE_FIRST_PRODUCT) == '$22.29', \
                    f"Expect: '$22.29', Actual: '{self.get_text_element(self.PRICE_FIRST_PRODUCT)}'"
                assert self.get_text_element(self.PRICE_SECOND_PRODUCT) == '$33.48', \
                    f"Expect: '$33.48', Actual: '{self.get_text_element(self.PRICE_SECOND_PRODUCT)}'"
                assert self.get_text_element(self.PRICE_THIRD_PRODUCT) == '$33.81', \
                    f"Expect: '$33.81', Actual: '{self.get_text_element(self.PRICE_THIRD_PRODUCT)}'"

    def change_currency(self):
        self.logger.info("Смена валюты")
        with allure.step("Смена валюты"):
            self.click_on_element(self.CURRENCY)
            self.click_on_element(self.CURRENCY_USD)
