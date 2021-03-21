from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_review_fields(self):
        assert 'Title' in self.browser.find_element(*ProductPageLocators.REVIEW_TITLE_FIELD).text
        assert 'Score' in self.browser.find_element(*ProductPageLocators.REVIEW_SCORE_FIELD).text
        assert 'Name' in self.browser.find_element(*ProductPageLocators.REVIEW_NAME_FIELD).text
        assert 'Body' in self.browser.find_element(*ProductPageLocators.REVIEW_BODY_FIELD).text
        assert 'Email' in self.browser.find_element(*ProductPageLocators.REVIEW_EMAIL_FIELD).text


