import openpyxl
import pypyodbc

credential="Driver={SQL Server};Server=AGD55\SQLSERVER2017;Database=JPDC;UID=sa;PWD=admin@123"
dbconnect=pypyodbc.connect(credential)
cursor=dbconnect.cursor()

query = cursor.execute("Select * from users")
result = cursor.fetchall()

path = "D:\\Resh JPDC\\Selenium_Python\\K_Notes\\DBfetching1.xlsx"
workbook = openpyxl.load_workbook(path)
worksheet = workbook["comparison"]

row=column=1

# collecting as List
kk = [i for i in result]
print(len(kk))

for j in range(len(kk)):
    # converting as Index
    print(kk[j])
    # converting to String
    sc = str(kk[j])
    # Split the values using the seperator
    s1 = sc.split(",")

    for k in range(len(s1)):
        # Remove d space
        print(s1[k].strip())
        s2 = str(s1[k])
        sheet = worksheet.cell(row, column).value = s2
        column += 1
        s3 = s2.strip()
        # to get index value
        v1 = s3.find(')')
        print("find value",v1)
        if v1 == 1 or v1 ==2:
            print(") is present")
            row += 1
            column = 1
        workbook.save(path)
        workbook.close()
