from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)

"""
# To click OK on alert/Popup
driver.switch_to_alert().accept()

"""

# To click Cancel on alert/Popup
driver.switch_to_alert().dismiss()

