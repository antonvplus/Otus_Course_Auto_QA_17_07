from pages.base_page import BasePage
from pages.locators import CatalogPageLocators
from pages.locators import MainPageLocators

dict_elements_on_page = {'art': CatalogPageLocators.ART,
                        'home': CatalogPageLocators.HOME,
                        'sort_by': CatalogPageLocators.SORT_BY,
                        'like_in_card_product': CatalogPageLocators.LIKE_HUMMINGBIRD_PRINTED_SWEATER,
                        'next': CatalogPageLocators.NEXT}

class CatalogPage(BasePage):


    def check_visibility_and_clickable_element(self, element: str) -> None:
        assert self.if_element_present(*dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."
        assert self.if_element_clickable(*dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.if_element_present(*dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def check_price(self, currency: str) -> None:
        if currency == 'EUR':
            assert self.get_text_element(*CatalogPageLocators.PRICE_FIRST_PRODUCT) == '€19.12', f"Expect: '€19.12', Actual: '{self.get_text_element(*MainPageLocators.PRICE_FIRST_PRODUCT)}'"
            assert self.get_text_element(*CatalogPageLocators.PRICE_SECOND_PRODUCT) == '€28.72', f"Expect: '€28.72', Actual: '{self.get_text_element(*MainPageLocators.PRICE_SECOND_PRODUCT)}'"
            assert self.get_text_element(*CatalogPageLocators.PRICE_THIRD_PRODUCT) == '€29.00', f"Expect: '€29.00', Actual: '{self.get_text_element(*MainPageLocators.PRICE_THIRD_PRODUCT)}'"
        elif currency == 'USD':
            assert self.get_text_element(*CatalogPageLocators.PRICE_FIRST_PRODUCT) == '$21.86', f"Expect: '$21.86', Actual: '{self.get_text_element(*MainPageLocators.PRICE_FIRST_PRODUCT)}'"
            assert self.get_text_element(*CatalogPageLocators.PRICE_SECOND_PRODUCT) == '$32.83', f"Expect: '$32.83', Actual: '{self.get_text_element(*MainPageLocators.PRICE_SECOND_PRODUCT)}'"
            assert self.get_text_element(*CatalogPageLocators.PRICE_THIRD_PRODUCT) == '$33.15', f"Expect: '$33.15', Actual: '{self.get_text_element(*MainPageLocators.PRICE_THIRD_PRODUCT)}'"

    def change_currency(self):
        self.click_on_element(*MainPageLocators.CURRENCY)
        self.click_on_element(*MainPageLocators.CURRENCY_USD)
