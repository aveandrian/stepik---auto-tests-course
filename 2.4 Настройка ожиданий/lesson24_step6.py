from selenium import webdriver

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/cats.html")
	browser.find_element_by_id("button") 

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()