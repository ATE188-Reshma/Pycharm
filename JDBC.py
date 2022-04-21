import pypyodbc


def containerTypeCount():
    credential = "Driver={SQL Server};Server=AGD55\SQLSERVER2017;Database=CT-LIMS-FLUSHDB;UID=sa;PWD=admin@123"
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    query2 = "select COUNT(*) from containertype where nstatus=1 and ncontainertypecode <> -1"

    cursor.execute(query2)

    row2 = cursor.fetchone()

    value2 = row2[0]

    print(value2)

    return value2


def returnOneValue(query):

    credential = "Driver={SQL Server};Server=AGD55\SQLSERVER2017;Database=CT-LIMS-FLUSHDB;UID=sa;PWD=admin@123"
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    cursor.execute(query)

    row2 = cursor.fetchone()

    value2 = row2[0]

    return value2