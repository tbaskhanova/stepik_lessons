from selenium import webdriver
import math

e = math.e


def calc(x):
    return str(math.log(abs(12*math.sin(int(x))), e))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_tag_name("button")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = browser.find_element_by_id('input_value').text
x = calc(x)
field_for_answer = browser.find_element_by_id("answer")
field_for_answer.send_keys(x)
submit_btn = browser.find_element_by_tag_name("button")
submit_btn.click()