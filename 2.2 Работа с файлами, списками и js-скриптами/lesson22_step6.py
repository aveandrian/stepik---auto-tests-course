from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	link = "http://SunInJuly.github.io/execute_script.html"
	browser.get(link)
	
	x_value_el = browser.find_element_by_id("input_value")
	x_value = x_value_el.text
	y = calc(x_value)
	
	text_field = browser.find_element_by_id("answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)
	text_field.send_keys(y)
	
	robot_check = browser.find_element_by_id("robotCheckbox")
	browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check)
	robot_check.click()
	
	robot_radio = browser.find_element_by_id("robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
	robot_radio.click()
	
	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
	assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()