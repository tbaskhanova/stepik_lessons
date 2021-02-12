from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
x = x_element.text
y = calc(x)
field_for_answer = browser.find_element_by_css_selector('input#answer.form-control')
field_for_answer.send_keys(y)
checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
checkbox.click()
radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
radiobutton.click()
submit_btn = browser.find_element_by_css_selector('button.btn.btn-default')
submit_btn.click()
browser.quit()