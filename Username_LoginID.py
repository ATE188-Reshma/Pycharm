import pypyodbc

databasecredentials="Driver={SQL Server};Server=AGD55\SQLSERVER2017;Database=IRSHALIMSPROD_31Dec;UID=sa;PWD=admin@123"
conn = pypyodbc.connect(databasecredentials)
print(conn)
cursor1 = conn.cursor()
selectscript="select sfirstname,slastname from users where sloginid='R1' "
script2=cursor1.execute(selectscript)

for i in script2:
    print(i)
    kk=[j for j in i]
    print(kk)

    un=kk[0]+" "+kk[1]
    print("User name is", un)
