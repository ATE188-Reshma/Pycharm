import time
from selenium.webdriver.chrome import webdriver

from configparser import ConfigParser

from selenium import webdriver
from BaseMaster import Log_SendKeys_Click

config = ConfigParser()
a = Log_SendKeys_Click

class Loginpage():

    config.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\BaseMaster\\login.ini")

    def browser(self, browser):
        chromebrowser = config.get(browser, "browser1")
        self.driver = webdriver.Chrome(executable_path= chromebrowser)



    def limslogin(self, limslink, loc_key, input_key):
        link = config.get(limslink, "link")
        loginxpath = config.get(loc_key, "id")
        loginvalue = config.get(input_key, "inputid")
        passwordxpath = config.get(loc_key, "psswd")
        passwordvalue = config.get(input_key, "inputpsswd")
        # userrolexpath = config.get(loc_key, "UserRole")
        # logintypexpath = config.get(loc_key, "LoginType")
        loginbuttonxpath = config.get(loc_key, "loginbttn")

        self.driver.get(link)
        time.sleep(4)
        a.sendkeys(self.driver, loginxpath, loginvalue)
        a.sendkeys(self.driver, passwordxpath, passwordvalue)
        time.sleep(3)

        try:
            a.click(self.driver, loginbuttonxpath)
            a.log1("Logged")

        except Exception as e:
            print(e)
            a.errorlog(e)
