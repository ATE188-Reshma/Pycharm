import time
from configparser import ConfigParser

from TestMethod import LaunchLims, ContainerType, AuditTrial
from TestMethod.AuditTrial import auditTrail

accessmethod1 = LaunchLims
accessmethod2 = AuditTrial
accessmethod3 = ContainerType

driver = accessmethod1.launchLIMS("launch browser", "browser link", "credentials locator", "credentials Values")
time.sleep(5)

# accessmethod3.containerType_Prequesite(driver, "basic", "module screen")
# time.sleep(3)

beforeCount = accessmethod2.auditTrailCount(driver, "audittrail")

time.sleep(2)
accessmethod3.containerType_Prequesite(driver, "basic", "module screen")

time.sleep(2)
accessmethod3.containerType_Add(driver, "screen locator", "screen value")

time.sleep(2)
afterCount = accessmethod2.auditTrailCount(driver, "audittrail")

baseMaster=ConfigParser()
baseMaster.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\InputData\\Data_LaunchLims.ini")

id=baseMaster.get("credentials Values", "inputid")

time.sleep(3)
auditTrail(driver, afterCount, beforeCount, "ADD CONTAINER TYPE", id, "Admin",
                   "Container Type: Soap Container;Description: container with 2 compartments;", "SYSTEM")

