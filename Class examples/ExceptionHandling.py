import sys
import os
a = 5
b = "0"
l = [1,2,3,4,5]
c = 5
d = 0
# try:
#     print(a+b)
# except TypeError:
#     print("Type Error occured!")

# try: print(l[7])
# except IndexError: print("Index error occured!")

# try: print "Hello world!"
# except SyntaxError: print(sys.exc_info())

# try: print(c/d)
# except ZeroDivisionError: print("Zero division error occured!")


# os.system("clear")
# try: f = open("myfile.txt")
# except FileNotFoundError:
#     print("The file does not exist!")
#     f = open("myfile.txt","w")
#     f.close()
# else:
#     print("The file exists!")
#     os.remove("myfile.txt")


# try:
#     print(a+b)
#     print(l[7])
#     print(c/d)
# except TypeError:
#     print("Type error occured!")
# except IndexError:
#     print("Index out of range!")
# except ZeroDivisionError:
#     print("Zero division error!")