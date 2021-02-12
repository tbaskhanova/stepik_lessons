from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
name = browser.find_element_by_name('firstname')
name.send_keys('test')
last_name = browser.find_element_by_name('lastname')
last_name.send_keys('test')
email = browser.find_element_by_name('email')
email.send_keys('test@gmail.com')
file_field = browser.find_element_by_id('file')
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
file_field.send_keys(file_path)
submit_btn = browser.find_element_by_tag_name("button")
submit_btn.click()