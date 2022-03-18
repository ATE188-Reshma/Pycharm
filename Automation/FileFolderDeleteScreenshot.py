import pyscreenshot
import PIL
from selenium import webdriver

# File Delete
# deletefile = "D:\\Resh JPDC\\Resh JPDC\\Bug List\\a\\Future Update.png"
# os.remove(deletefile)

# Folder Delete
# deletefolder = "D:\\Resh JPDC\\Resh JPDC\\Bug List\\a"
# os.rmdir(deletefolder)

# Screenshot
driver = webdriver.Chrome(executable_path="../Automation/chromedriver.exe")
driver.get("https://www.ajio.com/")
pyscreenshot.grab().save("D:\\Resh JPDC\\Resh JPDC\\Bug List\\a\\reshu.png")
