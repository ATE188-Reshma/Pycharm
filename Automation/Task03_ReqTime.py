from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

inputtime = input("Enter Date & Time: ")

driver = webdriver.Chrome(executable_path="../Automation/chromedriver.exe")
driver.get("http://localhost:8080/QuaLISWeb/")

driver.maximize_window()

login = driver.find_element(By.XPATH, "//input[@id='idEmail']")
login.send_keys("IT")

password = driver.find_element(By.XPATH, "//input[@id='idpassword']")
password.send_keys("123")

icon = driver.find_element(By.XPATH, "//input[@id='idLogin']")
icon.click()

driver.implicitly_wait(20)

master = driver.find_element(By.ID, "MainMenu_1")
master.click()
basemaster = driver.find_element(By.XPATH, "//a[@id='iModuleID_1']")
basemaster.click()

i = 1
while i > 0:
    sysdatetime = datetime.today() #collect today time
    print(sysdatetime)
    dateconversion = sysdatetime.strftime("%d/%m/%Y %H:%M:%S") #changing d collected time to req format
    print(inputtime)
    print(dateconversion)

    if inputtime == dateconversion:
        unitsofmeasurement = driver.find_element(By.XPATH, "//a[@id='iFormID_33']")
        unitsofmeasurement.click()
        break

print(driver.title)








