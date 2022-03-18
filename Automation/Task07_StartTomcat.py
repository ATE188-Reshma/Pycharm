import os

Data = """# Application Properties
path.webinf=webapps/WEB-INF
# JDBC Connection information
jdbc.driverClassName = com.microsoft.sqlserver.jdbc.SQLServerDriver

jdbc.url =jdbc:sqlserver://AGD55\\SQLSERVER2017;Database=IRSHALIMSPROD_31Dec
jdbc.username = sa
jdbc.password = admin@123

hibernate.show_sql=true
hibernate.dialect=org.hibernate.dialect.SQLServerDialect
hibernate.transaction.factory_class=org.hibernate.transaction.JDBCTransactionFactory

"""

file = "C:\\Program Files\\Apache Software Foundation\\Tomcat 8.0\\webapps\\QuaLIS\\WEB-INF\\hibApplication.properties"
pathfile = os.path.isfile(file)

if pathfile==True:
    txt = open(file, "w")
    txt.writelines(Data)
    print("Tomcat started")

else:
    print("Error")


# To start the Tomcat. But, It won't support because it has no Access
# Put this "comment" in a batch file. Send it to Desktop and Change it access as "Run as Administrator" in properties
# os.system("net start Tomcat8")

# Now start the file on the Path. Tomcat would be started
os.startfile("C:\\Users\\ate142\\Desktop\\servicefile - Shortcut.lnk")


