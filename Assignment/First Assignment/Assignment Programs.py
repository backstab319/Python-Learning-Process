from os import system,name
class Assignment:

    def clrscr(self): system("cls") if name == "nt" else system("clear")

    def pause(self): input("Press any key to continue..")

    def main_screen(self):
        self.clrscr()
        x = input("Demonstration of assignment programs\n1.Length of string\n2.Count of string\n3.Reverse of string\n4.Convert string to list\n5.Convert list to string\n6.Number of digits or letter in string\n7.Pattern using nested for loop\n8.Odd and even number from a given series\n9.Prime\n10.Factorial\n11.Exit\n")
        if x == "1":
            self.str_length()
        elif x == "2":
            self.count_str()
        elif x == "3":
            self.rev_str()
        elif x == "4":
            self.str_list()
        elif x == "5":
            self.list_str()
        elif x == "6":
            self.digandletters_str()
        elif x == "7":
            self.pattern_nestedfor()
        elif x == "8":
            self.evenodd_series()
        elif x == "9":
            self.primenumbers()
        elif x == "10":
            self.factorial()
        elif x == "11":
            self.clrscr()
            exit()
        else:
            print("Invalid Input!")
            self.pause()
        self.main_screen()

    def count_str(self):
        self.clrscr()
        x,li = input("Please enter a string\n"),[]
        for i in x: li.append(i)
        for i in li:
            print(li.count(i))
        self.pause()

    def rev_str(self):
        self.clrscr()
        x,j = input("Please enter a string\n"),""
        for i in reversed(x): j+=i
        print("The reverse of",x,"is",j)
        self.pause()

    def str_list(self):
        self.clrscr()
        x,list1 = input("Please enter a string to convert into list\n"),[]
        for i in x: list1.append(i)
        print(list1)
        self.pause()

    def list_str(self):
        self.clrscr()
        x,str1 = input("Please enter a list to convert into string\n"),""
        for i in x: str1+=i+" "
        print(str1)
        self.pause()

    def digandletters_str(self):
        self.clrscr()
        x,digno = input("Enter a string which contains digits and words\n"),0
        for i in x: digno= digno+1 if i.isdigit() else digno+0
        print("Number of digits",digno,"and number of words",len(x)-digno)
        self.pause()

    def pattern_nestedfor(self):
        None

    def evenodd_series(self):
        self.clrscr()
        x = input("Enter a series of numbers\n").split()
        for i in x: print(i+" Even" if int(i)%2 == 0 else i+" Odd")
        self.pause()

    def primenumbers(self):
        self.clrscr()
        inp = int(input("Enter a number"))
        print("The given number is prime" if inp%2==0 or inp%3==0 or inp%4==0 or inp%5==0 or inp%7==0 else "The given number is not prime")
        self.pause()

    def factorial(self):
        self.clrscr()
        inp = int(input("Factorial of a given number\nEnter a number "))
        fact = 1
        for i in range(1,inp+1): fact = i * fact
        print("Using for loop",fact)
        fact, num = 1,inp
        while num > 0:
            fact = fact * num
            num-=1
        print("Using while loop ",fact)
        self.pause()

    def str_length(self):
        self.clrscr()
        inp = input("Find the length of a string\nEnter a string ")
        for i in inp: x = i
        print("Length of the string is",x)
        self.pause()

curse = Assignment()
curse.main_screen()