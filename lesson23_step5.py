from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
	
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    time.sleep(1)
    new_window = browser.window_handles[1]
	
    browser.switch_to.window(new_window)

    x_value_el = browser.find_element_by_id("input_value")
    x_value = x_value_el.text
    y = calc(x_value)
	
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()