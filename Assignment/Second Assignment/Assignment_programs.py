from os import system, name
from time import ctime, sleep
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
                "1.Print my name\n2.Print lyrics of my favorite song\n0.To exit\n"
            )
            if x == "1": self.pr_name()
            elif x == "2": self.pr_lyric()
            elif x == "0":
                self.clrscr()
                self.pauser(1)
                exit()
            else:
                print("Invalid Input!")
                self.pause()

curse = Assignment2()
curse.main_exec()