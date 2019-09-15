import re
from os import name, system

class identifierRe:
    def clrscr(self): system("clear") if name != "nt" else system("cls")
    def pause(self): input("Press any key to continue..")
    
    def identifierFilter(self,data):
        matcher = re.match("^[a-k]$5",data)
        if matcher != None: print("Starts from a to k")
        else: print("Dosent starts from a to k")
        self.pause()

    def getInput(self):
        self.clrscr()
        data = input("Enter 'exit' to exit\nPlease enter a string that follows the identifier rule ")
        if data == "exit": return
        else:
            self.identifierFilter(data)
            self.getInput()

start = identifierRe()
start.getInput()