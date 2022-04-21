import pypyodbc

# DB won't do anything in d actual DB. It just takes the copy and perform d actions
dbcredentials="Driver={SQL Server};Server=AGD55\SQLSERVER2017;Database=IRSHALIMSPROD_31Dec;UID=sa;PWD=admin@123"

# Connect to DB
dbconnect = pypyodbc.connect(dbcredentials)

# Make d cursor ready
cursor = dbconnect.cursor()

# Required Script
updatequery = "update users set smobileno='1234567890'"
update = cursor.execute(updatequery)
# to perform actions in actual db
dbconnect.commit()
selectquery = "select * from users"
select = cursor.execute(selectquery)
print(select)

for i in select:
    print(i)
