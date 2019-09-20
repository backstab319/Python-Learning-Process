import os
import sys
class EH:
    a = 5
    b = "0"
    l = [1,2,3,4,5]
    c = 5
    d = 0
    i = 7
    temp = None
    def inpEval(self,msg):
        while True:
            try: self.temp = int(input(msg))
            except BaseException: print("Base exception!")
            else: break
        return self.temp
    def EHMethod(self):
        try:
            print(self.a+self.b)
            print(self.l[self.i])
            print(self.c/self.d)
        except TypeError:
            os.system("clear")
            print("Type error occured!")
            self. b = self.inpEval("Enter any integer value ")
            self.EHMethod()
        except IndexError:
            os.system("clear")
            print("Index out of range!")
            print("Please write between range",0,"to",len(self.l)-1)
            self.i = self.inpEval("Enter integer between the above range ")
            self.EHMethod()
        except ZeroDivisionError:
            os.system("clear")
            print("Zero division error!")
            self.d = self.inpEval("Please enter integer except 0 ")
            self.EHMethod()
        else:
            os.system("clear")
            print("No more exceptions!")
starter = EH()
starter.EHMethod()