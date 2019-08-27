inp,inp0 = input("Enter a string to check if it is palindrome "),""
i=len(inp)-1
while i >= 0: inp0,i=inp0+inp[i],i-1
print("It is a palindrome" if inp == inp0 else "It is not a palindrome")