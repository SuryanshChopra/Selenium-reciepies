from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

driver.maximize_window() # maximize the browser window


driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Users/hp/Desktop/date.txt")

time.sleep(5)

driver.find_element_by_xpath("//*[@id='FSsubmit']").click()



