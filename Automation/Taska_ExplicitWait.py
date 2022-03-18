from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path="../Automation/chromedriver.exe")
driver.get("https://www.google.com/gmail/about/")

driver.maximize_window()

a = driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]").click()

f1 = driver.find_element(By.XPATH, "//input[@id='identifierId']")
f1.send_keys("reshma.s@agaramtech.com")

n1 = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()

password = driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf'][@type='password']")

print(password.isenabled())

wait = WebDriverWait(driver, 30).until(ec.presence_of_element_located(password))
password.send_keys("reshmareshma")



n2 = driver.find_element(By.XPATH, "//span[@class='VfPpkd-vQzf8d'][@jsname='V67aGc']")
n2.click()

print(driver.title)

