from selenium import webdriver
from sys import argv

script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector('div.first_block input.form-control.first')
    first_name.send_keys('test')
    last_name = browser.find_element_by_css_selector('div.first_block input.form-control.second')
    last_name.send_keys('test')
    email = browser.find_element_by_css_selector('input.form-control.third')
    email.send_keys('test@test.ru')
    phone = browser.find_element_by_css_selector('div.second_block input.form-control.first')
    phone.send_keys('12345678900')
    address = browser.find_element_by_css_selector('div.second_block input.form-control.second')
    address.send_keys('test')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций
    browser.quit()