from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
link2 = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()
browser.get(link2)
num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text
sum = str(int(num1) + int(num2))
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(sum)
submit_btn = browser.find_element_by_css_selector('button.btn.btn-default')
submit_btn.click()
browser.quit()

