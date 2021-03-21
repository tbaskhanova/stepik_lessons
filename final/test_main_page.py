from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import MainPageLocators
import pytest
from faker import Faker


class TestMainPage:
    @pytest.mark.parametrize('page', ["1", "2"])
    def test_guest_can_go_to_review_form(self, browser, page):
        # Data
        link = f"http://selenium1py.pythonanywhere.com/catalogue/?page={page}"

        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.go_to_review_form()
        page = ProductPage(browser, browser.current_url)

        # Assert
        page.should_be_review_fields()

    def test_guest_can_go_to_previous_page_in_catalogue(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/"

        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.go_to_next_page_in_catalogue()
        cur_page_number = (browser.current_url.split('='))[1]
        page_number = str(int(cur_page_number) - 1)
        page.go_to_previous_page_in_catalogue()

        # Assert
        page.should_be_correct_number_of_page(page_number)

    def test_guest_can_find_available_product(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/"

        # Arrange
        page = MainPage(browser, link)
        page.open()
        product_name = browser.find_element(*MainPageLocators.PRODUCT_NAME).text
        product_price = browser.find_element(*MainPageLocators.PRODUCT_PRICE).text

        # Act
        page.find_product_by_name(product_name)

        # Assert
        page.should_be_found_product(product_name, product_price)
        page.should_not_be_unsuccess_msg()

    @pytest.mark.xfail(reason="negative test")
    def test_guest_cant_find_available_product(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/"

        # Arrange
        page = MainPage(browser, link)
        page.open()
        product_name = browser.find_element(*MainPageLocators.PRODUCT_NAME).text

        # Act
        page.find_product_by_name(product_name)

        # Assert
        page.should_be_unsuccess_msg()


class TestUserFindProduct:
    # Arrange
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake = Faker()
        email = fake.email()
        password = fake.password()
        reg_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, reg_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_find_available_product(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/"

        # Arrange
        page = MainPage(browser, link)
        page.open()
        product_name = browser.find_element(*MainPageLocators.PRODUCT_NAME).text
        product_price = browser.find_element(*MainPageLocators.PRODUCT_PRICE).text

        # Act
        page.find_product_by_name(product_name)

        # Assert
        page.should_be_found_product(product_name, product_price)
        page.should_not_be_unsuccess_msg()
