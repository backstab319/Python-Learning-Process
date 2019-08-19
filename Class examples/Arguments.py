# def add(a,b,c):
#     print("a is",a)
#     print("b is",b)
#     print("c is",c)
#     return (a+b,b+c,c+a)
# a = input()
# b = input()
# c = input()
# print(add(int(a),int(b),int(c)))

# def sq(val): return val**2
# inp = input().split()
# for i in inp: print(sq(int(i)))

# def test(a,b): return a+b
# print(test(10,20))

# def test1(a,b): print(a,b)
# test1(a=10,b=20)
# test1(b=20,a=10)

# def test(*a):
#     for i in a:
#         print(i)
# test(10,20,30,40,50)

# def sum(*n):
#     res = 0
#     for i in n: res+=i
#     print(res)
# sum(10,20,30,40,50)


# def sum(*n):
#     print(type(n))
#     res = 0
#     for i in n: res+=i
#     print(res)
# sum(10,20,30,40,50)

# def printer(*n):
#     for i in n: print(i)
# printer('sid','dev','gupta')

# def test(**kargs):
#     for i,j in kargs.items(): print(i,":",j)
# test(name=10,date=20)

def test(*a,**b):
    print(a)
test(10,b=20)