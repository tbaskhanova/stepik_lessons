from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from faker import Faker


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                            pytest.param("offer7", marks=pytest.mark.xfail), "offer8","offer9"])
    def test_guest_can_add_product_to_basket(self,browser,promo_offer):
        # Data
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_be_successful_msg()

    def test_guest_can_see_success_message_after_adding_product_to_basket(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_to_basket()

        # Assert
        page.should_be_successful_msg()

    @pytest.mark.xfail(reason="negative test")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_to_basket()

        # Assert
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="negative test")
    def test_message_disappeared_after_adding_product_to_basket(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_to_basket()

        # Assert
        page.should_not_be_disappeared_success_msg()

    def test_guest_should_see_login_link_on_product_page(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

        # Arrange
        page = ProductPage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        page = LoginPage(browser,browser.current_url)

        # Assert
        page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_basket_page()
        page = BasketPage(browser, browser.current_url)

        # Assert
        page.should_be_empty_basket_msg()


class TestUserAddToBasketFromProductPage:
    # Arrange
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        fake = Faker()
        email = fake.email()
        password = fake.password()
        reg_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, reg_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        # Arrange
        page = ProductPage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self,browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_be_successful_msg()