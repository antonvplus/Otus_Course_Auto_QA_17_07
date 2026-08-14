from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    PRODUCT = (By.CLASS_NAME, 'product-line-grid')
    PROCEED_TO_CHECKOUT_BUTTON = (By.CLASS_NAME, 'js-cart-detailed-actions')

    def check_item_in_cart(self) -> None:
        assert self.is_element_present(self.PRODUCT), "The product was not added to the cart"
        assert self.is_element_clickable(
            self.PROCEED_TO_CHECKOUT_BUTTON), "The product was not added to the cart"
