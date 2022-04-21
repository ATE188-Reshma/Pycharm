import allure
import pytest
import time
from TestMethod import AuditTrial
from TestMethod import LaunchLims
from TestMethod import ContainerType
from TestMethod.AuditTrial import *


accessmethod1 = LaunchLims
accessmethod2 = AuditTrial
accessmethod3 = ContainerType


@pytest.mark.kk
def test_parent():
        driver = accessmethod1.launchLIMS("launch browser", "browser link", "credentials locator", "credentials Values")

        # Add

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
                   "Container Type: Matrix-> Mat;Description: For use with Tachosil fibrin sealant kits.-> matrix container;",
                   "SYSTEM")

        # Delete

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
                   "Container Type: abc;", "SYSTEM")

        accessmethod3.containerType_Prequesite(driver, "basic", "module screen")

        accessmethod3.containerType_search(driver, "screen locator", "filter")

        accessmethod3.containerType_downloadPDF(driver, "screen locator")

        accessmethod3.containerType_downloadExcel(driver, "screen locator")

@allure.severity(allure.severity_level.NORMAL)
def test_child():
        print("ContainerType Operations completed with Audit Trail")


