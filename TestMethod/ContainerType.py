import time
from configparser import ConfigParser

from Utiliser import ReusableMethod

objectRepository = ConfigParser()
objectRepository.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\ObjectRepository\\Element_ContainerType.ini")

InputData = ConfigParser()
InputData.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\InputData\\Data_ContainerType.ini")

objectRepository1=ConfigParser()
objectRepository1.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\ObjectRepository\\Element_LaunchLims_BasicAction.ini")


def containerType_Prequesite(driver, basic, module_key):
    masterxpath = objectRepository1.get(basic, "master")
    pinxpath = objectRepository1.get(basic, "pin")
    basemasterxpath = objectRepository.get(module_key, "basemaster")
    containertypexpath = objectRepository.get(module_key, "containertype")

    try:
        time.sleep(8)
        ReusableMethod.clickXpath(driver,masterxpath)
        ReusableMethod.infoLog("Master module clicked")

        try:
            ReusableMethod.clickXpath(driver, pinxpath)
            ReusableMethod.infoLog("Module pinned")

            try:
                ReusableMethod.clickXpath(driver, basemasterxpath)
                ReusableMethod.infoLog("Basemaster module clicked")

                try:
                    ReusableMethod.clickXpath(driver, containertypexpath)
                    ReusableMethod.infoLog("Containertype screen clicked")

                except Exception as e:
                    ReusableMethod.errorLog("Containertype screen has not clicked, Exception occurred" + str(e))

            except Exception as e:
                ReusableMethod.errorLog("Basemaster module has not clicked, Exception occurred" + str(e))

        except Exception as e:
            ReusableMethod.errorLog("Module has not pinned, Exception occurred" + str(e))

    except Exception as e:
        ReusableMethod.errorLog("Master module has not clicked, Exception occurred" + str(e))


def containerType_Add(driver, loc_key, input_key):
    addxpath = objectRepository.get(loc_key, "add")
    containertypexpath = objectRepository.get(loc_key, "containertype")
    descriptionxpath = objectRepository.get(loc_key, "description")
    savexpath = objectRepository.get(loc_key, "save")
    containertypevalue = InputData.get(input_key, "inputcontainertype")
    descriptionvalue = InputData.get(input_key, "inputdescription")

    try:
        driver.implicitly_wait(10)
        ReusableMethod.clickXpath(driver, addxpath)
        ReusableMethod.infoLog("Add button clicked")

        try:
            ReusableMethod.sendKeysXpath(driver, containertypexpath, containertypevalue)
            ReusableMethod.infoLog("Entered ContainerType")

            try:
                ReusableMethod.sendKeysXpath(driver, descriptionxpath, descriptionvalue)
                ReusableMethod.infoLog("Entered ContainerTypeDescription")

                try:
                    ReusableMethod.clickXpath(driver, savexpath)
                    ReusableMethod.infoLog("ContainerType Added")

                except Exception as e:
                    ReusableMethod.errorLog("ContainerType has not Added, Exception occurred" + str(e))

            except Exception as e:
                ReusableMethod.errorLog("ContainerTypeDescription value has not passed, Excepton occurred" + str(e))

        except Exception as e:
            ReusableMethod.errorLog("ContainerType value has not passed, Excepton occurred" + str(e))

    except Exception as e:
        ReusableMethod.errorLog("Add button has not clicked, Exception occurred" + str(e))


def containerType_Edit(loc_key):
    containertyperecordxpath = objectRepository.get(loc_key, "containertyperecord")
    descriptionrecordxpath = objectRepository.get(loc_key, "descriptionrecord")
    editrecordxpath = objectRepository.get(loc_key, "editrecord")



