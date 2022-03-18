import time
import threading
import allure
import pytest
from selenium import webdriver
from datetime import datetime

from test_Task04_MultiThreading import Testa

masters = "//a[@id='iMenuID_1']"
link = "http://localhost:8080/QuaLISWeb/index.html"

un="it"
pswd="123"
class Testabc():
    # In pytest data can't be passed at runtym
    # fixture represents a before method, scope = class it means this has to be run only once
    @pytest.fixture(scope="class")
    def test_parent(self):
        global kk
        global inputtime
        # inputtime = input("Enter the date & time: ")
        driver = webdriver.Chrome(executable_path="C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\chromedriver.exe")
        kk = Testa(driver)
# Parameterisation
    @pytest.mark.parametrize("var1,var2",[(un,pswd),(un,pswd)])
    def test_child(self, test_parent, var1, var2):
        inputtime = "07-03-2022 13:36:30"

        i=1
        while i > 0:
            systime = datetime.today()
            print(systime)
            timeconversion = systime.strftime("%d-%m-%Y %H:%M:%S")
            print(inputtime)
            print(timeconversion)
            if inputtime == timeconversion:
                kk.test_login(link, var1, var2)
                time.sleep(4)
                kk.test_xpathclick(masters)
                time.sleep(10)
                break

# For Parallel run, slave can be used. pytest -m markername -n marker count to run depends on parameter arguments











