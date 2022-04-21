import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class kk(unittest.TestCase):
    global driver
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.maximize_window()

    def test_sample1(self):
        self.driver.get("http://62.171.183.83:9092/QuaLISWeb/#/login")
        kk=self.driver.title
        print(kk)
    def test_sample2(self):
        self.driver.get("http://62.171.183.83:9092/QuaLISWeb/#/login")
        time.sleep(4)
        self.driver.find_element_by_xpath("//*[@name='sloginid']").send_keys("cdolman")
        time.sleep(4)
        self.driver.find_element_by_xpath("//*[@name='spassword']").send_keys("123")
        time.sleep(4)
        self.driver.find_element_by_xpath("//*[text()='Login']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
