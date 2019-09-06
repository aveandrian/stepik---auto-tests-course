from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

  
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
		
    num1El = browser.find_element_by_id("num1")
    num1 = num1El.text
	
    num2El = browser.find_element_by_id("num2")
    num2 = num2El.text
    res = int(num1)+int(num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(res)) # ищем элемент с текстом num1+num2
	
	
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