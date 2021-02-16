from selenium import webdriver
from faker import Faker


link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
email_reg_locator = '#id_registration-email'
password_reg_locator = '#id_registration-password1'
confirm_password_locator = '#id_registration-password2'
registration_btn_locator = 'registration_submit'
msg_locator = 'div.alertinner.wicon'
email_login_locator = '#id_login-username'
password_login_locator = '#id_login-password'
login_btn = 'login_submit'


def test_registration_user():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    search_text = 'Спасибо за регистрацию!'

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    try:
        browser.get(link)
        field_for_email = browser.find_element_by_css_selector(email_reg_locator)
        field_for_email.clear()
        field_for_email.send_keys(email)
        field_for_password = browser.find_element_by_css_selector(password_reg_locator)
        field_for_password.clear()
        field_for_password.send_keys(password)
        field_for_confirm_password = browser.find_element_by_css_selector(confirm_password_locator)
        field_for_confirm_password.clear()
        field_for_confirm_password.send_keys(password)
        browser.find_element_by_name(registration_btn_locator).click()

        success_registration_msg = browser.find_element_by_css_selector(msg_locator).text
        assert success_registration_msg == search_text, \
            "Should be message after successful registration"
        browser.save_screenshot("screenshot_registration.png")

    finally:
        browser.quit()


def test_login_user():
    email = 'douglas75@yahoo.com'
    password = 'fhN1JP5r(x'
    search_text = 'Рады видеть вас снова'

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    try:
        browser.get(link)
        field_for_email = browser.find_element_by_css_selector(email_login_locator)
        field_for_email.clear()
        field_for_email.send_keys(email)
        field_for_password = browser.find_element_by_css_selector(password_login_locator)
        field_for_password.clear()
        field_for_password.send_keys(password)
        browser.find_element_by_name(login_btn).click()

        success_login_msg = browser.find_element_by_css_selector(msg_locator).text
        assert success_login_msg == search_text, \
            "Should be message after successful login"
        browser.save_screenshot("screenshot_login.png")

    finally:
        browser.quit()


test_registration_user()
test_login_user()