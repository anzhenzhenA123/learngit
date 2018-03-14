from selenium import webdriver
import time

browser=webdriver.Firefox()
time.sleep(2)

browser.get('http://www.baidu.com')
time.sleep(2)
browser.find_element_by_id('kw').send_keys("git教程")  
time.sleep(2)
browser.find_element_by_id('su').click
time.sleep(2)

browser.close()
