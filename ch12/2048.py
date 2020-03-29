#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open webpage
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

#get elements
htmlElem = browser.find_element_by_tag_name('html')
retryElem = browser.find_element_by_class_name('retry-button')

#key loop
while True:
	if retryElem.is_displayed():
		print('Press enter to go again. Ctrl + c to exit')
		input()
		retryElem.click()
		
	else:
		htmlElem.send_keys(Keys.UP)
		htmlElem.send_keys(Keys.RIGHT)
		htmlElem.send_keys(Keys.DOWN)
		htmlElem.send_keys(Keys.LEFT)

