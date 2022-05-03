from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        login_link = self.browser.find_element(by=By.CSS_SELECTOR, value="#login_link")
        login_link.click()
