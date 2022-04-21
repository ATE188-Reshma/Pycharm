import csv
import time
import pytest
from selenium import webdriver

def input_data():
    csvDataFile = open('data.csv')
    csvReader = csv.reader(csvDataFile)
    kk = [i for i in csvReader]
    return kk

@pytest.mark.parametrize("var1,var2", input_data())
def test_eval1(var1, var2):
    driver = webdriver.Chrome(executable_path="..\Automation\chromedriver.exe")
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@name='sloginid']").send_keys(var1)
    time.sleep(4)
    driver.find_element_by_xpath("//*[@name='spassword']").send_keys(var2)
    time.sleep(4)
    driver.find_element_by_xpath("//*[text()='Login']").click()