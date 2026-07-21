from pages.base_page import BasePage
from pages.locators import ProductPageLocators

dict_elements_on_page = {'image_product': ProductPageLocators.IMAGE_PRODUCT,
                        'price': ProductPageLocators.PRICE,
                        'add_to_cart': ProductPageLocators.ADD_TO_CART,
                        'facebook': ProductPageLocators.FACEBOOK,
                        'product_details': ProductPageLocators.PRODUCT_DETAILS}

class ProductPage(BasePage):


    def check_visibility_and_clickable_element(self, element: str) -> None:
        assert self.if_element_present(*dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."
        assert self.if_element_clickable(*dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        assert self.if_element_present(*dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."