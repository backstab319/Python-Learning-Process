# def add(a):
#     x = lambda a,b : a+b
#     return x(a,20)
# print(add(10))

# def sq_cu(num):
#     x = lambda num : [num**2,num**3]
#     return x(num)
# print(sq_cu(8))

# def tables(num):
#     x = lambda num,i : print(num,"*",i,"=",num*i)
#     for i in range(1,11): x(num,i)
# inp = int(input("Enter a number "))
# tables(inp)

# for i in range(1,11):
#     if i%2 is 0: print(i,"is even")
#     else: print(i,"is odd")

# x = lambda : print([i for i in range(1,11) if i%2==0])
# x()
# data = list(filter(lambda x: x%2 == 0,range(1,11)))
# print(data)
# def squre(): return list(map(lambda y:y**2,range(1,11)))
# print(squre())