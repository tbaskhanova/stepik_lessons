from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


class TestMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com"

        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.go_to_basket_page()
        page = BasketPage(browser,browser.current_url)

        # Assert
        page.should_be_empty_basket_msg()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com"

        # Arrange
        page = MainPage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com"

        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_page()