import pytest
from BaseMaster.POM_Login import Loginpage

aa = Loginpage()

class TestLogin():

    @pytest.fixture(scope="class")
    def test_parent(self):
        aa.browser("launch browser")

    def test_child(self, test_parent):
        aa.limslogin("browser link", "credentials locator", "credentials Values")
