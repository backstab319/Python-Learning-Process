import csv
# Writing into a file
with open("student.csv","w",newline="") as f:
    a = csv.writer(f)
    a.writerow(["NAME","ID","MARKS","ADDRESS"])
    while True:
        name = input("Enter student name ")
        id = int(input("Enter student id "))
        marks = int(input("Enter student marks "))
        addr = input("Enter student address ")
        a.writerow([name,id,marks,addr])
        option = input("Do you want to insert one more record? Y/N ")
        if option.lower()=="N":
            break
print("Students data are inserted to csv file successfully!")

# Reading

q = input("Do you want to read from the file? Y/N ")
if q == "Y": csvReader()
def csvReader():
    with open("student.csv","r") as f:
        a = csv.reader(f)
        data = list(a)
        for i in data:
            print(i[0],i[1],i[2],sep="\t\t")

# R+
q = input("Do you want to read and write the file? Y/N ")
if q == "Y":
    csvReaderWriter()
def csvReaderWriter():
    with open("student.csv","r+") as f:
        r = csv.reader(f)
        w = csv.writer(f)
        data = list(r)
        for row in data:
            if row[0] == "siddharth":
                w.writerow([row[0],100,row[2],row[3]])