from selenium import webdriver

driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.maximize_window()

#Open 2 tabs
driver.get("https://crontab.guru/")
driver.execute_script("window.open('http://10.10.10.4:8889/secure/Dashboard.jspa')")

#take handle
handles = driver.window_handles
handle = handles[1]
print(handle)

#switch window
driver.switch_to.window(handle)
print(driver.title)