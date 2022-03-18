import logging
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



def errorLog(errormsg):
    logging.basicConfig(filename="../Utiliser/rr.log", format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt="%d/%m/%Y %H:%M:%S %p", level=logging.ERROR)
    aa = logging.getLogger()
    kk=aa.error(errormsg)
    return kk

def infoLog(info):

    logging.basicConfig(filename="../Utiliser/ss.log", format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt="%m/%d/%Y %H:%M:%S %p", level=logging.INFO)
    bb = logging.getLogger()
    cc = bb.info(info)
    return cc

# to achieve log in pytest,
# from loguru import logger
# logger.info,error,debug,warning...
# Now can see the log in console using d command
# this s applicable only for venv folder
# pytest -vv -s --log-cli-level=INFO --log-cli-format="%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)" --log-cli-date-format="%Y-%m-%d %H:%M:%S" foldername/testcasename >logname.log

def sendKeysXpath(driver, loc1, input):
    wait = WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH, loc1)))
    wait.send_keys(input)

def clickXpath(driver, loc2):
    wait = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, loc2)))
    wait.click()