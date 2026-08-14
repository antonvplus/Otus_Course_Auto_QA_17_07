from pages.base_page import BasePage
from selenium.webdriver.common.by import By

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


    def check_clickable_element(self, element: str) -> None:
        assert self.is_element_clickable(self.dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.is_element_present(self.dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def check_price(self, currency: str) -> None:
        if currency == 'EUR':
            assert self.get_text_element(self.PRICE_FIRST_PRODUCT) == '€19.12', \
                f"Expect: '€19.12', Actual: '{self.get_text_element(self.PRICE_FIRST_PRODUCT)}'"
            assert self.get_text_element(self.PRICE_SECOND_PRODUCT) == '€28.72', \
                f"Expect: '€28.72', Actual: '{self.get_text_element(self.PRICE_SECOND_PRODUCT)}'"
            assert self.get_text_element(self.PRICE_THIRD_PRODUCT) == '€29.00', \
                f"Expect: '€29.00', Actual: '{self.get_text_element(self.PRICE_THIRD_PRODUCT)}'"
        elif currency == 'USD':
            assert self.get_text_element(self.PRICE_FIRST_PRODUCT) == '$21.80', \
                f"Expect: '$21.86', Actual: '{self.get_text_element(self.PRICE_FIRST_PRODUCT)}'"
            assert self.get_text_element(self.PRICE_SECOND_PRODUCT) == '$32.75', \
                f"Expect: '$32.83', Actual: '{self.get_text_element(self.PRICE_SECOND_PRODUCT)}'"
            assert self.get_text_element(self.PRICE_THIRD_PRODUCT) == '$33.07', \
                f"Expect: '$33.15', Actual: '{self.get_text_element(self.PRICE_THIRD_PRODUCT)}'"

    def change_currency(self):
        self.click_on_element(self.CURRENCY)
        self.click_on_element(self.CURRENCY_USD)
