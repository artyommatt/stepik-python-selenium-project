from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_login_page(self) -> None:
        login_link = self.browser.find_element(by=By.CSS_SELECTOR, value="#login_link_invalid")
        login_link.click()
