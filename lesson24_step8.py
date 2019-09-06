from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
	
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    x_value_el = browser.find_element_by_id("input_value")
    x_value = x_value_el.text
    y = calc(x_value)
	
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()