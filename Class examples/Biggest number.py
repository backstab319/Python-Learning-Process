a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))
if a > b and a > c:
    print("A is the biggest of three")
elif b > a and b > c:
    print("B is the biggest of three")
elif c > a and c > b:
    print("C is the biggest of three")
else:
    print("ABC are equal")