import pytest
from TestMethod import ContainerType
from TestMethod import LaunchLims

accessmethod1 = LaunchLims
accessmethod2 = ContainerType

class TestContainerType():

    @pytest.fixture(scope="class")
    def test_parent(self):
        driver = accessmethod1.launchLIMS("launch browser", "browser link", "credentials locator", "credentials Values")
        driver.implicitly_wait(10)
        accessmethod2.containerType_Prequesite(driver, "basic", "module screen")
        # accessmethod2.containerType_Add(driver, "screen locator", "screen value")
        accessmethod2.containerType_Edit(driver, "screen locator", "screen value", "tr")
        # accessmethod2.containerType_Delete(driver, "screen locator", "tr")

    def test_child(self, test_parent):
        print("Launched Lims")
        print("Pre-Req done")
        print("ContainerType Added")
        print("ContainerType Edited")
        print("ContainerType Deleted")

