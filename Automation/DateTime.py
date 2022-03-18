from datetime import datetime
currentsysdatetime=datetime.today()
print(currentsysdatetime)
usrsysdatetime=currentsysdatetime.strftime("%d/%m/%Y %H:%M:%S")
print(usrsysdatetime)





ouratetime=input("Enter the date & Time: ")
sysdatetime=datetime.strptime(ouratetime,"%d/%m/%Y %H:%M:%S")
print(sysdatetime)