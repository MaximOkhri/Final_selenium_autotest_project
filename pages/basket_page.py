from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    
    def should_not_be_item(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "item in basket"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"