# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).

# print(','.join([str(i) for i in range(2000, 3201) if i%7==0 and i%5!=0]))

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

# x = int(input())
# print(eval('*'.join([str(i) for i in range(1,x+1)]))) if x > 0 else print(1)

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

# x = int(input())
# print({i:i*i for i in range(1,x+1)})

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

# x = input().split(",")
# print([i for i in x],"\n"+str(tuple(i for i in x)))

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.

# class String_op:
#     def __init__(self): self.s = str
#     def get_str(self): self.s = input("Enter a string ")
#     def put_str(self): print(self.s.upper())
# str_obj = String_op()
# str_obj.get_str()
# str_obj.put_str()

# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# x,C,H = input().split(","),50,30
# print(",".join([str(int(((2*C*int(i))/H)**0.5)) for i in x]))

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# x = input().split(",")
# x.sort()
# print(",".join([i for i in x]))

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# x = []
# while True:
#     z = input()
#     if z == "": break
#     x.append(z.upper())
# for i in x: print(i)

# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# x = set(input().split())
# print(" ".join(sorted(x)))

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001

# x = input().split(",")
# print(",".join([i for i in x if int(i,2)%5==0]))

# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# nums=[]
# for i in range(1000,3000):
#     if [j for j in str(i) if int(j)%2!=0]: continue
#     nums.append(str(i))
# print(",".join(nums))