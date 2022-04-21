import time
from TestMethod import AuditTrial
from TestMethod import LaunchLims
from TestMethod import ContainerType
from TestMethod.AuditTrial import *


driver=LaunchLims.launchLIMS("launch browser", "browser link", "credentials locator", "credentials Values")

# Add

beforeCount=AuditTrial.auditTrailCount(driver, "audittrail")

time.sleep(2)

ContainerType.containerType_Prequesite(driver, "basic", "module screen")

time.sleep(2)

ContainerType.containerType_Add(driver, "screen locator", "screen value")

time.sleep(2)

afterCount=AuditTrial.auditTrailCount(driver, "audittrail")

time.sleep(3)

auditTrail(driver, afterCount, beforeCount,"ADD CONTAINER TYPE", "Carl Dolman", "Admin", "Container Type: Soap Container;Description: container with 2 compartments;", "SYSTEM")

#Edit

time.sleep(4)

beforeCount=AuditTrial.auditTrailCount(driver, "audittrail")

time.sleep(2)

ContainerType.containerType_Prequesite(driver, "basic", "module screen")

time.sleep(2)

ContainerType.containerType_Edit(driver, "screen locator", "screen value", "tr")

time.sleep(2)

afterCount=AuditTrial.auditTrailCount(driver, "audittrail")

time.sleep(3)

auditTrail(driver, afterCount, beforeCount,"EDIT CONTAINER TYPE", "Carl Dolman", "Admin", "Container Type: Matrix-> Mat;Description: For use with Tachosil fibrin sealant kits.-> matrix container;", "SYSTEM")

# Delete
time.sleep(4)

beforeCount=AuditTrial.auditTrailCount(driver, "audittrail")

time.sleep(2)

ContainerType.containerType_Prequesite(driver, "basic", "module screen")

time.sleep(2)

ContainerType.containerType_Delete(driver, "screen locator", "tr")

time.sleep(2)

afterCount=AuditTrial.auditTrailCount(driver, "audittrail")

time.sleep(3)

auditTrail(driver, afterCount, beforeCount,"DELETE CONTAINER TYPE", "Carl Dolman", "Admin", "Container Type: abc;", "SYSTEM")



