# set1 = set({1,2,3,4,5,6,7,8,9,10})
# for i in set1:
#     if i%2 == 0:
#         print("Even",i)
#     else:
#         print("Odd",i)

# inp = set(input("Enter numbers into the set ").split())
# for i in inp:
#     if int(i)%2 == 0:
#         print("Even",i)
#     else:
#         print("Odd",i)

# inp = set(input("Enter numbers into the set ").split())
# a = {i for i in inp if int(i)%2==0}
# print(a)

# seta = set({1,2,3,4,5})
# setb = set({1,2,3,4,5})
# setc = {i*j for i in seta for j in setb if i == j}
# print(setc)

print({i for i in range(2,100) for x in range(2,i) if i%x!=0})