from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pages.cart_page import CartPage

class ProductPage(BasePage):

    IMAGE_PRODUCT = (By.CSS_SELECTOR, 'div.images-container.js-images-container > div.product-cover')
    PRICE = (By.CLASS_NAME, 'current-price-value')
    ADD_TO_CART = (By.CLASS_NAME, 'add-to-cart')
    FACEBOOK = (By.CLASS_NAME, 'facebook.icon-gray')
    PRODUCT_DETAILS = (By.CSS_SELECTOR, '.nav-item:nth-child(2)')
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '.cart-content-btn > a')

    dict_elements_on_page = {'image_product': IMAGE_PRODUCT,
                             'price': PRICE,
                             'add_to_cart': ADD_TO_CART,
                             'facebook': FACEBOOK,
                             'product_details': PRODUCT_DETAILS}


    def check_clickable_element(self, element: str) -> None:
        assert self.is_element_clickable(self.dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.is_element_present(self.dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def add_item_to_cart(self, cart_page: CartPage) -> CartPage:
        self.click_on_element(self.ADD_TO_CART)
        self.click_on_element(self.PROCEED_TO_CHECKOUT_BUTTON)
        return cart_page