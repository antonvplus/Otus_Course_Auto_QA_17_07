from pages.base_page import BasePage
from pages.locators import MainPageLocators
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pages.product_page import ProductPage

dict_elements_on_page = {'contact_us': MainPageLocators.CONTACT_US,
                        'clothes': MainPageLocators.CLOTHES,
                        'product': MainPageLocators.PRODUCT_HUMMINGBIRD_PRINTED_SWEATER,
                        'all_products': MainPageLocators.ALL_PRODUCTS,
                        'subscribe': MainPageLocators.SUBSCRIBE_BUTTON}

class MainPage(BasePage):


    def check_clickable_element(self, element: str) -> None:
        assert self.is_element_clickable(dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def click_on_product(self, product_page: ProductPage) -> ProductPage:
        self.click_on_element(MainPageLocators.PRODUCT_HUMMINGBIRD_PRINTED_SWEATER)
        return product_page


    def check_price(self, currency: str) -> None:
        if currency == 'EUR':
            assert self.get_text_element(MainPageLocators.PRICE_FIRST_PRODUCT) == '€19.12', \
                f"Expect: '€19.12', Actual: '{self.get_text_element(MainPageLocators.PRICE_FIRST_PRODUCT)}'"
            assert self.get_text_element(MainPageLocators.PRICE_SECOND_PRODUCT) == '€28.72', \
                f"Expect: '€28.72', Actual: '{self.get_text_element(MainPageLocators.PRICE_SECOND_PRODUCT)}'"
            assert self.get_text_element(MainPageLocators.PRICE_THIRD_PRODUCT) == '€29.00', \
                f"Expect: '€29.00', Actual: '{self.get_text_element(MainPageLocators.PRICE_THIRD_PRODUCT)}'"
        elif currency == 'USD':
            assert self.get_text_element(MainPageLocators.PRICE_FIRST_PRODUCT) == '$21.80', \
                f"Expect: '$21.86', Actual: '{self.get_text_element(MainPageLocators.PRICE_FIRST_PRODUCT)}'"
            assert self.get_text_element(MainPageLocators.PRICE_SECOND_PRODUCT) == '$32.75', \
                f"Expect: '$32.83', Actual: '{self.get_text_element(MainPageLocators.PRICE_SECOND_PRODUCT)}'"
            assert self.get_text_element(MainPageLocators.PRICE_THIRD_PRODUCT) == '$33.07', \
                f"Expect: '$33.15', Actual: '{self.get_text_element(MainPageLocators.PRICE_THIRD_PRODUCT)}'"

    def change_currency(self):
        self.click_on_element(MainPageLocators.CURRENCY)
        self.click_on_element(MainPageLocators.CURRENCY_USD)
