from selenium import webdriver
import time
import os 

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
	
    elements = browser.find_elements_by_class_name('form-control')
    for element in elements:
        element.send_keys('A')
	
    send_file_el = browser.find_element_by_css_selector("[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    print(file_path)
    send_file_el.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()