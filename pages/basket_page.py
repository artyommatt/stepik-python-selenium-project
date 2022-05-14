from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty'

    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert 'Your basket is empty' in empty_basket_message, 'Empty basket message is invalid'
