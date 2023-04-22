from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def click_on_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_messege(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        name_massage = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        name_massage_text = name_massage.text
        assert product_name_text == name_massage_text, "product names are different"

    def should_be_right_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)
        price_message_text = price_message.text
        assert product_price_text == price_message_text, "product prices are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"