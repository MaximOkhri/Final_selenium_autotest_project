from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    NAME_MESSEGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE_MESSEGE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
