print("Operation on strings")
a = "HACKER"
print(a)
print(a[:5])
print(a[::-1])
print("Concatenation")
b = "Software "
print(b+a)
print(b + a[0:])
print("Replication")
b = a * 5
print(b)
print("Membership")
data = a,b,"sid","dev","gupta"
print(data)
val = ("sid" in data)
if (val == True):
    print("Yes the string is present")
else:
    print("No the string is not present")
