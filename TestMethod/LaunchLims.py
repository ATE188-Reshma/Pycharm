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

    try:
        driver = webdriver.Chrome(executable_path=chromebrowser)
        logger.info("Browser Launched")

        driver.maximize_window()
        driver.implicitly_wait(10)

        try:
            driver.get(link)
            logger.info("Link passed")


            try:
                ReusableMethod.clickXpath(driver, loginxpath)
                ReusableMethod.sendKeysXpath(driver, loginxpath, loginvalue)
                logger.info("Entered Login id")

                try:
                    time.sleep(4)
                    ReusableMethod.clickXpath(driver, passwordxpath)
                    ReusableMethod.sendKeysXpath(driver, passwordxpath,passwordvalue)
                    logger.info("Entered password")


                    try:
                        time.sleep(5)
                        ReusableMethod.clickXpath(driver, loginxpath)
                        time.sleep(2)
                        ReusableMethod.clickXpath(driver, loginbuttonxpath)
                        logger.info("Logged in")




                    except Exception as e:
                        logger.error("Login Failed, Exception occurred" + str(e))

                except Exception as e:
                    logger.error("Password has not sent, Exception occurred" + str(e))

            except Exception as e:
                logger.error("LoginId has not sent, Exception occurred" + str(e))

        except Exception as e:
            logger.error("Link has not passed, Exception occurred" + str(e))

    except Exception as e:
        logger.error("Browser has not Launched, Exception occurred" + str(e))

    return driver