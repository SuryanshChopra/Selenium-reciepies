from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get('http://www.stealmylogin.com/demo.html')

driver.implicitly_wait(3) # To implicitly wait

assert "StealMyLogin.com Demo" in driver.title # To confirm the title

driver.find_element_by_name("username").send_keys("Emily")
driver.find_element_by_name("password").send_keys("Blunt")

driver.find_element_by_xpath("/html/body/form/input[3]").click()


