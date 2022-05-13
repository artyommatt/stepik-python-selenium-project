from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def parse_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADD_TO_BASKET).text
        return product_name

    def parse_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADD_TO_BASKET).text
        return product_price

    def should_the_equal_product_name(self):
        product_name = self.parse_product_name()
        product_name_in_success_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert product_name == product_name_in_success_message, 'Product name is invalid in success message'

    def should_the_equal_product_price(self):
        product_price = self.parse_product_price()
        product_price_in_info_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_INFO_MESSAGE).text
        print('1', product_price)
        print('2', product_price_in_info_message)
        assert product_price == product_price_in_info_message, 'Product price is invalid in info message'
