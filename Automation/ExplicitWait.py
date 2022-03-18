from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as kk
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome(executable_path="..\Automation\chromedriver.exe")
driver.maximize_window()
driver.get("https://logilabelntesting.azurewebsites.net/")
org="agaramtech.onmicrosoft.com"
wait=WebDriverWait(driver,10).until(kk.presence_of_element_located((By.XPATH,"//input[@name='Username']")))
wait.send_keys(org)
#driver.find_element_by_xpath("//input[@name='Username']").send_keys(org)
driver.find_element(By.XPATH,"//*[@id='inputText']").click()

