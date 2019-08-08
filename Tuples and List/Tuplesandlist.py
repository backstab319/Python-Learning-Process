from os import system,name
def welcome_screen():
    val = input("Please select a choise of tuple examples: ")
    system("cls")
    if(val == 1):
        tupcreate()
    elif(val == 2):
        tupadd()
    elif(val == 3):
        tuprep()
    elif(val == 4):
        tupdel()
    else:
        exit()
def tupcreate():
    print("Creating tuple 1")
    tup1 = ["sid",120,"Good"]
    print(tup1)
    print("Creating tuple 2")
    tup2 = ["dev",100,"Good"]
    print(tup2)
def tupadd():
    tup1 = ["sid",120,"Good"]
    tup2 = ["dev",100,"Good"]
    print("Adding tuple 1 and tuple 2")
    tup3 = tup1 + tup2
    print(tup3)
def tupdel():
    tup1 = ["sid",120,"Good"]
    tup2 = ["dev",100,"Good"]
    print("Adding tuple 1 and tuple 2")
    tup3 = tup1 + tup2
    print("Deleting 3rd tuple")
    del tup3
    print(tup3)
def tuprep():
    print("Replication of tuple")
    print(tup1*2)