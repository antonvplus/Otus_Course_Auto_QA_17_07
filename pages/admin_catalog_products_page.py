from pages.base_page import BasePage
from selenium.webdriver.common.by import By

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

    def add_new_product(self) -> None:
        if self.is_element_clickable(self.CLOSE_BUTTON):
            self.click_on_element(self.CLOSE_BUTTON)
        self.click_on_element(self.NEW_PRODUCT_BUTTON)
        self.browser.switch_to.frame(0)
        self.click_on_element(self.ADD_NEW_PRODUCT_BUTTON)
        self.browser.switch_to.default_content()
        self.fill_in_text_field(self.SUMMARY_FIELD, "Test Summary")
        self.fill_in_text_field(self.DESCRIPTION_FIELD, "Test Description")
        self.click_on_element(self.DETAILS_TAB)
        self.fill_in_text_field(self.REFERENCE_FIELD, "Test Reference")
        self.click_on_element(self.PRICING_TAB)
        self.fill_in_text_field_which_are_introduced_from_end(self.RETAIL_PRICE_FIELD, "10")
        self.fill_in_text_field_which_are_introduced_from_end(self.COST_PRICE_FIELD, "1")
        self.click_on_element(self.SAVE_BUTTON)
        self.click_on_element(self.GO_TO_CATALOG_BUTTON)


    def check_new_product(self) -> None:
        assert self.is_element_present((By.XPATH,f"//table//td[normalize-space()='Test Reference']")), f"No new product was added."

    def delete_product(self) -> None:
        self.click_on_element(self.DROP_DOWN_LIST)
        self.click_on_element(self.DELETE_BUTTON)
        self.click_on_element(self.DELETE_2_BUTTON)

    def check_delete_product(self) -> None:
        assert self.is_not_element_present((By.XPATH,f"//table//td[normalize-space()='Test Reference']")), f"No new product was added."
