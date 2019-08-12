from os import system, name
class Pydata:
    tup1 = tup2 = tup3 = ()
    li1 = li2 = li3 = []
    code = int

    def future_enhancements(self):
        self.clrscr()
        print("Future update contains lists and its functions")
        self.pause()

    def version_status(self):
        return "Version 1.0"

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
            print(self.version_status())
            val = input("Welcome to python! Please select the data type that you want to learn. \n1.Strings\n2.Tuples\n3.Lists\n4.Dictionary\n0.Future enhancements\nOr any other key to exit.\n")
            if val == "1":
                self.string_screen()
            elif val == "2":
                self.tuple_screen()
            elif val == "3":
                self.list_screen()
            elif val == "4":
                self.dict_screen()
            elif val == "0":
                self.future_enhancements()
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
            val = input("Tuple Operations\n1.Create\n2.Add\n3.Replicate\n4.Delete\n5.Max\n6.Min\n7.Len\n8.To go back to main menu\nAny other key to exit\n")
            if(val == "1"):
                self.tupcreate()
            elif(val == "2"):
                self.tupadd()
            elif(val == "3"):
                self.tuprep()
            elif(val == "4"):
                self.tupdel()
            elif val == "5":
                self.tup_max_min("max")
            elif val == "6":
                self.tup_max_min("min")
            elif val == "7":
                self.tup_len()
            elif val == "8":
                self.main_screen()
            else:
                exit()

    def tup_create_prompt(self,tup_no):
        if tup_no == "1":
            if self.tup1 == ():
                self.tup1 = self.tuple_creator()
        elif tup_no == "2":
            if self.tup2 == ():
                self.tup2 = self.tuple_creator()
        elif tup_no == "3":
            if self.tup1 == ():
                self.tup1 = self.tuple_creator()
            if self.tup2 == ():
                self.tup2 = self.tuple_creator()
        else:
            print("Fatal Error!")

    def tup_max_min(self,op):
        self.clrscr()
        self.tup_create_prompt("1")
        val = "The maximum value in the tuple is "+max(self.tup1) if op == "max" else "The minimum value in the tuple is "+min(self.tup1)
        print(val)
        self.tup_create_prompt("2")
        val = "The maximum value in the tuple is "+max(self.tup2) if op == "max" else "The minimum value in the tuple is "+min(self.tup2)
        print(val)
        self.pause()

    def tup_len(self):
        self.clrscr()
        self.tup_create_prompt("3")
        print(len(self.tup1))
        print(len(self.tup2))
        self.pause()

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
                self.li_sort(1)
            elif val == "14":
                self.li_sort(0)
            elif val == "15":
                self.main_screen()
            elif val == "16":
                exit()
            else:
                print("Incorrect Input!")

    def li_index(self):
        self.clrscr()
        var = self.li_conditional_creator()
        val = input("Enter the data for which index need to be found\n")
        res = self.li_index_addr(var,val)
        if res != "error": print("The data is at index ",res)
        else: print("The data is not present")
        self.pause()

    def li_index_addr(self,op_list,val):
        addr = op_list.index(val) if (val in op_list) else "error"
        return addr

    def li_conditional_creator(self):
        for var in self.li1, self.li2, self.li3:
            if var: break
            else:
                self.li_create("1")
                self.clrscr()
                var = self.li1
                break
        return var

    def li_count(self):
        self.clrscr()
        var = self.li_conditional_creator()
        val = input("Enter the data to count in list\n")
        print("The given data occurs",var.count(val),"times in the list")
        self.pause()

    def li_pop(self):
        self.clrscr()
        op_list = self.li_conditional_creator()
        while True:
            for x,y in enumerate(op_list):
                print(str(x)+"."+y)
            inp = int(input("Please select the index of an element to pop it\n"))
            if inp > x:
                print("Out of index")
            else:
                self.li_check_delete(x+1,inp)
                break
        self.pause()

    def li_check_delete(self,x,inp):
        print("Deleted element",self.li1.pop(inp) if x == len(self.li1) else self.li2.pop(inp))

    def li_insert(self):
        self.clrscr()
        op_list = self.li_conditional_creator()
        while True:
            for x,y in enumerate(op_list):
                print(str(x)+"."+y)
            inp1 = input("Enter the element to insert\n")
            inp = int(input("Enter the index to insert the element at\n"))
            if inp > x: print("Out of index")
            else:
                print(self.li1.insert(inp,inp1) if x+1 == len(self.li1) else self.li2.insert(inp1,inp1))
                break
        self.pause()

    def li_extend(self):
        self.clrscr()
        if self.li1 == []: self.li_create("1")
        if self.li2 == []: self.li_create("2")
        local_li1 = self.li1
        local_li2 = self.li2
        self.li1.extend(local_li2)
        self.li2.extend(local_li1)
        print("Extending list 1 with list 2\n"+str(self.li1))
        print("Extending list 2 with list 1\n"+str(self.li2))
        self.pause()

    def li_remove(self):
        self.clrscr()
        while True:
            self.clrscr()
            print("1.List 1\n2.List 2\n3.Go back")
            list_no = input("Select a list\n")
            if list_no == "1":
                if self.li1 == []: self.li_create("1")
                self.li_remover(1)
            elif list_no == "2":
                if self.li2 == []: self.li_create("2")
                self.li_remover(2)
            elif list_no == "3":
                self.list_screen()
            else:
                print("Invalid Input!")
                self.pause()
        self.pause()

    def li_remover(self,list_no):
        if list_no == 1: op_list = self.li1
        if list_no == 2: op_list = self.li2
        while True:
            self.clrscr()
            for x,y in enumerate(op_list):
                print(y)
            print(str(x+1)+".Go back")
            inp = input("Enter the element to remove\n")
            if inp == str(x+1): self.list_screen()
            if inp not in op_list:
                print("Element not in the list")
                self.pause()
            else:
                if list_no == 1: self.li1.remove(inp)
                if list_no == 2: self.li2.remove(inp)
        print(self.li1 if list_no == 1 else self.li2)

    def li_sort(self,rev):
        while True:
            self.clrscr()
            x = input("Select the list to sort\n1.List 1\n2.List 2\n3.List 3\n4.Go back\n")
            if x == "1":
                if self.li1 == []: self.li_create("1")
                if rev == 1:
                    self.li1.sort(reverse=True)
                    print(self.li1)
                else:
                    self.li1.sort()
                    print(self.li1)
                break
            elif x == "2":
                if self.li2 == []: self.li_create("2")
                if rev == 1:
                    self.li2.sort(reverse=True)
                    print(self.li2)
                else:
                    self.li2.sort()
                    print(self.li2)
                break
            elif x == "3":
                if self.li3 == []: self.li_create("3")
                self.li_add()
                if rev == 1:
                    self.li3.sort(reverse=True)
                    print(self.li3)
                else:
                    self.li3.sort()
                    print(self.li3)
                break
            elif x == "4":
                self.list_screen()
            else:
                print("Invalid Input!")
        self.pause()

    def li_creator(self):
        self.clrscr()
        li = []
        print("Enter values into the list")
        while True:
            x = input()
            if x.endswith("  "):
                x = x.split()
                for i in x:
                    if i.isdigit(): i=int(i)
                    li.append(i)
            break
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
        if li_no == 1 and self.li1 == []: self.li_create("1")
        if li_no == 2 and self.li2 == []: self.li_create("2")
        temp_list = self.li1 if li_no == 1 else self.li2
        while True:
            self.clrscr()
            for x,y in enumerate(temp_list):
                z1, z2 = x, y
                print(str(z1)+"."+str(z2))
            inp = input("Select the index to update\n")
            if int(inp) > z1:
                print("Selected index out of bound!")
                self.pause()
            else:
                inp_1 = input("Please enter the value to be updated to\n")
                print("List Updated!")
                break
        temp_list[int(inp)] = inp_1
        if li_no == 1: self.li1 = temp_list
        else: self.li2 = temp_list
        self.pause()

    def li_deleter(self,li_no):
        li1_stat = "not" if li_no == 1 and self.li1 else "empty"
        li2_stat = "not" if li_no == 2 and self.li2 else "empty"
        li3_stat = "not" if li_no == 3 and self.li3 else "empty"
        if li_no == 1 and li1_stat == "not": del self.li1
        elif li_no == 1 and li1_stat == "empty": return "List1 already empty!"
        elif li_no == 2 and li2_stat == "not": del self.li2
        elif li_no == 2 and li2_stat == "empty": return "List2 already empty!"
        elif li_no == 3 and li3_stat == "not": del self.li3
        elif li_no == 3 and li3_stat == "empty": return "List3 already empty!"
        else: return "Fatal error!"

    def li_delete(self):
        while True:
            self.clrscr()
            x = input("Please select the list to be deleted\n1.List1\n2.List2\n3.List3\n4.Go back\n")
            if x == "1":
                print("Deleted!" if self.li_deleter(1) == None else self.li_deleter(1))
            elif x == "2":
                print("Deleted!" if self.li_deleter(2) == None else self.li_deleter(2))
            elif x == "3":
                print("Deleted!" if self.li_deleter(3) == None else self.li_deleter(3))
            elif x == "4":
                self.list_screen()
            else:
                print("Invalid Input!")
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