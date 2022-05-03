from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest


class BasePage:
    def __int__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(by=By.CSS_SELECTOR, value="#login_link")
    #     login_link.click()
    #
    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return False
    #     return True
