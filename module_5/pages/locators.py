from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    ADD_TO_BASKET_MINI_BTN = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators():
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR,'div#content_inner > p')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_REG_LOCATOR = (By.CSS_SELECTOR,'#id_registration-email')
    PASSWORD_REG_LOCATOR = (By.CSS_SELECTOR,'#id_registration-password1')
    CONFIRM_PASSWORD_LOCATOR = (By.CSS_SELECTOR,'#id_registration-password2')
    REGISTRATION_BTN = (By.NAME,'registration_submit')


class MainPageLocators():
    pass


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR,'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    ADD_TO_BASKET_MSG = (By.CSS_SELECTOR, 'div.alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')


