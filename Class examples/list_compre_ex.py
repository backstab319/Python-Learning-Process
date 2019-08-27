# for i in range(100):
#     if int(i)%2 == 0 and int(i)%3 == 0: print(i)

# x = [ i for i in range(100) if i%2==0 and i%3==0]
# print(x)

# for i in range(10):
#     if i%2==0:
#         print(i,"is even")
#     else:
#         print(i,"is odd")

# x = [ i if i%2 == 0 else "odd" for i in range(10)]
# print(x)

# list = []
# for x in [1,2,3]:
#     for y in [10,20,30]:
#         list.append(x*y)
# print(list)

# a = [x*y for x in [1,2,3] for y in [10,20,30]]
# print(a)

# common = []
# for i in [10,20,30,40,50]:
#     for j in [10,30,25,40,55]:
#         if i == j: common.append(i)
# print(common)

common = [i for i in [10,20,30,40,50] for j in [10,30,25,40,55] if i==j]
print(common)