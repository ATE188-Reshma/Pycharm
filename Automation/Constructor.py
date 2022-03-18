import time

orgnamexpath="//*[@name='Username']"
nextidxpath="//*[@id='inputText']"
usrnamexpath="//*[@id='idUsername']"
passwordnamexpath="//*[@name='Password']"
loginxpath="(//*[@value='Login'])[1]"

class kk():

    # Create instance thn only it can be accessed out of class
    # self means to current
    def __init__(self,driver2):
        self.driver=driver2

    def login(self,link,orgid,un,pwd):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(link)
        self.driver.find_element_by_xpath(orgnamexpath).send_keys(orgid)
        self.driver.find_element_by_xpath(nextidxpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(usrnamexpath).send_keys(un)
        self.driver.find_element_by_xpath(passwordnamexpath).send_keys(pwd)
        self.driver.find_element_by_xpath(loginxpath).click()

    def xpathclick(self,loc):
        self.driver.find_element_by_xpath(loc).click()

    def xpathsendkeys(self,loc,send):
        self.driver.find_element_by_xpath(loc).send_keys(send)

