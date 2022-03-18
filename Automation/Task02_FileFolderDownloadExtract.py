import os
from selenium import webdriver
import time
import wget
from zipfile import ZipFile

# display all driver & selection
sysname = os.getlogin()

a = [chr(97+i).upper() for i in range(4)]

for j in (range(len(a))):  # range(len(a,b...z)) range could b as frst o,1,2... i.e a,b,c...
        driverformat = a[j] + ":/"  #a[0],a[1].....
        print(driverformat)
        drivercheck = os.path.exists(driverformat)

        if drivercheck == True:
            print("Drive Present in " + sysname, driverformat)
            ab = driverformat



# folder
if ab == "D:/":
    apath = "D:\\sample\\drivers"

    if not os.path.exists(apath):
        os.mkdir(apath)

        print("\nFolder created")

# download
downloadpath = "D:\sample\drivers"
wget.download("https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip", downloadpath)

#extract
zipfilepath = "D:\sample\drivers\chromedriver_win32.zip"
zip = ZipFile(zipfilepath)

ZipFile.extractall(zip, downloadpath)

#run browser
driver = webdriver.Chrome(executable_path="D:\sample\drivers\chromedriver.exe")
driver.get("http://localhost:8080/QuaLISWeb/")

time.sleep(10)

driver.close()












