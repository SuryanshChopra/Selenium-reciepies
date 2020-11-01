from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get('http://google.com/')

search_field = driver.find_element_by_name("q") 
search_field.send_keys("Deadpool")
search_field.submit() # To hit enter keyz