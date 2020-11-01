from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')


#To insert in Text fields or Text Areas

driver.find_element_by_name("RESULT_TextField-1").send_keys("Emily")
driver.find_element_by_name("RESULT_TextField-2").send_keys("Blunt")
driver.find_element_by_name("RESULT_TextField-3").send_keys("9888652541")
driver.find_element_by_name("RESULT_TextField-4").send_keys("Germany")
driver.find_element_by_name("RESULT_TextField-5").send_keys("Kolechia")
driver.find_element_by_name("RESULT_TextField-6").send_keys("hitler4lyf@gmail.com")


#To insert in radio buttons and check boxes


button = driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-7_0']")
driver.execute_script("arguments[0].click();", button)


button = driver.find_element_by_xpath("//*[@id='RESULT_CheckBox-8_1']")
driver.execute_script("arguments[0].click();", button)

button = driver.find_element_by_xpath("//*[@id='RESULT_CheckBox-8_2']")
driver.execute_script("arguments[0].click();", button)

button = driver.find_element_by_xpath("//*[@id='RESULT_CheckBox-8_3']")
driver.execute_script("arguments[0].click();", button)

button = driver.find_element_by_xpath("//*[@id='RESULT_CheckBox-8_4']")
driver.execute_script("arguments[0].click();", button)

button = driver.find_element_by_xpath("//*[@id='RESULT_CheckBox-8_5']")
driver.execute_script("arguments[0].click();", button)


"""
This was the original code for Radio buttons and check boxes. However it always throw an exception i.e. why i have to go for a different approach

driver.find_element_by_id("RESULT_CheckBox-8_1").click()
driver.find_element_by_id("RESULT_CheckBox-8_2").click()
driver.find_element_by_id("RESULT_CheckBox-8_3").click()
driver.find_element_by_id("RESULT_CheckBox-8_4").click()
driver.find_element_by_id("RESULT_CheckBox-8_5").click()
"""


#To insert value in drop down menu

element = driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-9']")
drp=Select(element)

drp.select_by_index(1)

#To count no. of options in a dropdown

print(len(drp.options))

# To capture all the options and print in my console

all_options = drp.options

for option in all_options:
    print(option.text)


