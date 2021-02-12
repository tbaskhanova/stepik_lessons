from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

e = math.e


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x))), e))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
browser.find_element_by_tag_name("button").click()
x = browser.find_element_by_id('input_value').text
x = calc(x)
field_for_answer = browser.find_element_by_id("answer")
field_for_answer.send_keys(x)
submit_btn = browser.find_element_by_id("solve")
submit_btn.click()
