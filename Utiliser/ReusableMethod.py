import logging
import time
from configparser import ConfigParser
from loguru import logger
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

objectRepository = ConfigParser()
objectRepository.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\ObjectRepository\\Element_PageCount.ini")

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
    wait = WebDriverWait(driver,60).until(ec.element_to_be_clickable((By.XPATH, loc1)))
    wait.send_keys(input)

def clickXpath(driver, loc2):
    wait = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, loc2)))
    wait.click()

def dropdownByText(driver, text):
    wait = WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH, "//*[text()='{}']".format(text))))
    wait.click()

    # driver.find_element(By.XPATH, "//*[text()='"+text+"'")

def getText(driver, loc3):
    text = driver.find_element(By.XPATH, loc3).text
    return text

def scrollAction(driver, loc4):
    element = driver.find_element(By.XPATH, loc4)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(2)
    element.click()

# to get the page count
def count(driver, loc_key, xpath):
    # change xpath as required
    containertypepagecountxpath = objectRepository.get(loc_key, xpath)


    containertypepagecount = driver.find_element(By.XPATH, containertypepagecountxpath).text
    print(containertypepagecount)

    individualtext = containertypepagecount.split(' ')
    print(individualtext)

    count = individualtext[4]

    print(count)
    
    print(" ")

    count = int(count)

    return count


# Page count validation
def countvalidation(driver, beforecount, aftercount):
    if aftercount == beforecount+1:
        logger.info("Page count increased correctly")

    elif aftercount > beforecount+1:
        logger.info("Page count increased more")

    elif aftercount == beforecount:
        logger.info("Page count has not increased")




