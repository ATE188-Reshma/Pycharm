import time
import allure
import pytest
from TestMethod import LaunchLims, ContainerType

accessmethod1 = LaunchLims
accessmethod3 = ContainerType


@pytest.fixture(scope="function")
@allure.severity(allure.severity_level.CRITICAL)
def test_parent():

    global driver

    driver = accessmethod1.launchLIMS("launch browser", "browser link", "credentials locator", "credentials Values")
    time.sleep(5)
    accessmethod3.containerType_Prequesite(driver, "basic", "module screen")
    time.sleep(5)
    #
    # accessmethod3.containerTypeCountIndexAddValidation(driver)
    # time.sleep(4)
    #
    # accessmethod3.containerTypeCountIndexEditValidation(driver)
    # time.sleep(4)
    #
    # accessmethod3.containerTypeCountIndexDeleteValidation(driver)
    # time.sleep(4)

@allure.severity(allure.severity_level.NORMAL)
def test_child(test_parent):
    accessmethod3.containerTypeAddAuditTrail(driver)
    time.sleep(4)

    # accessmethod3.containerTypeEditAuditTrail(driver)
    # time.sleep(4)
    #
    # accessmethod3.containerTypeDeleteAuditTrail(driver)
    # time.sleep(4)

    # accessmethod3.containerType_Prequesite(driver, "basic", "module screen")
    # time.sleep(3)
    #
    # accessmethod3.containerType_search(driver, "screen locator", "filter")
    # time.sleep(3)
    #
    # accessmethod3.containerType_downloadPDF(driver, "screen locator")
    # time.sleep(3)
    #
    # accessmethod3.containerType_downloadExcel(driver, "screen locator")
    # time.sleep(3)
