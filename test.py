import pypyodbc

# DB won't do anything in d actual DB. It just takes the copy and perform d actions
dbcredentials="Driver={SQL Server};Server=AGD55\SQLSERVER2017;Database=master;Trusted_Connection=yes;UID=sa;PWD=admin@123"

# Connect to DB
dbconnect = pypyodbc.connect(dbcredentials)

# Make d cursor ready
cursor = dbconnect.cursor()


updatequery = "select @@version"
update = cursor.execute(updatequery)



for i in update:
    print(i)
