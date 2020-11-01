#How to go back and then forward to same page on a single tab

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get('http://reqzone.com') #1st site
print(driver.title)
time.sleep(5)

driver.get('http://google.com') #2nd site
print(driver.title)
time.sleep(5)

driver.back() # go back to 1st site
print(driver.title)
time.sleep(5)

driver.forward()
print(driver.title)
time.sleep(5)

driver.close()