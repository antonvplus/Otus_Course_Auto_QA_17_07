from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
import allure


class CartPage(BasePage):

    PRODUCT = (By.CLASS_NAME, 'product-line-grid')
    PROCEED_TO_CHECKOUT_BUTTON = (By.CLASS_NAME, 'js-cart-detailed-actions')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("Logger.CartPage")

    def open(self) -> None:
        self.logger.info(f"Открыт браузер: {self.url}")
        super().open()

    @allure.step("Выполняем проверку товара в корзине")
    def check_item_in_cart(self) -> None:
        self.logger.info("Проверка товара в корзине")
        assert self.is_element_present(self.PRODUCT), "The product was not added to the cart"
        assert self.is_element_clickable(
            self.PROCEED_TO_CHECKOUT_BUTTON), "The product was not added to the cart"
