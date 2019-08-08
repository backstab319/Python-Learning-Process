from os import system, name
class Pydata:
    tup1 = tup2 = tup3 = ()
    def clrscr(self):
        if(name == "nt"):
            system("cls")
        else:
            system("clear")
    
    def pause(self):
        input("\nPress any key to continue..\n")

    def main_screen(self):
        while True:
            self.clrscr()
            val = input("Welcome to python! Please select the data type that you want to learn. \n1.Strings\n2.Tuples\n3.Lists\n4.Dictionary\nOr any other key to exit.\n")
            if val == "1":
                self.string_screen()
            elif val == "2":
                self.tuple_screen()
            elif val == "3":
                self.list_screen()
            elif val == "4":
                self.dict_screen()
            else:
                exit()

    def string_screen(self):
        while True:
            self.clrscr()
            val = input("String Operations\n1.Capitalize\n2.Count\n3.Endswith\n4.Starts_with\n5.Find\n6.Isalnum\n7.Isdigit\n8.Isalpha\n9.Islower\n10.Isupper\n11.Isspace\n12.Swapcase\n13.Split\n14.Main menu\nAny other key to exit\n")
            if (val == "1"):
                self.cap()
            elif (val == "2"):
                self.count()
            elif (val == "3"):
                self.ends_with()
            elif (val == "4"):
                self.starts_with()
            elif (val== "5"):
                self.find_string()
            elif (val =="6"):
                self.isal_num()
            elif (val == "7"):
                self.is_digit()
            elif (val == "8"):
                self.is_alpha()
            elif (val == "9"):
                self.is_lower()
            elif (val == "10"):
                self.is_upper()
            elif (val == "11"):
                self.is_space()
            elif (val == "12"):
                self.swap_case()
            elif (val =="13"):
                self.split_str()
            elif val == "14":
                self.main_screen()
            else:
                exit()

    def split_str(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        split_str = input("Enter the splitting condition ")
        if(split_str == None):
            split_str = ' '
            print(str.split(split_str))
        self.pause()

    def swap_case(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        print(str.swapcase())
        self.pause()

    def is_space(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        print(str.isspace())
        self.pause()

    def is_upper(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        print(str.isupper())
        self.pause()

    def is_lower(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        print(str.islower())
        self.pause()

    def is_alpha(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        print(str.isalpha())
        self.pause()

    def is_digit(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        print(str.isdigit())
        self.pause()

    def isal_num(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        print(str.isalnum())
        self.pause()

    def find_string(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        find_str = input("Enter the string to be found ")
        print(str.find(find_str))
        self.pause()

    def cap(self):
        self.clrscr()
        print("Perform Capitalize Operation on a string")
        val = input("Please input a string to capitalize ")
        print(val.capitalize())
        self.pause()

    def count(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        count_str = input("Enter the string to count ")
        result = str.count(count_str)
        print(result)
        self.pause()

    def ends_with(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        end_str = input("Enter ending string ")
        print(str.endswith(end_str))
        self.pause()

    def starts_with(self):
        self.clrscr()
        str = input("Enter a set of strings ")
        start_str = input("Enter starting string")
        print(str.startswith(start_str))
        self.pause()

    def tuple_screen(self):
        while True:
            self.clrscr()
            val = input("Tuple Operations\n1.Create\n2.Add\n3.Replicate\n4Delete\n5.To go back to main menu\nAny other key to exit\n")
            if(val == "1"):
                self.tupcreate()
            elif(val == "2"):
                self.tupadd()
            elif(val == "3"):
                self.tuprep()
            elif(val == "4"):
                self.tupdel()
            elif val == "5":
                self.main_screen()
            else:
                exit()
    
    def tupcreate(self):
        self.clrscr()
        print("Creating tuple 1")
        self.tup1 = self.tuple_creator()
        print(self.tup1)
        print("Creating tuple 2")
        self.tup2 = self.tuple_creator()
        print(self.tup2)
        self.pause()

    def tuple_creator(self):
        li = []
        while True:
            inp = input("Enter elements into the tuple:\n")
            if inp.ends_with == " ":
                break
            li+=inp
        return li

    def tupadd(self):
        self.clrscr()
        tup1 = ["sid",120,"Good"]
        tup2 = ["dev",100,"Good"]
        print("Adding tuple 1 and tuple 2")
        tup3 = tup1 + tup2
        print(tup3)
        self.pause()

    def tupdel(self):
        self.clrscr()
        tup1 = ["sid",120,"Good"]
        tup2 = ["dev",100,"Good"]
        print("Adding tuple 1 and tuple 2")
        tup3 = tup1 + tup2
        print("Deleting 3rd tuple")
        del tup3
        print(tup3)
        self.pause()

    def tuprep(self):
        self.clrscr()
        print("Replication of tuple")
        
        self.pause()

    def list_screen(self):
        while True:
            self.clrscr()
            val = input("List Operations\n1.Perform list operations\n2.To go back to main menu\nAny other key to exit\n")
            if val == "1":
                print("Performed list operations!")
            elif val == "2":
                self.main_screen()
            else:
                exit()

    def dict_screen(self):
        while True:
            self.clrscr()
            val = input("Dictionary Operations\n1.Perform dictionary operations\n2.To go back to main menu\nAny other key to exit\n")
            if val == "1":
                print("Performed dictionary operations!")
            elif val == "2":
                self.main_screen()
            else:
                exit()

curse = Pydata()
curse.main_screen()