import time
import threading
import allure
import pytest
from selenium import webdriver
from datetime import datetime

from test_Task04_MultiThreading import Testa

masters = "//a[@id='iMenuID_1']"
link = "http://localhost:8080/QuaLISWeb/index.html"


class Testabc():
    # In pytest data can't be passed at runtym
    @pytest.fixture(scope="class")
    def test_parent(self):
        global kk
        global inputtime
        # inputtime = input("Enter the date & time: ")
        driver = webdriver.Chrome(executable_path="C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\chromedriver.exe")
        kk = Testa(driver)

    def test_child(self, test_parent):
        inputtime = "25-02-2022 18:38:00"

        i=1
        while i > 0:
            systime = datetime.today()
            print(systime)
            timeconversion = systime.strftime("%d-%m-%Y %H:%M:%S")
            print(inputtime)
            print(timeconversion)
            if inputtime == timeconversion:
                kk.test_login(link, "it", "123")
                time.sleep(4)
                kk.test_xpathclick(masters)
                time.sleep(10)
                break

    # Parent method can't b called directly
    # Multithread can't workedout in pytest
    t1 = threading.Thread(target=test_child)
    t1.start()
    t2 = threading.Thread(target=test_child)
    t2.start()









