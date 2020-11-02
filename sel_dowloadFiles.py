from selenium import webdriver

driver=webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

# How to Download a text file

driver.find_element_by_id("textbox").send_keys("testing download file")
driver.find_element_by_id("createTxt").click() #Generate file button
driver.find_element_by_id("link-to-download").click() #Download link

# The .txt and .pdf has nothing to do with that we can download both file by same code
# How to download pdf file

driver.find_element_by_id("pdfbox").send_keys("testing download file")
driver.find_element_by_id("createPdf").click() #Generate file button
driver.find_element_by_id("pdf-link-to-download").click() #Download link