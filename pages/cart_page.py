from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):

    def check_item_in_cart(self) -> None:
        assert self.is_element_present(CartPageLocators.PRODUCT), "The product was not added to the cart"
        assert self.is_element_clickable(
            CartPageLocators.PROCEED_TO_CHECKOUT_BUTTON), "The product was not added to the cart"
