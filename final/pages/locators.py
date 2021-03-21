from selenium.webdriver.common.by import By


class BasePageLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, '#id_q')
    SEARCH_BTN = (By.CSS_SELECTOR, ' div.navbar-collapse.primary-collapse.collapse > form > input')
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
    PRODUCT_NAME = (By.CSS_SELECTOR, 'li:nth-child(1) h3 a')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'li:nth-child(1) p.price_color')
    FOUND_PRODUCT_NAME = (By.CSS_SELECTOR, ' li h3 a')
    FOUND_PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_price p.price_color')
    UNSUCCESS_MSG_LOC = (By.CLASS_NAME, 'form-horizontal')
    NEXT_PAGE_BTN = (By.CSS_SELECTOR, 'li.next > a')
    PREVIOUS_PAGE_BTN = (By.CSS_SELECTOR, 'li.previous > a')
    CURRENT_PAGE = (By.CSS_SELECTOR,'li.current')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR,'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    ADD_TO_BASKET_MSG = (By.CSS_SELECTOR, 'div.alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    REVIEW_LINK = (By.CSS_SELECTOR, 'section > p > a')
    REVIEW_TITLE_FIELD = (By.CSS_SELECTOR, 'div:nth-child(3) > label')
    REVIEW_SCORE_FIELD = (By.CSS_SELECTOR, 'div:nth-child(4) > label')
    REVIEW_BODY_FIELD = (By.CSS_SELECTOR, 'div:nth-child(5) > label')
    REVIEW_NAME_FIELD = (By.CSS_SELECTOR, 'div:nth-child(6) > label')
    REVIEW_EMAIL_FIELD = (By.CSS_SELECTOR, 'div:nth-child(7) > label')



