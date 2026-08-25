from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
import logging
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("Logger.ProductPage")

    def open(self) -> None:
        self.logger.info(f"Открыт браузер: {self.url}")
        super().open()

    def check_clickable_element(self, element: str) -> None:
        self.logger.info(f"Проверка, что элемент {element} кликабельный")
        assert self.is_element_clickable(self.dict_elements_on_page[element]), f"Non-clickable element '{element}' on the page."

    def check_visibility_element(self, element: str) -> None:
        self.logger.info(f"Проверка, что элемент {element} отображается на странице")
        assert self.is_element_present(self.dict_elements_on_page[element]), f"The element '{element}' is not displayed on the page."

    def add_item_to_cart(self, cart_page: CartPage) -> CartPage:
        self.logger.info("Добавление товара в корзину")
        with allure.step("Добавление товара в корзину"):
            self.click_on_element(self.ADD_TO_CART)
            self.click_on_element(self.PROCEED_TO_CHECKOUT_BUTTON)
        with allure.step("Переходим в корзину"):
            self.logger.info("Переход на страницу CartPage")
            return cart_page