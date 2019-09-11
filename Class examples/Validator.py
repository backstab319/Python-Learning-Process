import re
from os import system, name
class myValidator:
    def clrscr(self): system("cls") if name == "nt" else system("clear")
    def pause(self): input("Please press any key to continue.")

    def phone(self,data):
        x = re.fullmatch("[6-9]\\d{9}",data)
        return True if x else False

    def email(self,data):
        x = re.fullmatch(".*@gmail.com",data)
        return True if x else False

    def data_input(self,switch):
        self.clrscr()
        x = input("Input ")
        if switch == "phone": print("Correct phone number") if self.phone(x) else print("Wrong phone number")
        if switch == "email": print("Correct email address") if self.email(x) else print("worng email address")
        self.pause()

    def splash(self):
        self.clrscr()
        x = input("1.Validate phone number\n2.Validate email\n0.Exit\n")
        if x == "1": self.data_input("phone")
        elif x == "2": self.data_input("email")
        else:
            print("Invalid input!")
            self.pause()
        if True: self.splash()

starter = myValidator()
starter.splash()