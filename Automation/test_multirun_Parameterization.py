import time
import pytest
from selenium import webdriver

browserpath="C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\chromedriver.exe"
link="http://192.168.0.199:9091/QuaLISWeb/#/login"
# Parameterization browser action performs four times
@pytest.mark.parametrize("var1,var2",[(browserpath,link),(browserpath,link),(browserpath,link),(browserpath,link)])
def test_login(var1,var2):
    driver=webdriver.Chrome(executable_path=var1)
    driver.maximize_window()
    driver.get(var2)
    time.sleep(4)
    driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")
    driver.find_element_by_xpath("//*[@id='spassword']").send_keys("123")
    time.sleep(4)
    driver.find_element_by_xpath("//*[text()='Login']").click()
    time.sleep(4)
