import pytest
from TestMethod import LaunchLims

accessmethod = LaunchLims

class TestLogin():

    @pytest.fixture(scope="class")
    def test_parent(self):
        accessmethod.launchLIMS("launch browser", "browser link", "credentials locator", "credentials Values")

    def test_child(self, test_parent):
        print("Success")

