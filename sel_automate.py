from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
driver.get('http://demo.automationtesting.in/Windows.html') 

print(driver.title) # rteurns the title of page
print(driver.current_url) # returns the url of the page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

driver.close() # It will close only currently focused browser


"""
driver.quit() #It will close all open browser
"""