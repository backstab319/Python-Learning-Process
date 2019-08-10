from os import system, name
class Pydata:
    tup1 = tup2 = tup3 = ()
    code = int
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
            val = input("Tuple Operations\n1.Create\n2.Add\n3.Replicate\n4.Delete\n5.To go back to main menu\nAny other key to exit\n")
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
        print("Enter elements into the tuple:")
        while True:
            inp = input()
            if inp.isspace():
                break
            if inp.endswith(" "):
                inp=inp.split()
                li += inp
                break
            li.append(inp)
        return tuple(li)

    def tupadd(self):
        self.clrscr()
        if (self.tup1 or self.tup2) == ():
            print("No previously created tuples. So making new tuples.\nCreating tuple 1")
            self.tup1 = self.tuple_creator()
            print("Creating tuple 2")
            self.tup2 = self.tuple_creator()
        self.tup3 = self.tup1 + self.tup2
        print("Adding tuple 1 and tuple 2")
        print(self.tup3)
        self.pause()

    def tup_show(self):
        self.clrscr()
        while True:
            inp = input("Check tuples contain data or not\n1.tuple1\n2.tuple2\n3.tuple3\n4.Go back to deleting tuple\n")
            if inp == "1":
                print(self.tup_data(self.tup1))
                self.pause()
                self.clrscr()
            elif inp == "2":
                print(self.tup_data(self.tup2))
                self.pause()
                self.clrscr()
            elif inp == "3":
                print(self.tup_data(self.tup3))
                self.pause()
                self.clrscr()
            elif inp == "4":
                self.tupdel()
            else:
                print("Wrong choice!")
        self.pause()

    def tup_data(self,data):
        if data == ():
            self.code = 0
            return "Tuple is empty!"
        else:
            self.code = 1
            return "Tuple contains data!"

    def tup_delete(self,var_no):
        if var_no == "1":
            self.tup_data(self.tup1)
        elif var_no == "2":
            self.tup_data(self.tup2)
        else:
            self.tup_data(self.tup3)
        if self.code == 0:
            print("Tuple"+str(var_no)+" deleted!")
        else:
            print("Tuple"+str(var_no)+" was already deleted!")

    def tupdel(self):
        self.clrscr()
        while True:
            inp = input("Select a tuple to delete its data\n1.tuple1\n2.tuple2\n3.tuple3\n4.Check data in tuple\n5.Go back to tuple operations\n")
            if inp == "1":
                print(self.tup_delete(1))
                self.pause()
                self.clrscr()
            elif inp == "2":
                print(self.tup_delete(2))
                self.pause()
                self.clrscr()
            elif inp == "3":
                print(self.tup_delete(3))
                self.pause()
                self.clrscr()
            elif inp == "4":
                self.tup_show()
            elif inp == "5":
                self.tuple_screen()
            else:
                print("Invalid Input!")
        self.pause()

    def times(self):
        times = int(input("How many times do you want to replicate the tuple?\n"))
        return times

    def tuprep(self):
        self.clrscr()
        print("Replication of tuple")
        inp = input("Which tuple do you want to replicate?\n1.tuple1\n2.tuple2\n3.tuple3\n")
        if(inp == "1"):
            times = self.times()
            if(self.tup1 == ()):
                print("Tuple 1 is empty. Creating Tuple 1")
                self.tup1 = self.tuple_creator()
                print(self.tup1*times)
            else:
                print(self.tup1*times)
        elif inp == "2":
            times = self.times()
            if self.tup2 == ():
                print("Tuple 2 is empty. Creating Tuple 2")
                self.tup2 = self.tup2*times
                print(self.tup2*times)
            else:
                print(self.tup2*times)
        elif inp == "3":
            times = self.times()
            if self.tup3 == ():
                print("Tuple 3 is empty. Creating Tuple 3")
                self.tup3 = self.tup3*times
                print(self.tup3*times)
            else:
                print(self.tup3*times)
        else:
            print("Incorrect choice!")
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