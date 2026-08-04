from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pages.cart_page import CartPage

dict_elements_on_page = {'image_product': ProductPageLocators.IMAGE_PRODUCT,
                        'price': ProductPageLocators.PRICE,
                        'add_to_cart': ProductPageLocators.ADD_TO_CART,
                        'facebook': ProductPageLocators.FACEBOOK,
                        'product_details': ProductPageLocators.PRODUCT_DETAILS}

class ProductPage(BasePage):


    def check_clickable_element(self, element: str) -> None:
        assert self.is_element_clickable(dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.is_element_present(dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def add_item_to_cart(self, cart_page: CartPage) -> CartPage:
        self.click_on_element(ProductPageLocators.ADD_TO_CART)
        self.click_on_element(ProductPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        return cart_page