import time

from selenium.webdriver.common.by import By

username="//input[@id='idEmail']"
psswd="//input[@id='idpassword']"
loginbutton="//input[@id='idLogin']"

class Testa():


    def __init__(self, browser):
        self.driver = browser


    def test_xpathsendkeys(self, location, input):
        self.driver.find_element(By.XPATH, location).send_keys(input)

    def test_xpathclick(self,location):

        self.driver.find_element(By.XPATH,location).click()


    def test_login(self, link, usrname, password):
        self.driver.implicitly_wait(10)
        self.driver.get(link)
        self.test_xpathsendkeys(username, usrname)
        self.test_xpathsendkeys(psswd, password)
        time.sleep(6)
        self.test_xpathclick(loginbutton)






