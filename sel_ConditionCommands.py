#Used for webtools like text fields, radio buttons, buttons, checkbox etc.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get('http://testhtml5.vulnweb.com/')
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/p[2]/a").click() #trying to find the register page

user_ele = driver.find_element_by_id("username")
pwd_ele = driver.find_element_by_id("password")

print(user_ele.is_displayed()) #if displayed retuns true
print(user_ele.is_enabled()) # if enable returns true

user_ele.send_keys("Emily")
pwd_ele.send_keys("Blunt")

driver.find_element_by_xpath("//*[@id='loginFormSubmit']").click()

time.sleep(10)

#To check the Radio buttons and checkbox

driver.get("https://www.mercurytravels.co.in/flights")
driver.find_element_by_xpath("//*[@id='modalPopup']/div/div/div[1]/button/span").click()
time.sleep(3)