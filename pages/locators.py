from selenium.webdriver.common.by import By

class MainPageLocators:
    CONTACT_US = (By.ID, 'contact-link')
    CLOTHES = (By.ID, 'category-3')
    PRODUCT_HUMMINGBIRD_PRINTED_SWEATER = (By.CSS_SELECTOR,
                                           '#content > section:nth-child(2) > div > div:nth-child(2) > article > div > div.thumbnail-top > a')
    ALL_PRODUCTS = (By.CSS_SELECTOR, '#content > section:nth-child(2) > a')
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, 'input.btn.btn-primary.float-xs-right.hidden-xs-down')
    PRICE_FIRST_PRODUCT = (By.CSS_SELECTOR,
                           'section:nth-child(2) > div > div:nth-child(1) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    PRICE_SECOND_PRODUCT = (By.CSS_SELECTOR,
                           'section:nth-child(2) > div > div:nth-child(2) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    PRICE_THIRD_PRODUCT = (By.CSS_SELECTOR,
                           'section:nth-child(2) > div > div:nth-child(3) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    CURRENCY = (By.CSS_SELECTOR, '#_desktop_currency_selector > div > button')
    CURRENCY_USD = (By.CSS_SELECTOR, '#_desktop_currency_selector > div > ul > li:nth-child(2) > a')


class CatalogPageLocators:
    ART = (By.CSS_SELECTOR, '#subcategories > ul > li:nth-child(3) > div.subcategory-image > a')
    HOME = (By.ID, 'js-product-list-header')
    SORT_BY = (By.CSS_SELECTOR, 'div.col-xs-8.col-sm-7.col-md-9.products-sort-order.dropdown > button')
    LIKE_HUMMINGBIRD_PRINTED_SWEATER = (By.CSS_SELECTOR, 'div.products.row > div:nth-child(2) > article > div > button')
    NEXT = (By.CSS_SELECTOR, 'div.col-md-6.offset-md-2.pr-0 > ul > li:nth-child(3) > a')
    PRICE_FIRST_PRODUCT = (By.CSS_SELECTOR,
                           'div.products.row > div:nth-child(1) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    PRICE_SECOND_PRODUCT = (By.CSS_SELECTOR,
                            'div.products.row > div:nth-child(2) > article > div > div.product-description > div.product-price-and-shipping > span.price')
    PRICE_THIRD_PRODUCT = (By.CSS_SELECTOR,
                           'div.products.row > div:nth-child(3) > article > div > div.product-description > div.product-price-and-shipping > span.price')

class ProductPageLocators:
    IMAGE_PRODUCT = (By.CSS_SELECTOR, 'div.images-container.js-images-container > div.product-cover')
    PRICE = (By.CLASS_NAME, 'current-price-value')
    ADD_TO_CART = (By.CLASS_NAME, 'add-to-cart')
    FACEBOOK = (By.CLASS_NAME, 'facebook.icon-gray')
    PRODUCT_DETAILS = (By.CSS_SELECTOR, '.nav-item:nth-child(2)')
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '.cart-content-btn > a')

class LoginAdministrationPageLocators:
    IMAGE = (By.ID, 'shop-img')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    LOG_IN_BUTTON = (By.ID, 'submit_login')
    I_FORGOT_MY_PASSWORD_BUTTON = (By.ID, 'forgot-password-link')

class RegistrationPageLocators:
    FIRST_NAME = (By.ID, 'field-firstname')
    LAST_NAME = (By.ID, 'field-lastname')
    EMAIL = (By.ID, 'field-email')
    PASSWORD = (By.ID, 'field-password')
    BIRTHDATE = (By.ID, 'field-birthday')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'footer > button')

class AdminPanelPageLocators:
    DEMO_MODE = (By.ID, 'page-header-desc-configuration-switch_demo')
    FORECAST = (By.ID, 'dashgoals')
    DASHBOARD = (By.ID, 'dashtrends')
    PRODUCTS_AND_SALES = (By.ID, 'dashproducts')
    USER_BUTTON = (By.ID, 'header_employee_box')
    SIGN_OUT_BUTTON = (By.ID, 'header_logout')

class CartPageLocators:
    PRODUCT = (By.CLASS_NAME, 'product-line-grid')
    PROCEED_TO_CHECKOUT_BUTTON = (By.CLASS_NAME, 'js-cart-detailed-actions')
