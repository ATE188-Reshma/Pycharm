import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

# Class Name should be start with Test
class Testpy():


# Defining this method as Parent
    @pytest.yield_fixture(scope="session")
# Method has to be defined in the below format test_
    def test_parent(self):
        global driver
        driver=webdriver.Chrome(executable_path="C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\chromedriver.exe")
        driver.maximize_window()
        time.sleep(4)
# AfterMethod
        yield
        driver.quit()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_first(self, test_parent):
        driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
        time.sleep(4)
        driver.find_element_by_xpath("//*[@name='sloginid']").send_keys("cdolman")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@name='spassword']").send_keys("123")
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='Login']").click()
# Allure ScreenShot
        allure.attach(driver.get_screenshot_as_png(), name="test", attachment_type=AttachmentType.PNG)
        time.sleep(4)

    @allure.severity(allure.severity_level.NORMAL)
    def test_second(self, test_parent):
        driver.find_element_by_xpath("//*[text()='Registration']").click()
