from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
treasure_img = browser.find_element_by_id('treasure')
x = treasure_img.get_attribute('valuex')
y = calc(x)
field_for_answer = browser.find_element_by_id('answer')
field_for_answer.send_keys(y)
checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()
radiobutton = browser.find_element_by_id('robotsRule')
radiobutton.click()
submit_btn = browser.find_element_by_css_selector('button.btn.btn-default')
submit_btn.click()
browser.quit()