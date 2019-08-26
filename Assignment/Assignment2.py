from os import system, name
class Assignment2:
    def clrscr(self): system("cls") if name == "nt" else system("clear")
    def pause(self): input()

    def main(self):
        

curse = Assignment2()
curse.main()