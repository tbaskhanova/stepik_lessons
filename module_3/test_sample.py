from selenium import webdriver
from faker import Faker


link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
email_locator = '#id_registration-email'
password_locator = '#id_registration-password1'
confirm_password_locator = '#id_registration-password2'
registration_btn_locator = 'registration_submit'
success_registration_msg_locator = 'div.alertinner.wicon'


def test_registration_user():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    search_text = 'Спасибо за регистрацию!'

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    try:
        browser.get(link)
        field_for_email = browser.find_element_by_css_selector(email_locator)
        field_for_email.clear()
        field_for_email.send_keys(email)
        field_for_password = browser.find_element_by_css_selector(password_locator)
        field_for_password.clear()
        field_for_password.send_keys(password)
        field_for_confirm_password = browser.find_element_by_css_selector(confirm_password_locator)
        field_for_confirm_password.clear()
        field_for_confirm_password.send_keys(password)
        browser.find_element_by_name(registration_btn_locator).click()

        success_registration_msg = browser.find_element_by_css_selector(success_registration_msg_locator).text
        assert success_registration_msg == search_text, \
            "Should be message after successful registration"

    finally:
        browser.quit()


test_registration_user()