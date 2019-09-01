# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).

# print(','.join([str(i) for i in range(2000, 3201) if i%7==0 and i&5!=0]))

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