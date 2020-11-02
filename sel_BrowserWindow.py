from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

"""
# To handle current window
driver.current_window_handle # returns the parent window

"""

# To handle all browser windows

handles = driver.window_handles # return all the handles of opened browser windows

for handle in handles:
    driver.switch_to.window(handle) # Switch to that browser window for which handle value is provided
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()






