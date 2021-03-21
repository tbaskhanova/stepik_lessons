from .base_page import BasePage
from .locators import MainPageLocators,ProductPageLocators


class MainPage(BasePage):
    def go_to_next_page_in_catalogue(self):
        self.browser.find_element(*MainPageLocators.NEXT_PAGE_BTN).click()

    def go_to_previous_page_in_catalogue(self):
        self.browser.find_element(*MainPageLocators.PREVIOUS_PAGE_BTN).click()

    def go_to_review_form(self):
        self.browser.find_element(*MainPageLocators.PRODUCT_NAME).click()
        self.browser.find_element(*ProductPageLocators.REVIEW_LINK).click()

    def should_be_found_product(self,product_name,product_price):
        found_product_name = self.browser.find_element(*MainPageLocators.FOUND_PRODUCT_NAME).text
        found_product_price = self.browser.find_element(*MainPageLocators.FOUND_PRODUCT_PRICE).text
        assert product_name == found_product_name,'The product name is not correct!'
        assert product_price == found_product_price, 'The product price is not correct!'

    def should_not_be_unsuccess_msg(self):
        msg = 'Found 0 results'
        self.is_element_present(*MainPageLocators.UNSUCCESS_MSG_LOC), "Message is not presented"
        unsuccess_msg = self.browser.find_element(*MainPageLocators.UNSUCCESS_MSG_LOC).text
        assert not msg in unsuccess_msg, 'The message is not correct!'

    def should_be_unsuccess_msg(self):
        msg = 'Found 0 results'
        self.is_element_present(*MainPageLocators.UNSUCCESS_MSG_LOC), "Message is not presented"
        unsuccess_msg = self.browser.find_element(*MainPageLocators.UNSUCCESS_MSG_LOC).text
        assert msg in unsuccess_msg, 'The message is not correct!'

    def should_be_correct_number_of_page(self,page_number):
        cur_page = self.browser.find_element(*MainPageLocators.CURRENT_PAGE).text
        assert page_number in cur_page, 'The page is not correct!'
