from zipfile import ZipFile

# zipfile to be created
zipfilepath='D:\\sample\\Excel\\test.zip'

# existing files to be written inside the above created zip file
zip=ZipFile(zipfilepath,'w')
zip.write("D:\sample\Excel\kk.xlsx")
zip.write("D:\sample\Excel\kk1.xlsx")

# read d zipfile in the zipfile path
zip=ZipFile(zipfilepath,'r')

# again zip d file
zip1=ZipFile(zipfilepath)

# extract
zip1.extractall('D:\\sample\\Excel\\test')



