y,x = input("Please enter a series of numbers ").split(),[]
x=[i for i in y if int(i)%2 == 0]
print(x)