from pages.base_page import BasePage
from pages.locators import AdminCatalogProductsPageLocators
from selenium.webdriver.common.by import By
class AdminCatalogProductsPage(BasePage):

    def add_new_product(self) -> None:
        if self.is_element_clickable(AdminCatalogProductsPageLocators.CLOSE_BUTTON):
            self.click_on_element(AdminCatalogProductsPageLocators.CLOSE_BUTTON)
        self.click_on_element(AdminCatalogProductsPageLocators.NEW_PRODUCT_BUTTON)
        self.browser.switch_to.frame(0)
        self.click_on_element(AdminCatalogProductsPageLocators.ADD_NEW_PRODUCT_BUTTON)
        self.browser.switch_to.default_content()
        self.fill_in_text_field(AdminCatalogProductsPageLocators.SUMMARY_FIELD, "Test Summary")
        self.fill_in_text_field(AdminCatalogProductsPageLocators.DESCRIPTION_FIELD, "Test Description")
        self.click_on_element(AdminCatalogProductsPageLocators.DETAILS_TAB)
        self.fill_in_text_field(AdminCatalogProductsPageLocators.REFERENCE_FIELD, "Test Reference")
        self.click_on_element(AdminCatalogProductsPageLocators.PRICING_TAB)
        self.fill_in_text_field_which_are_introduced_from_end(AdminCatalogProductsPageLocators.RETAIL_PRICE_FIELD, "10")
        self.fill_in_text_field_which_are_introduced_from_end(AdminCatalogProductsPageLocators.COST_PRICE_FIELD, "1")
        self.click_on_element(AdminCatalogProductsPageLocators.SAVE_BUTTON)
        self.click_on_element(AdminCatalogProductsPageLocators.GO_TO_CATALOG_BUTTON)


    def check_new_product(self) -> None:
        assert self.is_element_present((By.XPATH,f"//table//td[normalize-space()='Test Reference']")), f"No new product was added."

    def delete_product(self) -> None:
        self.click_on_element(AdminCatalogProductsPageLocators.DROP_DOWN_LIST)
        self.click_on_element(AdminCatalogProductsPageLocators.DELETE_BUTTON)
        self.click_on_element(AdminCatalogProductsPageLocators.DELETE_2_BUTTON)

    def check_delete_product(self) -> None:
        assert self.is_not_element_present((By.XPATH,f"//table//td[normalize-space()='Test Reference']")), f"No new product was added."
