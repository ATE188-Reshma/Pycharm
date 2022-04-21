import time
from configparser import ConfigParser
from loguru import logger
from selenium.webdriver.common.by import By

import JDBC
from Utiliser import ReusableMethod


auditTrail1=ConfigParser()
auditTrail1.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\ObjectRepository\\Element_AuditTrial.ini")



def auditTrailCount(driver, loc_key):

    global count
    masterxpath = auditTrail1.get(loc_key,"masterIcon")
    userManagementIconxpath = auditTrail1.get(loc_key, "userManagementIcon")
    auditTrailIconxpath = auditTrail1.get(loc_key, "auditTrailIcon")
    auditTraildataxpath = auditTrail1.get(loc_key, "auditTraildata")
    counttext = auditTrail1.get(loc_key, "counttext")

    try:
        time.sleep(2)
        ReusableMethod.clickXpath(driver, masterxpath)

    except Exception as e:
        print(str(e))

    try:
        time.sleep(2)
        ReusableMethod.clickXpath(driver, userManagementIconxpath)
    except Exception as e:
        print(str(e))

    try:
        time.sleep(2)
        ReusableMethod.clickXpath(driver, auditTrailIconxpath)
    except Exception as e:
        print(str(e))

    try:
        time.sleep(8)
        countText = driver.find_element(By.XPATH, counttext).text

        print(countText)

        individualText = countText.split(' ')

        count = individualText[4]

        count = int(count)

        print(count)

        logger.info("Count retrieved")

    except Exception as e:
        print(str(e))
        logger.error("Count has not retrieved")

    return count



def auditTrail(driver, afterCount, beforeCount, expectedAuditAction, expectedLoginID, userroledata, expectedCommentsdata, expectedActiontypedata):

    try:
        if afterCount == beforeCount + 1:
            logger.info("Audit trail criteria 1 matched")

            UIauditAction = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[3]").text


            DBAuditAction=JDBC.returnOneValue("select sauditaction from auditaction where nauditcode=(select COUNT(*) from auditaction)")

            if UIauditAction==expectedAuditAction:
                logger.info("Audit action is captured correctly in UI"+UIauditAction)
            else:
                logger.error("Audit action is not captured correctly in UI")

            if DBAuditAction==expectedAuditAction:
                logger.info("Audit action is captured correctly in DB"+DBAuditAction)
            else:
                logger.error("Audit action is not captured correctly in DB")

            if DBAuditAction==UIauditAction:
                logger.info("Audit action is same in DB and UI"+DBAuditAction+UIauditAction)
            else:
                logger.error("Audit action is not same in DB and UI")

            UIuserName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[5]").text

            DBUserName=JDBC.returnOneValue("select sfirstname from users where sloginid='cdolman'")+" "+JDBC.returnOneValue("select slastname from users where sloginid='cdolman'")


            if UIuserName==expectedLoginID:
                logger.info("UserName is captured correctly in UI"+UIuserName)
            else:
                logger.error("UserName is not captured correctly in UI")

            if DBUserName==expectedLoginID:
                logger.info("UserName is captured correctly in DB"+DBUserName)
            else:
                logger.error("UserName is not captured correctly in DB")

            if DBUserName==UIuserName:
                logger.info("UserName is same in DB and UI"+DBUserName+UIuserName)
            else:
                logger.error("UserName is not same in DB and UI")

            UIUserRole = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[6]").text

            # DBUserRole = ""

            if UIUserRole==userroledata:
                logger.info("UserRole is captured correctly in UI"+UIUserRole)
            else:
                logger.error("UserRole is not captured correctly in UI")

            UIComments = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[4]").text

            # DBComments =

            if UIComments==expectedCommentsdata:
                logger.info("Comments is captured correctly in UI"+UIComments)
            else:
                logger.error("Comments is not captured correctly in UI")


            UIActiontype = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[7]").text

            DBActionType = JDBC.returnOneValue("select sactiontype from auditaction where nauditcode=(select COUNT(*) from auditaction)")

            if UIActiontype==expectedActiontypedata:
                logger.info("Actiontype is captured correctly in UI"+UIActiontype)
            else:
                logger.error("Actiontype is not captured correctly in UI")

            if DBActionType==expectedActiontypedata:
                logger.info("Actiontype is captured correctly in DB"+DBActionType)
            else:
                logger.error("Actiontype is not captured correctly in DB")

            if DBActionType==UIActiontype:
                logger.info("Actiontype is same in DB and UI"+DBActionType+UIActiontype)
            else:
                logger.error("Actiontype is not same in DB and UI")





        # elif afterCount > beforeCount + 1:
        #     logger.info("Audit trail criteria 2 matched")
        #     for i in range(0, afterCount - beforeCount):
        #         auditactionlist = driver.find_elements(By.XPATH, "//tbody[@role='presentation']/tr/td[3]")
        #         print(auditactionlist[i].text)
        #         auditaction = auditactionlist[i].text
        #
        #         if auditaction == auditactiondata:
        #
        #             username = driver.find_element(By.XPATH,
        #                                            "//tbody[@role='presentation']/tr[{}]/td[5]".format(i + 2)).text
        #
        #             if username == usernamedata:
        #                 print("User Name matched")
        #                 print(username)
        #             else:
        #                 print("User Name is mismatched")
        #
        #             userrole = driver.find_element(By.XPATH,
        #                                            "//tbody[@role='presentation']/tr[{}]/td[6]".format(i + 2)).text
        #
        #             if userrole == userroledata:
        #                 print("User role matched")
        #                 print(userrole)
        #             else:
        #                 print("User role is mismatched")
        #
        #             comments = driver.find_element(By.XPATH,
        #                                            "//tbody[@role='presentation']/tr[{}]/td[4]".format(i + 2)).text
        #
        #             if comments == commentsdata:
        #                 print("comment matched")
        #                 print(comments)
        #             else:
        #                 print("comment is mismatched")
        #
        #             actiontype = driver.find_element(By.XPATH,
        #                                              "//tbody[@role='presentation']/tr[{}]/td[7]".format(i + 2)).text
        #
        #             if actiontype == actiontypedata:
        #                 print("actiontype matched")
        #                 print(actiontype)
        #             else:
        #                 print("actiontype is mismatched")

                # break

        elif afterCount == beforeCount:
            print("Audit trail has not recorded")


    except Exception as e:
        logger.error("Audit Trail failed")

