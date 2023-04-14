from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def click_on_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_messege(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        name_massege = self.browser.find_element(*ProductPageLocators.NAME_MESSEGE)
        name_massege_text = name_massege.text
        assert product_name_text == name_massege_text, "product names are different"


    def should_be_right_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        price_messege = self.browser.find_element(*ProductPageLocators.PRICE_MESSEGE)
        price_messege_text = price_messege.text
        assert product_price_text == price_messege_text, "product prices are different"