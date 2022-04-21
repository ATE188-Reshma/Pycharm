import os
import shutil
folder='C:\\Users\\'+os.getlogin()+'\\AppData\\Local\\Temp\\'

list_of_file_and_folder=os.listdir(folder)
delete_file_count=0
delete_folder_count=0
access_denied_count=0
for i in list_of_file_and_folder:
    file_details=folder+i
    #print(file_details)
    try:
        if os.path.isfile(file_details):
            os.remove(file_details)
            print(file_details,"file deleted")
            delete_file_count+=1
        elif os.path.isdir(file_details):
            shutil.rmtree(file_details)
            print(file_details,"folder deleted")
            delete_folder_count+=1
    except Exception:
        print(file_details,"Access Denied")
        access_denied_count+=1
print(delete_file_count,"files and ",delete_folder_count,"folders are deleted",access_denied_count,"Access Denied")
input('Press <Enter> to exit')