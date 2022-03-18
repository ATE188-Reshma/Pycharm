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

    @pytest.fixture(scope="class")
    def test_parent(self):
        global kk, bb
        driver = webdriver.Chrome(executable_path="C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\chromedriver.exe")
        driver1 = webdriver.Ie(executable_path="C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\IEDriverServer.exe")
        # Using constructor
        kk = Testa(driver)
        bb = Testa(driver1)

    @allure.severity(allure.severity_level.NORMAL)
    def test_child(self, test_parent):
        kk.test_login(link, "it", "123")
        bb.test_login(link, "it", "123")



    # t1 = threading.Thread(target=test_child)
    # t1.start()
    # t2 = threading.Thread(target=test_child)
    # t2.start()
