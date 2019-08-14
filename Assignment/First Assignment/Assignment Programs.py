inp = input("Find the length of a string\nEnter a string ")
for i,j in enumerate(inp, 1): x = i
print("Length of the string is",x)
inp = int(input("Factorial of a given number\nEnter a number "))
fact = 1
for i in range(1,inp+1): fact = i * fact
print("Using for loop",fact)
fact, num = 1,inp
while num > 0:
    fact = fact * num
    num-=1
print("Using while loop ",fact)
print("Prime numbers")

inp = int(input("Enter a number"))
if inp%2 == 0 or inp%3 == 0 or inp%4 == 0 or inp%5 == 0 or inp%7 == 0:
    print("The given number is prime")
else:
    print("The given number is not prime")