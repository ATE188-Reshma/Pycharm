import time
from configparser import ConfigParser
from selenium.webdriver.common.by import By
from Utiliser import ReusableMethod
from TestMethod import ContainerType
from TestMethod import LaunchLims

accessmethod1 = LaunchLims
accessmethod2 = ContainerType

driver = accessmethod1.launchLIMS("launch browser", "browser link", "credentials locator", "credentials Values")
driver.implicitly_wait(10)
accessmethod2.containerType_Prequesite(driver, "basic", "module screen")
driver.implicitly_wait(10)
# accessmethod2.containerType_Add(driver, "screen locator", "screen value")


objectRepository = ConfigParser()
objectRepository.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\ObjectRepository\\Element_ContainerType.ini")

InputData = ConfigParser()
InputData.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\InputData\\Data_ContainerType.ini")

def containerType_Edit(loc_key, input_key, tag):
    containertypexpath = objectRepository.get(loc_key, "containertype")
    descriptionxpath = objectRepository.get(loc_key, "description")
    savexpath = objectRepository.get(loc_key, "save")
    containertype_editvalue = InputData.get(input_key, "editinputcontainertype")
    description_editvalue = InputData.get(input_key, "editinputdescription")

    time.sleep(7)

    t = driver.find_elements(By.TAG_NAME, tag)
    tt = len (t)

    # input("enter containertype with description: ")
    # pass the record to edit
    container = "Matrix For use with Tachosil fibrin sealant kits."
    for i in range(1,tt):
        ttt = t[i].text
        print(ttt)
        if container == ttt:
            print("containertype count is",i,ttt)
            print(i)
            l = str(i)
            edit = "(//span[@data-tip='Edit'])["+l+"]"
            print(edit)
            driver.find_element(By.XPATH, edit).click()
            break

    driver.find_element(By.XPATH, containertypexpath).clear()
    time.sleep(2)
    ReusableMethod.sendKeysXpath(driver, containertypexpath, containertype_editvalue)
    # ReusableMethod.sendKeysXpath(driver, descriptionxpath, description_editvalue)
    ReusableMethod.clickXpath(driver, savexpath)


def containerType_Delete(loc_key, tag):
    containertypedeleteokxpath = objectRepository.get(loc_key, "deletepopupokbutton")
    containertypedeletecancelxpath = objectRepository.get(loc_key, "deletepopupcancelbutton")

    time.sleep(7)

    q = driver.find_elements(By.TAG_NAME, tag)
    qq = len(q)

    # input("enter containertype with description: ")
    container = "Mat For use with Tachosil fibrin sealant kits."
    for i in range(1, qq):
        qqq = q[i].text
        print(qqq)
        if container == qqq:
            print("containertype count is", i, qqq)
            print(i)
            m = str(i)
            delete = "(//span[@data-tip='Delete'])[" + m + "]"
            print(delete)
            driver.find_element(By.XPATH, delete).click()
            break

    time.sleep(10)
    # alert = driver.switch_to.alert

    ReusableMethod.clickXpath(driver, containertypedeleteokxpath)







containerType_Edit("screen locator", "screen value", "tr")
containerType_Delete("screen locator", "tr")

# pom and pytest only pending


