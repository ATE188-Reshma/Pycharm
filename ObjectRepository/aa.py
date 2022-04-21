import time
from configparser import ConfigParser
from loguru import logger
from TestMethod import AuditTrial
from selenium.webdriver.common.by import By

from TestMethod.AuditTrial import auditTrail
from Utiliser import ReusableMethod
from TestMethod import ContainerType
from TestMethod import LaunchLims
import os

accessmethod1 = LaunchLims
accessmethod2 = AuditTrial
accessmethod3 = ContainerType

driver = accessmethod1.launchLIMS("launch browser", "browser link", "credentials locator", "credentials Values")
driver.implicitly_wait(10)
time.sleep(5)
accessmethod3.containerType_Prequesite(driver, "basic", "module screen")
time.sleep(5)




objectRepository2 = ConfigParser()
objectRepository2.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\ObjectRepository\\Element_PageCount.ini")

# auditTrail1=ConfigParser()
# auditTrail1.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\ObjectRepository\\Element_AuditTrial.ini")

objectRepository1 = ConfigParser()
objectRepository1.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\ObjectRepository\\Element_ContainerType.ini")

InputData = ConfigParser()
InputData.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\InputData\\Data_ContainerType.ini")

# to get the page count
def count(driver, loc_key, xpath):
    # change xpath as required
    containertypepagecountxpath = objectRepository2.get(loc_key, xpath)


    containertypepagecount = driver.find_element(By.XPATH, containertypepagecountxpath).text
    print(containertypepagecount)

    individualtext = containertypepagecount.split(' ')
    print(individualtext)

    count = individualtext[4]

    print(count)

    count = int(count)

    return count


# Page count validation
def countvalidation(screen, beforecount, aftercount):
    if aftercount == beforecount+1:
        logger.info(screen+ " count increased by 1")

    elif aftercount > beforecount+1:
        logger.info(screen+ " count increased more than 1")

    elif aftercount == beforecount:
        logger.info(screen+ " count has not increased")

    elif aftercount == beforecount-1:
        logger.info(screen+ " count decreased by 1")

    elif aftercount < beforecount-1:
        logger.info(screen+ " count decreased more than 1")

def indexValidateAdd(driver, input_key):
    # containertypeindexxpath = objectRepository1.get(loc_key, "containertypeindex")
    containertypevalue = InputData.get(input_key, "inputcontainertype")
    descriptionvalue = InputData.get(input_key, "inputdescription")
    # refresh = objectRepository1.get(loc_key, "refreshbutton")

    containertypeindex = driver.find_elements(By.TAG_NAME, "tr")
    tt = len(containertypeindex)

    containerdata = containertypevalue+" "+descriptionvalue

    # ReusableMethod.clickXpath(driver, refresh)
    # time.sleep(4)

    if containertypeindex[1].text == containerdata:
        logger.info("Added Container Type displayed in first index")

    else:
        # ReusableMethod.clickXpath(driver,refresh)
        # time.sleep(2)
        for i in range(1, tt):
            ttt = containertypeindex[i].text
            print(ttt)

            if containerdata == ttt:
                print("Container Type displayed in index" +str(i))





# Add
def containerTypeCountIndexAddValidation():
    beforecount = count(driver, "containertype", "containertypepagecount")
    accessmethod3.containerType_Add(driver, "screen locator", "screen value")
    time.sleep(5)
    aftercount = count(driver, "containertype", "containertypepagecount")
    countvalidation("containerType", beforecount, aftercount)
    time.sleep(5)
    indexValidateAdd(driver, "screen value")
    time.sleep(5)


#Edit
def containerTypeCountIndexEditValidation():
    beforecount = count(driver, "containertype", "containertypepagecount")
    accessmethod3.containerType_Edit(driver, "screen locator", "screen value", "tr")
    time.sleep(5)
    aftercount = count(driver, "containertype", "containertypepagecount")
    countvalidation("containerType", beforecount, aftercount)
    time.sleep(5)



#Delete
def containerTypeCountIndexDeleteValidation():
    beforecount = count(driver, "containertype", "containertypepagecount")
    accessmethod3.containerType_Delete(driver, "screen locator", "tr")
    time.sleep(5)
    aftercount = count(driver, "containertype", "containertypepagecount")
    countvalidation("containerType", beforecount, aftercount)
    time.sleep(5)


# Add
def containerTypeAddAuditTrail():
    beforeCount = accessmethod2.auditTrailCount(driver, "audittrail")

    time.sleep(2)
    accessmethod3.containerType_Prequesite(driver, "basic", "module screen")

    time.sleep(2)
    accessmethod3.containerType_Add(driver, "screen locator", "screen value")

    time.sleep(2)
    afterCount = accessmethod2.auditTrailCount(driver, "audittrail")

    time.sleep(3)
    auditTrail(driver, afterCount, beforeCount, "ADD CONTAINER TYPE", "Carl Dolman", "Admin",
               "Container Type: Soap Container;Description: container with 2 compartments;", "SYSTEM")


#Edit
def containerTypeEditAuditTrail():
    time.sleep(4)

    beforeCount = accessmethod2.auditTrailCount(driver, "audittrail")

    time.sleep(2)
    accessmethod3.containerType_Prequesite(driver, "basic", "module screen")

    time.sleep(2)
    accessmethod3.containerType_Edit(driver, "screen locator", "screen value", "tr")

    time.sleep(2)
    afterCount = accessmethod2.auditTrailCount(driver, "audittrail")

    time.sleep(3)
    auditTrail(driver, afterCount, beforeCount, "EDIT CONTAINER TYPE", "Carl Dolman", "Admin",
               "Container Type: Soap Container-> Mat;Description: container with 2 compartments-> matrix container;",
               "SYSTEM")


# Delete
def containerTypeDeleteAuditTrail():
    time.sleep(4)

    beforeCount = accessmethod2.auditTrailCount(driver, "audittrail")

    time.sleep(2)
    accessmethod3.containerType_Prequesite(driver, "basic", "module screen")

    time.sleep(2)
    accessmethod3.containerType_Delete(driver, "screen locator", "tr")

    time.sleep(2)
    afterCount = accessmethod2.auditTrailCount(driver, "audittrail")

    time.sleep(3)
    auditTrail(driver, afterCount, beforeCount, "DELETE CONTAINER TYPE", "Carl Dolman", "Admin",
               "Container Type: Mat;Description: matrix container;", "SYSTEM")


time.sleep(5)
containerTypeCountIndexAddValidation()
time.sleep(4)
containerTypeCountIndexEditValidation()
time.sleep(4)
containerTypeCountIndexDeleteValidation()
time.sleep(4)
containerTypeAddAuditTrail()
time.sleep(4)
containerTypeEditAuditTrail()
time.sleep(4)
containerTypeDeleteAuditTrail()
