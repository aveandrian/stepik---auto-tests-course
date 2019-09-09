from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
	def test_1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_css_selector(".first_block input.first")
		input1.send_keys("A")
		input2 = browser.find_element_by_css_selector(".first_block input.second")
		input2.send_keys("B")
		input3 = browser.find_element_by_css_selector(".first_block input.third")
		input3.send_keys("C")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "First test failed")
		
	def test_2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_css_selector(".first_block input.first")
		input1.send_keys("A")
		input2 = browser.find_element_by_css_selector(".first_block input.second")
		input2.send_keys("B")
		input3 = browser.find_element_by_css_selector(".first_block input.third")
		input3.send_keys("C")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Second test failed")

if __name__ == "__main__":
    unittest.main()