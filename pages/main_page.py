from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.locators import ProductPageLocators
from pages.locators import CartPageLocators

dict_elements_on_page = {'contact_us': MainPageLocators.CONTACT_US,
                        'clothes': MainPageLocators.CLOTHES,
                        'product': MainPageLocators.PRODUCT_HUMMINGBIRD_PRINTED_SWEATER,
                        'all_products': MainPageLocators.ALL_PRODUCTS,
                        'subscribe': MainPageLocators.SUBSCRIBE_BUTTON}

class MainPage(BasePage):


    def check_visibility_and_clickable_element(self, element: str) -> None:
        assert self.if_element_present(*dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."
        assert self.if_element_clickable(*dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def add_item_to_cart(self) -> None:
        self.click_on_element(*MainPageLocators.PRODUCT_HUMMINGBIRD_PRINTED_SWEATER)
        self.click_on_element(*ProductPageLocators.ADD_TO_CART)
        assert self.if_element_clickable(*ProductPageLocators.PROCEED_TO_CHECKOUT_BUTTON), "There is no button: 'proceed to checkout'"
        self.click_on_element(*ProductPageLocators.PROCEED_TO_CHECKOUT_BUTTON)

    def check_item_in_cart(self) -> None:
        assert self.if_element_present(*CartPageLocators.PRODUCT), "The item was not added to the cart"
        assert self.if_element_clickable(*CartPageLocators.PROCEED_TO_CHECKOUT_BUTTON)

    def check_price(self, currency: str) -> None:
        if currency == 'EUR':
            assert self.get_text_element(*MainPageLocators.PRICE_FIRST_PRODUCT) == '€19.12', f"Expect: '€19.12', Actual: '{self.get_text_element(*MainPageLocators.PRICE_FIRST_PRODUCT)}'"
            assert self.get_text_element(*MainPageLocators.PRICE_SECOND_PRODUCT) == '€28.72', f"Expect: '€28.72', Actual: '{self.get_text_element(*MainPageLocators.PRICE_SECOND_PRODUCT)}'"
            assert self.get_text_element(*MainPageLocators.PRICE_THIRD_PRODUCT) == '€29.00', f"Expect: '€29.00', Actual: '{self.get_text_element(*MainPageLocators.PRICE_THIRD_PRODUCT)}'"
        elif currency == 'USD':
            assert self.get_text_element(*MainPageLocators.PRICE_FIRST_PRODUCT) == '$21.86', f"Expect: '$21.86', Actual: '{self.get_text_element(*MainPageLocators.PRICE_FIRST_PRODUCT)}'"
            assert self.get_text_element(*MainPageLocators.PRICE_SECOND_PRODUCT) == '$32.83', f"Expect: '$32.83', Actual: '{self.get_text_element(*MainPageLocators.PRICE_SECOND_PRODUCT)}'"
            assert self.get_text_element(*MainPageLocators.PRICE_THIRD_PRODUCT) == '$33.15', f"Expect: '$33.15', Actual: '{self.get_text_element(*MainPageLocators.PRICE_THIRD_PRODUCT)}'"

    def change_currency(self):
        self.click_on_element(*MainPageLocators.CURRENCY)
        self.click_on_element(*MainPageLocators.CURRENCY_USD)
