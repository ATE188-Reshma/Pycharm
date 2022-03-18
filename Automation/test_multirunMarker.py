import time
import pytest
from selenium import webdriver

# For multithreading mthd shouldn't b before method
#  If wanna run multiple methods of various classes in same name marker has to be used
@pytest.mark.login
def test_login():
    driver=webdriver.Chrome(executable_path="C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")
    driver.find_element_by_xpath("//*[@id='spassword']").send_keys("123")
    time.sleep(4)
    driver.find_element_by_xpath("//*[text()='Login']").click()
@pytest.mark.login
def test_login2():
    driver=webdriver.Chrome(executable_path="C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")
    driver.find_element_by_xpath("//*[@id='spassword']").send_keys("123")
    time.sleep(4)
    driver.find_element_by_xpath("//*[text()='Login']").click()

    # Action performed for each marker