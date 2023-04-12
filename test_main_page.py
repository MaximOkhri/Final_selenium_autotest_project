from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser: WebDriver):

    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser: WebDriver):
    
    browser.get(link)
    go_to_login_page(browser)
