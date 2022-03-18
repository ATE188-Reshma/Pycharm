from configparser import ConfigParser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Automation import Task08_Log

locator = ConfigParser()

file = locator.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\Task08_LocatorFile.ini")

driver = webdriver.Chrome(executable_path=locator.get("launch browser", "browser"))

driver.get(locator.get("browser link", "link"))

loginid = driver.find_element(By.XPATH, locator.get("credentials locator", "id"))
loginid.click()
loginid.send_keys(locator.get("credentials Values", "id"))


psswd = driver.find_element(By.XPATH, locator.get("credentials locator", "psswd"))
psswd.click()
psswd.send_keys(locator.get("credentials Values", "psswd"))

time.sleep(5)
loginxpath=locator.get("credentials locator", "loginbttn")

try:
    loginbttn = driver.find_element(By.XPATH, loginxpath)
    loginbttn.click()
    Task08_Log.log1("Logged in")


except Exception as r:
    print(r)
    Task08_Log.errorlog(r)

