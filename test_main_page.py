from selenium.webdriver.common.by import By


link: str = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser) -> None:
    login_link = browser.find_element(by=By.CSS_SELECTOR, value="#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser) -> None:
    browser.get(link)
    go_to_login_page(browser)
