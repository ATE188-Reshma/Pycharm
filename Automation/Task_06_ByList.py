import pypyodbc
import openpyxl

dbcredentials = "Driver={SQL Server};Server=AGD55\SQLSERVER2017;Database=IRSHALIMSPROD_31Dec;UID=sa;PWD=admin@123"
dbconnect = pypyodbc.connect(dbcredentials)
cursor = dbconnect.cursor()

selectquery = "select sfirstname from users"
select = cursor.execute(selectquery)
print(select)

path = "D:\\Resh JPDC\\Selenium_Python\\K_Notes\\DBfetching1.xlsx"
workbook = openpyxl.load_workbook(path)
worksheet = workbook["comparison"]

# Collect all the data and store as list
kk=[i for i in select]
print(kk)
print(len(kk))
count=len(kk)
row = 1
column = 1
# Save total count in variable
for j in range(count):
    # Get the values as index
    jj=kk[j]
    print(jj)
    # Convert data to String
    hh = str(jj)
    print(hh)
    worksheet.cell(row, column).value = hh
    row+=1
    workbook.save(path)
    workbook.close()












