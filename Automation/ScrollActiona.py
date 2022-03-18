import time
from selenium.webdriver.common.by import By
import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="../Automation/chromedriver.exe")

url = driver.get("https://www.ajio.com/")

driver.maximize_window()

#scrolldown to end of the page
scrolldownend = driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)

#scrollup the page by pixel
# scrolldownpixel = driver.execute_script("window.scrollBy(0,-7000)")

#Horizontalscroll to end of the page
# driver.execute_script("window.scrollBy(document.body.scrollHeight,0)")

#scrollup the page by Keys
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.HOME)

# or scroll till element found
element = driver.find_element(By.ID, "10_Coupe")
driver.execute_script("arguments[0].scrollIntoView();", element)








