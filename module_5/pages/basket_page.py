from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_msg(self):
        msg = 'Your basket is empty'
        assert msg in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG).text
