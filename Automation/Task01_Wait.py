import threading
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path="../Automation/chromedriver.exe")
driver.get("https://www.google.com/gmail/about/")

driver.maximize_window()

a = driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]").click()
# u = driver.find_element(By.XPATH, "//div[contains(text(),'Use another account')]").click()


f1 = driver.find_element(By.XPATH, "//input[@id='identifierId']")
f1.send_keys("reshma.s@agaramtech.com")

n1 = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()

time.sleep(10)

# driver.implicitly_wait(30)

password = driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf'][@type='password']")
password.send_keys("reshmareshma")


# try:
#   wait = WebDriverWait(driver, 30).until(ec.presence_of_element_located(password))
#   password.send_keys("reshmareshma")
# except:
#   print("exception occurred")

time.sleep(5)

# driver.implicitly_wait(30)

n2 = driver.find_element(By.XPATH, "//span[@class='VfPpkd-vQzf8d'][@jsname='V67aGc']")

n2.click()

print(driver.title)

time.sleep(10)

driver.close()

a = input("Enter Date with Time:" )
b = datetime.strptime(a, "%d/%m/%Y %H:%M:%S")
print(b)
