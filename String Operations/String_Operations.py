from os import system,name
def welcome_screen():
    print("Welcome! Please select the below options to perform a string operations\n1.Capitalize\n2.Count\n3.Endswith\n4.Starts_with\n5.Find\n6.Isalnum\n7.Isdigit\n8.Isalpha\n9.Islower\n10.Isupper")
    print("11.Isspace\n12.Swapcase\n13.Split")
    val = input()
    system("cls")
    if (val == "1"):
        cap()
    elif (val == "2"):
        count()
    elif (val == "3"):
        ends_with()
    elif (val == "4"):
        starts_with()
    elif (val== "5"):
        find_string()
    elif (val =="6"):
        isal_num()
    elif (val == "7"):
        is_digit()
    elif (val == "8"):
        is_alpha()
    elif (val == "9"):
        is_lower()
    elif (val == "10"):
        is_upper()
    elif (val == "11"):
        is_space()
    elif (val == "12"):
        swap_case()
    elif (val =="13"):
        split_str()
    else:
        exit()

def split_str():
    str = input("Enter a set of strings ")
    split_str = input("Enter the splitting condition ")
    if(split_str == None):
        split_str = ' '
    print(str.split(split_str))

def swap_case():
    str = input("Enter a set of strings ")
    print(str.swapcase())

def is_space():
    str = input("Enter a set of strings ")
    print(str.isspace())

def is_upper():
    str = input("Enter a set of strings ")
    print(str.isupper())

def is_lower():
    str = input("Enter a set of strings ")
    print(str.islower())

def is_alpha():
    str = input("Enter a set of strings ")
    print(str.isalpha())

def is_digit():
    str = input("Enter a set of strings ")
    print(str.isdigit())

def isal_num():
    str = input("Enter a set of strings ")
    print(str.isalnum())

def find_string():
    str = input("Enter a set of strings ")
    find_str = input("Enter the string to be found ")
    print(str.find(find_str))

def cap():
    print("Perform Capitalize Operation on a string")
    val = input("Please input a string to capitalize ")
    print(val.capitalize())

def count():
    str = input("Enter a set of strings ")
    count_str = input("Enter the string to count ")
    result = str.count(count_str)
    print(result)

def ends_with():
    str = input("Enter a set of strings ")
    end_str = input("Enter ending string ")
    print(str.endswith(end_str))

def starts_with():
    str = input("Enter a set of strings ")
    start_str = input("Enter starting string")
    print(str.startswith(start_str))

welcome_screen()