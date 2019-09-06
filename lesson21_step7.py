from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
		
    input1 = browser.find_element_by_id("treasure")
    value_x = input1.get_attribute("valuex")
    y = calc(value_x)
	
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
	
    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()
	
    input3 = browser.find_element_by_css_selector("[value='robots']")
    input3.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()