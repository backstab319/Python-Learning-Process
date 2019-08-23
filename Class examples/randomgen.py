import random
import time
li = ["test","tester","debug","debugger"]
tup = ("test","tester","debug","debugger")
di = {"test":"tester","debug":"debugger"}
print("Shuffling list",random.shuffle(li))
print(li)
# print("Shuffling tuple",shuffle(tup))
# print("Shuffling dictionary",shuffle(di))
while True:
    time.sleep(0.2)
    print(random.randrange(0,999))