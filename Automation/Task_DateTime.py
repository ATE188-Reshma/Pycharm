from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from _datetime import datetime

driver = webdriver.Chrome(executable_path="../Automation/chromedriver.exe")
driver.get("http://localhost:8080/QuaLISWeb/")

driver.maximize_window()

login = driver.find_element(By.XPATH, "//input[@id='idEmail']")
login.send_keys("IT")

password = driver.find_element(By.XPATH, "//input[@id='idpassword']")
password.send_keys("123")

wait = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//input[@id='idLogin']")))
wait.click()

print(driver.title)

a = input()
b = datetime.strptime(a, "%d/%m/%Y %H:%M:%S")
print(b)
