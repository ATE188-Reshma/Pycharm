
from configparser import ConfigParser

config = ConfigParser()

# Specify the ini file path below
config.read("C:\\Users\\ate142\\PycharmProjects\\pythonProject1\\Automation\\Property_File.ini")

print(config.get("login credentials", "un"))
