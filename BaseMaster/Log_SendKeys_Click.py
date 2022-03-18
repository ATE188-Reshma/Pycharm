import logging
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



def errorlog(errormsg):
    logging.basicConfig(filename="../BaseMaster/rr.log", format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt="%d/%m/%Y %H:%M:%S %p", level=logging.ERROR)
    aa = logging.getLogger()
    kk=aa.error(errormsg)
    return kk

def log1(info):

    logging.basicConfig(filename="../BaseMaster/ss.log", format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt="%m/%d/%Y %H:%M:%S %p", level=logging.INFO)
    bb = logging.getLogger()
    cc = bb.info(info)
    return cc

def sendkeys(driver, loc1, input):
    wait = WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH, loc1)))
    wait.send_keys(input)

def click(driver, loc2):
    wait = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, loc2)))
    wait.click()