from os import system, name
from time import ctime, sleep
from datetime import date
import random
class Assignment2:
    def clrscr(self): system("cls") if name == "nt" else system("clear")
    def pauser(self,sec): sleep(sec)
    def pause(self): input("Please press any key to continue...")
    def dis_datetime(self): print(ctime())

    def pr_name(self):
        self.clrscr()
        while True:
            inp = input("Please enter your name ")
            if inp is not "": break
            else: self.clrscr()
        print(inp)
        self.pause()

    def pr_lyric(self):
        lyric = [
            "I did my time, and I want out","So effusive, fade","It doesn't cut","The soul is not so vibrant","The reckoning, the sickening","Packaging subversion",
            "Pseudo sacrosanct perversion","Go drill your deserts","Go dig your graves","Then fill your mouth","With all the money you will save",
            "Sinking in, getting smaller again","Undone, it has begun","I'm not the only one",
            "Oh, there are cracks, in the road we lay","But where the temple fell","The secrets have gone mad","This is nothing new",
            "But when we killed it all","The hate was all we had","Who needs another mess?","We could start over",
            "Just look me in the eyes","And say I'm wrong","Now there's only emptiness","Venomous, insipid","I think we're done",
            "I'm not the only one"
        ]
        for i in lyric: print(i,self.pauser(0.8)) if len(i) < 23 else print(i,self.pauser(1.5))
        self.pause()

    def main_exec(self):
        while True:
            self.clrscr()
            x = input(
                "1.Print my name\n2.Print lyrics of my favorite song\n3.Print numbers\n4.Summation of 64 and 32\n5.Summation of x and y\n6.Favourite actor name\n7.Print lucky inside var s\n8.Print date\n9.String replace\n00.Next set of programs\n0.To exit\n"
            )
            if x == "1": self.pr_name()
            elif x == "2": self.pr_lyric()
            elif x == "3":
                self.clrscr()
                i = 0
                while i < 10:
                    print(random.randint(1,100))
                    i+=1
                self.pause()
            elif x == "4":
                self.clrscr()
                print("64 + 32 =",eval("64+32"))
                self.pause()
            elif x == "5":
                self.clrscr()
                x,y = input("Enter value of x "),input("Enter value of y ")
                print(x+" + "+y+" =",int(x)+int(y))
                self.pause()
            elif x == "6":
                self.clrscr()
                print("My favourite actor's name is ")
                self.pause()
            elif x == "7":
                self.clrscr()
                s = "lucky"
                print(s,type(s))
                self.pause()
            elif x == "8":
                self.clrscr()
                print("Today's date is",date.today())
                self.pause()
            elif x == "9":
                self.str_replace()
            elif x == "00":
                self.next_main()
            elif x == "0":
                self.clrscr()
                self.pauser(1)
                exit()
            else:
                print("Invalid Input!")
                self.pause()

    def str_replace(self):
        self.clrscr()
        a,b,c = input("Enter a string "),input("Enter string to be replaced "),input("Enter the replacing string ")
        print(a.replace(b,c))
        self.pause()

    def next_main(self):
        self.clrscr()
        x,rec = input("1.String find\n2.String find case sensitive\n3.Join words\n4.Join words with underscore\n5.Split given string\n6.Split article\n7.Create random number in var\n8.Create three random numbers\n9.Frequenzy of 100 random numbers\n00.Next set of programs\n0.Go back\n"),1
        if x == "1":
            self.str_find()
        elif x == "2":
            self.str_case_sens()
        elif x == "3":
            self.join_str("space")
        elif x == "4":
            self.join_str("under")
        elif x == "5":
            self.clrscr()
            str = "World,Earth,America,Canada"
            print("Before Splitting\n"+str)
            print("After Splitting")
            for i in str.split(","): print(i)
            self.pause()
        elif x == "6":
            self.article_split()
        elif x == "7":
            self.random_numbers("one")
        elif x == "8":
            self.random_numbers("three")
        elif x == "9":
            self.random_freq()
        elif x == "0": rec = 0
        elif x == "00": self.next_main_1()
        else: print("Incorrect input!")
        if rec == 1: self.next_main()

    def random_freq(self):
        self.clrscr()
        num = [random.randint(1,10) for i in range(1,100)]
        print("100 Random numbers\n"+str(num))
        the_dict = {}
        for i in num:
            if i not in the_dict.keys(): the_dict.update({i:1})
            else:
                val = the_dict.get(i)
                val+=1
                the_dict.update({i:val})
        print(the_dict)
        self.pause()

    def random_numbers(self,numbers):
        self.clrscr()
        i = 0
        if numbers == "one":
            x = random.randint(1,10)
            print("The random number is",x)
        else:
            while i < 3:
                print(random.randint(1,10))
                i+=1 
        self.pause()

    def article_split(self):
        self.clrscr()
        art = "Minification (also minimisation or minimization), is the process of removing all unnecessary characters from the source codes of interpreted programming languages or markup languages without changing their functionality. These unnecessary characters usually include white space characters, new line characters, comments, and sometimes block delimiters, which are used to add readability to the code but are not required for it to execute. Minification reduces the size of the source code, making its transmission over a network (e.g. the Internet) more efficient. In programmer culture, aiming at extremely minified source code is the purpose of recreational code golf competitions.Minification must not be confused with obfuscation; the former can be readily reversed using a pretty-printer. Minification can be distinguished from the more general concept of data compression in that the minified source can be interpreted immediately without the need for an uncompression step: the same interpreter can work with both the original as well as with the minified source."
        print(art)
        sp = input("Enter the prase to be splitting with\n")
        print("\nAfter splitting\n\n"+str(art.split(sp)))
        self.pause()

    def join_str(self,switch):
        self.clrscr()
        x = input("Please enter some strings ").split()
        print("".join(x)) if switch == "space" else print("_".join(x))
        self.pause()

    def str_find(self):
        self.clrscr()
        x,y = input("Please enter a string "),input("Please enter a string to be found ")
        if x.find(y) != -1: print("The element is present in the target string. At address",x.find(y))
        else: print("Element not present")
        self.pause()

    def str_case_sens(self):
        self.clrscr()
        x = input("Please enter a string ")
        if x == x.capitalize(): print("The given string is case sensitive")
        else: print("The string is not case sensitive")
        self.pause()

    def next_main_1(self):
        self.clrscr()
        x,rec = input("1.To input phone number\n2.To enter preffered programming language\n3.Number between rnage\n4.Input password\n5.List countries in the set\n6.Count from 0 to 100\n7.Multiplication table\n8.Print 1 to 10 backwards\n9.Even numbers till 10\n0.Go back\n"),0
        if x == "1": self.input_methods("phone")
        elif x == "2": self.input_methods("lang")
        elif x == "3":
            self.clrscr()
            inp = int(input("Please enter a number in the range 1 and 10 "))
            print("Condition satisfied!") if inp<=10 and inp >=1 else print("Number out of range!")
            self.pause()
        elif x == "4":
            self.clrscr()
            password = input("Please enter your password ")
            self.clrscr()
            print("Your entered password is",password)
            self.pause()
        elif x == "5":
            self.clrscr()
            list1 = ['Canada','USA','Mexico','Australia']
            for i in list1: print(i)
            self.pause()
        elif x == "6":
            self.clrscr()
            for i in range(0,101): print(i)
            self.pause()
        elif x == "7":
            self.clrscr()
            for i in range(1,11): print("2","X",i,"=",2*i)
            self.pause()
        elif x == "8":
            self.clrscr()
            for i in reversed(range(1,11)): print(i)
            self.pause()
        elif x == "9":
            self.clrscr()
            print(len([i for i in range(1,11) if i%2 == 0]))
            self.pause()
        elif x == "0": rec = 1
        else:
            print("Invalid Input!")
            self.pause()
        if rec == 0: self.next_main_1()

    def input_methods(self,switch):
        self.clrscr()
        print("Please enter your phone number") if switch == "phone" else print("Please enter your preferred programming language")
        inp = input()
        self.clrscr()
        print("Your phone number is",inp) if switch == "phone" else print("Your preffered language is",inp)
        self.pause()

curse = Assignment2()
curse.main_exec()
# Test for ubuntu