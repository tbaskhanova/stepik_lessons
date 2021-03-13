from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket.click()
        assert True

    def should_be_successful_msg(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MSG), "Message is not presented"
        assert 'has been added to your basket' in self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MSG).text
        assert product_name.text in self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MSG).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MSG), \
            'Message is presented'

    def should_not_be_disappeared_success_msg(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_MSG), \
            'Message is disappeared'


