from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_ADD_TO_BASKET = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE_ADD_TO_BASKET = (By.CSS_SELECTOR, 'tr:nth-child(3) > td')
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success strong')
    PRODUCT_PRICE_IN_INFO_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
