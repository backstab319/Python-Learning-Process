# f = open("test.py","w")
# f.write("Hello world")
# f.close()

# f = open("test.py","w")
# list1 = ["hello\n","world\n","Good\n","morning\n"]
# f.writelines(list1)
# print("The lines have been written in test.py file.")
# f.close()

# f = open("test/test.txt","a")
# x = input("Please enter a string ")
# f.write(x)
# print("Data succesfully written!")
# f.close()

# f = open("test/test.text","a")
# list1 = []
# while True:
#     x = input().split("\n")
#     if x != "": list1.append(x)
#     else: False
# for i in x:
#     f.write(i+"\n")
# print("Text written succesfully!")
# f.close()

# f = open("test/test.text")
# data = f.readlines()
# print(data)
# f.close()

# f = open("test/test.text")
# print("Name of the file",f.name)
# print("Mode",f.mode)
# print("Closed",f.closed)
# print("Writable",f.writable())
# print("Readable",f.readable())
# f.close()

# Copying
# f1 = open("test/test.text")
# f2 = open("test/copy.text","w")
# f2.write(f1.read())
# f1.close()
# f2.close()