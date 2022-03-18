import pypyodbc
import openpyxl

dbcredentials = "Driver={SQL Server};Server=AGD55\SQLSERVER2017;Database=JPDC;UID=sa;PWD=admin@123"
dbconnect = pypyodbc.connect(dbcredentials)
cursor = dbconnect.cursor()


selectquery = "select * from users"
select = cursor.execute(selectquery)
# to collect as table
result = cursor.fetchall()

path = "D:\\Resh JPDC\\Selenium_Python\\K_Notes\\DBfetching1.xlsx"
workbook = openpyxl.load_workbook(path)
worksheet = workbook["comparison"]

row = 1

for i in result:

    column = 1

    for j in i:

        sheet = worksheet.cell(row, column).value = j
        workbook.save(path)
        workbook.close()

        column += 1

    row += 1








