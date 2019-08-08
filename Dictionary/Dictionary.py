from os import system
system("cls")
def startscr():
    a = {'name':'xyz','Id':20}
    while 1:
        val = input("Select an operations to perform on dictionary \n1.create\n2.access\n3.update\n4.del\n5.len\n6.keys\n7.values\n8.item\n0.Exit\n")
        system("cls")
        if (val == "1"):
            dict_create(a)
        elif (val == "2"):
            dict_access(a)
        elif (val == "3"):
            dict_update(a)
        elif (val == "4"):
            dict_del(a)
        elif (val == "5"):
            dict_len(a)
        elif (val == "6"):
            dict_keys(a)
        elif (val == "7"):
            dict_values(a)
        elif (val == "8"):
            dict_items(a)
        else:
            exit()
def dict_create(a):
    print("Creating a dictionary")
    print(a)
    input()
def dict_access(a):
    print("Accessing a dictionary")
    print(a['Id'])
    input()
def dict_update(a):
    a = {'name':'xyz','Id':20}
    print("Updating a dictionary")
    a["name"] = "sid"
    print(a)
    input()
def dict_del(a):
    print("Deleting a dictionary")
    a = {'name':'xyz','Id':20}
    del a
    print(a)
    input()
def dict_len(a):
    a = {'name':'xyz','Id':20}
    print(len(a))
def dict_keys(a):
    print(a.keys())
def dict_values(a):
    print(a.values())
def dict_items(a):
    print(a.items())
startscr()