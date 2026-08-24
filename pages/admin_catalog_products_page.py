from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
import allure

class AdminCatalogProductsPage(BasePage):

    NEW_PRODUCT_BUTTON = (By.ID, "page-header-desc-configuration-add")
    ADD_NEW_PRODUCT_BUTTON = (By.ID, "create_product_create")
    SUMMARY_FIELD = (By.ID, "mceu_20")
    DESCRIPTION_FIELD = (By.ID, "mceu_41")
    DETAILS_TAB = (By.CSS_SELECTOR, "#product_details-tab-nav > a")
    REFERENCE_FIELD = (By.ID, "product_details_references_reference")
    PRICING_TAB = (By.CSS_SELECTOR, "#product_pricing-tab-nav > a")
    RETAIL_PRICE_FIELD = (By.ID, "product_pricing_retail_price_price_tax_excluded")
    COST_PRICE_FIELD = (By.ID, "product_pricing_wholesale_price")
    SAVE_BUTTON = (By.ID, "product_footer_save")
    GO_TO_CATALOG_BUTTON = (By.ID, "product_footer_actions_catalog")
    CLOSE_BUTTON = (By.CSS_SELECTOR, '[title="Close Toolbar"]')
    TEST = (By.CSS_SELECTOR,
            '#create_product > div.product-type-selector.form-group > div.product-type-choices > button.product-type-choice.btn.btn-primary')
    DROP_DOWN_LIST = (By.CSS_SELECTOR,
                      'a.btn.btn-link.dropdown-toggle.dropdown-toggle-dots.dropdown-toggle-split.no-rotate')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'a.btn.tooltip-link.js-submit-row-action.dropdown-item.grid-delete-row-link')
    DELETE_2_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-danger.btn-lg.btn-confirm-submit')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("Logger.AdminCatalogProductsPage")

    def open(self) -> None:
        self.logger.info(f"Открыт браузер: {self.url}")
        super().open()


    def add_new_product(self) -> None:
        with allure.step("Открываем форму для добавления нового товара"):
            if self.is_element_clickable(self.CLOSE_BUTTON):
                self.logger.info("Клик на элемент 'CLOSE_BUTTON'")
                self.click_on_element(self.CLOSE_BUTTON)
            self.logger.info("Клик на элемент 'NEW_PRODUCT_BUTTON'")
            self.click_on_element(self.NEW_PRODUCT_BUTTON)
            self.browser.switch_to.frame(0)
            self.logger.info("Клик на элемент 'ADD_NEW_PRODUCT_BUTTON'")
            self.click_on_element(self.ADD_NEW_PRODUCT_BUTTON)
            self.browser.switch_to.default_content()
        with allure.step("Заполняем карточку нового товара"):
            self.logger.info("Заполняем поле 'SUMMARY_FIELD'")
            self.fill_in_text_field(self.SUMMARY_FIELD, "Test Summary")
            self.logger.info("Заполняем поле 'DESCRIPTION_FIELD'")
            self.fill_in_text_field(self.DESCRIPTION_FIELD, "Test Description")
            self.logger.info("Клик на элемент 'DETAILS_TAB'")
            self.click_on_element(self.DETAILS_TAB)
            self.logger.info("Заполняем поле 'REFERENCE_FIELD'")
            self.fill_in_text_field(self.REFERENCE_FIELD, "Test Reference")
            self.logger.info("Клик на элемент 'PRICING_TAB'")
            self.click_on_element(self.PRICING_TAB)
            self.logger.info("Заполняем поле 'RETAIL_PRICE_FIELD'")
            self.fill_in_text_field_which_are_introduced_from_end(self.RETAIL_PRICE_FIELD, "10")
            self.logger.info("Заполняем поле 'COST_PRICE_FIELD'")
            self.fill_in_text_field_which_are_introduced_from_end(self.COST_PRICE_FIELD, "1")
        with allure.step("Сохраняем новые продукт"):
            self.logger.info("Клик на элемент 'PRICING_TAB'")
            self.click_on_element(self.SAVE_BUTTON)
            self.logger.info("Клик на элемент 'GO_TO_CATALOG_BUTTON'")
            self.click_on_element(self.GO_TO_CATALOG_BUTTON)

    @allure.step("Выполняем проверку, что новый товар сохранился")
    def check_new_product(self) -> None:
        self.logger.info("Проверка, что новый товар сохранился")
        assert self.is_element_present((By.XPATH, "//table//td[normalize-space()='Test Reference']")), "No new product was added."

    @allure.step("Удаляем товар")
    def delete_product(self) -> None:
        self.click_on_element(self.DROP_DOWN_LIST)
        self.click_on_element(self.DELETE_BUTTON)
        self.click_on_element(self.DELETE_2_BUTTON)
        self.logger.info("Товар удален")

    @allure.step("Выполняем проверку, что товар удалился")
    def check_delete_product(self) -> None:
        self.logger.info("Проверка, что товар удалился")
        assert self.is_not_element_present((By.XPATH, "//table//td[normalize-space()='Test Reference']")), "No new product was added."
