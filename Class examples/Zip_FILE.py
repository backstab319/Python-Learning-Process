from zipfile import *
# f = ZipFile("myfile1.zip","w",ZIP_DEFLATED)
# f.write("student.csv")
# f.close()

# # Reading a zipfile

# with ZipFile("myfile.zip","r") as zipObj:
#     zipObj.extractall("temp")

# The content of all the files in the zip file

f = ZipFile("myfile.zip","r",ZIP_STORED)
names = f.namelist()
for name in names:
    print(name)
    print("The content of the file is ")
    f1 = open(name,"r")
    print(f1.read())