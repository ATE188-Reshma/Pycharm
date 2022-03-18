import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Automation/chromedriver.exe")
driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")

loginid = driver.find_element(By.XPATH, "//input[@id='sloginid']")
loginid.click()
loginid.send_keys("cdolman")

time.sleep(4)

psswd = driver.find_element(By.XPATH, "//input[@id='spassword']")
psswd.click()
psswd.send_keys("123")

time.sleep(5)

loginbttn = driver.find_element(By.XPATH, "//*[text()='Login']")
loginbttn.click()

time.sleep(10)

registration = driver.find_element(By.XPATH, "(//span[@class='sc-iJuUWI fTbwUB'])[2]")
registration.click()

time.sleep(5)

sampleregistration = driver.find_element(By.XPATH, "//a[text()='Sample Registration']")
sampleregistration.click()

time.sleep(4)

preregister = driver.find_element(By.XPATH, "(//*[name()='svg']//*[name()='path' and @d='M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z'])[1]")
preregister.click()

time.sleep(4)

prdctctgry = driver.find_element(By.XPATH, "(//div[@class='react-select__control css-yk16xz-control'])[2]")
time.sleep(3)
prdctctgry.click()

time.sleep(6)

dd = driver.find_elements(By.XPATH, ("//div[@class='react-select__menu-list css-11unzgr']/div"))

# for i in dd:
#     if i.text=='Coagulation Factors':
#         i.click()

aa = driver.find_element(By.XPATH, "//*[text()='Therapeutics']")

bb=aa.location_once_scrolled_into_view()
time.sleep(4)
print(bb)
time.sleep(4)
aa.click()

