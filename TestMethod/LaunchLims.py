import time
from configparser import ConfigParser
from selenium import webdriver
from Utiliser import ReusableMethod
from loguru import logger

objectRepository=ConfigParser()
objectRepository.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\ObjectRepository\\Element_LaunchLims_BasicAction.ini")

InputData=ConfigParser()
InputData.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\InputData\\Data_LaunchLims.ini")


def launchLIMS(browser, limslink, loc_key, input_key):
    chromebrowser = objectRepository.get(browser, "browser1")
    link = objectRepository.get(limslink, "link")

    loginxpath = objectRepository.get(loc_key, "id")
    loginvalue = InputData.get(input_key, "inputid")
    passwordxpath = objectRepository.get(loc_key, "psswd")
    passwordvalue = InputData.get(input_key, "inputpsswd")
    userrolexpath = objectRepository.get(loc_key, "UserRole")
    logintypexpath = objectRepository.get(loc_key, "LoginType")
    loginbuttonxpath = objectRepository.get(loc_key, "loginbttn")
    pinxpath = objectRepository.get(loc_key, "pin")

    try:
        driver = webdriver.Chrome(executable_path=chromebrowser)
        logger.info("Browser Launched")

        driver.maximize_window()
        driver.implicitly_wait(10)

    except:
        logger.error("Browser not launched")

    try:

            driver.get(link)
            logger.info("Link passed")

    except:
            logger.error("link is not hit")

    try:
        ReusableMethod.clickXpath(driver, loginxpath)
        ReusableMethod.sendKeysXpath(driver, loginxpath, loginvalue)
        logger.info("Entered Login id")


    except:
        logger.error("unable to hit the link")

    try:
            time.sleep(4)
            ReusableMethod.clickXpath(driver, passwordxpath)
            ReusableMethod.sendKeysXpath(driver, passwordxpath, passwordvalue)
            logger.info("Entered password")
    except Exception as e:
                    logger.error("Password has not sent, Exception occurred" + str(e))



    try:
                time.sleep(2)
                ReusableMethod.clickXpath(driver, userrolexpath)
                ReusableMethod.dropdownByText(driver, "Admin")

    except Exception as e:
                        logger.error("UserRole has not selected, Exception occurred" + str(e))



    try:
                    time.sleep(2)
                    ReusableMethod.clickXpath(driver, logintypexpath)
                    ReusableMethod.dropdownByText(driver, "Internal")

    except Exception as e:
        logger.error("LoginType has not selected, Exception occurred" + str(e))

    try:
                        time.sleep(5)
                        ReusableMethod.clickXpath(driver, loginxpath)
                        time.sleep(2)
                        ReusableMethod.clickXpath(driver, loginxpath)
                        # ReusableMethod.clickXpath(driver, passwordxpath)
                        time.sleep(2)
                        ReusableMethod.clickXpath(driver, loginbuttonxpath)
                        logger.info("Logged in")

    except Exception as e:
        logger.error("Login Failed, Exception occurred" + str(e))

    # try:
    #     time.sleep(2)
    #     ReusableMethod.clickXpath(driver, pinxpath)
    #     logger.info("Module pinned")
    #
    # except Exception as e:
    #     logger.error("Module has not pinned, Exception occurred" + str(e))


    return driver



