from selenium import webdriver
from sys import argv
import unittest

# script_name, link = argv
link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'


class TestRegistration1(unittest.TestCase):
    def test_registration1(self):
        browser = webdriver.Chrome()
        browser.get(link1)

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
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be message")
        # assert "Congratulations! You have successfully registered!" == welcome_text

    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get(link2)

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
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be message")
        # assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    unittest.main()