import time
from configparser import ConfigParser
from selenium import webdriver
from BaseMaster import Log_SendKeys_Click
from BaseMaster.POM_Login import Loginpage

config = ConfigParser()
a = Log_SendKeys_Click
b = Loginpage()

class ContainerType():
    config.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\BaseMaster\\containertype.ini")
    config.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\BaseMaster\\login.ini")

    def prerequesite(self, basic, module_key):
        masterxpath = config.get(basic, "master")
        pinxpath = config.get(basic, "pin")
        basemasterxpath = config.get(module_key, "basemaster")
        containertypexpath = config.get(module_key, "containertype")

        b.browser("launch browser")
        b.limslogin("browser link", "credentials locator", "credentials Values")
        time.sleep(4)

        a.click(driver, masterxpath)


    def containertype(self, loc_key, input_key):
        config.get(loc_key, "add")
        config.get(loc_key, "containertype")
        config.get(loc_key, "description")
        config.get(loc_key, "save")
        config.get(input_key, "inputcontainertype")
        config.get(input_key, "inputdescription")



