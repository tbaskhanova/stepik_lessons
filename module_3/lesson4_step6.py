from selenium import webdriver
import math
from math import e


def calc(x):
    return str(math.log(abs(12*math.sin(int(x))), e))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_id('input_value').text
x = calc(x)
field_for_answer = browser.find_element_by_id("answer")
field_for_answer.send_keys(x)
checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()
radiobutton = browser.find_element_by_id('robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()
submit_btn = browser.find_element_by_tag_name("button")
submit_btn.click()