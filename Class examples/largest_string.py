li,greater = list(input("Enter any number of strings ").split()),""
for i in li: greater = i if len(greater) < len(i) else greater
print(greater)