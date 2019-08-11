from os import system, name
class Pydata:
    tup1 = tup2 = tup3 = ()
    li1 = li2 = li3 = []
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
        message1 = "Tuple deleted successfully!"
        if var_no == "1":
            del self.tup1
        elif var_no == "2":
            del self.tup2
        else:
            self.tup3
        return message1

    def tupdel(self):
        message2 = "Tuple is already empty"
        self.clrscr()
        while True:
            inp = input("Select a tuple to delete its data\n1.tuple1\n2.tuple2\n3.tuple3\n4.Check data in tuple\n5.Go back to tuple operations\n")
            if inp == "1":
                print(message2 if self.tup1 == () else self.tup_delete("1"))
                self.pause()
                self.clrscr()
            elif inp == "2":
                print(message2 if self.tup2 == () else self.tup_delete("2"))
                self.pause()
                self.clrscr()
            elif inp == "3":
                print(message2 if self.tup3 == () else self.tup_delete("3"))
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
            val = input("List Operations\n1.Create\n2.Access\n3.Adding\n4.Replication\n5.Update\n6.Delete\n7.Index\n8.Count\n9.Pop\n10.Insert\n11.Extend\n12.Remove\n13.Reverse\n14.Sort\n15.Go back\n16.Exit\n")
            if val == "1":
                self.li_create("3")
            elif val == "2":
                self.li_access()
            elif val == "3":
                self.li_add()
            elif val == "4":
                self.li_rep()
            elif val == "5":
                self.li_update()
            elif val == "6":
                self.li_delete()
            elif val == "7":
                self.li_index()
            elif val == "8":
                self.li_count()
            elif val == "9":
                self.li_pop()
            elif val == "10":
                self.li_insert()
            elif val == "11":
                self.li_extend()
            elif val == "12":
                self.li_remove()
            elif val == "13":
                self.li_reverse()
            elif val == "14":
                self.li_sort()
            elif val == "15":
                self.main_screen()
            elif val == "16":
                exit()
            else:
                print("Incorrect Input!")

    def li_index(self):
        self.clrscr()
        print("Module under construction!")
        self.pause()

    def li_count(self):
        self.clrscr()
        print("Module under construction!")
        self.pause()

    def li_pop(self):
        self.clrscr()
        print("Module under construction!")
        self.pause()

    def li_insert(self):
        self.clrscr()
        print("Module under construction!")
        self.pause()

    def li_extend(self):
        self.clrscr()
        print("Module under construction!")
        self.pause()

    def li_remove(self):
        self.clrscr()
        print("Module under construction!")
        self.pause()

    def li_reverse(self):
        self.clrscr()
        print("Module under construction!")
        self.pause()

    def li_sort(self):
        self.clrscr()
        print("Module under construction!")
        self.pause()

    def li_creator(self):
        self.clrscr()
        li = []
        print("Enter values into the list")
        while True:
            inp = input()
            if inp.isspace():
                break
            if inp.endswith(" "):
                inp=inp.split()
                li += inp
                break
            li.append(inp)
        return li

    def li_create(self,li_no):
        self.clrscr()
        if li_no == "1" or li_no == "3":
            if self.li1 == []:
                self.li1 = self.li_creator()
            else:
                print("List already contains values")
        if li_no == "2" or li_no == "3":
            if self.li2 == []:
                self.li2 = self.li_creator()
            else:
                print("List already contains values")
        print("Lists created!")
        self.pause()

    def li_access(self):
        self.clrscr()
        list1 = self.li1 if self.li1 else "List 1 is empty"
        list2 = self.li2 if self.li2 else "List 2 is empty"
        print("The contents of list1 are\n",list1)
        print("The contents of list2 are\n",list2)
        self.pause()

    def li_add(self):
        self.clrscr()
        if (self.li1 and self.li2) == []:
            self.li_create("3")
            self.clrscr()
        self.li3 = self.li1 + self.li2
        print(self.li3)
        self.pause()

    def li_replicator(self,li_no,times):
        if li_no == "1":
            if self.li1 == []: self.li_create("1")
            return self.li1*int(times)
        elif li_no == "2":
            if self.li2 == []: self.li_create("2")
            return self.li1*int(times)

    def li_rep(self):
        self.clrscr()
        times = input("How many times to replicate the list ")
        while True:
            self.clrscr()
            x = input("Which list do you want to replicate?\n1.List1\n2.List2\n3.Back\n")
            if x == "1":
                print(self.li_replicator("1",times))
                break
            elif x == "2":
                print(self.li_replicator("2",times))
                break
            elif x == "3":
                self.list_screen()
                break
            else:
                print("Incorrect input!")
        self.pause()

    def li_update(self):
        while True:
            self.clrscr()
            x = input("Select the list updation method\n1.Whole list\n2.A part of the list\n3.Go back\n")
            if x == "1":
                self.li_update_selector(1)
            elif x == "2":
                self.li_update_selector(2)
            elif x == "3":
                self.list_screen()
            else:
                print("Invalid Input!")
        self.pause()

    def li_update_selector(self,status):
        while True:
            self.clrscr()
            x = input("Which list do you want to update?\n1.List 1\n2.List 2\n3.Go back\n")
            if x == "1" and status == 1:
                self.li_create("1")
            elif x == "1" and status == 2:
                self.li_update_part(1)
            elif x == "2" and status == 1:
                self.li_create("2")
            elif x == "2" and status == 2:
                self.li_update_part(2)
            elif x == "3":
                self.list_screen()
        self.pause()

    def li_update_part(self,li_no):
        self.clrscr()
        temp_list = self.li1 if li_no == 1 else self.li2
        for x,y in enumerate(temp_list):
            print(x,y)
        self.pause()

    def li_delete(self):
        self.clrscr()
        print("Module under construction!")
        self.pause()

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