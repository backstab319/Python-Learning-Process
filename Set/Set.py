print("Declaring a set")
z = y = x = {10,"Hello","Good morning",100}
print(x)
print(type(x),"\n")
print("Adding an element to a set")
x.add("Good evening")
print(x,"\n")
print("Deleting a set")
del x
print("Removing a particular element")
y.remove("Good evening")
print(y,"\n")
print("Finding the length of a set")
print(len(y),"\n")
print("Clearing a set")
y.clear()
print(y,"\n")
print("Copying a set")
x = {}
x = z.copy()
print(z)
print(x,"\n")
print("Popping an element from a set\n",x.pop())