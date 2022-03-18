import time
from Constructor import kk
from selenium import webdriver
import threading


def b(orgid,usrnm,pswd):

    browserdriver=webdriver.Chrome(executable_path="../Automation/chromedriver.exe")
    x=kk(browserdriver)


    x.login("https://logilabelntesting.azurewebsites.net/",orgid,usrnm,pswd)
    x.xpathclick("(//*[text()='Orders'])[1]")
    time.sleep(100)

# MultiThreading
# initialise the method name in "target" and pass the method's argument in "args"
th1=threading.Thread(target=b,args=("agaramtech.onmicrosoft.com","arul","admin"))
th1.start()
th2=threading.Thread(target=b,args=("agaramtech.onmicrosoft.com","arul","admin"))
th2.start()
