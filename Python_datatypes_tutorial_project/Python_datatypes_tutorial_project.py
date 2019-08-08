from os import system, name
class Pydata:
    def clrscr(self):
        if(name == "nt"):
            system("cls")
        else:
            system("clear")
    def main_screen(self):
        self.clrscr()
        while True:
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
        self.clrscr()
        while True:
            val = input("String Operations\n1.Perform string operations\n2.To go back to main menu\nAny other key to exit\n")
            if val == "1":
                print("Performed string operations!")
            elif val == "2":
                self.main_screen()
            else:
                exit()
    def tuple_screen(self):
        self.clrscr()
        while True:
            val = input("Tuple Operations\n1.Perform tuple operations\n2.To go back to main menu\nAny other key to exit\n")
            if val == "1":
                print("Performed tuple operations!")
            elif val == "2":
                self.main_screen()
            else:
                exit()
    def list_screen(self):
        self.clrscr()
        while True:
            val = input("List Operations\n1.Perform list operations\n2.To go back to main menu\nAny other key to exit\n")
            if val == "1":
                print("Performed list operations!")
            elif val == "2":
                self.main_screen()
            else:
                exit()
    def dict_screen(self):
        self.clrscr()
        while True:
            val = input("Dictionary Operations\n1.Perform dictionary operations\n2.To go back to main menu\nAny other key to exit\n")
            if val == "1":
                print("Performed dictionary operations!")
            elif val == "2":
                self.main_screen()
            else:
                exit()
curse = Pydata()
curse.main_screen()