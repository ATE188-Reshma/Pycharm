import os
sysname=os.getlogin()

alphabets=[chr(97+i).upper() for i in range(26)]  # range starts from zero. Here 0 to 25, Alphabets were collected as list here.
print(alphabets)
print(len(alphabets))  # length starts from one

for j in (range(len(alphabets))):  # range(len(a,b...z)) range could b as frst o,1,2... i.e a,b,c...
    driverformat=alphabets[j]+":/"  #dbt
    print(driverformat)
    drivercheck=os.path.exists(driverformat)

    if drivercheck==True:
        print("Drive Present in " + sysname, driverformat)
        finalselecteddrive=driverformat
print("Final Selected drive "+finalselecteddrive)
