def square_no(val): return val*val
def qube_no(val): return val*val*val
def pow_no(val,poww): return val**poww
sq = int(input("Enter a number to find square "))
print(square_no(sq))
qu = int(input("ENter a number to find qube "))
print(qube_no(qu))
val,poww = int(input("Enter the value ")),int(input("Enter the power "))
print(pow_no(val,poww))