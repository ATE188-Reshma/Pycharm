import os
from cryptography.fernet import Fernet
import pypyodbc
from selenium import webdriver
import time
import pyscreenshot
import shutil
from datetime import datetime
import wget
from zipfile import ZipFile

# display all driver & selection

from selenium.webdriver.common.by import By

sysname = os.getlogin()

a = [chr(97+i).upper() for i in range(4)]

for j in (range(len(a))):  # range(len(a,b...z)) range could b as frst o,1,2... i.e a,b,c...
        driverformat = a[j] + ":/"  #a[0],a[1].....
        print(driverformat)
        drivercheck = os.path.exists(driverformat)

        if drivercheck == True:
            print("Drive Present in " + sysname, driverformat)
            ab = driverformat

# folder creation

if ab == "D:/":
    apath = "D:\\sample\\drivers"

    if not os.path.exists(apath):
        os.mkdir(apath)

        print("\nFolder created")

# download

downloadpath = "D:\sample\drivers"
wget.download("https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip", downloadpath)

print("Chromedriver downloaded")

#extract

zipfilepath = "D:\sample\drivers\chromedriver_win32.zip"
zip = ZipFile(zipfilepath)

ZipFile.extractall(zip, downloadpath)

print("Extracted successfully")

#run browser

inputtime = input("Enter Date & Time: ")

driver = webdriver.Chrome(executable_path="D:\sample\drivers\chromedriver.exe")
driver.get("http://localhost:8080/QuaLISWeb/")

time.sleep(3)

driver.maximize_window()

login = driver.find_element(By.XPATH, "//input[@id='idEmail']")
login.send_keys("IT")

password = driver.find_element(By.XPATH, "//input[@id='idpassword']")
password.send_keys("123")

icon = driver.find_element(By.XPATH, "//input[@id='idLogin']")
icon.click()

time.sleep(5)

master = driver.find_element(By.ID, "MainMenu_1")
master.click()
basemaster = driver.find_element(By.XPATH, "//a[@id='iModuleID_1']")
basemaster.click()

# Click on Gvn tym

k = 1
while k > 0:
    sysdatetime = datetime.today() #collect today time
    print(sysdatetime)
    dateconversion = sysdatetime.strftime("%d/%m/%Y %H:%M:%S") #changing d collected time to req format
    print(inputtime)
    print(dateconversion)

    if inputtime == dateconversion:
        unitsofmeasurement = driver.find_element(By.XPATH, "//a[@id='iFormID_33']")
        unitsofmeasurement.click()
        break

time.sleep(5)

pyscreenshot.grab().save("D:\\Resh JPDC\\Resh JPDC\\Bug List\\a\\reshu.png")

driver.close()

# copy and paste

src = ("D:\Resh JPDC\Resh JPDC\Bug List\TestData.txt")
dstntn = ("D:\\Resh JPDC\\Resh JPDC\\Bug List\\a")

time.sleep(5)

shutil.copy(src, dstntn)

print("\nCopy Paste Done")

# FileWrite

filepath="D:\\sample\\tst.txt"
result=os.path.isfile(filepath)
if result==True:
    print("Exist")
else:
    txt=open(filepath,"w")
    s = ('Reshma is sweet\nShe is kind and Good')
    txt.writelines(s)
    print("\nFile Created and Written")


# File Delete

deletefile = "D:\\Resh JPDC\\Resh JPDC\\Bug List\\a\\TestData.txt"
os.remove(deletefile)

print("\nFile Deleted\n")

# DB Connectivity
dbcredentials="Driver={SQL Server};Server=AGD55\SQLSERVER2017;Database=IRSHALIMSPROD_31Dec;UID=sa;PWD=admin@123"


dbconnect = pypyodbc.connect(dbcredentials)


cursor = dbconnect.cursor()


updatequery = "update users set smobileno='1234567890' where nusercode = 3 "
update = cursor.execute(updatequery)

selectquery = "select * from users where nusercode = 3"
select = cursor.execute(selectquery)
print(select)

for i in select:
    print(i)

# Encryption
content = "Reshma"

keys = Fernet.generate_key()
print(keys)

contentencode = content.encode()
print(contentencode)

encrypt = Fernet(keys).encrypt(contentencode)
print(encrypt)

















