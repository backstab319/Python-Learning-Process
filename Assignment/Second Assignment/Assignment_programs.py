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
                for i in range(1,10): print(random.randint(1,100))
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
        x,rec = input("1.String find\n2.String find case sensitive\n0.Go back\n"),1
        if x == "1":
            self.str_find()
        elif x == "2":
            self.str_case_sens()
        elif x == "0": rec = 0
        else: print("Incorrect input!")
        self.next_main() if rec == 1 else 0

    def str_find(self):
        self.clrscr()
        x,y = input("Please enter a string "),input("Please enter a string to be found ")
        if x.find(y) != -1: print("The element is present in the target string")
        else: print("Element not present")
        self.pause()

    def str_case_sens(self):
        self.clrscr()
        x = input("Please enter a string ")
        if x == x.capitalize(): print("The given string is case sensitive")
        else: print("The string is not case sensitive")
        self.pause()

curse = Assignment2()
curse.main_exec()