import shutil
import time
import os




srcfilepath1 = "D:\\Agaram Files\\NIBSC\Build\\02-09-2021\\NIBSC build_2021_09_01\\QuaLISWeb"
srcfilepath2 = "D:\\Agaram Files\\NIBSC\\Build\\02-09-2021\\NIBSC build_2021_09_01\\QuaLIS.war"
targetpath1="C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0_Tomcat9_HPCL\\webapps\\QuaLISWeb"
targetpath2="C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0_Tomcat9_HPCL\\webapps"
targetpathforhib="C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0_Tomcat9_HPCL\\webapps\\QuaLIS\\WEB-INF\\"

try:

    shutil.copytree(srcfilepath1,targetpath1)
    shutil.copy(srcfilepath2, targetpath2)





except PermissionError:
    print("Permission denied.")

sqlserver=input("Enter the SQL server name: ")
DB=input("Enter the SQL DB name: ")
UN=input("Enter the SQL user name: ")
PSWD=input("Enter the SQL password name: ")

hib="""

# Application Properties
path.webinf=webapps/WEB-INF
# JDBC Connection information
jdbc.driverClassName = com.microsoft.sqlserver.jdbc.SQLServerDriver

jdbc.url =jdbc:sqlserver://"""+sqlserver+""";Database="""+DB+"""
jdbc.username ="""+ UN+"""
jdbc.password ="""+ PSWD+"""

hibernate.show_sql=true
hibernate.dialect=org.hibernate.dialect.SQLServerDialect
hibernate.transaction.factory_class=org.hibernate.transaction.JDBCTransactionFactory



"""

print(hib)
input("This is an reminder to start the services, press <Enter> to exit")
os.startfile("C:\\Users\\Karun\\Desktop\\kk.lnk")#start tom service
time.sleep(20)
os.remove("C:\Program Files\Apache Software Foundation\Tomcat 9.0_Tomcat9_HPCL\webapps\QuaLIS\WEB-INF\hibApplication.properties")
print("Old Hib file removed sucessfully")
time.sleep(3)
filepath='C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0_Tomcat9_HPCL\\webapps\\QuaLIS\WEB-INF\\hibApplication.properties'
open(filepath,'w')
filewrite1=open(filepath,'a').writelines(hib)
fileread2=open(filepath,'r')

os.startfile("C:\\Users\\Karun\\Desktop\\service_stop.bat.lnk")
time.sleep(40)
os.startfile("C:\\Users\\Karun\\Desktop\\kk.lnk")